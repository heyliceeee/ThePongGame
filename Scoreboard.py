from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def create(self):
        """
        create the scoreboard
        """
        self.color("white") # set color
        self.penup()  # no draw while moving
        self.hideturtle() # hide the turtle
    def update(self):
        """
        update the scoreboard
        """
        self.clear()
        self.goto(-100, 200)  # set position
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)  # set position
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
    def left_point(self):
        """
        add one point to the left score
        """
        self.left_score += 1
        self.update()
    def right_point(self):
        """
        add one point to the right score
        """
        self.right_score += 1
        self.update()