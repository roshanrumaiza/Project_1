import logging
import time
import pytest
from POM.Homepage import Homepage
from POM.Login import Login
from POM.User_page import UserPage
from conftest import setup
from conftest import capture_screenshot


#this line connects to the logger file
logger = logging.getLogger(__name__)

#Runs the setup fixtures from conftest file before every test case
@pytest.mark.usefixtures("setup")


class TestScenario:
    #Test_case 1:Verify URL is valid or not
    def test_valid_URL(self):
        logger.info("validating the Url {https://www.guvi.in}")
        try:
            current_url=self.driver.current_url
            assert "guvi.in" in current_url ,'Page not loaded successfully'
            logger.info("The URL:{https://www.guvi.in} loaded successfully")
            capture_screenshot(self.driver,"after validating URL")
        except Exception as e:
            logger.info(f"Unable to open URL due to {e} ")
            capture_screenshot(self.driver,"Unable to open URL")
            raise


    #Test_case 2:Verify whether the title of the webpage is correct
    def test_validate_title(self):
        logger.info("Validating the title of the webpage")
        try:
            title = self.driver.title
            assert title=='HCL GUVI | Learn to code in your native language','Mismatch in title'
            logger.info("The title has been validated")
            capture_screenshot(self.driver,"Validated title")
        except Exception as e:
            logger.info(f"The title is not as expected due to {e}")
            capture_screenshot(self.driver,"Title not verified")
            raise


    #Test_case 3 :Verify visibility and clickability of the Login button.
    def test_validation_of_login_button(self):
        logger.info("validating the login button")
        try:
            homepage=Homepage(self.driver)
            title=homepage.validate_visibility_clickability_of_login_button(self.driver)
            assert title=='HCL GUVI | Login','login button is not clickable'
            time.sleep(2)
            self.driver.back()
            logger.info("Login button is visible and clickable")
            capture_screenshot(self.driver,"After validating login button")
        except Exception as e:
            logger.info(f"Unable to validate login button due to {e}")
            capture_screenshot(self.driver,"Login button not clickable")
            raise



    #Test_case 4 :Verify visibility and clickability of the Sign-Up button.
    def test_validation_of_Sign_Up_button(self):
        logger.info("validating the Sign_Up button")
        try:
            homepage=Homepage(self.driver)
            current_url=homepage.validate_visibility_clickability_of_signup_button(self.driver)
            assert 'register' in current_url , 'Signup button not visible'
            self.driver.back()
            logger.info("Sign_up button is visible and clickable")
            capture_screenshot(self.driver,"After validating Sign_up button")
        except Exception as e:
            logger.info(f"Unable to validate sign_up button")
            capture_screenshot(self.driver,"Sign_Up button not validated")



    #Test_case 5 :Verify navigation to the Sign-In page via the Sign-Up button.
    def test_validation_of_Sign_In_via_Sign_Up_button(self):
        logger.info("Validating Sign_in Via Sign_Up")
        try:
            homepage=Homepage(self.driver)
            current_url = homepage.validate_signin_page_via_signup_page(self.driver)
            assert 'register' in current_url, 'Page not loaded properly'
            self.driver.back()
            logger.info("Sign_in Via Sign_up is validated")
            capture_screenshot(self.driver,"Sign_in via Sign_up button validated")
        except Exception as e:
            logger.info(f"Unable to validate sign_in via sign_up due to {e}")
            capture_screenshot(self.driver,"Sign_in via Sign_up not ")
            raise



    #Test _case 8:Verify that menu items like “Courses”, “LIVE Classes”, and “Practice” are displayed.
    def test_validate_menu_items(self):
        logger.info("Validate the menu items")
        try:
            homepage = Homepage(self.driver)
            homepage.validate_visibility_of_menu_items()
            logger.info("The menu items like Courses, LIVE Classes, and Practice are displayed and accessible")
            capture_screenshot(self.driver,"After validating menu items")
        except Exception as e:
            logger.info(f"unable to validate menu items")
            capture_screenshot(self.driver,"Menu items not present")


    #Test_case 9:Validate that the Dobby Guvi Assistant is present on the page.
    def test_validate_dobby_assistant(self):
        logger.info("Validating Dobby assistant")
        try:
            homepage = Homepage(self.driver)
            homepage.validate_dobby_guvi_assistant()
            logger.info("Dobby assistant is present on the page")
            capture_screenshot(self.driver,"validated dobby assistant")
        except Exception as e:
            logger.info(f"Dobby assistant is not present on the page")
            capture_screenshot(self.driver,"Dobby assistant is not present")



    #Test_case 7:Verify login with invalid credentials
    def test_invalid_login(self):
        logger.info("Validating the login with invalid credentials")
        try:
            login=Login(self.driver)
            error_msg=login.invalid_login(self.driver)
            assert error_msg =='Incorrect Email or Password', "Error message not displayed correctly "
            logger.info("The error message displayed correctly with invalid credentials")
            capture_screenshot(self.driver,"Invalid login")
        except Exception as e:
            logger.info(f"error message not displayed as expected due to {e}")
            capture_screenshot(self.driver,"Error message not displayed")
            raise



    #Test_case 6 :Verify login functionality with valid credentials.
    def test_valid_login(self):
        logger.info("Validating the login with valid credentials")
        try:
            login=Login(self.driver)
            title = login.valid_login(self.driver)
            assert title =='HCL GUVI | Learn to code in your native language', 'Login is not successful'
            logger.info("Login is successful")
            capture_screenshot(self.driver,"After successful login")
        except Exception as e:
            logger.info(f"Unable to login due to{e} ")
            capture_screenshot(self.driver,"Login failed")
            raise



    #Test_case 10:Validate logout functionality.
    def test_logout(self):
        logger.info("validating the logout")
        try:
            logout= UserPage()
            title=logout.logout(self.driver)
            assert title=='HCL GUVI | Learn to code in your native language' ,'Logout is not successful'
            logger.info("Logout is successful")
            capture_screenshot(self.driver,"After successful logout")
        except Exception as e:
            logger.info(f"Unable to logout due to {e}")
            capture_screenshot(self.driver,"Logout failed")
            raise





