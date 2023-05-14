from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.goto(-200,170)
        self.write(self.l_score,align="center", font=("Courier",80,"normal"))
        
        self.goto(200,170)
        self.write(self.r_score,align="center", font=("Courier",80,"normal"))
        
    def scoreup(self):
        self.clear()
        self.goto(-200,170)
        self.write(self.l_score,align="center", font=("Courier",80,"normal"))
        
        self.goto(200,170)
        self.write(self.r_score,align="center", font=("Courier",80,"normal"))
        