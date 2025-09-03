import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.current_url()

@pytest.mark.ui
def test_login_fail(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("wrong_user", "wrong_pass")
    assert "Epic sadface" in login_page.get_error()
