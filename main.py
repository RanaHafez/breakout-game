from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from block import Block

COLORS = ["#7D1E6A", "#EEB0B0", "#FFE59D", "#BDE6F1"]
SCORES = [1, 3, 5, 7]
screen = Screen()
paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()

bricks = []
x = -360
y = -50
for i in range(4):
    for j in range(2):
        # creating 2 rows of the same color and value
        while x < 380:
            block = Block(color=COLORS[i], position=(x, y), assigned_score=SCORES[i])
            bricks.append(block)
            x += 50
        x = -360
        y += 30


screen.bgcolor("#FF5D5D")
screen.setup(width=800, height=600)
screen.title(titlestring="Breakout Game")
# Stopping the animation does not work ??
screen.tracer(n=0,delay=0)
screen.listen()
screen.onkey(key="Right", fun=paddle.move_right)
screen.onkey(key="Left", fun=paddle.move_left)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect the collision with wall and bounce
    if ball.ycor() >= 290:
        ball.bounce_y()

    if ball.xcor() >= 390 or ball.xcor() <= -390:
        ball.bounce_x()

    # Detect the collision with the paddle ..
    if ball.distance(paddle) < 50 and ball.ycor() < -260:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            if ball.distance(brick) > ball.distance(brick):
                ball.bounce_x()
            else:
                ball.bounce_x()
                ball.bounce_y()
            scoreboard.update_score(brick_score=brick.score)
            bricks.remove(brick)
            break

    # Detect collision with the bottom wall.
    if ball.ycor() < -290:
        ball.reset_ball()
        scoreboard.update_tries()

    if scoreboard.tries == 0:
        game_on = False
        print("No More Tries .. ")


scoreboard.game_over()
screen.exitonclick()
