import pandas
import os
import time 

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
result = {row.letter:row.code for (index,row) in nato.iterrows() }
ison = True
while ison:
     word = input("enter").upper()
     try:
       output = [result[letter] for letter in word]
       print(output)
     except KeyError:
        print("sorry you input an invalid word")
        time.sleep(1)
        os.system('cls')



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

