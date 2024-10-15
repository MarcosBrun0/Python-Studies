import tkinter
def button_clicked2():

    calculate_miles_to_km()

def calculate_miles_to_km():
    num = float(entry.get())
    print(num)
    result = str(num*1.60934)
    numberlabel["text"] = result



window = tkinter.Tk()
window.minsize(250, 150)
window.config(padx=20,pady=20)

entry = tkinter.Entry(width=6)
label1 = tkinter.Label()
label2 = tkinter.Label()
label3 = tkinter.Label(text="Km")
numberlabel = tkinter.Label()
button2 = tkinter.Button(text="Calculate", command=button_clicked2)
entry.grid(row=1,column=2)
label1.config(text="Miles")
label1.grid(row=1,column=3)

label2.config(text="is equal to:")
label2.grid(row=2,column=1)

numberlabel.config(text="0")
numberlabel.grid(row=2,column=2)

label3.grid(row=2,column=3)
button2.grid(row=3,column=2)





# my_label = tkinter.Label(text="I am a label")
# my_label.grid(row=1,column=1)
# #
#
# def button_clicked():
#     txt = entry.get()
#     my_label.config(text=txt)
#
#
# button = tkinter.Button(text="click me", command=button_clicked)
# # button.grid(row=2,column=2)
# #
# #
# new_button = tkinter.Button(text="ola")
# new_button.grid(row=1,column=3)
# entry = tkinter.Entry()
# entry.grid(row=4,column =4)
#
#
#
#
# def add(*argues):
#     sum = 0
#     for argue in argues:
#         sum = sum + argue
#         print(sum)
#
#
# add(10, 20, 30, 40, 50)

window.mainloop()
