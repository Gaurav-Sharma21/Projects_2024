from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-230,230)
        self.write(f"Level: {self.level}", align="left", font=("Arial", 20, "normal"))


    
    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(-230,230)
        self.write(f"Level : {self.level}", align="left", font=("Arial", 20, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center", font=("Arial", 20, "normal"))

