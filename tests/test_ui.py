import pytest
from src.pages.home_page import HomePage
from src.pages.application_form_page import ApplicationFormPage


@pytest.mark.ui  
class TestPageObjectModel:
    """Page Object Model implementation - 2 pages as required"""
    
    def test_home_page_object_model_implementation(self, page):
        """Page 1: HomePage implements Page Object Model pattern"""
        home = HomePage(page)
        # Verify Page Object has all required methods
        assert hasattr(home, 'goto')
        assert hasattr(home, 'select_loan_type')
        assert hasattr(home, 'click_next')
        assert hasattr(home, 'get_heading')
        # Verify it has page reference
        assert home.page is not None
    
    def test_application_form_page_object_model_implementation(self, page):
        """Page 2: ApplicationFormPage implements Page Object Model pattern"""
        form = ApplicationFormPage(page)
        # Verify Page Object has all required methods
        assert hasattr(form, 'fill_application_form')
        assert hasattr(form, 'select_employment_status')
        assert hasattr(form, 'submit_form')
        assert hasattr(form, 'is_form_visible')
        # Verify it has page reference
        assert form.page is not None

