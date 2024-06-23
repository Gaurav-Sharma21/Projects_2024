import random 
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard_one import Score


screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor("black")
screen.title("PING_PONG")
game_ball = Ball()

screen.tracer(0)

paddle_right = Paddle(350,0)
paddle_left = Paddle(-350,0)

score1 = Score()




screen.listen()
screen.onkey(paddle_right.forward_movement, "w")
screen.onkey(paddle_left.forward_movement, "Up")
screen.onkey(paddle_right.backward_movement, "s")
screen.onkey(paddle_left.backward_movement, "Down")


game_working = True
while game_working:
    time.sleep(game_ball.ball_speed)
    screen.update()
    game_ball.start()

    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce()

    if (game_ball.distance(paddle_right) < 30 and game_ball.xcor() > 300) or (game_ball.distance(paddle_left) < 30 and game_ball.xcor() < -300):
        game_ball.collide()
    
    if game_ball.xcor() > 380:
        game_ball.reset_position()
        score1.update_for_left()
    if game_ball.xcor() < -380:
        game_ball.reset_position()
        score1.update_for_right()
























screen.exitonclick()