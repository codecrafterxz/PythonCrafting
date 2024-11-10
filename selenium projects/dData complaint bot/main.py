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

TWITER_USER = "DarkPhoenix_Dev"
TWITER_PASS = "!6BiI8L(goCI%5&"
PROMISED_UP = "10"
PROMISED_DOWN = "150"
CHROME_DRIVER_PATH = "D:\Python\chromedriver_win32\chromedriver.exe"


class Internetspeedtestbot:
    def __init__(self,driver_path):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=driver_path,options=self.options)
        self.up = 0
        self.down = 0
    
    def get_internetspeed(self):
         self.driver.get("https://www.speedtest.net/")
         time.sleep(3)
         self.go = self.driver.find_element(By.CSS_SELECTOR,'.start-button a')
         self.go.click()
         time.sleep(60)
         print("clicked")
         self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
         self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
         print(f"speed-down:{self.down.text}\nspeed-up:{self.up.text}")
         



    def Tweet_post(self):
         self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
         time.sleep(5)
         self.email = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
         self.email.send_keys(TWITER_USER)
         self.email.send_keys(Keys.ENTER)
         time.sleep(5)
         self.password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
         self.password.send_keys(TWITER_PASS)
         self.password.send_keys(Keys.ENTER)
         time.sleep(5)
         self.tweet_compose = self.driver.find_element(By.CSS_SELECTOR,'.public-DraftStyleDefault-block public-DraftStyleDefault-ltr input')
         self.tweet = "hello"
         self.tweet_compose.send_keys(self.tweet)
         time.sleep(5)
        #  self.tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div')
        #  self.tweet_button.click()
        #  time.sleep(5)
    
bot = Internetspeedtestbot(CHROME_DRIVER_PATH)
bot.Tweet_post()
# bot.get_internetspeed()
         

