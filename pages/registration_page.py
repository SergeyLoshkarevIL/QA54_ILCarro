import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    REGISTRATION_LINK = (By.CSS_SELECTOR, "[href='/register']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[name="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name = "username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name = "password"]')
    BUTTON_REGISTRATION = (By.XPATH, '//button[text()="Y\u2019alla!"]')
#    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "[class='btn btn--primary']")
    TERM_OF_USE_CHECK_BOX = (By.ID, "terms-of-use")
    LOG_OUT_BUTTON = (By.XPATH, "//button[text()='Log out']")
    CONFIRMATION_TEXT1 = (By.CSS_SELECTOR, "h3")
    CONFIRMATION_TEXT2 = (By.CSS_SELECTOR, "p")
    OK_BUTTON = (By.XPATH, "//*[text()='OK']")
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Name is required']")


    def open_registration_page(self):
        self.click(self.REGISTRATION_LINK)
        time.sleep(2)

    def fill_first_name_field(self,first_name):
        self.fill(self.FIRST_NAME_INPUT, first_name)

    def fill_last_name_field(self,last_name):
        self.fill(self.LAST_NAME_INPUT, last_name)

    def fill_email_field(self,email):
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self,password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_on_registration_button(self):
        self.click(self.BUTTON_REGISTRATION)

    def click_term_of_use_checkbox(self):
        self.click(self.TERM_OF_USE_CHECK_BOX)

    def is_log_out_button_displayed(self):
        return self.driver.find_element(*self.LOG_OUT_BUTTON).is_displayed()

    def fill_registration_form(self, user):
        self.fill_first_name_field(user.first_name)
        self.fill_last_name_field(user.last_name)
        self.fill_email_field(user.email)
        self.fill_password_field(user.password)
        self.click_term_of_use_checkbox()
        self.click_on_registration_button()

    def confirmation1(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.CONFIRMATION_TEXT1)
        )
        return element.text

    def confirmation2(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.CONFIRMATION_TEXT2)
        )
        return element.text

    def close_window(self):
        self.driver.find_element(*self.OK_BUTTON).click()

    def error_message_text(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text

    def submit_button_disabled(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.BUTTON_REGISTRATION)
        )
        return element.get_attribute("disabled") is not None