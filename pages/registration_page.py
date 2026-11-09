import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
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

    def __init__(self,driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTRATION_LINK).click()
        time.sleep(2)

    def fill_first_name_field(self,first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def fill_last_name_field(self,last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_email_field(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_on_registration_button(self):
        self.driver.find_element(*self.BUTTON_REGISTRATION).click()

    def click_term_of_use_checkbox(self):
        self.driver.find_element(*self.TERM_OF_USE_CHECK_BOX).click()

    def is_log_out_button_displayed(self):
        return self.driver.find_element(*self.LOG_OUT_BUTTON).is_displayed()

    #def is_sign_out_displayed(self):
    #    return self.driver.find_element(*self.SIGN_OUT_BUTTON).is_displayed()

    # def is_sign_out_displayed(self):
    #     try:
    #         WebDriverWait(self.driver, timeout=5).until(
    #             expected_conditions.visibility_of_element_located(self.SIGN_OUT_BUTTON))
    #         return True
    #     except TimeoutException:
    #         return False

    # def get_alert_text(self):
    #     alert = WebDriverWait(self.driver,timeout=5).until(
    #         expected_conditions.alert_is_present()
    #     )
    #     return alert.text
    #
    # def accept_alert(self):
    #     self.driver.switch_to.alert.accept()

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