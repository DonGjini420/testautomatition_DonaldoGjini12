from playwright.sync_api import Page


class HomePage:
    """Page Object for home page"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def goto(self):
        self.page.goto("https://souderbroder-loan-lab.lovable.app")
        self.page.wait_for_load_state("networkidle")
    
    def select_loan_type(self, loan_type: str):
        """Select a loan type: car, boat, wedding, renovation, vacation"""
        button_text = {
            "car": "Bil",
            "boat": "Båt",
            "wedding": "Bröllop",
            "renovation": "Renoverring",
            "vacation": "Semester"
        }
        text = button_text.get(loan_type)
        if text:
            self.page.click(f"button:has-text('{text}')")
    
    def click_next(self):
        """Click next button"""
        self.page.click("button:has-text('Nästa')")
        self.page.wait_for_load_state("networkidle")
    
    def get_heading(self) -> str:
        """Get main heading text"""
        return self.page.text_content("h1") or ""
