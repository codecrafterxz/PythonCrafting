from bs4 import BeautifulSoup
import lxml
import requests 

response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content,'html.parser')
news_tag = soup.find_all(name="span",class_="titleline")
all_news_texts = []
all_news_links =[]
all_news_upvotes =[]
for tag in news_tag:
    text = tag.getText()
    all_news_texts.append(text)
    
for tag in soup.find_all("a"):
    link = tag.get("href")
    
    all_news_links.append(link)
        

news_upvote = soup.find_all(name="span",class_="score")
for score in news_upvote:
    score = score.getText()
    score = score.split()[0]
    all_news_upvotes.append(int(score))
    
largest_score = max(all_news_upvotes)
largest_index = all_news_upvotes.index(largest_score)

print(f"{largest_index}).{all_news_texts[largest_index]}")
print(all_news_links[largest_index])
print(all_news_upvotes[largest_index])