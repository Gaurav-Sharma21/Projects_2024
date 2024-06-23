from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self) :
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setposition(0,275)
        self.write(f"Score: {self.score}", align="center",font=("Arial", 20, "normal"))
    
    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center",font=("Arial", 20, "normal"))
    
    def final_score(self):
        self.goto(0,0)
        self.write(f"GAME OVER! ", align="center",font=("Courier", 20, "normal"))
