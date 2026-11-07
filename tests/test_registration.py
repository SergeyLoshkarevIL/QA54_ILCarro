from pages.registration_page import RegistrationPage

VALID_EMAIL = "manuel1121@gmail.com"
VALID_PASSWORD = "Manuel12345$"
INVALID_EMAIL = "manuelgmail.com"
INVALID_PASSWORD = "Manuel12345"


def test_valid_login_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_on_registration_button()

    #assert registration_page.is_sign_out_displayed()

def test_registration_with_invalid_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(INVALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_on_registration_button()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_invalid_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(INVALID_PASSWORD)
    registration_page.click_on_registration_button()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_existed_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field("manuel@gmail.com")
    registration_page.fill_password_field("Manuel12345$")
    registration_page.click_on_registration_button()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()