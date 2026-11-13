import pytest
from selenium import webdriver
import pages.login_page
from tests.test_login import VALID_EMAIL, VALID_PASSWORD


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")

    yield driver

    driver.quit()

@pytest.fixture
def authenticated(driver):
    login_page = pages.login_page.LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()

    return driver