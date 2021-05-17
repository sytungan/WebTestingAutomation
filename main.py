import time
import os
import unittest
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.common.keys import Keys

class SeleniumDriver(object):
    def __init__(
        self,
        # chromedriver path
        driver_path='./chrome_driver/chromedriver_win32/chromedriver.exe',
        # pickle file path to store cookies
        cookies_file_path='./Cookies',
        # list of websites to reuse cookies with
        cookies_websites=["https://tinhte.vn"]

    ):
        self.driver_path = driver_path
        self.cookies_file_path = cookies_file_path
        self.cookies_websites = cookies_websites
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            executable_path=self.driver_path,
            options=chrome_options
        )
        try:
            # load cookies for given websites
            cookies = pickle.load(open(self.cookies_file_path, "rb"))
            for website in self.cookies_websites:
                self.driver.get(website)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                self.driver.refresh()
        except Exception as e:
            # it'll fail 
            # for the first time, when cookie file is not present
            print(str(e))
            print("Error loading cookies")

    def save_cookies(self):
        # save cookies
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(self.cookies_file_path, "wb"))

    def close_all(self):
        # close all open tabs
        if len(self.driver.window_handles) < 1:
            return
        for window_handle in self.driver.window_handles[:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()

    def quit(self):
        self.save_cookies()
        self.close_all()

def tinhte_login(driver):
    # driver.get("https://tinhte.vn")
    # if len(driver.find_elements_by_class_name("jsx-1783754700.blue-switch.header-mode")) == 1:
    #     return True
    driver.find_element_by_partial_link_text("Đăng nhập").click()
    driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
    driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
    driver.find_elements_by_class_name("button.primary")[3].click()

class TinhTeAutomationTesting(unittest.TestCase):
    """A sample test class to show how page object works"""
    
    def setUp(self):
        if system() == 'Windows':
            self.PATH = "./chrome_driver/chromedriver_win32/chromedriver.exe"
        elif system() == 'Linux':
            self.PATH = "./chrome_driver/chromedriver_linux64/chromedriver"
        elif system() == 'Darwin':
            self.PATH = "./chrome_driver/chromedriver_mac64/chromedriver"
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://tinhte.vn")

        print("==========================START-TEST==========================")
    
    def login_(self):
        # self.driver.close()
        # seleniumObj = SeleniumDriver(driver_path=self.PATH)
        # self.driver = seleniumObj.driver
        # if tinhte_login(self.driver):
        #     print("Already logged in")
        # else:
        #     print("Not logged in. Login")
        #     seleniumObj.save_cookies()
        tinhte_login(self.driver)
            

    def search_(self, str):
        searchButton = self.driver.find_element_by_class_name("placeholder")
        searchButton.click()

        searchTextBox = self.driver.find_element_by_class_name("search-textbox")
        searchTextBox.send_keys(str)
        searchTextBox.send_keys(Keys.RETURN)
        # time.sleep(10)

    # def test_search_S0C(self):
    #     """Search without a character."""
    #     self.search_("")

    # def test_search_S1C(self):
    #     """Search with text have an only character."""
    #     self.search_("k")

    # def test_search_SOneorMoreSpace(self):
    #     """Search with text have only one or more space character."""
    #     self.search_("a simple string")

    # def test_search_SNoSpace(self):
    #     """Search a string and no space character."""
    #     self.search_("aSimpleString")

    # def test_search_SSpace(self):
    #     """Search a string with space character."""
    #     self.search_("    ")

    # def test_search_SUnicode(self):
    #     """Search a string with unicode character."""
    #     self.search_("con chó mùa thu")

    # def test_search_SLink(self):
    #     """Search a link."""
    #     self.search_("https://www.google.com/")
    
    # def test_search_Shieroglyphics(self):
    #     """Search a link."""
    #     self.search_("ベトナム人")
    def makeMessage(self, participants, title, paragraph):
        self.driver.find_element_by_class_name("jsx-2971791619.main").click()
        self.driver.find_element_by_class_name("jsx-756775732.view-all-btn").click()
        self.driver.find_element_by_class_name("callToAction").click()
        participantBox = self.driver.find_element_by_id("ctrl_recipients")

        for participant in participants:
            participantBox.send_keys(participant)
            time.sleep(1)
            participantBox.send_keys(Keys.RETURN)

        titleBox = self.driver.find_element_by_id("ctrl_title")
        titleBox.send_keys(title)

        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        pTag = self.driver.find_element_by_tag_name("p")
        self.driver.execute_script("arguments[0].textContent = arguments[1];", pTag, paragraph)

        self.driver.switch_to.default_content()

        writeBtn = self.driver.find_elements_by_class_name("button.primary")[1]
        writeBtn.click()
        # time.sleep(10)

    # def test_CMFullComplete(self):
    #     """Create a message with at least one participants and message not empty"""
    #     self.login_()
    #     self.makeMessage(["hi", "hehe"], "hello", "Tui la An ne")
    
    # def test_CMWithoutPar(self):
    #     """Create a message without participants"""
    #     self.login_()
    #     self.makeMessage([],"Hello", "Lai la tui day")

    # def test_CMWithoutMess(self):
    #     """Create a message without text field"""
    #     self.login_()
    #     self.makeMessage(["ankun"],"Hello", "")

    # def test_CMWithUnvalidPar(self):
    #     """Create a message with a not valid recipient."""
    #     self.login_()
    #     self.makeMessage(["conchomuathumuadongmuaha"],"Hello", "Lai la tui day")

    # def test_CMWithUnValidTitle(self):
    #     """Create a message with a not valid recipient."""
    #     self.login_()
    #     self.makeMessage(["ankun"],"", "Lai la tui day")
    def makeReview(self, title, price, description, like, dislike, advice, isSendImg = True):
        self.driver.find_element_by_class_name("jsx-817685855.cta").click()
        txtBox = self.driver.find_elements_by_class_name("review-editor-text-input")
        txtBox[0].send_keys(title)
        txtBox[1].send_keys(price)
        txtBox[2].send_keys(description)
        txtBox[3].send_keys(like)
        txtBox[4].send_keys(dislike)
        txtBox[5].send_keys(advice)
        section = self.driver.find_elements_by_class_name("jsx-2282145060.section-container")
        img = section[3].find_element_by_tag_name("input")
        self.driver.execute_script("arguments[0].setAttribute('style','display:')", img)
        if isSendImg:
            img.send_keys(os.getcwd() + ("\image.png" if system() == 'Windows' else "/image.png"))
            time.sleep(5)
    # def test_RVFullComplete(self):
    #     """Create a review full infomation"""
    #     self.login_()
    #     self.makeReview("iPhone 12 Pro Max", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB", 
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp", 
    #         "Màn hình hơi nhỏ", "Nên mua")
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("jsx-1378818985.thread-is-draft")) == 1)

    # def test_RVWithoutName(self):
    #     """Create a review without a product name"""
    #     self.login_()
    #     self.makeReview("", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB", 
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp", 
    #         "Màn hình hơi nhỏ", "Nên mua")
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("jsx-2282145060.error")) == 1)

    # def test_RVWithoutImage(self):
    #     """Create a review without a product name"""
    #     self.login_()
    #     self.makeReview("IP12", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB", 
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp", 
    #         "Màn hình hơi nhỏ", "Nên mua", False)
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("jsx-1378818985.thread-is-draft")) == 1)
    
    # def test_RVEdit(self):
    #     """Edit a review exist"""
    #     self.login_()
    #     self.makeReview("IP12", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB", 
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp", 
    #         "Màn hình hơi nhỏ", "Nên mua")
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     time.sleep(5)
    #     self.driver.find_element_by_class_name("jsx-2176532799.moderator-action__button").click()
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("jsx-1378818985.thread-is-draft")) == 1)

    # def test_RVDelete(self):
    #     """Delete a review exist"""
    #     self.login_()
    #     self.makeReview("IP12", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB", 
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp", 
    #         "Màn hình hơi nhỏ", "Nên mua")
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     time.sleep(5)
    #     self.driver.find_elements_by_class_name("jsx-1378818985.moderator-action__button")[3].click()
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_id("ctrl_reason")) == 1)
    def commentReview(self, content):
        self.driver.get("https://tinhte.vn/thread/review-iphone-12-pro-max.3327910/")
        txtBox = self.driver.find_elements_by_class_name("post-reply-input")[1]
        txtBox.click()
        txtBox.send_keys(content)

    # def test_CoRP1(self):
    #     """Comment on review as a guest"""
    #     self.login_()

    # def test_CoRP2(self):
    #     """Comment blank"""
    #     self.commentReview("Review của bạn thật là xịn")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         # self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         self.assertTrue(False)
    #     else:
    #         self.assertTrue(True)

    # def test_CoRP3(self):
    #     """Comment with whitespace only"""
    #     self.commentReview("Review của bạn thật là xịn")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         if len(self.driver.find_elements_by_class_name("jsx-3593820457.error")) != 0:
    #             self.assertTrue(False)
    #         else:
    #             self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def test_CoRP4(self):
    #     """Comment with hyperlink"""
    #     self.commentReview("https://stackoverflow.com/questions/36614118/python-selenium-sending-keys-into-textarea")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         self.assertTrue(False)
    #     else:
    #         self.assertTrue(True)        

    # def test_CoRP5(self):
    #     """Comment with hieroglyphics character"""
    #     self.commentReview("ベトナム人")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         self.assertTrue(False)
    #     else:
    #         self.assertTrue(True)     

    # def test_CoRP6(self):
    #     """Delete a comment"""
    #     self.login_()
    #     self.commentReview("hehehe")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         buttons = self.driver.find_elements_by_class_name("jsx-2274533257.thread-action")
    #         buttons[2].click()
    #         self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #         self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)     

    def makePost(self,driver,paragraph):
        iframe = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(iframe)
        pTag = driver.find_element_by_tag_name("p")
        driver.execute_script("arguments[0].textContent = arguments[1];", pTag, paragraph)
        driver.switch_to.default_content()
        textfield = driver.find_element_by_id("ctrl_location")
        textfield.send_keys(Keys.RETURN)

    def fillPassText(self,driver,text,locator):
        textfield = driver.find_element_by_id(locator)
        textfield.clear()
        textfield.send_keys(text)

    def fillText(self,driver,text,locator):
        textfield = driver.find_element_by_id(locator)
        textfield.clear()
        textfield.send_keys(text)
        textfield.send_keys(Keys.RETURN)
        time.sleep(1)


    # def test_CA(self):
    #     """ Change avatar """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.driver.find_element_by_class_name("img.m").click()
    #     time.sleep(2)
    #     s = self.driver.find_element_by_class_name("labelText")
    #     input_text= s.find_element_by_tag_name("input")
    #     input_text.send_keys(os.getcwd() + ("\image.png" if system() == 'Windows' else "/image.png"))
    #     time.sleep(5)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)
    
    # def test_CARIT(self):
    #     """ Change avatar with wrong image type """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.driver.find_element_by_class_name("img.m").click()
    #     time.sleep(1)
    #     s = self.driver.find_element_by_class_name("labelText")
    #     input_text= s.find_element_by_tag_name("input")
    #     input_text.send_keys(os.getcwd() + ("\image.png" if system() == 'Windows' else "/image.png"))
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 0)
    
    # def test_FPNT(self):
    #     """ Fill place with no text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPWT(self):
    #     """ Fill place with text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"66/7, Hùng Vương, phường 1, quận 10, TP.HCM","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPWU(self):
    #     """ Fill place with unicode """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"ベトナムの都市","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPWL(self):
    #     """ Fill place with numerous char"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"66/7, Hùng Vương, phường 1, quận 10, TP.HCM,MV không phải là một câu chuyện tình yêu mà như một khoảng hoài niệm về tuổi trẻ/ tuổi thơ ngây an nhiên (tiếng tút micro ở đầu và cuối clip như là mở đầu/kết thúc của một đoạn băng tư liệu ko liên quan gì đến accident).","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 0)

    # def test_FJT(self):
    #     """ Fill job with text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"Kỹ sư","ctrl_occupation")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FJNT(self):
    #     """ Fill job with no text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"","ctrl_occupation")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FP(self):
    #     """Fill phone number"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"0919891230","ctrl_custom_field_citizenPhoneNumber")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)


    # def test_FPE(self):
    #     """Fill phone number with Empty number """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"","ctrl_custom_field_citizenPhoneNumber")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPS(self):
    #     """ Fill string in phone number """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"Đây là 1 chuỗi","ctrl_custom_field_citizenPhoneNumber")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 0)

    # def test_FIU(self):
    #     """ Fill user's information """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"Tôi là Ankunkun")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FIUC(self):
    #     """ Fill user's information with unicode """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"ベトナム人")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FIUS(self):
    #     """ Fill user's information with special character """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"@#$%!")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FIUI(self):
    #     """ Fill user's information with icon """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"@@,:>,:)")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)


    # def test_FA(self):
    #     """ Fill following account with text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     self.fillText(self.driver,"Ankunkun","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("username.StatusTooltip")) == 1)

    # def test_FAE(self):
    #     """ Fill following account with empty text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     time.sleep(1)
    #     self.fillText(self.driver,"","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 1)

    # def test_FAU(self):
    #     """Fill following account with unicode"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     time.sleep(1)
    #     self.fillText(self.driver,"うずまきナルト","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 1)

    # def test_FAL(self):
    #     """Fill following account with link"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     time.sleep(1)
    #     self.fillText(self.driver,"https://tinhte.vn/members/ankunkun.2693711/","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 1)


    # def test_CP(self):
    #     """Change password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CP8(self):
    #     """Change password with less than 8 character"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

        # time.sleep(1)
        # self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CPES(self):
    #     """Change password with empty string"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"","ctrl_password_original")
    #     self.fillPassText(self.driver,"","ctrl_password")
    #     self.fillPassText(self.driver,"","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)
        
    #     time.sleep(2)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("close.OverlayCloser"))==1)

    # def test_CPOP(self):
    #     """Change password with old password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CPWU(self):
    #     """Change password with unicode password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CPW(self):
    #     """Change password with wrong confirm password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"","ctrl_password_original")
    #     self.fillPassText(self.driver,"","ctrl_password")
    #     self.fillPassText(self.driver,"","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)
        
    #     time.sleep(2)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("close.OverlayCloser"))==1)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()