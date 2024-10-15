from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 1
        self.y_move = 1
       
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce(self, d):
        if d == 1:
            self.y_move = self.y_move*(-1)
        else:
            self.x_move = self.x_move*(-1)
            
       