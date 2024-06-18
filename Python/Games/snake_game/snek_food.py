import turtle
import random as r


class Food(turtle.Turtle):
    def __init__(self, game_scale):
        super().__init__()
        self.reach = int(game_scale/2) - 1
        self.up()
        self.shape('square')
        self.color('red')
        self.shapesize(1.5)
        self.speed(0)
        self.move()

    def move(self):
        self.setpos(
            r.randint(-self.reach, self.reach) * 40,
            r.randint(-self.reach, self.reach) * 40)

    def coords(self):
        x = round(self.xcor())
        y = round(self.ycor())
        coords = (x, y)
        return coords
