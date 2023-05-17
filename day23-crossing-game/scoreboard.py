from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.goto(-200,200)
        self.level = 0
        self.write(f"Level: {self.level}",font=FONT)




    def levelup(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)




    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT)

