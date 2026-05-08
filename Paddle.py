from turtle import Turtle
WIDTH = 20
"""
width of the paddle
"""
HEIGHT = 100
"""
height of the paddle
"""
MOVE_DISTANCE = 20
"""
number of the steps that paddle move 
"""
X_POS_RIGHT = [-350, 350]
"""
x position of the paddles
"""
Y_POS_RIGHT = 0
"""
y position of the paddles
"""

class Paddle:
    def __init__(self):
        self.all_paddles = []
        self.create()

    def create(self):
        """
        create the paddles (left and right)
        """
        for current_paddle in range(0, 2):
            new_paddle = Turtle()
            new_paddle.shape("square") # set shape
            new_paddle.color("white") # set color
            new_paddle.shapesize(stretch_wid=5, stretch_len=1) # set size
            new_paddle.penup() # no draw while moving
            new_paddle.goto(X_POS_RIGHT[current_paddle], Y_POS_RIGHT) # set position

            self.all_paddles.append(new_paddle) # add new_paddle to the list
    def move_up_paddle_left(self):
        """
        move up the left paddle
        """
        new_y = self.all_paddles[0].ycor() + 20
        self.all_paddles[0].goto(self.all_paddles[0].xcor(), new_y)
    def move_down_paddle_left(self):
        """
        move down the left paddle
        """
        new_y = self.all_paddles[0].ycor() - 20
        self.all_paddles[0].goto(self.all_paddles[0].xcor(), new_y)
    def move_up_paddle_right(self):
        """
        move up the right paddle
        """
        new_y = self.all_paddles[1].ycor() + 20
        self.all_paddles[1].goto(self.all_paddles[1].xcor(), new_y)
    def move_down_paddle_right(self):
        """
        move down the right paddle
        """
        new_y = self.all_paddles[1].ycor() - 20
        self.all_paddles[1].goto(self.all_paddles[1].xcor(), new_y)