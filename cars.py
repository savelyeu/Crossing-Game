import random
from turtle import Turtle
import random

COLORS = ["#cb8175", "#e2a97e", "#f0cf8e", "#a8c8a6", "#6d8d8a", "#655057"]
STARTING_MOVE_POSITION = 5
MOVE_INCREMENT = 10

class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_POSITION

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_POSITION)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT