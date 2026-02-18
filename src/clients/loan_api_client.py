# ============================================================================
# LOAN API KLIENT - Hanterar all HTTP-kommunikation med Loan API
# ============================================================================
# Denna klient kapslar in alla REST API-anrop till Söderbröder Loan Lab API
# Den hanterar autentisering, endpoint-hantering och request/response-hantering

import requests
from src.helpers import DEFAULT_API_KEY, ADMIN_API_KEY


class LoanAPIClient:
    """
    Klient för att interagera med Söderbröder Loan Lab API.
    
    Denna klass hanterar alla HTTP-förfrågningar till Loan API, inklusive:
    - Skapa nya låneansökningar
    - Hämta befintliga lån
    - Uppdatera lån (admin-operationer)
    - Ta bort lån (admin-operationer)
    - Lista alla lån
    
    Klienten hanterar API-autentisering med API-nycklar via x-api-key header.
    """
    
    # Bas-URL för alla API-endpoints
    BASE_URL = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"
    
    def __init__(self, api_key: str = DEFAULT_API_KEY):
        """
        Initialisera API-klienten med en API-nyckel.
        
        Args:
            api_key (str): API-nyckeln som ska användas för autentisering.
                          Standardvärde är DEFAULT_API_KEY (nyckel för lånkapande)
        """
        self.api_key = api_key
        # Ställ in HTTP-headers med API-nyckel och content-type
        self.headers = {
            "x-api-key": api_key,  # API-nyckel för autentisering
            "Content-Type": "application/json"  # Vi skickar och förväntar JSON
        }
    
    def create_loan(self, payload):
        """
        Skapa en ny låneansökan.
        
        Args:
            payload (dict): Ordbok som innehåller låneansökningsdata
                           (applicantName, loanAmount, loanType, personalNumber, osv.)
            
        Returns:
            requests.Response: Response-objekt innehållande statuskod och JSON-data
        """
        # POST-förfrågan till /loans endpoint för att skapa ett nytt lån
        response = requests.post(f"{self.BASE_URL}/loans", json=payload, headers=self.headers)
        return response
    
    def get_loan(self, loan_id: str):
        """
        Hämta detaljer om ett specifikt lån med ID.
        
        Args:
            loan_id (str): Det unika identifieringen av lånet att hämta
            
        Returns:
            requests.Response: Response-objekt med låndetaljer
        """
        # GET-förfrågan för att hämta ett specifikt lån
        response = requests.get(f"{self.BASE_URL}/loans/{loan_id}", headers=self.headers)
        return response
    
    def update_loan(self, loan_id: str, payload):
        """
        Uppdatera ett befintligt lån (admin-operation).
        
        Args:
            loan_id (str): Det unika identifieringen av lånet att uppdatera
            payload (dict): Ordbok innehållande uppdaterad låndata
            
        Returns:
            requests.Response: Response-objekt som bekräftar uppdateringen
        """
        # Använd ADMIN_API_KEY för denna operation (admin kräver en annan nyckel)
        headers = self.headers.copy()
        headers["x-api-key"] = ADMIN_API_KEY
        # PUT-förfrågan för att uppdatera lånet
        response = requests.put(f"{self.BASE_URL}/loans/{loan_id}", json=payload, headers=headers)
        return response
    
    def delete_loan(self, loan_id: str):
        """
        Ta bort ett lån (admin-operation).
        
        Args:
            loan_id (str): Det unika identifieringen av lånet att ta bort
            
        Returns:
            requests.Response: Response-objekt som bekräftar borttagningen
        """
        # Använd ADMIN_API_KEY för denna operation
        headers = self.headers.copy()
        headers["x-api-key"] = ADMIN_API_KEY
        # DELETE-förfrågan för att ta bort lånet
        response = requests.delete(f"{self.BASE_URL}/loans/{loan_id}", headers=headers)
        return response
    
    def get_all_loans(self):
        """
        Hämta alla lån.
        
        Returns:
            requests.Response: Response-objekt innehållande listan över alla lån
        """
        # GET-förfrågan för att lista alla lån
        response = requests.get(f"{self.BASE_URL}/loans", headers=self.headers)
        return response
