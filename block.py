from turtle import Turtle


class Block(Turtle):
    def __init__(self, color, position, assigned_score):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(position)
        self.score = assigned_score
