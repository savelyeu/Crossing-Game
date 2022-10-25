from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("#E3DEDA")
        self.hideturtle()
        self.penup()
        self.goto(270, -280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Uzrovień: {self.level}", align="right", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("KANIEC HUĹNI", align="center", font=FONT)

