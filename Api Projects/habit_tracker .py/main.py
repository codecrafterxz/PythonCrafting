import requests
from datetime import datetime
USERNAME = "dark"
TOKEN = "lkjhgfdsapoiuytrewq"
GRAPHID = "graph1"
start_point = "https://pixe.la/v1/users"

data = {
    "token" : TOKEN ,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# respond = requests.post(url = start_point,json=data)
# print(respond.text)

graph_end_point = f"{start_point}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPHID,
    "name" : "coding",
    "unit" : "minutes",
    "type" : "int",
    "color" : "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_end_point,json=graph_config,headers=headers)
# print(response.text)

post_pixel = f"{start_point}/{USERNAME}/graphs/{GRAPHID}"
 
today = datetime.now()
DATE = today.strftime("%Y%m%d")

pixel_config = {
    "date" : DATE,
    "quantity" : input("how many hours did you code today ?")
}

response2 = requests.post(url=post_pixel,json=pixel_config,headers=headers)
print(response2.text)
# put_pixel = f"{start_point}/{USERNAME}/graphs/{GRAPHID}/{DATE}"
# response3 = requests.delete(url=put_pixel,json=pixel_config,headers=headers)
# print(response3.text)