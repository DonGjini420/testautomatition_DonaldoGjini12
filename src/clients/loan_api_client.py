import requests
from src.helpers import DEFAULT_API_KEY, ADMIN_API_KEY


class LoanAPIClient:
    """API client for Loan API"""
    
    BASE_URL = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"
    
    def __init__(self, api_key: str = DEFAULT_API_KEY):
        self.api_key = api_key
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }
    
    def create_loan(self, payload):
        response = requests.post(f"{self.BASE_URL}/loans", json=payload, headers=self.headers)
        return response
    
    def get_loan(self, loan_id: str):
        response = requests.get(f"{self.BASE_URL}/loans/{loan_id}", headers=self.headers)
        return response
    
    def update_loan(self, loan_id: str, payload):
        headers = self.headers.copy()
        headers["x-api-key"] = ADMIN_API_KEY
        response = requests.put(f"{self.BASE_URL}/loans/{loan_id}", json=payload, headers=headers)
        return response
    
    def delete_loan(self, loan_id: str):
        headers = self.headers.copy()
        headers["x-api-key"] = ADMIN_API_KEY
        response = requests.delete(f"{self.BASE_URL}/loans/{loan_id}", headers=headers)
        return response
    
    def get_all_loans(self):
        response = requests.get(f"{self.BASE_URL}/loans", headers=self.headers)
        return response
