from platform import platform
import selenium
from platform import system 
import time
from selenium import webdriver
print(system())
if system() == 'Windows':
    PATH = "./chrome_driver/chromedriver_win32/chromedriver.exe"
elif system() == 'Linux':
    PATH = "./chrome_driver/chromedriver_linux64/chromedriver"
elif system() == 'Darwin':
    PATH = "./chrome_driver/chromedriver_mac64/chromedriver"
dest = open("chrome_driver/notes.txt")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("./Cookies")
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.get("https://tinhte.vn/login")
print(driver.title)
# driver.find_element_by_class_name("fbLogin").click()
login = driver.find_elements_by_name("login")
login[2].send_keys("test")
button = driver.find_elements_by_class_name("button.primary")
button[3].click()
time.sleep(30)

driver.quit()