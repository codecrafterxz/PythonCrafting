THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class Quizinterface :
     def __init__(self,quiz_brain :QuizBrain) -> None:
          self.quiz = quiz_brain
          self.score_label = 0
          self.window = Tk()
          self.window.title("Quizler")
          self.window.config(padx=20,pady=20,bg=THEME_COLOR)
          self.label = Label(text=f"score :{self.score_label}",fg="white",bg=THEME_COLOR,font=("arial",20,"italic"))
          self.label.grid(row=0,column=3)

          self.canvas = Canvas(width=300,height=250,bg="white")
          self.question_text = self.canvas.create_text(150,125,width=280, text="amzon start here",font=("arial",20,"italic"))
          self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

         

          falseimg = PhotoImage(file="images/false.png")
          self.butthon1 = Button(image=falseimg,command=self.fal_pres)
          self.butthon1.grid(column=0,row=2)

          trueimg = PhotoImage(file="images/true.png")
          self.button2 = Button(image=trueimg,command=self.true_pr)
          self.button2.grid(column=3,row=2)
          self.next_question()
          self.window.mainloop()
         
     def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=f"{q}")
        else:
            self.canvas.itemconfig(self.question_text,text="congratulations you finish the game")
            self.butthon1.config(state="disabled")
            self.button2.config(state="disabled")
     def true_pr(self):
         is_right = self.quiz.check_answer("True")
         self.feedback(is_right)
       
     def fal_pres(self):
         is_right = self.quiz.check_answer("False")
         self.feedback(is_right)
   
     def feedback(self,is_right):
         if is_right:
            self.canvas.config(bg="green")
            self.score_label += 1
            self.label.config(text=f"score :{self.score_label}")
         else:
            self.canvas.config(bg="red")
         self.window.after(1000,self.next_question)

        
