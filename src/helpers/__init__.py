# Test data and fixtures
from faker import Faker
from typing import Dict, Any

# API Keys (from specification)
DEFAULT_API_KEY = "626125a0cad5d31395fdb24d7b6ba4e5080e14e75153491de96111e3c78d985e"
ADMIN_API_KEY = "8fc12c147ead07fa39ce5203195bd80aec504e1e6fb92d18e12dd95b13abbacb"

# Swedish test personnumbers (official from Skatteverket)
SWEDISH_TEST_PERSONNUMBERS = [
    "199503152679",
    "199105053217",
    "199510072710",
    "199212345678",
    "199411111234",
]

fake = Faker('sv_SE')


def get_test_personnumber(index: int = 0) -> str:
    """Get Swedish test personnumber"""
    return SWEDISH_TEST_PERSONNUMBERS[index % len(SWEDISH_TEST_PERSONNUMBERS)]


def generate_synthetic_loan_application() -> Dict[str, Any]:
    """Generate synthetic loan application using Faker"""
    loan_types = ["car", "boat", "wedding", "renovation", "vacation"]
    
    return {
        "applicantName": fake.name(),
        "applicantEmail": fake.email(),
        "applicantPhone": fake.phone_number()[:15],
        "personalNumber": get_test_personnumber(),
        "loanAmount": fake.random_int(min=10000, max=500000),
        "loanType": fake.random_element(loan_types),
        "loanTerm": fake.random_int(min=12, max=60),
        "monthlyIncome": fake.random_int(min=15000, max=100000),
        "existingDebts": fake.random_int(min=0, max=200000),
        "employmentStatus": fake.random_element(["employed", "self-employed", "retired"]),
        "address": fake.address(),
    }


# Test data fixtures (GDPR compliant - using official test personnumbers)
VALID_LOAN_APPLICATION = {
    "applicantName": "Test Andersson",
    "applicantEmail": "test.andersson@example.com",
    "personalNumber": get_test_personnumber(0),
    "loanAmount": 50000,
    "loanType": "car",
}

LARGE_LOAN_APPLICATION = {
    "applicantName": "Stora Belopp",
    "applicantEmail": "stora.belopp@example.com",
    "personalNumber": get_test_personnumber(1),
    "loanAmount": 400000,
    "loanType": "renovation",
}

WEDDING_LOAN_APPLICATION = {
    "applicantName": "Bröllops Person",
    "applicantEmail": "brollop@example.com",
    "personalNumber": get_test_personnumber(2),
    "loanAmount": 100000,
    "loanType": "wedding",
}

VACATION_LOAN_APPLICATION = {
    "applicantName": "Semester Svensson",
    "applicantEmail": "semester@example.com",
    "personalNumber": get_test_personnumber(3),
    "loanAmount": 30000,
    "loanType": "vacation",
}
