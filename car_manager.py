from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 280


def random_position(car):
    starting_y = random.randint(-220, 230)
    car.goto(STARTING_X, starting_y)
class CarManager():
    def __init__(self):
        self.all_cars = []
        self.pace = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_len=4)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_position(new_car)
        self.all_cars.append(new_car)

    def move(self, car):
        car.backward(self.pace)



    def move_increment(self):
        self.pace += MOVE_INCREMENT



