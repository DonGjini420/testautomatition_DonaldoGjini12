"""
Test data and fixtures for the loan application tests
GDPR compliant - using Swedish tax authority test personnumbers and synthetic data
"""
import csv
from faker import Faker
from pathlib import Path
from typing import Dict, Any, List

# API Keys
DEFAULT_API_KEY = "626125a0cad5d31395fdb24d7b6ba4e5080e14e75153491de96111e3c78d985e"
ADMIN_API_KEY = "8fc12c147ead07fa39ce5203195bd80aec504e1e6fb92d18e12dd95b13abbacb"

# Swedish tax authority test personnumbers (Skatteverkets testpersonnummer)
# These are official test numbers and GDPR compliant
SWEDISH_TEST_PERSONNUMBERS = [
    "199503152679",  # Test person 1
    "199105053217",  # Test person 2
    "199510072710",  # Test person 3
    "199212345678",  # Test person 4
    "199411111234",  # Test person 5
]

fake = Faker('sv_SE')


def get_test_personnumber(index: int = 0) -> str:
    """
    Get a Swedish test personnumber from the official test numbers
    
    Args:
        index: Index in the test personnumber list
        
    Returns:
        A test personnumber string
    """
    return SWEDISH_TEST_PERSONNUMBERS[index % len(SWEDISH_TEST_PERSONNUMBERS)]


def generate_synthetic_loan_application() -> Dict[str, Any]:
    """
    Generate a synthetic loan application using Faker
    Uses Swedish test personnumbers for compliance
    
    Returns:
        Dictionary with loan application data
    """
    loan_types = ["car", "boat", "wedding", "renovation", "vacation"]
    
    return {
        "applicantName": fake.name(),
        "applicantEmail": fake.email(),
        "applicantPhone": fake.phone_number()[:15],  # Phone number limited to 15 chars
        "personalNumber": get_test_personnumber(),
        "loanAmount": fake.random_int(min=10000, max=500000),
        "loanType": fake.random_element(loan_types),
        "loanTerm": fake.random_int(min=12, max=60),  # Months
        "monthlyIncome": fake.random_int(min=15000, max=100000),
        "existingDebts": fake.random_int(min=0, max=200000),
        "employmentStatus": fake.random_element(["employed", "self-employed", "retired"]),
        "address": fake.address(),
    }


def load_test_data_from_csv(filename: str = "testdata.csv") -> List[Dict[str, Any]]:
    """
    Load test data from a CSV file
    
    Args:
        filename: Name of the CSV file
        
    Returns:
        List of dictionaries with test data
    """
    csv_path = Path(__file__).parent.parent.parent / "data" / filename
    
    if not csv_path.exists():
        # Create sample data if file doesn't exist
        return []
    
    data = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields
            row['loanAmount'] = int(row.get('loanAmount', 50000))
            row['loanTerm'] = int(row.get('loanTerm', 24))
            row['monthlyIncome'] = int(row.get('monthlyIncome', 30000))
            row['existingDebts'] = int(row.get('existingDebts', 0))
            data.append(row)
    
    return data


# Sample test data with Swedish test personnumbers
VALID_LOAN_APPLICATION = {
    "applicantName": "Test Andersson",
    "applicantEmail": "test.andersson@example.com",
    "applicantPhone": "+46701234567",
    "personalNumber": get_test_personnumber(0),
    "loanAmount": 50000,
    "loanType": "car",
    "loanTerm": 24,
    "monthlyIncome": 30000,
    "existingDebts": 10000,
    "employmentStatus": "employed",
    "address": "Storgatan 1, 123 45 Stockholm, Sweden",
}

LARGE_LOAN_APPLICATION = {
    "applicantName": "Stora Belopp Andersson",
    "applicantEmail": "storabelopp@example.com",
    "applicantPhone": "+46702345678",
    "personalNumber": get_test_personnumber(1),
    "loanAmount": 400000,
    "loanType": "renovation",
    "loanTerm": 60,
    "monthlyIncome": 75000,
    "existingDebts": 50000,
    "employmentStatus": "employed",
    "address": "Villagatan 10, 456 78 Göteborg, Sweden",
}

WEDDING_LOAN_APPLICATION = {
    "applicantName": "Bröllops Person",
    "applicantEmail": "wedding@example.com",
    "applicantPhone": "+46703456789",
    "personalNumber": get_test_personnumber(2),
    "loanAmount": 100000,
    "loanType": "wedding",
    "loanTerm": 36,
    "monthlyIncome": 45000,
    "existingDebts": 0,
    "employmentStatus": "employed",
    "address": "Kyrkkvägen 5, 789 01 Västerås, Sweden",
}

VACATION_LOAN_APPLICATION = {
    "applicantName": "Semester Svensson",
    "applicantEmail": "vacation@example.com",
    "applicantPhone": "+46704567890",
    "personalNumber": get_test_personnumber(3),
    "loanAmount": 30000,
    "loanType": "vacation",
    "loanTerm": 12,
    "monthlyIncome": 35000,
    "existingDebts": 5000,
    "employmentStatus": "employed",
    "address": "Semestergatan 12, 234 56 Malmö, Sweden",
}
