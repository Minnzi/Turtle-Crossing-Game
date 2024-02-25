import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.onkey(key="Up", fun=player.move)


loop = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop % 6 == 0:
        car_manager.create_car()
    for car in car_manager.all_cars:
        car_manager.move(car)
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.finish_line():
        scoreboard.increase_level()
        car_manager.move_increment()
    loop += 1


screen.exitonclick()
