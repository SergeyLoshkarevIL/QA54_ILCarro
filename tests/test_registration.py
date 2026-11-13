import random
import uuid

from pages.registration_page import RegistrationPage
from models.user import User


def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
#    random_suffix = random.randint(1, 1000000)
    random_suffix = uuid.uuid4()
    user = User(
        first_name= "Sergey",
        last_name= "loshkarev",
        email = f"qwas{random_suffix}aaaddad@gmail.com",
        password= "Aa_12345!"
    )

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)

    assert registration_page.confirmation1() == "Registered"
    assert registration_page.confirmation2() == "You are logged in success"
    registration_page.close_window()


def test_invalid_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        first_name= "",
        last_name= "loshkarev",
        email = "qwasaaaddad@gmail.com",
        password= "Aa_12345!"
    )

    registration_page.open_registration_page()
    registration_page.fill_first_name_field(user.first_name)

    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_disabled()

