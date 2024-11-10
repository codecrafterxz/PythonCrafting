# body mass calculator

#print("welcome to the bmi calculator")
#weight = int(input("enter the weight"))
#heigh = int(input("enter the height"))
#height = heigh**2#
#bmi = int(weight)/int(height)
#print(bmi)



#age = int(input("whats your age"))
#if age<18:
    #num = int(input("tell the num"))
    #print("unable")
    #print("what your num")
    #if num<20:
        #print("you hve to pay 20 rupees")
        #if num<30:
            ##print("you have to pay 30 rupees")
#else:
   # print("able")
    #print("you does not have to pay  ")

# import random

# ry = random.randint(0,1)

# if ry==1:
#     print("heads")

# else:
#     print("tails")


#bill payer fidner

# import random
# people = input("enter the names")
# names = people.split(",")
# h = len(names)
# billpayer = random.randint(0,h-1 )
# payer = names[billpayer]
# print(payer + "is going to pay")


# treasure hunt
# row1 = ["l","w","r"]
# row2 = ["a","s","d"]
# row3 = ["z","x","c"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("treasure")
# horizontal = int(position[0])
# vertical =int(position[1])
# selectedrow = map[vertical - 1]
# selectedrow[horizontal - 1] = 5
# print(selectedrow)


#rockpappr scissor
# import random
# rock = 1
# papper = 2
# scissor = 3 
# you = int(input("choice"))
# computer = random.randint(1,3)
# print(computer)
# if you == 1 and computer == 2:
#     print("you loose")
# elif computer > you :

#     print("you win")
# elif you == computer :
#     print("draw")
# else :
#     print("win")
# 
# 
# 
# averege height


# even num adder
# total = 0 
# for n in range(2,101,2):
#     total +=n
# print(total )
# first we will import the subprocess module
# import subprocess

# now we will store the profiles data in "data" variable by 
# running the 1st cmd command using subprocess.check_output
# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# now we will store the profile by converting them to list
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# # using for loop in python we are checking and printing the wifi 
# # passwords if they are available using the 2nd cmd command
# for i in profiles:
#     # running the 2nd cmd command to check passwords
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
#                         'key=clear']).decode('utf-8').split('\n')
#     # storing passwords after converting them to list
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     # printing the profiles(wifi name) with their passwords using 
#     # try and except method 
#     try:
#         print ("{:<30}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print ("{:<30}|  {:<}".format(i, ""))


# # fizz buzz challenge

# # for n in range(1,101):
# #     if n % 3 == 0 and n % 5 == 0:
# #         print("fizzbuzz")
# #     elif n % 3 == 0:
# #         print("fizz")
# #     elif n % 5 == 0:
# #         print ("buzz")
# #     else :
# #         print(n)






# hangman]

# def win():
#     if "_" not in display:
#         endofgame = True
#         print("you win")       
# import random 
# fruits = ["apple","mango","banana"]
# choice = random .choice(fruits)
# print(f"choosen word is {choice}")
# display = []
# wordlength = len(choice)
# for _ in range(wordlength):
#     display+="_"
# print(display)
# endofgame = False
# life = 6 
# while not endofgame:  
#     guess = input("guess:")
#     for i in range(wordlength):
#         letter = choice[i]
#         #print(display)
#         if letter == guess:
#             display[i] = letter
#             print(display)
#     if guess  not in choice:
#         life-=1
#         print(f"you choose {guess} it is a wrong word so you have now {life} life")
#         if life == 0:
#             endofgame = True
#             print("you loose")
#     win()

# import random    
# def myfunc(n):
#     n = int(n)
#     isprime = True
#     for i in range(2,n):
#         if n % i == 0:
#             print("it is not a prime number ")
#             isprime = False
#     if isprime :
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is not a prime number")
# m = int(input("choose number for checking it is a prime number or not "))
# myfunc(m)
               
   

# d
# travellog = [
# {"coutry" : "france" ,
# "citiies" : ['japan','asia','aris'] ,
# "visits" : 12} 
# ]


# def c(contryvisted,coties,vidited) :
#     countryvisited = {}
#     countryvisited["country"] =contryvisted
#     countryvisited["cities"] = coties
#     countryvisited["visits"] = vidited
#     travellog.append(countryvisited)
#     print(travellog)

# c("russia",['japan','asia','ar'],5)



# def winner(bidder):
#     highbid = 0
#     for i in bidder:
#         if bids[i] > highbid:
#             highbid = bids[i]
#     print(f"the highest bid is {highbid} and paid by {i}" )        
# import os 
# bids = {}
# biddingfinished = False
# while not biddingfinished:
#     name = input("what is your name ")
#     price = int(input("how much do you wana bid"))
#     bids[name] = price
#     shouldstop = input("is there anyother person for bidding")
#     if shouldstop == "no":
#         biddingfinished = True
#         winner(bids)
#     elif shouldstop == "yes":
#         os.system('cls')

# # def winner(bidder):
# #     highbid = 0
# #     for i in bidder:
# #         if bids[i] > highbid:
# #             highbid = bids[i]
# #     print(f"the highest bid is {highbid} and paid by {i}" )        


# calculating days 
# def isleap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                  return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_inmonth(year,month):

#     monthdays = [31,28,31,30,31,30,31,30,31,30,31,30]
#     if isleap(year) and month == 2:
#         return 29
#     return monthdays[month-1]

# year = int(input("enter the year"))
# month = int(input("ener te month"))
# days = days_inmonth(year,month)
# print(days)

# import os
# print("welcome to my calculator")
# def add (n1,n2):
#         sum_ans = n1+n2
#         print(sum_ans) 
# def sub(n1,n2):
#         sub_ans = n1-n2
#         print(sub_ans)
# def mult(n1,n2):
#          mult_ans = n1*n2
#          print(mult_ans)
# def divi(n1,n2):
#         divi_ans = n1/n2
#         print(divi_ans)                     
# stop = True
# while  stop == True :
#       num = int(input("enter a number"))
#       user = input("choose a operation \n ''+'' \n ''-'' \n ''*'' \n ''/ ''")
#       num2 = int(input("enter second number"))
#       if user == "+":
#            add(num,num2)
#            end = input("enter do you wana continue or exit \n yes for exit \n no for continue")
#            if end == "yes":
#             stop = False
#            elif end == "no":
#             os.system('cls')    
#       elif user == "-":
#           sub(num,num2)
#           end = input("enter do you wana continue or exit \n yes for exit \n no for continue ")
#           if end == "yes":
#             stop = False
#           elif end == "no":
#             os.system('cls')  
#       elif user ==  "*":
#           mult(num,num2)
#           end = input("enter do you continue or exit \n yes for exit \n no for continue")
#           if end == "yes":
#             stop = False
#           elif end == "no":
#             os.system('cls')
#       elif user == "/":
#           divi(num,num2)
#           end = input("enter do yoyu wana continue or exit \n yes for exit \n no for continue")
#           if end == "yes":
#             stop = False
#           elif end == "no":
#             os.system('cls')    
#       else:
#           print("you choose a invalid operation")
#           os.system('cls')
    


#
# # first genrate a random number for using
# import random
# num = random.randint(1,100)
# print(num)
# # now creating a while loop for running
# level = input("choose difficulty easy medium hard = ")

# i = 0
# if level == "easy":
#   guess_again = 15
# elif level == "medium":
#   guess_agin = 10
# else:
#   guess_again = 5
# print(f"ou have {guess_again} lives for guessing the number")
# def guessing():
#     guess = int(input("guess the number = "))
    
#     if guess > num :
#       print("too high")
#     elif guess == num:
#       print("you win")
#     else:
#       print("to low")
#  # now creating a guessing thats make easier to guess
# while i<guess_again:
#   guessing()
#   i+=1
#   print(f"your {i} live are used")
  
  
##########DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 6)
# print(dice_imgs[dice_num-1])

# # # Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age >= 18:
#    print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page =int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,)]
# import random 

# for i in range(100):
#     num = random.randint(-280,280)
#     print(num)
# numbers = [1,2,3,4,5]
# newitem=[n+1 for n in range(1,6)]
# print(newitem)
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆

# #Write your 1 line code 👇 below:
# squared_numbers =[n*n for n in numbers]


# #Write your code 👆 above:

# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above

# #Write your 1 line code 👇 below:
# result =[n for n in numbers if n % 2 == 0]


# #Write your code 👆 above:

# print(result)
# with open("file1.txt") as file1:
#     c1 = file1.readlines()
# with open("file2.txt") as file2:
#     c2 = file2.readlines()
# result =[int(n) for n in c1 if n in c2]
# print(result)




# sentence1 = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# sentence = sentence1.split()
# result = {key:len(key)for key in sentence }


# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# weather_f = {key:value*(9/5+32)for key,value in weather_c.items()}


# print(weather_f)

fruits = ["Apple", "Pear", "Orange"]


#TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#         try:
#             fruit = fruits[index]
#         except:
#             print("fruitpie")
#         else:
#             print(fruit + " pie")
# make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try :
#          total_likes = total_likes + post['Likes']
#     except  :
#         pass


# print(total_likes)
# import json
# import pandas 
# with open("file2.txt","r",encoding="utf8") as data:
#     content = data.readlines()
    
# h = pandas.DataFrame(content)
# h.to_csv("dataofja.csv")
# import smtplib,ssl
# my_email = "zhackerx3@gmail.com"
# my_password = "fzsiksvtnsfdajjm"
# smtp = "smtp.gmail.com" 
# port = 587
# context = ssl.create_default_context()
# connection = smtplib.SMTP(smtp,port)
# connection.ehlo()
# connection.starttls(context=context)
# connection.ehlo()
# connection.login(my_email, my_password)
# connection.sendmail (
#     from_addr=my_email,
#     to_addrs = "pv8920034911@gmail.com",
#     msg=f"Subject:Happy Birthday!")
# connection.quit()
# print("it worked")
# from datetime import datetime , timedelta
# import requests
# TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
# TEQUILA_API_KEY = "fHgXX9M9XoeNCM2GMsFnGEU6MTmotEHq"
# TODAY_DATE = datetime.now().strftime("%d/%m/%Y")
# to_6 = six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
# T0_DATE = to_6.strftime("%d/%m/%Y")
from tkinter import *
# -------------------------------------function----------------------------------------------
expression = ""
def press(num):
    global expression 

    expression = expression +  str(num)
    equation.set(expression)
    
def clear():
    global expression 
    expression = ""
    entry.delete(0,END)

def equal():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
# ---------------------------------------------- UI SETUP ----------------------------------------------
window = Tk()
window.title("MY CALCULATOR")
window.minsize(width=600,height=300)
window.configure(bg="black",padx=150,pady=100)
equation = StringVar()
entry = Entry(window,textvariable=equation)
entry.grid()
button1= Button(text="1",width=10,height=1, command=lambda : press(1))
button1.grid(row=2, column=0)
button2= Button(text="2",width=10,height=1,command=lambda :press(2))
button2.grid(row=2, column=1)
button3 = Button(text="3",width=10,height=1,command=lambda :press(3))
button3.grid(row=2, column=2)
button4 = Button(text="4",width=10,height=1,command=lambda :press(4))
button4.grid(row=3, column=0)
button5 = Button(text="5",width=10,height=1,command=lambda :press(5))
button5.grid(row=3, column=1)
button6 = Button(text="6",width=10,height=1,command=lambda :press(6))
button6.grid(row=3, column=2)
button7 = Button(text="7",width=10,height=1,command=lambda :press(7))
button7.grid(row=4, column=0)
button8 = Button(text="8",width=10,height=1,command=lambda :press(8))
button8.grid(row=4, column=1)
button9 = Button(text="9",width=10,height=1,command=lambda :press(9))
button9.grid(row=4, column=2)
button0 = Button(text="0",width=10,height=1,command=lambda :press(0))
button0.grid(row=5,column=0)
button_equal = Button(text="=",width=10,height=1,command=equal)
button_equal.grid(row=5, column=2)
button_add = Button(text="+",width=10,height=1,command=lambda :press("+"))
button_add.grid(row=2, column=3)
button_sub = Button(text="-",width=10,height=1,command=lambda :press("-"))
button_sub.grid(row=3, column=3)
button_into = Button(text="x",width=10,height=1,command=lambda :press("*"))
button_into.grid(row=4, column=3)
button_divide = Button(text="/",width=10,height=1,command=lambda :press("/"))
button_divide.grid(row=5, column=3)
button_clear = Button(text="AC",width=10,height=1,command=clear)
button_clear.grid(row=5, column=1)
window.mainloop()