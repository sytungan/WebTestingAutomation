from platform import platform
import selenium
from platform import system 
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def signUp():
    driver.find_element_by_partial_link_text("Đăng nhập").click()
    driver.find_elements_by_name("login")[2].send_keys("thuy113113")
    driver.find_elements_by_name("password")[2].send_keys("10121999HQK")
    # driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
    # driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
    driver.find_elements_by_class_name("button.primary")[3].click()

def createFact():
    factBtn = driver.find_elements_by_class_name("create-fact")
    factBtn[0].click()
    time.sleep(10)

def createShare():
    factBtn = driver.find_elements_by_class_name("create-fact")
    factBtn[0].click()
    shareBtn = driver.find_elements_by_class_name("switch-toggle")
    shareBtn[0].click()
    time.sleep(10)

def CFT1():
    #create fact without character
    createFact()
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CFT2():
    #create fact with less than 10 charater
    createFact()
    content = driver.find_elements_by_class_name("createTinhteFact")
    content[0].send_keys("testing")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CFT3():
    # create fact with the wrong format picture
    createFact()
    picBtn = driver.find_elements_by_class_name("image-picker")
    inputFile = picBtn[0].find_elements_by_tag_name("input")
    inputFile[0].send_keys(os.getcwd() + "\\image.txt")
    time.sleep(10)

def CFT4():
    # create fact with the correct format but without text
    createFact()
    picBtn = driver.find_elements_by_class_name("image-picker")
    inputFile = picBtn[0].find_elements_by_tag_name("input")
    inputFile[0].send_keys(os.getcwd() + "\\image.jpg")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CFT5():
    #create fact with the correct format but less than 10 character
    createFact()
    picBtn = driver.find_elements_by_class_name("image-picker")
    inputFile = picBtn[0].find_elements_by_tag_name("input")
    inputFile[0].send_keys(os.getcwd() + "\\image.jpg")
    content = driver.find_elements_by_class_name("createTinhteFact")
    content[0].send_keys("testing")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CFT6():
    #create fact with more than 10 charater
    createFact()
    content = driver.find_elements_by_class_name("createTinhteFact")
    content[0].send_keys("Software testing")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CFT7():
    #create fact with more than 10 charater with picture
    createFact()
    content = driver.find_elements_by_class_name("createTinhteFact")
    picBtn = driver.find_elements_by_class_name("image-picker")
    inputFile = picBtn[0].find_elements_by_tag_name("input")
    inputFile[0].send_keys(os.getcwd() + "\\image.jpg")
    content[0].send_keys("Software testing")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(20)

def CST1():
    #switch to share mode
    createShare()

def CST2():
    #create share without character
    createShare()
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CST3():
    #create share with less than 10 charater
    createShare()
    content = driver.find_elements_by_tag_name("textarea")
    content[0].send_keys("testing")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CST4():
    #create share with more than 10 charater
    createShare()
    content = driver.find_elements_by_tag_name("textarea")
    content[0].send_keys("Software testing")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)

def CST5():
    # create share and add link then switch to Fact mode
    createFact()
    shareBtn = driver.find_elements_by_class_name("switch-toggle")
    shareBtn[0].click()
    driver.find_elements_by_class_name("thread-background-switch")[0].click()
    time.sleep(1)
    shareBtn = driver.find_elements_by_class_name("switch-toggle")
    shareBtn[0].click()
    time.sleep(10)

def CST6():
    # create share and click change theme button then switch to Fact mode
    createFact()
    shareBtn = driver.find_elements_by_class_name("switch-toggle")
    shareBtn[0].click()
    driver.find_elements_by_class_name("thread-background-switch")[1].click()
    time.sleep(1)
    s = driver.find_elements_by_class_name("thread-background-image")
    s[0].click()
    time.sleep(1)
    shareBtn = driver.find_elements_by_class_name("switch-toggle")
    shareBtn[0].click()
    time.sleep(10)

def CST7():
    #Create share with link
    createShare()
    content = driver.find_elements_by_tag_name("textarea")
    content[0].send_keys("Software testing")
    time.sleep(1)
    driver.find_elements_by_class_name("thread-background-switch")[0].click()
    time.sleep(1)
    driver.find_elements_by_class_name("link-input")[0].send_keys("https://www.youtube.com/channel/UCVJ6jQF0XOaBVTPCT-en2sw")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)


def CST8():
    #create share with theme
    createShare()
    driver.find_elements_by_class_name("thread-background-switch")[1].click()
    time.sleep(1)
    s = driver.find_elements_by_class_name("thread-background-image")
    s[0].click()
    time.sleep(1)
    content = driver.find_elements_by_tag_name("textarea")
    content[0].send_keys("Software testing")
    time.sleep(1)
    postBtn = driver.find_elements_by_class_name("publish-btn")
    postBtn[0].click()
    time.sleep(10)


def CST9():
    # create share and test long post feature
    createShare()
    driver.find_elements_by_class_name("category-selector-switch")[0].click()
    time.sleep(10)
    driver.find_elements_by_class_name("title-input")[0].send_keys("Ba rọi béo - Thầy giáo ba")
    time.sleep(1)
    driver.find_elements_by_class_name("ck-content")[0].send_keys("Baroibeo tên thật là Phan Tấn Trung, sinh năm 1989. Anh là rapper thế hệ F1 tự xưng. Baroibeo từng là tuyển thủ Liên Minh Huyền Thoại chuyên nghiệp và hiện tại là 1 streamer nổi tiếng Việt Nam. Hiện nay, kênh Youtube của Thầy Giáo Ba có khoảng nửa triệu người đăng ký còn trang Facebook thì cũng có tới hàng trăm ngàn lượt theo dõi. Phan BaRoiBeo Tấn Trung is a streamer and top laner for Academy SBTC. He is also known as Thầy Giáo Ba. He was previously known as 3RB, Teacher Ba and Ba Gà.")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("save-button")
    postBtn[0].click()
    time.sleep(10)

def CST10():
    # create share andtest save function in long post feature
    createShare()
    driver.find_elements_by_class_name("category-selector-switch")[0].click()
    time.sleep(10)
    driver.find_elements_by_class_name("title-input")[0].send_keys("Ba rọi béo - Thầy giáo ba")
    time.sleep(1)
    driver.find_elements_by_class_name("ck-content")[0].send_keys("Baroibeo tên thật là Phan Tấn Trung, sinh năm 1989. Anh là rapper thế hệ F1 tự xưng. Baroibeo từng là tuyển thủ Liên Minh Huyền Thoại chuyên nghiệp và hiện tại là 1 streamer nổi tiếng Việt Nam. Hiện nay, kênh Youtube của Thầy Giáo Ba có khoảng nửa triệu người đăng ký còn trang Facebook thì cũng có tới hàng trăm ngàn lượt theo dõi. Phan BaRoiBeo Tấn Trung is a streamer and top laner for Academy SBTC. He is also known as Thầy Giáo Ba. He was previously known as 3RB, Teacher Ba and Ba Gà.")
    time.sleep(3)
    postBtn = driver.find_elements_by_class_name("toolbar-save-button")
    postBtn[0].click()
    time.sleep(10)

def CST11():
    # create share and test and test auto save function in long post feature
    createShare()
    driver.find_elements_by_class_name("category-selector-switch")[0].click()
    time.sleep(10)
    driver.find_elements_by_class_name("title-input")[0].send_keys("Ba rọi béo - Thầy giáo ba")
    time.sleep(1)
    driver.find_elements_by_class_name("ck-content")[0].send_keys("Baroibeo tên thật là Phan Tấn Trung, sinh năm 1989. Anh là rapper thế hệ F1 tự xưng. Baroibeo từng là tuyển thủ Liên Minh Huyền Thoại chuyên nghiệp và hiện tại là 1 streamer nổi tiếng Việt Nam. Hiện nay, kênh Youtube của Thầy Giáo Ba có khoảng nửa triệu người đăng ký còn trang Facebook thì cũng có tới hàng trăm ngàn lượt theo dõi. Phan BaRoiBeo Tấn Trung is a streamer and top laner for Academy SBTC. He is also known as Thầy Giáo Ba. He was previously known as 3RB, Teacher Ba and Ba Gà.")
    time.sleep(3)
    time.sleep(70) #After 1 minute, auto save function will enable

    
signUp()
CST8()
driver.quit()