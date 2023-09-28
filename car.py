from turtle import Turtle
import random
COLOR = ("blue", "yellow", "green", "red", "black")

DIFFICULTY = {"Easy": 25,
              "Medium": 40,
              "Hard": 75}


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.car_coordinates = []
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)
        self.shape("square")
        self.color(random.choice(COLOR))
        self.penup()
        self.setheading(180)
        self.random_y = random.randint(-240, 240)
        self.random_x = random.randint(320, 1320)
        self.start_pos = (self.random_x, self.random_y)
        self.goto(self.start_pos)

    def move(self):
        new_x = self.xcor()
        new_x -= 1
        self.setx(new_x)
        if self.xcor() < -320:
            self.setx(310)

