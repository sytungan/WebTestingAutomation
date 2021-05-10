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


    def test_search_S0C(self):
        """Search without a character."""
        searchButton = self.driver.find_element_by_class_name("placeholder")
        searchButton.click()

        searchTextBox = self.driver.find_element_by_class_name("search-textbox")
        searchTextBox.send_keys("")
        searchTextBox.send_keys(Keys.RETURN)

    def test_search_S1C(self):
        """Search with text have an only character."""
        searchButton = self.driver.find_element_by_class_name("placeholder")
        searchButton.click()

        searchTextBox = self.driver.find_element_by_class_name("search-textbox")
        searchTextBox.send_keys("hihii")
        searchTextBox.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()