from turtle import Turtle
import random


block_colors = ["blue", "green", "red"]

class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = 5
        
    
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(block_colors))
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y + 20)
            self.cars.append(new_car)
    
    def move_car(self):
        for i in self.cars:
            i.backward(self.move_distance)
    
    def level_up(self):
        self.move_distance += 5



        
