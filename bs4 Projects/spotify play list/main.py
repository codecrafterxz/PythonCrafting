import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,CacheHandler

ClientID = "17b9e527932f4dfbbfe2b60818013df5"
ClientSecret =  "62fd8da28181464e87d856ca72a6dbeb" 
spotify_url  = " https://api.spotify.com"

date = input("which year songs do you wana hear:")
url  = "https://www.billboard.com/charts/hot-100/"+ date
response = requests.get(url=url)
content = response.text

soup = BeautifulSoup(content,"lxml")

all_songs = []

year = date.split("-")[0]
spotify_response = requests.post(url=spotify_url,auth=(ClientID,ClientSecret))
songs = soup.find_all( "h3",attrs={'class': 'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only'})
for song in songs:
      song = song.getText()
      all_songs.append(song)
sp1 = SpotifyClientCredentials(client_id=ClientID,client_secret=ClientSecret)
sp = spotipy.Spotify(client_credentials_manager=sp1)
# user = sp.current_user()
# user_id = user['id']
user_id = {"access_token": "BQCeuBpiHYIJdDf3qXCuckDCVdB8mEY06FWZbVD-yzOFEyvKHYAaWHTQr2q5kVOKgPkPhekD1fCNpL95PvleuYkVyWd8UfWdzERDUd_Caqf-7OuaaQnl", "token_type": "Bearer", "expires_in": 3600, "expires_at": 1675962395}

all_songs_uri = []
for song in all_songs:
         result = sp.search(q=f"track:{song} year:{year}", type="track")
         try:
             uri = result["tracks"]["items"][0]["uri"]
             all_songs_uri.append(uri)
         except IndexError:
            print(f"{song} uri doesn't found .Skipped")
            with open("songs with links.txt",mode = "a") as file:
                  try:
                     file.write(f"{song} : {uri}")
                  except IndexError:
                     file.write(f"{song} uri doesn't found .Skipped")

# spotify_post_url = requests.post(url="https://developer.spotify.com/dashboard/applications/17b9e527932f4dfbbfe2b60818013df5",auth=(ClientID,ClientSecret),json=all_songs_uri)
# print(spotify_post_url.text)

    

