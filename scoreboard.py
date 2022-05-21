from turtle import Turtle

GAMEOVER = """


░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

"""

SCORED = """

░██████╗░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝██║░░██║██████╔╝█████╗░░██║░░██║
░╚═══██╗██║░░██╗██║░░██║██╔══██╗██╔══╝░░██║░░██║
██████╔╝╚█████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
"""
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#85586F")
        self.tries = 4
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(x=-350, y=250)
        self.write(arg=f"Tries {self.tries}", align="center", font=("courier", 15, "bold"))
        self.goto(x=-340, y=220)
        self.write(arg=f"Score {self.score}", align="center", font=("courier", 15, "bold"))

    def update_tries(self):
        self.tries -= 1
        self.update()

    def update_score(self, brick_score):
        self.score += brick_score
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"{GAMEOVER}", align="center")