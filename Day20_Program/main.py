from turtle import Screen
import time
import snake_body
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("SNAKE_GAME")
screen.tracer(0)


snake1 = snake_body.Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake1.up, "w")
screen.onkey(snake1.down, "s")
screen.onkey(snake1.left, "a")
screen.onkey(snake1.right, "d")

default_motion = True

while default_motion:
    screen.update()
    time.sleep(0.1)
    
    snake1.move()
    # Checking for food
    if snake1.collection_snake[0].distance(food) < 15:
        food.refresh()
        snake1.extend()
        score.update()
    
    # Banging on the Wall
    if (snake1.collection_snake[0].xcor() > 280) or (snake1.collection_snake[0].xcor() < -280) or (snake1.collection_snake[0].ycor() > 280) or (snake1.collection_snake[0].ycor() < -280):
        default_motion = False
        score.final_score()
    
    # Eating your own tail
    for i in snake1.collection_snake[1:]:
        if snake1.collection_snake[0].distance(i) < 15:
            default_motion = False
            score.final_score()




screen.exitonclick()