import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = CarManager()
player = Player()
score = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
incremento = 0
game_is_on = True
while game_is_on:
    

    time.sleep(0.1)
    screen.update()
    
    screen.listen()
    screen.onkey(player.move,"w")

    cars.creat_car()
    cars.movecar(incremento)


    for car in cars.allcars:
        if car.distance(player)<20:
            pass       
            score.game_over()
            game_is_on = False

    if player.ycor() > player.chgada:
        player.finished()
        incremento += 1
        score.levelup()
   
screen.exitonclick()