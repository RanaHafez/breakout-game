from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=-280)
        self.shape("square")
        self.fillcolor("#FFE3A9")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(x=new_x, y=self.ycor())
