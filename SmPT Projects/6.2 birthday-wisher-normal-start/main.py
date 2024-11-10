##################### Normal Starting Project ######################
import datetime as dt 
import pandas 
import random
import smtplib , ssl
USERNAME = "zhackerx3@gmail.com"
PASSWORD = "fzsiksvtnsfdajjm"
today = dt.datetime.now()
today_month = today.month
today_day = today.day
today1 = (today_month,today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
print(birthdays_dict)

if today1 in birthdays_dict:
    birthday_person = birthdays_dict[today1]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        content = letter.read()
        content = content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.ehlo()
        connection.starttls( )
        connection.ehlo()
        connection.login(user=USERNAME,password=PASSWORD)
        connection.sendmail(from_addr=USERNAME,
         to_addrs=birthday_person["email"],
         msg=f"subject :hello Prince \n\n{content}"
        )



