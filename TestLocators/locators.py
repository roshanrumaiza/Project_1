# contains all the locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class GUVILocators:
    #Homepage locators
        login_locator = (By.XPATH, "(//button[text()='Login'])[1]")
        sign_up_locator = (By.XPATH, "(//button[text()='Sign up'])[1]")
        live_classes_locator = (By.XPATH, "(//p[text()='LIVE Classes'])[1]")
        courses_locator = (By.XPATH, "(//p[text()='Courses'])[1]")
        practice_locator = (By.XPATH, "(//p[text()='Practice'])[1]")
        Dobby_Assistant_locator = (By.ID, 'zs_fl_chat')
        sign_in_locator = (By.XPATH, "//a[@class='login']")


        #User_page locators

        profile_icon_locator = (By.XPATH, '(//div[contains(@class,"account-box-toggler")])[1]')
        sign_out_locator = (By.XPATH, '(//p[text()="Sign Out"])[1]')

        #Login locators
        username_locator = (By.XPATH, "(//input[@type='email'])[1]")
        password_locator = (By.XPATH, "(//input[@type='password'])[1]")
        Login_locator = (By.XPATH, "(//a[text()='Login'])[1]")
        error_msg_locator = (By.XPATH, "(//div[text()='Incorrect Email or Password'])[1]")