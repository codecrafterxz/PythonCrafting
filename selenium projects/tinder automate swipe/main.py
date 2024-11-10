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

USERNAME = "pv8920034911@gmail.com"
PASSWORD =  "9911797533"

driver_path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://tinder.com/app/explore")
log_in = driver.find_element(By.LINK_TEXT,'Log in')
log_in.click()
time.sleep(1000)
goggle = driver.find_element(By.LINK_TEXT,"Continue with Google")
goggle.click()
username = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
username.send_keys(USERNAME)