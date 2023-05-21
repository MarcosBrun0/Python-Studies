import turtle
import pandas





screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.addshape("blank_states_img.gif")


tur = turtle.Turtle("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
print(data)










game_is_on = True
while game_is_on:

    answer = screen.textinput("50 States","Type State name")
    print(answer)
    if data[data["state"] == answer]:

        print("oi")







screen.exitonclick()