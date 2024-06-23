import time
from turtle import Turtle

class Snake:

    def __init__(self):
        self.collection_snake = []
        self.create_snake()
        self.head_body()
    
    def create_snake(self): 
        for i in range(3):
            self.position_snake(i)
            
    
    def position_snake(self,i):
        name = Turtle(shape="square")
        name.penup()
        name.color("white")
        name.goto(-20*i,0)
        self.collection_snake.append(name)

    
    def extend(self):
        self.position_snake(2)


    def move(self):
        for num in range(len(self.collection_snake)- 1, 0, -1):
            new_x = self.collection_snake[num - 1].xcor()
            new_y = self.collection_snake[num -1].ycor()
            self.collection_snake[num].goto(new_x,new_y)
        self.collection_snake[0].forward(20)

    def head_body(self):
        self.collection_snake[0].color("cyan")
        self.collection_snake[0].shape("circle")
        self.collection_snake[0].shapesize(0.6,0.8)
    
    def up(self):
        if self.collection_snake[0].heading() != 270:
            self.collection_snake[0].setheading(90)
    def down(self):
        if self.collection_snake[0].heading() != 90:
            self.collection_snake[0].setheading(270)
    def left(self):
        if self.collection_snake[0].heading() != 0:
            self.collection_snake[0].setheading(180)
    def right(self):
        if self.collection_snake[0].heading() != 180:
            self.collection_snake[0].setheading(0)
