import tkinter
import random
import string
import csv
import pandas
import time


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    print("File not Found")
    data = pandas.read_csv("data/french_words.csv")




to_learn_dict = data.to_dict(orient="records")

print(to_learn_dict)
card_atual = {}

def next_card():


    global card_atual,flip_timer
    windows.after_cancel(flip_timer)
    card_atual = random.choice(to_learn_dict)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=card_atual["French"],fill="black")
    canvas.itemconfig(canvas_img, image= Card_Front)
    print(card_atual)

    flip_timer =windows.after(3000, func=reveal_word)

def reveal_word():

    canvas.itemconfig(canvas_img, image=Card_Back)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text= card_atual["English"], fill="white")

def remove_word():

    global card_atual
    to_learn_dict.remove(card_atual)
    dados = pandas.DataFrame(to_learn_dict)
    dados.to_csv("data/words_to_learn.csv", index=False)

    next_card()

BACKGROUND_COLOR = "#B1DDC6"

#layout and setup

windows = tkinter.Tk()
windows.title("Flash Cards")
flip_timer = windows.after(3000, func=reveal_word)
windows.config(pady=50,padx=50, background=BACKGROUND_COLOR)
Card_Front = tkinter.PhotoImage(file="images/card_front.png")
Card_Back = tkinter.PhotoImage(file="images/card_back.png")
canvas = tkinter.Canvas(width=800,height=526)
canvas_img = canvas.create_image(400,263, image = Card_Front)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)

canvas_title = canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic",),fill="black")
canvas_word = canvas.create_text(400,263, text="Word", font=("Ariel",70,"bold"), fill="black")
canvas.grid(row=0, columnspan=3)

cross_img = tkinter.PhotoImage(file="images/wrong.png")
Unknown_button =tkinter.Button(image=cross_img, command=next_card)
Unknown_button.config(highlightthickness=0, background=BACKGROUND_COLOR)
Unknown_button.grid(row=2,column=2)

check_img = tkinter.PhotoImage(file="images/right.png")
check_button = tkinter.Button(image=check_img, command=remove_word)
check_button.config(highlightthickness=0,bg=BACKGROUND_COLOR)
check_button.grid(row=2,column=0)
next_card()


windows.mainloop()