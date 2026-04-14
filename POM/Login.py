import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import capture_screenshot
from TestDATA.data import GUVI
from TestLocators.locators import GUVILocators

#creating the class login
class Login:
    #creating the method and initializing the attributes
    def __init__(self,driver):
        #locating the elements and storing it in the attributes

        self.wait = WebDriverWait(driver,10)

    #creating a method for valid login
    def valid_login(self,driver):
        self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.username_locator)).send_keys(GUVI.valid_username)
        driver.find_element(*GUVILocators.password_locator).send_keys(GUVI.valid_password)
        self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.Login_locator)).click()
        time.sleep(2)
        return driver.title

    #creating a method for invalid login
    def invalid_login(self,driver):
        self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.login_locator)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.username_locator)).send_keys(GUVI.invalid_username)
        driver.find_element(*GUVILocators.password_locator).send_keys(GUVI.invalid_password)
        driver.find_element(*GUVILocators.Login_locator).click()
        err_msg=self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.error_msg_locator)).text
        driver.find_element(*GUVILocators.username_locator).clear()
        driver.find_element(*GUVILocators.password_locator).clear()
        return err_msg


