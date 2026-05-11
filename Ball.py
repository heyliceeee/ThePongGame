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
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

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
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        """
        bounce in y the ball
        """
        self.y_move *= -1
    def bounce_x(self):
        """
        bounce in x the ball
        """
        self.x_move *= -1
        self.move_speed *= 0.9 # increase move speed
    def reset_position(self):
        """
        go center of the screen and bounce in x the ball
        """
        self.goto(0, 0)
        self.move_speed = 0.1 # set normal move speed
        self.bounce_x()