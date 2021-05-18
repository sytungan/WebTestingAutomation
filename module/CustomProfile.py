from platform import platform

import os
import time
import unittest
import selenium
from selenium import webdriver
from platform import system
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
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


def signUp():
    driver.find_element_by_partial_link_text("Đăng nhập").click()
    driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
    driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
    driver.find_elements_by_class_name("button.primary")[3].click()

# def fillText(driver,text,locator):
#     textfield = driver.find_element_by_id(locator)
#     textfield.clear()
#     textfield.send_keys(text)
#     textfield.send_keys(Keys.RETURN)
#     time.sleep(1)

# def fillPassText(driver,text,locator):
#     textfield = driver.find_element_by_id(locator)
#     textfield.clear()
#     textfield.send_keys(text)

# def makePost(driver,paragraph):
#     iframe = driver.find_element_by_tag_name("iframe")
#     driver.switch_to.frame(iframe)
#     pTag = driver.find_element_by_tag_name("p")
#     driver.execute_script("arguments[0].textContent = arguments[1];", pTag, paragraph)
#     driver.switch_to.default_content()
#     textfield = driver.find_element_by_id("ctrl_location")
#     textfield.send_keys(Keys.RETURN)



# def CA():
#     """ Change avatar """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     driver.find_element_by_class_name("img.m").click()
#     time.sleep(2)
#     s = driver.find_element_by_class_name("labelText")
#     input_text= s.find_element_by_tag_name("input")
#     input_text.send_keys(os.getcwd() + "\\image.jpg")
#     time.sleep(1)
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Tải lên thành công"
#     # btn=driver.find_element_by_class_name("buttons")

# def CARIT():
#     """ Change avatar with wrong image type """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     driver.find_element_by_class_name("img.m").click()
#     s = driver.find_element_by_class_name("labelText")
#     input_text= s.find_element_by_tag_name("input")
#     input_text.send_keys(os.getcwd() + "\\CustomProfile.jpg")
#     failed = len(driver.find_elements_by_class_name("xenOverlay"))
#     # assert failed, 1

# def FPNT():
#     """ Fill place with no text """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"","ctrl_location")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FPWT():
#     """ Fill place with text """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"66/7, Hùng Vương, phường 1, quận 10, TP.HCM","ctrl_location")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."


# def FPWU():
#     """ Fill place with unicode """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"ベトナムの都市","ctrl_location")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FPWL():
#     """ Fill place with numerous char"""
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"66/7, Hùng Vương, phường 1, quận 10, TP.HCM,MV không phải là một câu chuyện tình yêu mà như một khoảng hoài niệm về tuổi trẻ/ tuổi thơ ngây an nhiên (tiếng tút micro ở đầu và cuối clip như là mở đầu/kết thúc của một đoạn băng tư liệu ko liên quan gì đến accident).","ctrl_location")
#     failed = len(driver.find_elements_by_class_name("xenOverlay"))
#     # assert failed, 1


# def FJT():
#     """ Fill job with text """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"Kỹ sư","occupation")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FJNT():
#     """ Fill job with no text """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"","occupation")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FP():
#     """Fill phone number"""
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     textfield = driver.find_element_by_id("ctrl_custom_field_citizenPhoneNumber")
#     fillText(driver,"0919891230","ctrl_custom_field_citizenPhoneNumber")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FPE():
#     """Fill phone number with Empty number """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"","ctrl_custom_field_citizenPhoneNumber")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FPS():
#     """ Fill string in phone number """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"Đây là 1 chuỗi","ctrl_custom_field_citizenPhoneNumber")
#     failed = len(driver.find_elements_by_class_name("xenOverlay"))
#     # assert failed, 1


# def FIU():
#     """ Fill user's information """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     makePost(driver,"Tôi là An ngu")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FIUC():
#     """ Fill user's information with unicode """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     makePost(driver,"ベトナム人")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FIUS():
#     """ Fill user's information with special character """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     makePost(driver,"@#$%!")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FIUI():
#     """ Fill user's information with icon """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     makePost(driver,"@@,:>,:)")
#     time.sleep(1)
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FA():
#     """ Fill following account with text """
#     signUp()
#     driver.get("https://tinhte.vn/account/following")
#     fillText(driver,"Ankunkun","ctrl_users")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FAE():
#     """ Fill following account with empty text """
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"Ankunkun","ctrl_users")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FAU():
#     """Fill following account with unicode"""
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"うずまきナルト","ctrl_users")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def FAL():
#     """Fill following account with link"""
#     signUp()
#     driver.get("https://tinhte.vn/account/personal-details")
#     fillText(driver,"https://tinhte.vn/members/ankunkun.2693711/","ctrl_users")
#     success = driver.find_element_by_class_name("content.baseHtml").text
#     # assert success,"Nội dung đã được cập nhật thành công."

# def CP():
#     """Change password"""
#     signUp()
#     driver.get("https://tinhte.vn/account/security")
#     fillPassText(driver,"うずまきナルト","ctrl_password_original")
#     fillPassText(driver,"xinchaocacban","ctrl_password")
#     fillPassText(driver,"xinchaocacban","ctrl_password_confirm")
#     confirm = driver.find_element_by_id("ctrl_password_confirm")
#     confirm.send_keys(Keys.RETURN)

#     failed = len(driver.find_elements_by_class_name("xenOverlay"))
#     # assert success,"Nội dung đã được cập nhật thành công."

# def CP8():
#     """Change password with less than 8 character"""
#     signUp()
#     driver.get("https://tinhte.vn/account/security")
#     fillPassText(driver,"うずまきナルト","ctrl_password_original")
#     fillPassText(driver,"うずまきナルト","ctrl_password")
#     fillPassText(driver,"うずまきナルト","ctrl_password_confirm")
#     confirm = driver.find_element_by_id("ctrl_password_confirm")
#     confirm.send_keys(Keys.RETURN)

#     failed = len(driver.find_elements_by_class_name("xenOverlay"))
#     # assert success,"Nội dung đã được cập nhật thành công."

# def CPES():
#     """Change password with empty string"""
#     signUp()
#     driver.get("https://tinhte.vn/account/security")
#     fillPassText(driver,"うずまきナルト","ctrl_password_original")
#     fillPassText(driver,"","ctrl_password")
#     fillPassText(driver,"","ctrl_password_confirm")
#     confirm = driver.find_element_by_id("ctrl_password_confirm")
#     confirm.send_keys(Keys.RETURN)
#     time.sleep(2)
#     failed = len(driver.find_elements_by_class_name("close.OverlayCloser"))
#     print(failed)
#     # assert failed, 1


# def CPOP():
#     """Change password with old password"""
#     signUp()
#     driver.get("https://tinhte.vn/account/security")
#     fillPassText(driver,"うずまきナルト","ctrl_password_original")
#     fillPassText(driver,"うずまきナルト","ctrl_password")
#     fillPassText(driver,"うずまきナルト","ctrl_password_confirm")
#     confirm = driver.find_element_by_id("ctrl_password_confirm")
#     confirm.send_keys(Keys.RETURN)
#     failed = len(driver.find_elements_by_class_name("xenOverlay"))
#     # assert success,"Nội dung đã được cập nhật thành công."



# def CPWU():
#     """Change password with unicode password"""
#     signUp()
#     driver.get("https://tinhte.vn/account/security")
#     fillPassText(driver,"うずまきナルト","ctrl_password_original")
#     fillPassText(driver,"うずまきナルト","ctrl_password")
#     fillPassText(driver,"うずまきナルト","ctrl_password_confirm")
#     confirm = driver.find_element_by_id("ctrl_password_confirm")
#     confirm.send_keys(Keys.RETURN)
#     time.sleep(2)
#     failed = len(driver.find_elements_by_class_name("close.OverlayCloser"))
#     print(failed)
#     # assert success,"Nội dung đã được cập nhật thành công."

def CPW():
    """Change password with unicode password"""
    signUp()
    driver.get("https://tinhte.vn/account/security")
    fillPassText(driver,"うずまきナルト","ctrl_password_original")
    fillPassText(driver,"coconchimnho","ctrl_password")
    fillPassText(driver,"coconchimto","ctrl_password_confirm")
    confirm = driver.find_element_by_id("ctrl_password_confirm")
    confirm.send_keys(Keys.RETURN)

#     failed = len(driver.find_elements_by_class_name("xenOverlay"))

#     # assert success,"Nội dung đã được cập nhật thành công."

def CPW():
    """Change password with unicode password"""
    signUp()
    driver.get("https://tinhte.vn/thread/dieu-khien-bang-giong-noi-tren-xe-hoi-ngay-cang-da-dang-va-tien-loi-dang-lam-quen-de-dung.3328477/")
    driver.find_element_by_xpath("//textarea[@placeholder='Viết bình luận nào bạn ơi...']").send_keys("123")
    time.sleep(4)
CPW()
print(driver.title)
driver.quit()