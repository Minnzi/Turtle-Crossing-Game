from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.color("Black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)



