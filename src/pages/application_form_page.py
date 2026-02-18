from playwright.sync_api import Page


class ApplicationFormPage:
    """Page Object for application form"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def fill_application_form(self, data: dict):
        """Fill the application form with data"""
        if "applicantName" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Namn" in placeholder or "namn" in placeholder.lower():
                    inputs.nth(i).fill(data["applicantName"])
                    break
        
        if "applicantEmail" in data:
            self.page.locator("input[type='email']").fill(data["applicantEmail"])
        
        if "applicantPhone" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Telefon" in placeholder or "telefon" in placeholder.lower():
                    inputs.nth(i).fill(data["applicantPhone"])
                    break
        
        if "personalNumber" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Personnummer" in placeholder or "personnummer" in placeholder.lower():
                    inputs.nth(i).fill(data["personalNumber"])
                    break
        
        if "loanAmount" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Lånebelopp" in placeholder or "lån" in placeholder.lower():
                    inputs.nth(i).fill(str(data["loanAmount"]))
                    break
        
        if "loanTerm" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Lånelöptid" in placeholder or "löptid" in placeholder.lower():
                    inputs.nth(i).fill(str(data["loanTerm"]))
                    break
        
        if "monthlyIncome" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Månadsinkomst" in placeholder or "inkomst" in placeholder.lower():
                    inputs.nth(i).fill(str(data["monthlyIncome"]))
                    break
        
        if "existingDebts" in data:
            inputs = self.page.locator("input")
            for i in range(inputs.count()):
                placeholder = inputs.nth(i).get_attribute("placeholder") or ""
                if "Befintliga" in placeholder or "skulder" in placeholder.lower():
                    inputs.nth(i).fill(str(data["existingDebts"]))
                    break
        
        if "address" in data:
            textarea = self.page.locator("textarea")
            if textarea.count() > 0:
                textarea.fill(data["address"])
    
    def select_employment_status(self, status: str):
        """Select employment status"""
        select = self.page.locator("select")
        if select.count() > 0:
            select.select_option(status)
    
    def submit_form(self):
        """Submit the form"""
        self.page.click("button:has-text('Skicka')")
        self.page.wait_for_load_state("networkidle")
    
    def is_form_visible(self) -> bool:
        """Check if form is visible"""
        return self.page.locator("input").count() > 0
