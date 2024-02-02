from tkinter import *
import quiz_brain
THEME_COLOR = "#375362"

class QuizzInterface():
    def __init__(self, quiz_brain : quiz_brain.QuizBrain ):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250,background="white")
        self.canvas_title= self.canvas.create_text(150,125, text="??????",font=("Ariel",20,"italic",),fill="black",width=280)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(text="true", image=true_img, command=self.itsTrue)
        self.false_button = Button(text="false",image=false_img, command=self.itsFalse)
        self.label = Label(text="Score: 0")



        #grid
        self.true_button.grid(row=4,column=1)
        self.false_button.grid(row=4,column=2)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.label.grid(row=1,column=2)
        self.nextquestion()
        self.window.mainloop()


    def nextquestion(self):
        can_continue = self.quiz.still_has_questions()
        self.canvas.config(background="white")
        if can_continue:

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_title,text=q_text )
        else:
            self.canvas.itemconfig(self.canvas_title,text="You reached the end of the Quiz!")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")
    def itsTrue(self):
        result = self.quiz.check_answer("True")
        self.Check_Result(result)

    def itsFalse(self):
        result = self.quiz.check_answer("False")

        self.Check_Result(result)




    def Check_Result(self,result):
        if result == 1:
            print("right")
            self.score = self.score + 1
            self.label.config(text=f"score:{self.score}")

            self.canvas.config(background="green")
            self.window.after(1000,func=self.nextquestion)

        else:
            print("wrong")
            self.canvas.config(background="red")
            self.window.after(1000,func=self.nextquestion)







