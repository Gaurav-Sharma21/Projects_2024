from turtle import Turtle 
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.setpos(0,0)
        self.color("white")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.ball_speed = 0.1
    

    def start(self):
        new_xcor = self.xcor() + self.x_cor
        new_ycor = self.ycor() + self.y_cor
        self.setpos(new_xcor,new_ycor)
    
    def bounce(self):
        self.y_cor *= -1
    
    def collide(self):
        self.x_cor *= -1
        self.ball_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.collide()
        self.ball_speed = 0.1
    
        

