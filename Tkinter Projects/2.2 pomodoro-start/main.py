from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    countdown(6)
    text_label.config(text="Start",font=(GREEN,50))

def reset_timer():
    canvas.itemconfig(timer,text="00:00")
    text_label.config(text="Start",font=(GREEN,50))

def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count>0:
        canvas.itemconfig(timer,text = f"{count_min}:{count_sec}")
        window.after(1000,countdown,count-1)
    if count == 0:   
        text_label.config(text="Now you can have a five minutes break",font=(GREEN,24))
        countdown(5)
        reset_timer(0)
        
        
       
       
           
          
           
           


   


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

text_label = Label(text="Start",fg=GREEN,bg= YELLOW, font=(FONT_NAME,50))
text_label.grid()

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomatoimage = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomatoimage)
timer = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid()

start = Button(text="Start",command=start_timer,highlightthickness=0)
start.grid(column=0,row=2)

reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)


window.mainloop()