from tkinter import *
import pandas 
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
   data = pandas.read_csv("data/words_to _learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
f_word = data.to_dict(orient="records")
french_word = {}
# function for yes 
def y ():
    global french_word , flip_timer
    window.after_cancel(flip_timer)
    french_word = random.choice(f_word)
    canvas.itemconfig(card_background,image=cardf)
    canvas.itemconfig(l,text="french",fill="black")
    canvas.itemconfig(m,text= french_word["French"],fill= "black")
    flip_timer = window.after(3000,func=english)

def english():
    canvas.itemconfig(card_background,image=carde)
    canvas.itemconfig(l,text="english",fill="white")
    canvas.itemconfig(m,text= french_word["English"],fill="white")

def R():
    y()
    f_word.remove(french_word)
    data = pandas.DataFrame(f_word)
    data.to_csv("data/words_to _learn.csv")
   

    

        
window = Tk()
window.title("FLASHY")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=english)

# creating canvas 
canvas = Canvas(width=800,height=526)
cardf = PhotoImage(file="images/card_front.png")
carde = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=cardf)
l =canvas.create_text(400,150,text="French",font=("ariel",40,"italic"))
m = canvas.create_text(400,263,text="word",font=("ariel",40,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
# creating buttons
y_image = PhotoImage(file="images/right.png")
yes = Button(image=y_image,command=R, highlightthickness=0)
yes.grid(row=1,column=1)

n_image = PhotoImage(file="images/wrong.png")
no = Button(image=n_image,command=y,highlightthickness=0)
no.grid(row=1,column=0)


window .mainloop()



