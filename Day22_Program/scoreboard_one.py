from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=("Arial", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center",font=("Arial", 50, "normal"))
        
    
    def update_for_left(self):
        self.clear()
        self.l_score += 1
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=("Arial", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center",font=("Arial", 50, "normal"))
    
    def update_for_right(self):
        self.clear()
        self.r_score += 1
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=("Arial", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center",font=("Arial", 50, "normal"))