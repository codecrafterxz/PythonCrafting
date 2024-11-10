from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

INSTAGRAM_USERNAME = "darkphoenix_dev"
INSTAGRAM_PASSWORD = "IJ*thq4xud*05R"
CHROME_DRIVER_PATH = "D:\Python\chromedriver_win32\chromedriver.exe"
ACCOUNT = "_coding_hub__"
class INSTAGRAMFOLLOWERBOT :
    def __init__(self,driver_path):
         self.options = webdriver.ChromeOptions()
         self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
         self.driver = webdriver.Chrome(executable_path=driver_path,options=self.options)
    def login_instagram(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        self.username_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.username_input.send_keys(INSTAGRAM_USERNAME)
        
        self.password_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password_input.send_keys(INSTAGRAM_PASSWORD)
        
        self.login = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button')
        self.login.click()
        time.sleep(10)
    def find_follower(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/followers/?next=%2F")
        time.sleep(10)
    def follow(self):
        self.all_button = self.driver.find_elements(By.CSS_SELECTOR,'._aano button')
        for self.button in self.all_button:
            self.button.click()
            time.sleep(2)
             

instagram_bot = INSTAGRAMFOLLOWERBOT(CHROME_DRIVER_PATH)
instagram_bot.login_instagram()
instagram_bot.find_follower()
instagram_bot.follow()