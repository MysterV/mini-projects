import turtle


class Score(turtle.Turtle):
    def __init__(self, game_size, text, text_color):
        super().__init__()
        self.font_size = int(game_size / 2)
        self.offset = int(-game_size / 2.3)
        self.up()
        self.hideturtle()
        self.speed(0)
        self.sety(self.offset)
        self.pencolor(text_color)
        self.update_score(text)

    def update_score(self, text):
        self.clear()
        self.write(text, False, align='center', font=('DM Mono', self.font_size, 'normal'))
