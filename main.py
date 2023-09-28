from turtle import Screen
from scoreboard import ScoreBoard
import car
from player import Player
from car import Car
import time
import random
cars = []
car_speed = 0.005

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_on = True

player = Player()
scoreboard = ScoreBoard()

screen.onkeypress(player.go_forwards, "Up")
screen.listen()

for i in range(0, car.DIFFICULTY["Hard"]):
    car = Car()
    cars.append(car)
    print(cars[i])

while game_on:
    screen.update()
    time.sleep(car_speed)
    for i in cars:
        i.move()
        if player.distance(i) < 23 and (player.ycor() > (i.ycor()-10) or player.ycor() < (i.ycor()+10)):
            game_on = False
            scoreboard.game_over()

        if player.ycor() > 280:
            scoreboard.update_score()
            car_speed *= 0.5
            player.goto(0, -270)
            for i in cars:
                if i.xcor() < 300:
                    i.setx(i.xcor() + random.randint(300, 600))

screen.exitonclick()