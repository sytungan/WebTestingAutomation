import unittest
from selenium import webdriver
from platform import system
from selenium.webdriver.common.keys import Keys

class TinhTeAutomationTesting(unittest.TestCase):
    """A sample test class to show how page object works"""
    
    def setUp(self):
        if system() == 'Windows':
            PATH = "./chrome_driver/chromedriver_win32/chromedriver.exe"
        elif system() == 'Linux':
            PATH = "./chrome_driver/chromedriver_linux64/chromedriver"
        elif system() == 'Darwin':
            PATH = "./chrome_driver/chromedriver_mac64/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.tinhte.vn")
        print("==========================START-TEST==========================")

    def search_(self, str):
        searchButton = self.driver.find_element_by_class_name("placeholder")
        searchButton.click()

        searchTextBox = self.driver.find_element_by_class_name("search-textbox")
        searchTextBox.send_keys(str)
        searchTextBox.send_keys(Keys.RETURN)

    def test_search_S0C(self):
        """Search without a character."""
        self.search_("")

    def test_search_S1C(self):
        """Search with text have an only character."""
        self.search_("k")

    def test_search_SOneorMoreSpace(self):
        """Search with text have only one or more space character."""
        self.search_("a simple string")

    def test_search_SNoSpace(self):
        """Search a string and no space character."""
        self.search_("aSimpleString")

    def test_search_SSpace(self):
        """Search a string with space character."""
        self.search_("    ")

    def test_search_SUnicode(self):
        """Search a string with unicode character."""
        self.search_("con chó mùa thu")

    def test_search_SLink(self):
        """Search a link."""
        self.search_("https://www.google.com/")
    
    def test_search_Shieroglyphics(self):
        """Search a link."""
        self.search_("ベトナム人") 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()