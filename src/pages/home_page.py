# ============================================================================
# HEMPAGE - Page Object Model för låneansökning hempage
# ============================================================================
# Denna modul implementerar Page Object Model-mönstret för Söderbröder
# hemsida där användare väljer sin lånetyp (bil, båt, bröllop, osv.)

from playwright.sync_api import Page


class HomePage:
    """
    Page Object för Söderbröder Loan Lab hemsida.
    
    Kapslar in alla interaktioner med hemsidan inklusive:
    - Navigering till sidan
    - Val av lånetyp
    - Klicka på nästa för att gå till ansökan
    - Få rubriktexten
    
    Detta följer Page Object Model-mönstret där alla sidalements
    och interaktioner kapslas in i denna klass.
    """
    
    def __init__(self, page: Page):
        """
        Initialisera HomePage med ett Playwright Page-objekt.
        
        Args:
            page (Page): Playwright page-objekt som representerar webbläsarsidan
        """
        self.page = page
    
    def goto(self):
        """
        Navigera till Söderbröder hemsidan.
        
        Denna metod gör följande:
        1. Navigerar till applikations-URL:en
        2. Väntar på att sidan laddar helt
        """
        self.page.goto("https://souderbroder-loan-lab.lovable.app")
        # Vänta på att sidan laddar helt
        self.page.wait_for_load_state("networkidle")
    
    def select_loan_type(self, loan_type: str):
        """
        Välj en lånetyp på hemsidan.
        
        Args:
            loan_type (str): Typ av lån att välja. Måste vara en av:
                           - "car" (Bil)
                           - "boat" (Båt)
                           - "wedding" (Bröllop)
                           - "renovation" (Renovering)
                           - "vacation" (Semester)
        
        Denna metod hittar knappen med lämplig svensk text
        och klickar på den för att välja lånetypen.
        """
        # Mappa engelska lånetyper till svensk knapptext
        button_text = {
            "car": "Bil",
            "boat": "Båt",
            "wedding": "Bröllop",
            "renovation": "Renoverring",
            "vacation": "Semester"
        }
        # Hämta den svenska texten för knappen
        text = button_text.get(loan_type)
        if text:
            # Klicka på knappen med motsvarande text
            self.page.click(f"button:has-text('{text}')")
    
    def click_next(self):
        """
        Klicka på "Nästa" knappen för att gå vidare till ansökningsformuläret.
        
        Denna metod gör följande:
        1. Hittar och klickar på "Nästa" knappen
        2. Väntar på att nästa steg laddar
        """
        # Hitta och klicka på knappen som innehåller "Nästa" (Svenska för "Next")
        self.page.click("button:has-text('Nästa')")
        # Vänta på att formulärsidan laddar
        self.page.wait_for_load_state("networkidle")
    
    def get_heading(self) -> str:
        """
        Hämta huvudrubiktexten från hemsidan.
        
        Returns:
            str: Textinnehållet från h1-elementet (eller tom sträng om inte funnen)
        """
        # Hitta h1-elementet och hämta dess textinnehål
        heading = self.page.text_content("h1") or ""
        return heading
