import tkinter
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
reps = 0
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    timer_label.config(text="Timer")
    global marks
    marks = ""
    global reps
    reps = 0
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global marks
    reps += 1
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break")
    elif reps % 2 == 0:

        countdown(short_break_sec)
        timer_label.config(text="Break")

    else:
        countdown(work_sec)
        timer_label.config(text="Work")

    if reps % 2 == 0:
        marks = marks + "✓"
        check_marks.config(text=marks)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 140, text="25:00", font=(FONT_NAME, 37, "bold"))
canvas.grid(row=2, column=2)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 37, "bold"))
timer_label.grid(row=1, column=2)
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)
check_marks = Label(text="")
check_marks.grid(row=3, column=2)

window.mainloop()
