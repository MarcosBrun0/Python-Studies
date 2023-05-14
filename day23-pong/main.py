from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(700,600)


Lpaddle = Paddle((-330,0))
Rpaddle = Paddle((330,0))
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(Lpaddle.up,"w")
screen.onkey(Lpaddle.down,"s")
screen.onkey(Rpaddle.up,"Up")
screen.onkey(Rpaddle.down,"Down")


game_is_on = True
while game_is_on:
    ball.move()
    print(ball.ycor())
#Detect collision with the wall
    if ball.ycor()>300 or ball.ycor() < -300:
        ball.bounce(1)

#Detect collision with the r-paddle
    if ball.xcor() > 330 and ball.distance(Rpaddle) <50:
        
        ball.x_move =  ball.x_move*1.1
        ball.y_move = ball.y_move*1.1
        
        ball.bounce(0)
      
  

    if ball.xcor() < -330 and ball.distance(Lpaddle)<50:
        ball.x_move =  ball.x_move*1.1
        ball.y_move =  ball.y_move*1.1
        
        ball.bounce(0)
        
#Detect out of bounds
    if ball.xcor() > 350 or ball.xcor() < -350:
        if ball.xcor() > 350:
            score.l_score += 1
        else:
            score.r_score += 1

        score.scoreup()
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        time.sleep(0.5)
        
        ball.x_move = 1
        ball.y_move = 1
        ball.bounce(0)

screen.exitonclick()