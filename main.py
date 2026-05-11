import time
from turtle import Screen
from Ball import Ball
from Paddle import Paddle
from Scoreboard import Scoreboard

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
    scoreboard = Scoreboard() # create the scoreboard

    screen.listen()
    screen.onkey(left_paddle.move_up, "w")  # when click on up w, paddle right move up
    screen.onkey(left_paddle.move_down, "s")  # when click on s a key, paddle right move down
    screen.onkey(right_paddle.move_up, "Up")  # when click in an up key, paddle right move up
    screen.onkey(right_paddle.move_down, "Down")  # when click in a down key, paddle right move down

    is_game_on = True
    while is_game_on: # while the game happens
        screen.update() # show the initial paddles
        time.sleep(ball.move_speed)  # a brief pause to show the movement

        ball.move() # move the ball

        if ball.ycor() > 280 or ball.ycor() < -280: # detect collision with up/down wall
            ball.bounce_y() # needs bounce

        if ball.xcor() < -320 and ball.distance(left_paddle) < 50: # detect collision with left paddle
            ball.bounce_x() # needs bounce

        if ball.xcor() > 320 and ball.distance(right_paddle) < 50: # detect collision with right paddle
            ball.bounce_x() # needs bounce

        if ball.xcor() < -380: # detect when the left paddle misses the ball
            ball.reset_position() # center of the screen
            scoreboard.right_point()  # right paddle wins

        if ball.xcor() > 380: # detect when the right paddle misses the ball
            ball.reset_position() # center of the screen
            scoreboard.left_point() # left paddle wins

        # check if the game is over
        if scoreboard.left_score == 3 or scoreboard.right_score == 3:
            scoreboard.game_over()
            is_game_on = False


create_screen() # create the screen
game() # move the paddle and the ball until the game ends
screen.exitonclick()