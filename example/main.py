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
    
    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."

if __name__ == "__main__":
    unittest.main()