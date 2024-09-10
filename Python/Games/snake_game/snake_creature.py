import turtle
import random as r


class Snek:
    def __init__(self, game_size, starting_length=3, is_easy_mode=False):
        self.is_easy_mode = is_easy_mode
        self.reach = int(game_size / 2) - 40
        self.alive = True
        self.segments = []
        self.grow(starting_length)
        self.head = self.segments[0]
        self.head.shapesize(2)
        for i in range(1, self.len()):
            self.segments[i].back(40 * i)

    def grow(self, count=1):
        for i in range(count):
            self.segments.append(turtle.Turtle('square'))
            self.segments[-1].up()
            self.segments[-1].color('#bbdd33')
            self.segments[-1].speed(0)
            if self.len() > 1:
                self.segments[-1].goto(self.segments[-2].xcor(), self.segments[-2].ycor())

    def move(self):
        for i in range(self.len() - 1, 0, -1):
            self.segments[i].setpos(self.coords(self.segments[i-1]))

        self.segments[1].setheading(self.head.heading())  # lets us compare head turns
        self.head.forward(40)
        if self.is_easy_mode:
            if self.coords(self.head)[0] > self.reach:
                self.head.setx(-self.reach)
            elif self.coords(self.head)[1] > self.reach:
                self.head.sety(-self.reach)
            elif self.coords(self.head)[0] < -self.reach:
                self.head.setx(self.reach)
            elif self.coords(self.head)[1] < -self.reach:
                self.head.sety(self.reach)
        else:
            self.check_if_alive()

    def check_if_alive(self):
        # collides with wall?
        for coord in self.coords(self.head):
            if coord not in range(-self.reach, self.reach + 1):
                self.alive = False
                return

        # collides with tail?
        for i in range(1, self.len()):
            if self.coords(self.head) == self.coords(self.segments[i]):
                self.alive = False
                return

    def coords(self, segment):
        x = round(segment.xcor())
        y = round(segment.ycor())
        coords = (x, y)
        return coords

    def len(self):
        return len(self.segments)

    # snake movement functions to make the "onkey" screen method work (it doesn't accept arguments)
    def head_left(self):
        if self.segments[1].heading() != 0 and self.head.heading() != 0:
            self.head.setheading(180)

    def head_right(self):
        if self.segments[1].heading() != 180 and self.head.heading() != 180:
            self.head.setheading(0)

    def head_down(self):
        if self.segments[1].heading() != 90 and self.head.heading() != 90:
            self.head.setheading(270)

    def head_up(self):
        if self.segments[1].heading() != 270 and self.head.heading() != 270:
            self.head.setheading(90)
