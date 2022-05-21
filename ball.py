from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.color("#FFC3C3")
        self.goto(x=0, y=-255)
        self.x_move = 5
        self.y_move = 5

    def move(self):
        self.goto(x=self.xcor()+self.x_move, y=self.ycor()+self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(x=0, y=-255)
        self.bounce_x()
        self.bounce_y()
