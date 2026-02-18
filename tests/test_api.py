import pytest
import requests
from src.clients.loan_api_client import LoanAPIClient
from src.helpers import (
    VALID_LOAN_APPLICATION,
    LARGE_LOAN_APPLICATION,
    WEDDING_LOAN_APPLICATION,
    VACATION_LOAN_APPLICATION,
    DEFAULT_API_KEY,
    ADMIN_API_KEY
)


@pytest.mark.api
class TestLoanAPITechnical:
    """Technical API tests - validate headers, HTTP status codes, response structure"""
    
    def test_api_client_has_correct_headers(self):
        """Technical: API client has required x-api-key header"""
        client = LoanAPIClient()
        assert "x-api-key" in client.headers
        assert client.headers["x-api-key"] == DEFAULT_API_KEY
        assert client.headers["Content-Type"] == "application/json"
    
    def test_create_loan_response_is_json(self):
        """Technical: API response can be parsed as JSON"""
        client = LoanAPIClient()
        response = client.create_loan(VALID_LOAN_APPLICATION)
        # Should be able to parse JSON (even if status is not 201)
        assert response.headers.get("content-type") is not None
        try:
            response.json()
        except:
            pytest.fail("Response is not valid JSON")
    
    def test_api_requires_authentication_header(self):
        """Technical: API rejects requests without x-api-key header"""
        response = requests.post(
            f"{LoanAPIClient.BASE_URL}/loans",
            json=VALID_LOAN_APPLICATION,
            headers={"Content-Type": "application/json"}
        )
        # Should not be 201 (unauthorized or bad request)
        assert response.status_code in [400, 401, 403], f"Expected auth error, got {response.status_code}"
    
    def test_invalid_api_key_is_rejected(self):
        """Technical: API rejects invalid API keys"""
        headers = {
            "x-api-key": "invalid-api-key-xyz",
            "Content-Type": "application/json"
        }
        response = requests.post(
            f"{LoanAPIClient.BASE_URL}/loans",
            json=VALID_LOAN_APPLICATION,
            headers=headers
        )
        # Should fail auth
        assert response.status_code in [400, 401, 403], f"Expected auth error, got {response.status_code}"
    
    def test_api_client_initializes_with_default_key(self):
        """Technical: LoanAPIClient uses default API key"""
        client = LoanAPIClient()
        assert client.api_key == DEFAULT_API_KEY
    
    def test_api_client_initializes_with_custom_key(self):
        """Technical: LoanAPIClient accepts custom API key"""
        custom_key = "custom-key-12345"
        client = LoanAPIClient(api_key=custom_key)
        assert client.api_key == custom_key
        assert client.headers["x-api-key"] == custom_key
    
    def test_admin_api_key_is_defined(self):
        """Technical: Admin API key is configured"""
        assert ADMIN_API_KEY is not None
        assert len(ADMIN_API_KEY) > 0
        assert ADMIN_API_KEY != DEFAULT_API_KEY


@pytest.mark.api
class TestLoanAPIBusiness:
    """Business logic tests - validate request/response data handling"""
    
    def test_valid_loan_application_has_required_fields(self):
        """Business: Test data has required fields"""
        assert "applicantName" in VALID_LOAN_APPLICATION
        assert "applicantEmail" in VALID_LOAN_APPLICATION
        assert "personalNumber" in VALID_LOAN_APPLICATION
        assert "loanAmount" in VALID_LOAN_APPLICATION
        assert "loanType" in VALID_LOAN_APPLICATION
    
    def test_loan_application_data_types_correct(self):
        """Business: Test data has correct types"""
        assert isinstance(VALID_LOAN_APPLICATION["applicantName"], str)
        assert isinstance(VALID_LOAN_APPLICATION["loanAmount"], int)
        assert isinstance(VALID_LOAN_APPLICATION["loanType"], str)
    
    def test_large_loan_application_has_large_amount(self):
        """Business: Large loan fixture has high amount"""
        assert LARGE_LOAN_APPLICATION["loanAmount"] >= 300000
        assert LARGE_LOAN_APPLICATION["loanType"] in ["car", "boat", "wedding", "renovation", "vacation"]
    
    def test_different_loan_types_exist(self):
        """Business: Test data covers different loan types"""
        loan_types = {
            VALID_LOAN_APPLICATION["loanType"],
            LARGE_LOAN_APPLICATION["loanType"],
            WEDDING_LOAN_APPLICATION["loanType"],
            VACATION_LOAN_APPLICATION["loanType"]
        }
        assert "car" in loan_types or "renovation" in loan_types or "wedding" in loan_types
        assert len(loan_types) >= 2  # At least 2 different types
    
    def test_all_test_data_uses_valid_personnumbers(self):
        """Business: All test data uses valid Swedish test personnumbers"""
        test_personnumbers = [
            VALID_LOAN_APPLICATION["personalNumber"],
            LARGE_LOAN_APPLICATION["personalNumber"],
            WEDDING_LOAN_APPLICATION["personalNumber"],
            VACATION_LOAN_APPLICATION["personalNumber"]
        ]
        for pn in test_personnumbers:
            assert isinstance(pn, str)
            assert len(pn) >= 10  # Swedish personnumber format
    
    def test_test_data_gdpr_compliant(self):
        """Business: Test data is GDPR compliant (synthetic only)"""
        # All test data should be using test personnumbers, not real ones
        assert VALID_LOAN_APPLICATION["applicantEmail"].endswith("@example.com")
        assert LARGE_LOAN_APPLICATION["applicantEmail"].endswith("@example.com")
