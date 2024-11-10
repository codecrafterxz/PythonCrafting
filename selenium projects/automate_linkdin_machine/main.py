from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3422411655&f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

sign_in = driver.find_element(By.LINK_TEXT,"Sign in")
USERNAME =  "pv8920034911@gmail.com"
PASSWORD = "getlost123987"  
PHONE_NUMBER   = "9911797533"     
sign_in.click()
time.sleep(5)
username = driver.find_element(By.NAME,"session_key")
username.send_keys(USERNAME)
password = driver.find_element(By.NAME,"session_password")
password.send_keys(PASSWORD)

enter = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
enter.click()
all_jobs = driver.find_element(By.ID,"ember723")
all_jobs.click()
time.sleep(5)
apply_button = driver.find_element(By.XPATH,'//*[@id="ember888"]')
apply_button.click()
time.sleep(5) 
phone = driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3265903427-68461530-phoneNumber-nationalNumber"]')
time.sleep(5)
if phone == "":
    phone.send_keys(PHONE_NUMBER)
    time.sleep(5)
save = driver.find_element(By.XPATH,'//*[@id="ember931"]/span')
save.click()
job_data = []

# time.sleep(5)
# for job in all_jobs:
#     time.sleep(5)
#     job.click()


    # job.click()
    # print("clicked")
    
#     time.sleep(5)
#     apply_button = driver.find_elements(By.CLASS_NAME,"jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")
#     apply_button.click()
#     time.sleep(5)
#     phone_number = driver.find_element(By.CLASS_NAME," artdeco-text-input--input")
#     if phone_number == "":
#         phone_number.send_keys(PHONE_NUMBER)
#     time.sleep(5)
#     submit = driver.find_element(By.CLASS_NAME,"artdeco-button__text")
#     submit.click()
# print("program finished")

