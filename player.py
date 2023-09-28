import random
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, -270)
        self.shape("turtle")
        self.setheading(90)

    def go_forwards(self):
        new_y = self.ycor()
        new_y += 10
        self.sety(new_y)

    def go_backwards(self):
        new_y = self.ycor()
        new_y -= 10
        self.sety(new_y)
