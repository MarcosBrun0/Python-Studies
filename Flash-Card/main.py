import tkinter
import random
import string
import csv
import pandas
import time

data = pandas.read_csv("data/french_words.csv")
to_learn_dict = data.to_dict(orient="records")



def next_card():
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_word, text=current_card["French"])
    windows.after(3000)
    reveal_word(current_card)


def reveal_word(current_card):
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=current_card["English"])


BACKGROUND_COLOR = "#B1DDC6"

#layout and setup
windows = tkinter.Tk()
windows.title("Flash Cards")
windows.config(pady=50,padx=50, background=BACKGROUND_COLOR)
Card_Front = tkinter.PhotoImage(file="images/card_front.png")
canvas = tkinter.Canvas(width=800,height=526)
canvas.create_image(400,263, image = Card_Front)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)

canvas_title = canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic",),fill="black")
canvas_word = canvas.create_text(400,263, text="Word", font=("Ariel",70,"bold"), fill="black")
canvas.grid(row=0, columnspan=3)

cross_img = tkinter.PhotoImage(file="images/wrong.png")
Unknown_button =tkinter.Button(image=cross_img, command=next_card)
Unknown_button.config(highlightthickness=0, background=BACKGROUND_COLOR)
Unknown_button.grid(row=2,column=2)

check_img = tkinter.PhotoImage(file="images/right.png")
check_button = tkinter.Button(image=check_img, command=next_card)
check_button.config(highlightthickness=0,bg=BACKGROUND_COLOR)
check_button.grid(row=2,column=0)

current_word = next_card()



def UpdateWord():

    with open("/Users/MBhome/Documents/Codes/Python/Flash-Card/data/french_words.csv", "r") as csvFile:
        csvreader = csv.reader(csvFile)

        for row in csvreader:
            print(row)





windows.mainloop()