from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
    def increament(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score}",align="center",font=("Arial",24,"normal"))
    def gameover(self):
        self.goto(0,0)
        self.clear()
        self.write(f"score: {self.score}\ngame over",align="center",font=("Arial",24,"normal"))