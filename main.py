import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player_one = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player_one.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
#     turtle collides with a car
    for car in car_manager.all_cars:
        if car.distance(player_one) < 20:
            game_is_on = False
            scoreboard.game_over()

#     car successful crossing
    if player_one.is_at_finish_line():
        player_one.go_to_start()
        car_manager.leval_up()
        scoreboard.increase_level()








screen.exitonclick()