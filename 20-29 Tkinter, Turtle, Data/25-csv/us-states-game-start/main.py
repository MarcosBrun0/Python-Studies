import turtle
import pandas





screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("lightblue")
screen.addshape("/home/mb/Documents/codes/PythonCourse/day25-csv/us-states-game-start/blank_states_img.gif")


tur = turtle.Turtle("/home/mb/Documents/codes/PythonCourse/day25-csv/us-states-game-start/blank_states_img.gif")

data = pandas.read_csv("/home/mb/Documents/codes/PythonCourse/day25-csv/us-states-game-start/50_states.csv")
print(data)

all_states = data.state.to_list()


writer = turtle.Turtle()
writer.hideturtle()
writer.penup()




guessed_states = []
while len(guessed_states) < 50:

    answer = screen.textinput(f"Guess States:{len(guessed_states)}/50","Type State name").title()
    
    for state in all_states:
        if answer == state:
            guessed_states.append(answer)
            state_data = data[data.state == answer]
            print(answer)
            cor = (int(state_data.x), int(state_data.y))
            print(cor)
            writer.goto(cor)
            writer.write(f"{answer}")


    


screen.exitonclick()