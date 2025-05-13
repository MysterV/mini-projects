# This is a 'simple' game that will have you
# dodging high-speed vehicles coming at you from all directions
# and jumping across a stone-filled field,
# but don't blink - one wrong move and you're out!

import turtle
import time
import math
import crossing_player
import crossing_obstacles
import crossing_score

# TODO
# - [ ] dynamic screen - starts following turtle once turtle gets to the screen center
#     - [ ] OR is slowly moving forward, and if the turtle touches the bottom edge, game over

# config
start_game_size = 600  # for optimal results set to half your screen height
score_factor = 2  # increase to reduce obstacle count

background_color = '#779955'
text_color = '#658743'

player_speed = 20
car_speed = 10

score = 1
start_rock_count = 5
start_car_count = 10


def game_setup(rock_count, car_count):
    global game, player, cars, rocks, scoreboard
    game = turtle.Screen()

    if score >= 50: game.game_size = int(start_game_size * 1.75)
    elif score >= 25: game.game_size = int(start_game_size * 1.5)
    elif score >= 10: game.game_size = int(start_game_size * 1.25)
    else: game.game_size = start_game_size

    game.clear()
    game.tracer(0, 0)
    game.setup(game.game_size, game.game_size)
    game.colormode(255)
    game.bgcolor(background_color)
    game.listen()

    player = crossing_player.Player(game.game_size, player_speed)
    rocks = crossing_obstacles.Rocks(game.game_size, rock_count)
    cars = crossing_obstacles.Cars(game.game_size, car_count, car_speed)
    scoreboard = crossing_score.Score(game.game_size, score, text_color)

    # WASD movement
    game.onkeypress(player.move_up, 'w')
    game.onkeypress(player.move_left, 'a')
    game.onkeypress(player.move_down, 's')
    game.onkeypress(player.move_right, 'd')
    # arrow movement
    game.onkeypress(player.move_up, 'Up')
    game.onkeypress(player.move_left, 'Left')
    game.onkeypress(player.move_down, 'Down')
    game.onkeypress(player.move_right, 'Right')


def play():
    global game, player, cars, rocks, scoreboard, score
    rock_count = int(max(math.log(score, score_factor), 1) * start_rock_count)
    car_count = int(max(math.log(score, score_factor), 1) * start_car_count)
    game_setup(rock_count, car_count)

    while True:
        is_touching_rocks = False
        time.sleep(0.05)
        game.update()
        scoreboard.update_score(score)
        cars.move()
        for i in cars.cars:
            if player.distance(i) < 25:
                player.sety(player.start_pos)

        for i in rocks.rocks:
            if player.distance(i) < 40:
                is_touching_rocks = True
                player.speed = player_speed/2
        if not is_touching_rocks:
            player.speed = player_speed

        if player.ycor() >= game.game_size/2 - 20:
            score += 1
            break
    play()


play()

game.mainloop()
