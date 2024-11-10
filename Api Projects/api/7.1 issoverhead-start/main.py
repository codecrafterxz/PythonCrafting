import requests
from datetime import datetime
import smtplib
import time

MY_LAT =  20.593683 # Your latitude
MY_LONG =  78.962883 # Your longitude

USERNAME = "zhackerx3@gmail.com"
PASSWORD = "fzsiksvtnsfdajjm"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data1 = response.json()

iss_latitude = float(data1["iss_position"]["latitude"])
iss_longitude = float(data1["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
ison = True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
while ison:
    time.sleep(60)
    if iss_latitude == MY_LAT - 5 and iss_longitude == MY_LONG - 5:
        if time_now >sunset and time_now<sunrise:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.ehlo()
            connection.starttls()
            connection.ehlo
            connection.login(USERNAME,PASSWORD)
            connection.sendmail(
                from_addr= USERNAME,
                to_addrs= "pv8920034911@gmail.com",
                msg="hey Prince see the iss is close to your position "
              )
            connection.quit()
    
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



