from turtle import Turtle
WIDTH = 20
"""
width of the ball
"""
HEIGHT = 20
"""
height of the ball
"""
X_POS = 0
"""
x position of the ball
"""
Y_POS = 0
"""
y position of the ball
"""


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        """
        create the ball
        """
        self.shape("circle") # set shape
        self.color("white") # set color
        self.shapesize(stretch_wid=1, stretch_len=1)  # set size
        self.penup()  # no draw while moving
        self.goto(0, 0)  # set position

    def move(self):
        """
        move the ball
        """
        new_x = self.xcor() + 1
        new_y = self.ycor() + 1
        self.goto(new_x, new_y)