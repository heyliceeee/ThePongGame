import time
from turtle import Screen

from Ball import Ball
from Paddle import Paddle
BORDERS = [280, -280]

screen = Screen()

def create_screen():
    """
    create the screen
    """
    screen.setup(800, 600) # set up the screen
    screen.bgcolor("black")
    screen.title("The Pong Game")
    screen.tracer(0) # turn off automatic animation
def game():
    """
    move the paddle and the ball until the game ends
    """
    left_paddle = Paddle(-350) # create the left paddle
    right_paddle = Paddle(350) # create the right paddle
    ball = Ball() # create the ball
    # create the scoreboard

    screen.listen()
    screen.onkey(left_paddle.move_up, "w")  # when click in up w, paddle right move up
    screen.onkey(left_paddle.move_down, "s")  # when click in s key, paddle right move down
    screen.onkey(right_paddle.move_up, "Up")  # when click in up key, paddle right move up
    screen.onkey(right_paddle.move_down, "Down")  # when click in down key, paddle right move down

    is_game_on = True
    while is_game_on: # while game happens
        screen.update() # show the initial paddles
        time.sleep(0.1)  # a brief pause to show the movement

        ball.move() # move the ball

        if ball.ycor() > 280 or ball.ycor() < -280: # detect collision with wall
            ball.bounce() # needs bounce
        # detect collision with paddle
        # detect when paddle misses

create_screen() # create the screen
game() # move the paddle and the ball until the game ends
screen.exitonclick()

# class:
# - scoreboard (player 1 & player 2)
# - ball
# - paddle (player 1 & player 2)

# tasks:
# 6. detect collision with paddle
# 7. detect when paddle misses
# 8. keep score