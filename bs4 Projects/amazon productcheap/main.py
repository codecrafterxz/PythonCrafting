import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import lxml

USERNAME = "zhackerx3@gmail.com"
PASSWORD = "fzsiksvtnsfdajjm"

header = {"Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(url="https://www.amazon.in/Nothing-Phone-Black-128-RAM/dp/B0BKZVF7VV/ref=sr_1_1?crid=JWB9ZD8GW0HW&keywords=nothing+phone+1&qid=1676216343&sprefix=nothing%2Caps%2C948&sr=8-1",headers=header)
content = response.text
lxml = "lxml"
soup = BeautifulSoup(content,'lxml')


price_of_product_1 = soup.find(name="span", attrs={"class":"a-price-whole"}).text
price_of_product_1 = price_of_product_1.replace(',', '')
price_of_product = float(price_of_product_1)
print(price_of_product)
# if price_of_product <= 25000:
# connection = SMTP("smtp.gmail.com",587)
# connection.ehlo()
# connection.starttls()
# connection.login(USERNAME,PASSWORD)
# connection.sendmail(from_addr=USERNAME,to_addrs="pv8920034911@gmail.com",msg=f"look Prince the price of product that have been looking to buy is reduces from its actual price its now available for only{price_of_product}")
         



