import requests
from bs4 import BeautifulSoup
response = requests.get(url = "https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text
soup = BeautifulSoup(content,"html.parser")
movies = soup.find_all("h3",class_="jsx-4245974604")
for movie in movies:
      print(movie)




   
