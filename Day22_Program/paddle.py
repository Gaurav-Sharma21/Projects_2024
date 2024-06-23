from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,cor_x,cor_y):
        super().__init__()
        self.cor_x = cor_x
        self.cor_y = cor_y
        self.shape("square")
        self.color("white")
        self.penup()
        self.position()
        self.shapesize(stretch_len=1, stretch_wid=5)



    
    def position(self):
        return self.goto(self.cor_x, self.cor_y)
    
    def forward_movement(self):
        new_cor = self.ycor() + 20
        self.goto(self.xcor(), new_cor)
    
    def backward_movement(self):
        new_cor = self.ycor() - 20
        self.goto(self.xcor(), new_cor)

    