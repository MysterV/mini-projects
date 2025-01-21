import turtle
import random as r



class Cars():
    def __init__(self, game_size, car_count, car_speed):
        super().__init__()
        self.border = int(game_size / 2)
        self.cars = []
        self.summon_cars(car_count, init=True)
        self.speed = car_speed
        self.move()

    def summon_cars(self, count, init):
        for i in range(count):
            self.cars.append(turtle.Turtle('square'))
            j = self.cars[-1]
            j.up()
            j.speed(0)
            j.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
            j.side = r.choice((1, -1))
            j.shapesize(1, 2)
            if init:
                j.goto(r.choice(range(-self.border, self.border, 40)),
                       r.choice(range(-self.border+60, self.border, 20)))
            else:
                j.goto(j.side * (self.border + 20),
                       r.choice(range(-self.border, self.border, 20)))
            if j.side == 1:
                j.setheading(0)
            elif j.side == -1:
                j.setheading(180)

    def move(self):
        for i in self.cars:
            if abs(i.xcor()) <= self.border:
                i.forward(self.speed)
            else:
                i.setx(-i.side * self.border)


class Rocks():
    def __init__(self, game_size, rock_count):
        self.border = int(game_size / 2)
        self.rocks = []
        self.summon_rocks(rock_count)

    def summon_rocks(self, count):
        for i in range(count):
            self.rocks.append(turtle.Turtle('circle'))
            j = self.rocks[-1]
            j.up()
            j.speed(0)
            j.color('#414243')
            j.shapesize(2)
            j.goto(r.randint(-self.border, self.border),
                   r.randint(-self.border+60, self.border))
