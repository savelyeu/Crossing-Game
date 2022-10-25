import time
from turtle import Screen
from player import Player
from cars import Cars
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#272329")
screen.title("ŽABA")
screen.tracer(0)

player = Player()
car_manager = Cars()
score = Score()

screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.finish():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()



screen.exitonclick()
