import requests
from datetime import *
APPID = "28bbcf68"
APPKEY = "6f0f696d56d38b650168f7f99e3bd37b"	

GENDER = "male"
WEIGHT_KG = "47"
HEIGHT_CM = "6"
AGE = "14"

exercise = input("what exercise did you today ")
starting_point =  "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id" : APPID,
    "x-app-key" : APPKEY
   
}
parameter = {
    "query": exercise ,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}



response = requests.post(url=starting_point,json= parameter ,headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
header = (".dark","9911797533")

for i in result["exercises"]:
    sheet_input ={
        "workout" :{
         "date": today_date,
            "time": now_time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }

SHEETYAPI = "https://api.sheety.co/b32d8a92f2266a4a555d8dea9aedfeee/copyOfMyWorkouts3/workouts"
respond = requests.post(url=SHEETYAPI,json=sheet_input,auth=header)
print(respond.text)

