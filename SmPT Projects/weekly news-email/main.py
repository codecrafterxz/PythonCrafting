import requests
from bs4 import BeautifulSoup
from lxml import etree
from smtplib import SMTP
from email.mime.text import MIMEText

USERNAME = "zhackerx3@gmail.com"
PASSWORD = "fzsiksvtnsfdajjm"

url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"

data = requests.get(url=url).text

soup = BeautifulSoup(data, "lxml")

title = soup.find("p", attrs={"class": "wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy"}).text

dom = etree.HTML(str(soup))

content0 = dom.xpath('//*[@id="__next"]/div[6]/main/article/div[2]/div[2]/div[2]/p')[0].text
content1 = dom.xpath('//*[@id="__next"]/div[6]/main/article/div[2]/div[2]/div[2]/p/a')[0].text
content2 = dom.xpath('//*[@id="__next"]/div[6]/main/article/div[2]/div[2]/div[2]/p/text()[2]')[0]

content = f"{content0}{content1}{content2}"

msg = MIMEText(f"Title: {title}\nContent: {content}", "plain", "utf-8")

msg["Subject"] = "Example Subject"
msg["From"] = USERNAME
msg["To"] = "pv8920034911@gmail.com"

email = SMTP("smtp.gmail.com", 587)
email.starttls()
email.login(USERNAME, PASSWORD)
email.send_message(msg)
email.quit()
