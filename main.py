from turtle import Screen
BORDERS = [280, -280]

screen = Screen()

def create_screen():
    """
    create the screen
    """
    screen.setup(600, 600) # set up the screen
    screen.bgcolor("black")
    screen.title("The Pong Game")
    screen.tracer(0) # turn off automatic animation

def game():
    """
    move the paddle and the ball until the game ends
    """
    print("game method")

create_screen() # create the screen
game() # move the paddle and the ball until the game ends
screen.exitonclick()

# class:
# - scoreboard (player 1 & player 2)
# - ball
# - paddle (player 1 & player 2)

# tasks:
# 2. create and move a paddle
# 3. create another paddle
# 4. create the ball and make it move
# 5. detect collision with wall and bounce
# 6. detect collision with paddle
# 7. detect when paddle misses
# 8. keep score