from platform import platform
import selenium
from platform import system 
from selenium import webdriver
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
driver.quit()