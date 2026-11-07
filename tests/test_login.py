from pages.login_page import LoginPage

VALID_EMAIL = "manuel@gmail.com"
VALID_PASSWORD = "Manuel12345$"
INVALID_EMAIL = "manuelgmail.com"
INVALID_PASSWORD = "Manuel12345"

def test_valid_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()
    assert login_page.is_sign_out_displayed()

def test_with_wrong_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(INVALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()
    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_with_valid_email_and_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(INVALID_PASSWORD)
    login_page.click_on_login_button()
    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()


def test_login_unregistered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field("manuel987@gmail.com")
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()
    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()