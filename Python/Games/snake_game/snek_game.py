import time
import turtle
import snek_creature, snek_score, snek_food

# config
game_scale = 21  # needs to be an even number if easy_mode is enabled, I'll convert it for you if you forget
snake_starting_length = 3  # aka starting score
initial_game_speed = 0.5
background_color = '#228833'
easy_mode = 0  # set 1 or 0 to toggle it, or use the [E] key in-game


if game_scale % 2 != 0:
    game_scale -= 1


def play():
    def restart():
        if not snek.alive:
            game.clear()
            play()
        return

    def toggle_easy():
        global easy_mode
        if easy_mode == 0: easy_mode = 1
        elif easy_mode == 1: easy_mode = 0
        score.update_score(snek.len())
        score.output(-int(game_size/2.05), f'easy mode: {easy_mode}', int(game_size/15), 'bold', '#ddeebb', True)
        snek.is_easy_mode = easy_mode
        return

    # initialize game window
    game_size = game_scale * 40
    game = turtle.Screen()
    game.title('Snake')
    game.setup(game_size, game_size)
    game.bgcolor(background_color)
    game.tracer(1, 0)
    game.listen()

    # initialize game elements
    score = snek_score.Score(game_size=game_size, text=snake_starting_length)
    food = snek_food.Food(game_scale=game_scale)
    snek = snek_creature.Snek(game_size=game_size, starting_length=snake_starting_length, is_easy_mode=easy_mode)

    # add control
    game.onkeypress(snek.head_up, 'w')
    game.onkeypress(snek.head_down, 's')
    game.onkeypress(snek.head_left, 'a')
    game.onkeypress(snek.head_right, 'd')
    game.onkeypress(snek.head_up, 'Up')
    game.onkeypress(snek.head_down, 'Down')
    game.onkeypress(snek.head_left, 'Left')
    game.onkeypress(snek.head_right, 'Right')
    game.onkeypress(restart, 'Escape')
    game.onkeypress(toggle_easy, 'e')

    # bring it all together
    won = False
    while snek.alive:
        if snek.len() == game_scale**2:
            snek.alive = False
            won = True
        game_speed = max(0.05, initial_game_speed - 0.02 * snek.len())
        snek.move()
        time.sleep(game_speed)
        if snek.coords(snek.head) == food.coords():
            score.update_score(snek.len() + 1)
            food.move()
            snek.grow()
    else:
        if won:
            food.hideturtle()
            score.win(snek.len())
        else:
            score.game_over(snek.len())

    game.mainloop()


play()
