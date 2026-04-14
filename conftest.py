import logging
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from TestDATA.data import GUVI


@allure.step("Take screenshot and attach it to the report")
def capture_screenshot(driver,step_name):
    allure.attach(driver.get_screenshot_as_png(),name=step_name,attachment_type=allure.attachment_type.PNG)


#Running tests in both browser chrome and firefox for cross browser validation
@pytest.fixture(params=["chrome","firefox"], scope="class")
def setup(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # maximizing the window
    driver.maximize_window()
    driver.implicitly_wait(20)
    # go to the required URL
    driver.get(GUVI.GUVI_url)
    #to make driver available to all the test case in that class
    request.cls.driver = driver
    # yield pauses and checks if all the above steps are completed and continues the execution from line next to yield
    yield driver
    # closing browser
    driver.quit()


#logger file
def pytest_configure():
    logger=logging.getLogger()
    #setlevel for what we want
    logger.setLevel(logging.INFO)
    #format includes the details we want in theo utput
    formatter=logging.Formatter(fmt="%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    #to display the information in the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    #saving the logger in the mentioned file
    file_handler=logging.FileHandler("test_logs.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


