from platform import platform
import selenium
from platform import system 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
dest = open("chrome_driver/notes.txt")
driver = webdriver.Chrome(PATH)
driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
def login(driver):
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3593820457.thread-login")))
    except:
        driver.quit()
    search.click()
     # driver.get("https://tinhte.vn")
    # if len(driver.find_elements_by_class_name("jsx-1783754700.blue-switch.header-mode")) == 1:
    #     return True
    # driver.find_element_by_partial_link_text("Đăng nhập").click()
    driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
    driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
    driver.find_elements_by_class_name("button.primary")[3].click()

def CoT1(driver):
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3593820457.thread-login")))
    except:
        driver.quit()
    search.click()

def CoT2(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3593820457.post-reply-submit")))
    except:
        driver.quit()
    search.click()

def CoT3(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"jsx-3593820457.post-reply-main ")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("textarea")
    search.send_keys("                                                                      ")
    search = search.find_element_by_xpath("//button[contains( text( ), 'Đăng')]")
    search.click()

def CoT4(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"jsx-3593820457.post-reply-main ")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("textarea")
    search.send_keys("https://www.google.com")                                                                      
    search = search.find_element_by_xpath("//button[contains( text( ), 'Đăng')]")
    search.click()

def CoT5(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"jsx-3593820457.post-reply-main ")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("textarea")
    search.send_keys("ベトナム人")                                                                      
    search = search.find_element_by_xpath("//button[contains( text( ), 'Đăng')]")
    search.click()

def Cot6(driver):
    CoT5(driver)
    time.sleep(2)
    driver.refresh()
    count = 2
    breaker = 0
    while(1):
        search = driver.find_element_by_class_name("jsx-1984507624.thread-comments__container")
        search = search.find_elements_by_class_name("jsx-1984507624")
        for each in search:
            number = each.find_elements_by_tag_name("button")
            if (len(number)>=5):
                breaker += 1
                break
        if breaker == 2:
            break    
        time.sleep(2)
        driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/page-"+str(count))
        count += 1
        if (count>10):
            break
    number[3].click()
    driver.find_element_by_class_name("jsx-3932553558.button.active").click()

def Cot7(driver):
    login(driver)
    count = 2
    breaker = 0
    while(1):
        search = driver.find_element_by_class_name("jsx-1984507624.thread-comments__container")
        search = search.find_elements_by_class_name("jsx-1984507624")
        for each in search:
            number = each.find_elements_by_tag_name("button")
            if (len(number)>=5):
                breaker += 1
                break
        if breaker == 2:
            break    
        time.sleep(2)
        driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/page-"+str(count))
        count += 1
        if (count>10):
            break
    number[3].click()
    driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    driver.find_element_by_xpath("//button[contains( text( ), 'Sửa')]").click()


def Cot10(driver):
    login(driver)
    driver.find_element_by_class_name("jsx-3529665607.sticker-button").click()
    time.sleep(2)
    search = driver.find_element_by_class_name("jsx-3529665607.stickers")
    search.find_elements_by_tag_name("button")[0].click()
    driver.find_element_by_class_name("jsx-3529665607.sticker-button").click()
    time.sleep(2)
    search = driver.find_element_by_class_name("jsx-3529665607.stickers")
    search.find_elements_by_tag_name("button")[1].click()

Cot7(driver)
time.sleep(5)
driver.quit()