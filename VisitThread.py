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
driver.get("https://www.tinhte.vn")

# Visit a thread by headline as a guest 
def login(driver):
    if len(driver.find_elements_by_class_name("jsx-1783754700.blue-switch.header-mode")) == 1:
        return True
    driver.find_element_by_partial_link_text("Đăng nhập").click()
    driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
    driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
    driver.find_elements_by_class_name("button.primary")[3].click()

# Visit a thread by headline as a guest 
def VTasGH(driver):
    try:
        search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("article")
    search = search.find_element_by_tag_name("h3")
    search = search.find_element_by_tag_name("a")
    search.click()

# Visit a thread by headline as a user
def VTasUH(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("article")
    search = search.find_element_by_tag_name("h3")
    search = search.find_element_by_tag_name("a")
    search.click()
# Visit a thread by image as a guest
def VTasGI(driver):
    try:
        search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()

# Visit a thread by image as a registered user
def VTasUI(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()


# Visit author of a thread on home screen
def VTauthor(driver):
    try:
        search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_class_name("jsx-631305314.author")
    search.click()

# Visit author of  thread on thread screen
def Vauthor(driver):
    try:
        search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.info")))
    except:
        driver.quit()
    search = search.find_element_by_class_name("jsx-1378818985.author-name")
    search = search.find_element_by_class_name("jsx-1378818985")
    search.click()


# Fast travel to a fragment of thread
def Fasttravel(driver):
    count = 0
    while(1):
        try:
            listSearch= WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "jsx-3078623109.thumb ")))
        except:
            driver.quit()
        listSearch[count].click()
        try:
            search = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.content-list")))
        except:
            driver.back()
            count += 1
            continue
        break
    search = search.find_element_by_class_name("jsx-1378818985")
    search.click()
# Visit advertisement
def Vads(driver):
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "landing")))
    except:
        driver.quit()
    search.click()

# Visit most active user
def VAuser(driver):
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-2501851499.active-user-list")))
    except:
        driver.quit()
    search = search.find_element_by_class_name("jsx-984767296.active-user")
    search.click()

# Visit popular community
def VPcom(driver):
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-938776874.main")))
    except:
        driver.quit()
    search = search.find_element_by_class_name("jsx-938776874.item-container")
    search = search.find_element_by_class_name("jsx-938776874.item")
    search = search.find_element_by_tag_name("a")
    search.click()

# Bookmark thread as a guest
def BthreadG(driver):
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-725335046.bookmark-button")))
    except:
        driver.quit()
    print(search.text)

# React love when logged in
def RLoveU(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.thread-like")))
    except:
        driver.quit()
    search = search.find_element_by_class_name("jsx-1378818985.thread-like__button")
    search = search.find_element_by_tag_name("svg")
    search.click()

# React love as a guest
def RLoveG(driver):
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.thread-like")))
    except:
        driver.quit()
    search = search.find_element_by_class_name("jsx-1378818985.thread-like__button")
    search = search.find_element_by_tag_name("svg")
    search.click()

# Subcribe to author of thread as a registered user\
def SubcribeU(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3973219579.follow-button-container")))
    except:
        driver.quit()
    time.sleep(2)
    search.click()

# Subcribe to author of thread as a guest
def SubcribeG(driver):
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3973219579.follow-button-container")))
    except:
        driver.quit()
    search.click()

# Share thread with no comment
def ShareU(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3454747502.fact-share-button")))
    except:
        driver.quit()
    search.click()
    search = search.find_element_by_xpath("//button[contains( text( ), 'Chia sẻ')]")
    search.click()

# Share thread with extensive length
def ShareULC(driver):
    login(driver)
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3454747502.fact-share-button")))
    except:
        driver.quit()
    search.click()
    try:
        search = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "caption-text-input")))
    except:
        driver.quit()
    search.clear()
    search.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    # search = search.find_element_by_xpath("//button[contains( text( ), 'Chia sẻ')]")
    # search.click()

# Share thread as guest
def ShareG(driver):
    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    except:
        driver.quit()
    search = search.find_element_by_tag_name("a")
    search.click()
    try:
        search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3454747502.fact-share-button")))
    except:
        driver.quit()
    search.click()
    try:
        search = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "caption-text-input")))
    except:
        driver.quit()
    search.clear()
    search.send_keys("pycon")
    search = search.find_element_by_class_name("jsx-401034285.caption-modal-footer")
    search.click()
    

ShareULC(driver)
time.sleep(5)
driver.quit()