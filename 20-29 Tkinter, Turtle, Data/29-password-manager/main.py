import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    pyperclip.copy(password)
    password_entry.delete(0,'end')
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    website_entry.delete(0,'end')

    email = email_entry.get()
    email_entry.delete(0,'end')

    password = password_entry.get()
    password_entry.delete(0,'end')
    if password == "" or email == "" or website == "":
        messagebox.showinfo(title="erro", message="don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title="Title",message=f"These are the details entered \n Email: {email} \n Password {password} \n Is it ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website}|{email}|{password} \n")
            f.close()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = tkinter.Canvas(width=200, height=200)
img_logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(130,100,image=img_logo)
canvas.grid(row=0,column=1)




website_label = tkinter.Label(text="Website:")
email_label = tkinter.Label(text="Email/Username:")
password_label = tkinter.Label(text="Password:")
website_entry = tkinter.Entry(width=38)
email_entry = tkinter.Entry(width=38)
password_entry = tkinter.Entry(width=21)
gen_pass_button = tkinter.Button(text="Generate Password", command=password_gen)
add_button = tkinter.Button(text="Add",width=36, command=save)
website_label.grid(row=1,column=0)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_label.grid(row=2,column=0)
email_entry.grid(row=2,column=1, columnspan=2)
password_label.grid(row=3,column=0)
password_entry.grid(row=3,column=1)
add_button.grid(row=4,column=1, columnspan=2)
gen_pass_button.grid(row=3,column=2)




window.mainloop()