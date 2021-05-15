import time
import unittest
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.common.keys import Keys

class SeleniumDriver(object):
    def __init__(
        self,
        # chromedriver path
        driver_path='./chrome_driver/chromedriver_win32/chromedriver.exe',
        # pickle file path to store cookies
        cookies_file_path='./Cookies',
        # list of websites to reuse cookies with
        cookies_websites=["https://tinhte.vn"]

    ):
        self.driver_path = driver_path
        self.cookies_file_path = cookies_file_path
        self.cookies_websites = cookies_websites
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            executable_path=self.driver_path,
            options=chrome_options
        )
        try:
            # load cookies for given websites
            cookies = pickle.load(open(self.cookies_file_path, "rb"))
            for website in self.cookies_websites:
                self.driver.get(website)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                self.driver.refresh()
        except Exception as e:
            # it'll fail 
            # for the first time, when cookie file is not present
            print(str(e))
            print("Error loading cookies")

    def save_cookies(self):
        # save cookies
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(self.cookies_file_path, "wb"))

    def close_all(self):
        # close all open tabs
        if len(self.driver.window_handles) < 1:
            return
        for window_handle in self.driver.window_handles[:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()

    def quit(self):
        self.save_cookies()
        self.close_all()

def tinhte_login(driver):
    # driver.get("https://tinhte.vn")
    # if len(driver.find_elements_by_class_name("jsx-1783754700.blue-switch.header-mode")) == 1:
    #     return True
    driver.find_element_by_partial_link_text("Đăng nhập").click()
    driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
    driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
    driver.find_elements_by_class_name("button.primary")[3].click()

class TinhTeAutomationTesting(unittest.TestCase):
    """A sample test class to show how page object works"""
    
    def setUp(self):
        if system() == 'Windows':
            self.PATH = "./chrome_driver/chromedriver_win32/chromedriver.exe"
        elif system() == 'Linux':
            self.PATH = "./chrome_driver/chromedriver_linux64/chromedriver"
        elif system() == 'Darwin':
            self.PATH = "./chrome_driver/chromedriver_mac64/chromedriver"
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://tinhte.vn")

        print("==========================START-TEST==========================")
    
    def login_(self):
        # self.driver.close()
        # seleniumObj = SeleniumDriver(driver_path=self.PATH)
        # self.driver = seleniumObj.driver
        # if tinhte_login(self.driver):
        #     print("Already logged in")
        # else:
        #     print("Not logged in. Login")
        #     seleniumObj.save_cookies()
        tinhte_login(self.driver)
            

    def search_(self, str):
        searchButton = self.driver.find_element_by_class_name("placeholder")
        searchButton.click()

        searchTextBox = self.driver.find_element_by_class_name("search-textbox")
        searchTextBox.send_keys(str)
        searchTextBox.send_keys(Keys.RETURN)

    # def test_search_S0C(self):
    #     """Search without a character."""
    #     self.search_("")

    # def test_search_S1C(self):
    #     """Search with text have an only character."""
    #     self.search_("k")

    # def test_search_SOneorMoreSpace(self):
    #     """Search with text have only one or more space character."""
    #     self.search_("a simple string")

    # def test_search_SNoSpace(self):
    #     """Search a string and no space character."""
    #     self.search_("aSimpleString")

    # def test_search_SSpace(self):
    #     """Search a string with space character."""
    #     self.search_("    ")

    # def test_search_SUnicode(self):
    #     """Search a string with unicode character."""
    #     self.search_("con chó mùa thu")

    # def test_search_SLink(self):
    #     """Search a link."""
    #     self.search_("https://www.google.com/")
    
    # def test_search_Shieroglyphics(self):
    #     """Search a link."""
    #     self.search_("ベトナム人")
    def makeMessage(self, participants, title, paragraph):
        self.driver.find_element_by_class_name("jsx-2971791619.main").click()
        self.driver.find_element_by_class_name("jsx-756775732.view-all-btn").click()
        self.driver.find_element_by_class_name("callToAction").click()
        participantBox = self.driver.find_element_by_id("ctrl_recipients")

        for participant in participants:
            participantBox.send_keys(participant)
            time.sleep(1)
            participantBox.send_keys(Keys.RETURN)

        titleBox = self.driver.find_element_by_id("ctrl_title")
        titleBox.send_keys(title)

        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        pTag = self.driver.find_element_by_tag_name("p")
        self.driver.execute_script("arguments[0].textContent = arguments[1];", pTag, paragraph)

        self.driver.switch_to.default_content()

        writeBtn = self.driver.find_elements_by_class_name("button.primary")[1]
        writeBtn.click()
        time.sleep(10)

    def test_CMFullComplete(self):
        """Create a message with at least one participants and message not empty"""
        self.login_()
        self.makeMessage(["hi", "hehe"], "hello", "Tui la An ne")
    
    def test_CMWithoutPar(self):
        """Create a message without participants"""
        self.login_()
        self.makeMessage([],"Hello", "Lai la tui day")

    def test_CMWithoutMess(self):
        """Create a message without text field"""
        self.login_()
        self.makeMessage(["ankun"],"Hello", "")

    def test_CMWithUnvalidPar(self):
        """Create a message with a not valid recipient."""
        self.login_()
        self.makeMessage(["conchomuathumuadongmuaha"],"Hello", "Lai la tui day")

    def test_CMWithUnValidTitle(self):
        """Create a message with a not valid recipient."""
        self.login_()
        self.makeMessage(["ankun"],"", "Lai la tui day")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()