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
Y_POS_RIGHT = 0
"""
y position of the paddles
"""

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.create(x_pos)

    def create(self, x_pos):
        """
        create the paddle
        """
        self.shape("square") # set shape
        self.color("white") # set color
        self.shapesize(stretch_wid=5, stretch_len=1) # set size
        self.penup() # no draw while moving
        self.goto(x_pos, Y_POS_RIGHT) # set position
    def move_up(self):
        """
        move up the left paddle
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def move_down(self):
        """
        move down the left paddle
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)