import tkinter
import random
import string
import csv

BACKGROUND_COLOR = "#B1DDC6"

#layout and setup
windows = tkinter.Tk()
windows.title("Flash Cards")
windows.config(pady=50,padx=50, background=BACKGROUND_COLOR)
Card_Front = tkinter.PhotoImage(file="card_front.png")
canvas = tkinter.Canvas(width=800,height=526)
canvas.create_image(400,263, image = Card_Front)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)

canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"))
canvas.create_text(400,263, text="Word", font=("Ariel",70,"bold"))
canvas.grid(row=0,column=1)

cross_img = tkinter.PhotoImage(file="images/wrong.png")
Unknown_button =tkinter.Button(image=cross_img)
Unknown_button.config(highlightthickness=0, background=BACKGROUND_COLOR)
Unknown_button.grid(row=2,column=2)

check_img = tkinter.PhotoImage(file="images/right.png")
check_button = tkinter.Button(image=check_img)
check_button.config(highlightthickness=0,bg=BACKGROUND_COLOR)
check_button.grid(row=2,column=0)
def UpdateWord():

    with open("/Users/MBhome/Documents/Codes/Python/Flash-Card/data/french_words.csv", "r") as csvFile:
        csvreader = csv.reader(csvFile)

        for row in csvreader:
            print(row)





windows.mainloop()