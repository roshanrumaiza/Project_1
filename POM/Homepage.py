
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestLocators.locators import GUVILocators
from conftest import capture_screenshot

#creating method homepage
class Homepage():

    def __init__(self,driver):
        self.wait=WebDriverWait(driver,10)
    #creating a method for validating login button
    def validate_visibility_clickability_of_login_button(self,driver):
        login_displayed =self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.login_locator)).is_displayed()
        if login_displayed is True:
            print("Login button is visible")
        else:
            print("login is not visible")
        self.wait.until(expected_conditions.element_to_be_clickable(GUVILocators.login_locator)).click()
        return driver.title

    #creating a method for validating signup button
    def validate_visibility_clickability_of_signup_button(self,driver):
        signup_displayed =self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.sign_up_locator)).is_displayed()
        if signup_displayed is True:
            print("Signup button is visible")
        else:
            print("signup button not visible")
        self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.sign_up_locator)).click()
        return driver.current_url

    #creating a method for validating sign in page via sign up
    def validate_signin_page_via_signup_page(self,driver):
        self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.sign_up_locator)).click()
        sign_in_button_visible = self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.sign_in_locator)).is_displayed()
        if sign_in_button_visible is True:
            print("sign_in button is visible")
        else:
            print("sign_in button not visible")
        return driver.current_url

    #validating menu items
    def validate_visibility_of_menu_items(self):
        Live_class_visible = self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.live_classes_locator)).is_displayed()
        Courses_visible= self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.courses_locator)).is_displayed()
        Practice_visible= self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.practice_locator)).is_displayed()
        if Live_class_visible and Courses_visible and Practice_visible is True:
            print("The menu items like Courses, LIVE Classes, and Practice are displayed")
        else:
            print("The menu items like Courses, LIVE Classes, and Practice are not displayed")

    #creating a method to Validate dobby Assistant
    def validate_dobby_guvi_assistant(self):
        Dobby_Assistant=self.wait.until(expected_conditions.visibility_of_element_located(GUVILocators.Dobby_Assistant_locator)).is_displayed()
        if Dobby_Assistant is True:
            print("Dobby Assistant is present on the page")
        else:
            print("Dobby Assistant is not present on the page")

