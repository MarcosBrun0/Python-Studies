from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.chgada = FINISH_LINE_Y


    def move(self):

        new_cord = self.ycor()
        new_cord = new_cord + 10
        self.sety(new_cord)
        self.color("black")

    def finished(self):
         self.goto(STARTING_POSITION)
