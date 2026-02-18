# ============================================================================
# ANSÖKNINGSFORMULÄR SIDA - Page Object Model för låneansökningsformulär
# ============================================================================
# Denna modul implementerar Page Object Model-mönstret för låneansökning
# där användare anger sin personlig och finansiell information

from playwright.sync_api import Page


class ApplicationFormPage:
    """
    Page Object för låneansökningsformulär-sidan.
    
    Kapslar in alla interaktioner med ansökningsformuläret inklusive:
    - Fylla in sökandes information (namn, email, telefon)
    - Ange låndetaljerna (belopp, löptid)
    - Välja anställningsstatus
    - Skicka formuläret
    - Kontrollera formulärets synlighet och fullständighet
    
    Detta följer Page Object Model-mönstret genom att centralisera alla
    formulärelement-interaktioner i en klass.
    """
    
    def __init__(self, page: Page):
        """
        Initialisera ApplicationFormPage med ett Playwright Page-objekt.
        
        Args:
            page (Page): Playwright page-objekt som representerar webbläsarsidan
        """
        self.page = page
    
    def fill_application_form(self, data: dict):
        """
        Fylla i alla synliga formulärfält med de angivna uppgifterna.
        
        Denna metod försöker fylla formulärfält dynamiskt genom att söka
        efter inmatningselement och matcha dem med placeholder-text.
        
        Args:
            data (dict): Ordbok med låneansökningsdata:
                        - applicantName: Fullständigt namn på sökande
                        - applicantEmail: E-postadress
                        - applicantPhone: Telefonnummer
                        - personalNumber: Svenskt personnummer
                        - loanAmount: Belopp i SEK
                        - loanTerm: Löptid i månader
                        - monthlyIncome: Månadlig inkomst i SEK
                        - existingDebts: Befintliga skulder i SEK
                        - address: Fysisk adress
        """
        # Fylla i namnfältet för sökande
        if "applicantName" in data:
            # Hämta alla input-element
            inputs = self.page.locator("input")
            # Loopa genom inputs för att hitta namnfältet
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Namn" in placeholder or "namn" in placeholder.lower():
                    inputs.nth(i).fill(data["applicantName"])
                    break
        
        # Fylla i email-fältet (type="email" är lättare att identifiera)
        if "applicantEmail" in data:
            self.page.locator("input[type='email']").fill(data["applicantEmail"])
        
        # Fylla i telefonfältet
        if "applicantPhone" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Telefon" in placeholder or "telefon" in placeholder.lower():
                    inputs.nth(i).fill(data["applicantPhone"])
                    break
        
        # Fylla i personnummerfältet
        if "personalNumber" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Personnummer" in placeholder or "personnummer" in placeholder.lower():
                    inputs.nth(i).fill(data["personalNumber"])
                    break
        
        # Fylla i lånebeloppsfältet
        if "loanAmount" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Lånebelopp" in placeholder or "lån" in placeholder.lower():
                    inputs.nth(i).fill(str(data["loanAmount"]))
                    break
        
        # Fylla i lånelöptiden
        if "loanTerm" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Lånelöptid" in placeholder or "löptid" in placeholder.lower():
                    inputs.nth(i).fill(str(data["loanTerm"]))
                    break
        
        # Fylla i månadsinkomstfältet
        if "monthlyIncome" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Månadsinkomst" in placeholder or "inkomst" in placeholder.lower():
                    inputs.nth(i).fill(str(data["monthlyIncome"]))
                    break
        
        # Fylla i befintliga skulder-fältet
        if "existingDebts" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Befintliga" in placeholder or "skulder" in placeholder.lower():
                    inputs.nth(i).fill(str(data["existingDebts"]))
                    break
        
        # Fylla i adressfältet (vanligtvis en textarea)
        if "address" in data:
            textarea = self.page.locator("textarea")
            if textarea.count() > 0:
                textarea.fill(data["address"])
    
    def select_employment_status(self, status: str):
        """
        Välj anställningsstatus från dropdown-menyn.
        
        Args:
            status (str): Anställningsstatus. Alternativ:
                         - "employed" (anställd)
                         - "self-employed" (egen företagare)
                         - "retired" (pensionär)
        """
        # Hitta select-elementet på sidan
        select = self.page.locator("select")
        if select.count() > 0:
            # Välj alternativet med det angivna värdet
            select.select_option(status)
    
    def submit_form(self):
        """
        Skicka ansökningsformuläret.
        
        Denna metod gör följande:
        1. Hittar och klickar på skicka-knappen
        2. Väntar på att sidan behandlar inskickningen
        """
        # Klicka på knappen som innehåller "Skicka" (Svenska för "Send")
        self.page.click("button:has-text('Skicka')")
        # Vänta på att sidan behandlar inskickningen
        self.page.wait_for_load_state("networkidle")
    
    def is_form_visible(self) -> bool:
        """
        Kontrollera om formuläret är synligt på sidan.
        
        Returns:
            bool: True om formulärinmatningselement är synliga, False annars
        """
        # Formuläret är synligt om det finns inmatningsfält på sidan
        return self.page.locator("input").count() > 0
