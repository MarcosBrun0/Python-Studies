import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = CarManager()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:


    time.sleep(0.1)
    screen.update()
    
    screen.listen()
    screen.onkey(player.move,"w")

    cars.creat_car()
    cars.movecar()





    if player.ycor() > player.chgada:
        player.finished()
   
screen.exitonclick()