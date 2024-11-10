# password genrator
import random
alphabet1 = ['A' 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p','q', 'r',
 's', 't', 'u', 'v','w', 'x', 'y', 'Z']
number1 = ['1','2','3','4','5','6','7','8','9']
symbol1 = ["!","@","#","$","%","^","&","*"]
print("welcome to my passwoed genrator")
alphabet = int(input("how many alphabets do you want in your password "))
number = int(input("how many numbers do you want in password"))
symbol = int(input("how many symbols do you want in password genrator "))
password = []
for c in range(1,alphabet + 1):
    password+=random.choice(alphabet1)
for c in range(1,number + 1):
    password+=random.choice(number1)
for c in range(1,symbol + 1):
    password+=random.choice(symbol1)
random.shuffle(password)
password1 = ""
for c in password:
    password1+=c
print(f"your password is {password1}")
