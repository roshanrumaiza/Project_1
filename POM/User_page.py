from TestLocators.locators import GUVILocators
from conftest import capture_screenshot
#creating class UserPage
class UserPage:
    #creating the method for logout
    def logout(self,driver):
        profile = driver.find_element(*GUVILocators.profile_icon_locator)
        driver.execute_script("arguments[0].click();", profile)

        logout = driver.find_element(*GUVILocators.sign_out_locator)
        driver.execute_script("arguments[0].click();", logout)
        return driver.title