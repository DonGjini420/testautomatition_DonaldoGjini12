# ============================================================================
# PYTEST KONFIGURATION OCH FIXTURES
# ============================================================================
# Denna modul konfigurerar Pytest och tillhandahåller återanvändbara fixtures.
# Fixtures är hjälpobjekt som automatiskt tillhandahålls till testfunktioner.

import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


# ============================================================================
# BROWSER FIXTURE - Session scope (körs en gång per test-session)
# ============================================================================
@pytest.fixture(scope="session")
def browser():
    """
    Skapar en webbläsare-instans som finns kvar under hela test-sessionen.
    
    Session scope betyder:
    - Webbläsaren startas en gång i början av testningen
    - Alla tester delar samma webbläsare-instans
    - Webbläsaren stängs efter alla tester är klara
    
    Detta förbättrar prestandan jämfört med att starta en ny webbläsare för varje test.
    
    Returns:
        Browser: En Playwright webbläsare-instans (Chromium)
    
    Yields:
        Browser: Ger webbläsaren till testen, sedan stängs den (städning)
    """
    # Starta Playwright och öppna en Chromium webbläsare
    with sync_playwright() as p:
        # Starta webbläsaren i headless-läge (inget visuellt fönster)
        browser = p.chromium.launch(headless=True)
        # Ge webbläsaren till testen
        yield browser
        # Städning: Stäng webbläsaren efter alla tester
        browser.close()


# ============================================================================
# CONTEXT FIXTURE - Function scope (ny kontext för varje test)
# ============================================================================
@pytest.fixture
def context(browser: Browser):
    """
    Skapar en ny webbläsare-kontext för varje test.
    
    Function scope (standard) betyder:
    - En ny kontext skapas för varje testfunktion
    - Kontexterna är isolerade (separata cookies, lagring, cache)
    - Varje kontext städas upp efter sitt test
    
    En kontext är som ett inkognito-fönster - isolerat från andra kontexterna.
    Detta säkerställer att tester inte påverkar varandra.
    
    Args:
        browser (Browser): Den delade webbläsaren (från browser fixture)
    
    Returns:
        BrowserContext: En ny isolerad webbläsare-kontext
    
    Yields:
        BrowserContext: Ger kontexten till testen, sedan stängs den
    """
    # Skapa en ny kontext i den delade webbläsaren
    context = browser.new_context()
    # Ge kontexten till testen
    yield context
    # Städning: Stäng kontexten efter testen
    context.close()


# ============================================================================
# PAGE FIXTURE - Function scope (ny sida för varje test)
# ============================================================================
@pytest.fixture
def page(context: BrowserContext) -> Page:
    """
    Skapar en ny sida (tab) i webbläsaren-kontexten för varje test.
    
    Function scope betyder:
    - Varje test får sin egen friska sida
    - Sidor städas automatiskt upp efter varje test
    
    En sida är som en flik i webbläsaren - tester kan navigera, fylla formulär, osv.
    
    Args:
        context (BrowserContext): Webbläsaren-kontexten (från context fixture)
    
    Returns:
        Page: En ny sida/flik i webbläsaren-kontexten
    
    Yields:
        Page: Ger sidan till testen, sedan stängs den
    """
    # Skapa en ny sida i kontexten
    page = context.new_page()
    # Ge sidan till testen
    yield page
    # Städning: Stäng sidan efter testen
    page.close()
