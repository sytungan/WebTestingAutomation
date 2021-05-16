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

driver.find_element_by_partial_link_text("Đăng nhập").click()
driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
driver.find_elements_by_class_name("button.primary")[3].click()
factBtn = driver.find_elements_by_class_name("create-fact")
factBtn[0].click()
time.sleep(10)
driver.quit()