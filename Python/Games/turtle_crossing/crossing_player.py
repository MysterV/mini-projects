import turtle


class Player(turtle.Turtle):
    def __init__(self, game_size, player_speed):
        super().__init__('turtle')
        self.up()
        self.speed(0)
        self.border = int(game_size/2)
        self.color(''
                   '#114422')
        self.setheading(90)
        self.start_pos = -self.border + 20
        self.sety(self.start_pos)
        self.speed = player_speed

    def move_up(self):
        if self.ycor() < self.border-20:
            self.sety(self.ycor() + self.speed)

    def move_down(self):
        if self.ycor() > -(self.border-20):
            self.sety(self.ycor() - self.speed)

    def move_left(self):
        if self.xcor() > -(self.border-20):
            self.setx(self.xcor() - self.speed)

    def move_right(self):
        if self.xcor() < self.border-20:
            self.setx(self.xcor() + self.speed)