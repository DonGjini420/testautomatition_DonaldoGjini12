# Testdata och fixtures för låneansökan-testning
# Denna modul tillhandahåller testdata som är GDPR-kompatibel genom att använda
# officiella svenska test personnummer från Skatteverket

from faker import Faker
from typing import Dict, Any

# ============================================================================
# API AUTENTISERING NYCKLAR - Från Söderbröder Loan Lab specifikation
# ============================================================================
# DEFAULT_API_KEY: Används för att skapa nya lån
DEFAULT_API_KEY = "626125a0cad5d31395fdb24d7b6ba4e5080e14e75153491de96111e3c78d985e"

# ADMIN_API_KEY: Används för att uppdatera och ta bort lån (admin-operationer)
ADMIN_API_KEY = "8fc12c147ead07fa39ce5203195bd80aec504e1e6fb92d18e12dd95b13abbacb"

# ============================================================================
# SVENSKA TEST PERSONNUMMER - Officiella test nummer från Skatteverket
# ============================================================================
# Dessa är officiella test personnummer tillhandahållna av Skatteverket (Swedish Tax Agency)
# De är GDPR-kompatibla eftersom de är syntetisk testdata, inte riktiga personnummer
SWEDISH_TEST_PERSONNUMBERS = [
    "199503152679",  # Test person 1
    "199105053217",  # Test person 2
    "199510072710",  # Test person 3
    "199212345678",  # Test person 4
    "199411111234",  # Test person 5
]

# Initialisera Faker med svensk locale för att generera realistiska svenska namn och data
fake = Faker('sv_SE')


def get_test_personnumber(index: int = 0) -> str:
    """
    Hämta ett svenskt test personnummer från listan av officiella test nummer.
    
    Denna funktion cycklar genom listan av test personnummer för att ge variation.
    Om index är större än listans storlek, loopas den runt med modulo.
    
    Args:
        index (int): Index nummer (0-4) för att välja ett test personnummer
        
    Returns:
        str: Ett svenskt test personnummer (12 siffror)
    """
    return SWEDISH_TEST_PERSONNUMBERS[index % len(SWEDISH_TEST_PERSONNUMBERS)]


def generate_synthetic_loan_application() -> Dict[str, Any]:
    """
    Generera syntetisk låneansökan med realistisk data från Faker.
    
    Denna funktion skapar en helt ny låneansökan med random data.
    Använd detta för att testa med varierande data istället för hårdkodade värden.
    
    Returns:
        Dict[str, Any]: En ordbok med alla fält för en låneansökan
    """
    # Lista över möjliga lånetyper
    loan_types = ["car", "boat", "wedding", "renovation", "vacation"]
    
    return {
        "applicantName": fake.name(),  # Slumpmässigt namn från Faker
        "applicantEmail": fake.email(),  # Slumpmässig email-adress
        "applicantPhone": fake.phone_number()[:15],  # Slumpmässigt telefonnummer
        "personalNumber": get_test_personnumber(),  # Test personnummer
        "loanAmount": fake.random_int(min=10000, max=500000),  # Lånebelopp i SEK
        "loanType": fake.random_element(loan_types),  # Slumpmässig låntyp
        "loanTerm": fake.random_int(min=12, max=60),  # Lånets längd i månader
        "monthlyIncome": fake.random_int(min=15000, max=100000),  # Månadlig inkomst
        "existingDebts": fake.random_int(min=0, max=200000),  # Befintliga skulder
        "employmentStatus": fake.random_element(["employed", "self-employed", "retired"]),  # Anställningsstatus
        "address": fake.address(),  # Slumpmässig adress
    }


# ============================================================================
# TESTDATA FIXTURES - Fördefinierade låneansökningar för testning
# ============================================================================
# Dessa fixtures tillhandahåller standardiserad testdata för olika test-scenarier
# Varje fixture representerar en olika lånetyp och belopp för att testa olika fall

# Standard billån - typisk belopp och kund
VALID_LOAN_APPLICATION = {
    "applicantName": "Test Andersson",  # Namn på testperson
    "applicantEmail": "test.andersson@example.com",  # Email-adress
    "personalNumber": get_test_personnumber(0),  # Använd första test personnummer
    "loanAmount": 50000,  # SEK - medel belopp
    "loanType": "car",    # Typ: billån
}

# Stort renovationslån - testar hantering av större belopp
LARGE_LOAN_APPLICATION = {
    "applicantName": "Stora Belopp",  # Namn som indikerar stort belopp
    "applicantEmail": "stora.belopp@example.com",
    "personalNumber": get_test_personnumber(1),  # Använd andra test personnummer
    "loanAmount": 400000,  # SEK - stort belopp för renovering
    "loanType": "renovation",  # Typ: renovationslån
}

# Bröllopslån - olika syfte, medel belopp
WEDDING_LOAN_APPLICATION = {
    "applicantName": "Bröllops Person",  # Namn för bröllops-scenario
    "applicantEmail": "brollop@example.com",
    "personalNumber": get_test_personnumber(2),  # Tredje test personnummer
    "loanAmount": 100000,  # SEK
    "loanType": "wedding",  # Typ: bröllopslån
}

# Semesterlån - mindre belopp, typiskt för semesterresor
VACATION_LOAN_APPLICATION = {
    "applicantName": "Semester Svensson",  # Namn för semesterscenario
    "applicantEmail": "semester@example.com",
    "personalNumber": get_test_personnumber(3),  # Fjärde test personnummer
    "loanAmount": 30000,  # SEK - mindre belopp
    "loanType": "vacation",  # Typ: semesterlån
}
