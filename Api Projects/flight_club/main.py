import requests

print("welcome to Prince flight club \n")
print("we will find the best deals flight for you \n")
first_name = input("enter your first name \n ")
last_name = input("enter your last name \n")
email = input(" enter your email  \n")
email_again = input("enter your email again \n ")

body = {
   'user' :{
   'First name ' : first_name,
    'Last name' : last_name,
    'Email' : email_again
    }     }

response = requests.post(url= "https://api.sheety.co/8a47ffd1a35e32bea72219f8e5999965/copyOfFlightDeals/users" , json=body)
print(response.text)

# print("you are in our club now ")