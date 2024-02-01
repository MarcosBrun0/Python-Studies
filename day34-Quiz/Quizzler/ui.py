from tkinter import *
THEME_COLOR = "#375362"

class QuizzInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250,background="white")
        self.canvas_title= self.canvas.create_text(150,125, text="??????",font=("Ariel",20,"italic",),fill="black")
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(text="true",image=self.true_img, command=checkiftrue(1))
        self.false_button = Button(text="false",image=self.false_img, command=checkiftrue(0))
        self.label = Label(text="Score: 0")



        #grid
        self.true_button.grid(row=3,column=1)
        self.false_button.grid(row=3,column=2)
        self.canvas.grid(column=1, row=2, columnspan=2)
        self.label.grid(row=1,column=2)

        self.window.mainloop()

        def DisplayQuestion(question):
            self.canvas.itemconfig(self.canvas_title,text=question)

        def checkiftrue(button):
            pass

