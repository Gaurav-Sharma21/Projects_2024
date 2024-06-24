from turtle import Turtle, Screen
import random
import time
from create_turtle import Player
from random_blocks import Blocks
from score import Score

screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")


screen.tracer(0)

player1 = Player()
screen.listen()
screen.onkey(player1.movement, "w")

car_1 = Blocks()

score_1 = Score()

game_mode = True

while game_mode:
    time.sleep(0.1)
    screen.update()
    car_1.create_car()
    car_1.move_car()


    if player1.ycor() > 290:
        player1.reset_player()
        car_1.level_up()
        score_1.update_score()
    
    for car in car_1.cars:
        if player1.distance(car) < 20:
            game_mode = False
            score_1.game_over()
    













screen.exitonclick()