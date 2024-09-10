import turtle


class Score(turtle.Turtle):
    def __init__(self, game_size, text):
        super().__init__()
        self.game_size = game_size
        self.up()
        self.hideturtle()
        self.speed(0)
        self.update_score(text)

    def output(self, pos_y, text, size, weight, color, shadow=False):
        if shadow:
            offset = 5
            self.setx(offset)
            self.output(pos_y - offset, text, size, weight, '#117722')
            self.setx(0)
        self.sety(pos_y)
        self.pencolor(color)
        self.write(text, False, align='center', font=('DM Mono', size, weight))

    def update_score(self, text):
        self.clear()
        self.output(-self.game_size / 2.2, text, int(self.game_size / 2), 'normal', '#117722')

    def game_over(self, text):
        self.clear()
        self.output(self.game_size * 0.275, 'Game over', int(self.game_size / 9), 'bold', '#ddeebb', True)
        # write(self.game_size * 0.1, 'Score:', int(self.game_size / 9), 'bold', '#ddeebb', True)
        self.output(-self.game_size / 2.85, text, int(self.game_size * 0.375), 'bold', '#ddeebb', True)
        self.output(-self.game_size * 0.45, 'Press ESC to play again', int(self.game_size * 0.05), 'normal', '#ddeebb', True)
    
    def win(self, text):
        self.clear()
        self.output(self.game_size * 0.275, 'You won!', int(self.game_size / 9), 'bold', '#ddeebb', True)
        # write(self.game_size * 0.1, 'Score:', int(self.game_size / 9), 'bold', '#ddeebb', True)
        self.output(-self.game_size / 2.85, text, int(self.game_size * 0.375), 'bold', '#ddeebb', True)
        self.output(-self.game_size * 0.45, 'Press ESC to play again', int(self.game_size * 0.05), 'normal', '#ddeebb', True)
