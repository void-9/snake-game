from turtle import Turtle

ALIGEMENT = 'center'
FONT = ('Arial', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('orange')
        self.goto(x=0, y=270)
        self.score = 0
        self.write(arg=f'Score: {self.score}', align=ALIGEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGEMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f'Game over!', align=ALIGEMENT, font=FONT)
