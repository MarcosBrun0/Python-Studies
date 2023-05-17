from turtle import Turtle
import random
from typing import Self

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        
        self.allcars = []



    def creat_car(self):
            dice = random.randint(1,7)
            if dice == 1:
                new_car = Turtle()
                new_car.shape("square")
                new_car.penup()
                new_car.shapesize(1, 2)
                new_car.setx(300)
                new_car.color(random.choice(COLORS))
                new_car.sety(random.randrange(-240, 240))
                self.allcars.append(new_car)

        
    def movecar(self, increment):
         for car in self.allcars:
              car.backward(STARTING_MOVE_DISTANCE + increment*MOVE_INCREMENT) 

