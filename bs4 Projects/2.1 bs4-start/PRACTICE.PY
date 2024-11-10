from bs4 import BeautifulSoup
import lxml
import requests 
response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content,'html.parser')
news_tag = soup.find_all(name="a",class_="titleline")
for tag in news_tag:
    print(tag.get("href"))