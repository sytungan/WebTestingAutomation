from platform import platform
import selenium
import time
from platform import system 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print(system())
if system() == 'Windows':
    PATH = "./chrome_driver/chromedriver_win32/chromedriver.exe"
elif system() == 'Linux':
    PATH = "./chrome_driver/chromedriver_linux64/chromedriver"
elif system() == 'Darwin':
    PATH = "./chrome_driver/chromedriver_mac64/chromedriver"
dest = open("chrome_driver/notes.txt")
driver = webdriver.Chrome(PATH)
driver.get("https://www.tinhte.vn")
print(driver.title)


searchButton = driver.find_element_by_class_name("placeholder")
searchButton.click()

searchTextBox = driver.find_element_by_class_name("search-textbox")
searchTextBox.send_keys("test")
searchTextBox.send_keys(Keys.RETURN)
print(searchButton)
time.sleep(5)
driver.quit()