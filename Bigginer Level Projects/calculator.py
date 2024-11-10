import os
from tkinter import *
print("welcome to my calculator")
def add (n1,n2):
        sum_ans = n1+n2
        print(f" result = {sum_ans}") 
def sub(n1,n2):
        sub_ans = n1-n2
        print(f" rsult {sub_ans}")
def mult(n1,n2):
         mult_ans = n1*n2
         print(mult_ans)
def divi(n1,n2):
        divi_ans = n1/n2
        print(divi_ans)
def using(end):
  if end == "yes":
   stop = True
  elif end == "no":
   os.system('cls')
stop = False  
while not stop :
      num = int(input("enter a number"))
      user = input("choose a operation \n ''+'' \n ''-'' \n ''*'' \n ''/ ''")
      num2 = int(input("enter second number"))
      if user == "+":
           add(num,num2)
           end = input("enter do you wana continue or exit \n yes for exit \n no for continue")
           using(end)   
      elif user == "-":
          sub(num,num2)
          end = input("enter do you wana continue or exit \n yes for exit \n no for continue ")
          using(end) 
      elif user ==  "*":
          mult(num,num2)
          end = input("enter do you continue or exit \n yes for exit \n no for continue")
          using(end)
      elif user == "/":
          divi(num,num2)
          end = input("enter do yoyu wana continue or exit \n yes for exit \n no for continue")
          using(end)
      else:
          print("you choose a invalid operation")
          os.system('cls')
    


        



    