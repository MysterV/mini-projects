import time
import turtle
import random as r

# TODO
# - ball
#   - going behind paddle and game reset
#   - better reaction to paddles
#   - fix turning
# - score updates

game = turtle.Screen()
game.setup(800, 600)
game.title('Ping: 2147483647ms')
game.bgcolor('#142434')
game.tracer(1, 0)
game.listen()

line = turtle.Turtle('square')
line.up()
line.shapesize(0.4, 1)
line.color('#344454')
line.hideturtle()

line.right(90)
line.sety(game.window_height()/2-25)

s = []
for i in range(int(game.window_height()/34)):
    s.append(line.stamp())
    line.forward(34)


class Paddle(turtle.Turtle):
    def __init__(self, starting_pos, paddle_scale):
        super().__init__()
        self.shape('square')
        self.length = paddle_scale*20
        self.shapesize(paddle_scale, 0.8)
        self.color('#d4e4f4')
        self.up()
        self.goto(starting_pos)

    def move_up(self):
        if self.ycor() <= game.window_height()/2 - 20 - self.length/2:
            self.sety(self.ycor()+20)

    def move_down(self):
        if self.ycor() >= -game.window_height()/2 + 20 + self.length/2:
            self.sety(self.ycor()-20)


class Pong(turtle.Turtle):
    def __init__(self, angle):
        super().__init__()
        self.shape('circle')
        self.color('#d4a4a4')
        self.up()
        self.out = 0
        self.right(angle)
        self.speed = starting_speed

    def move_forward(self):
        # bounce off the left paddle
        if self.xcor() <= p_1.xcor()+24:
            if self.distance(p_1) <= p_1.length/2 + 10:
                self.bounce_paddle()
                self.speed = max(0.015, self.speed - 0.005)
            else:
                self.out_of_bounds(2)

        # bounce off the right paddle
        if self.xcor() >= p_2.xcor()-24:
            if self.distance(p_2) <= p_2.length/2 + 10:
                self.bounce_paddle()
                self.speed = max(0.02, self.speed - 0.002)
            else:
                self.out_of_bounds(1)

        # bounce off the world edge
        if abs(self.ycor()) >= game.window_height()/2-20:
            self.setheading(-self.heading())

        self.forward(10)

    def bounce_paddle(self):
        self.setheading(180 - self.heading())

    def out_of_bounds(self, p):
        self.goto(0, r.randint(int(-game.window_height()/2+20), int(game.window_height()/2)-20))
        self.bounce_paddle()
        eval(f'score_{p}').update_score()
        self.speed = starting_speed
        self.out = 1


class Score(turtle.Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.up()
        self.hideturtle()
        self.pencolor('#243444')
        self.score = 0
        self.goto(pos_x, -300)
        self.update_score()

    def update_score(self):
        self.score += 1
        text_scale = len(str(self.score))+1
        if text_scale == 2:
            self.sety(-225)
        elif text_scale == 3:
            self.sety(-150)
        else:
            self.sety(-100)
        self.clear()
        self.write(self.score, False, align='center', font=('DM Mono', int(500/text_scale), 'normal'))


# config
paddle_distance = 350
paddle_length = 5
starting_speed = 0.05
ball_angle = 45

p_1 = Paddle((-paddle_distance, 0), paddle_length)
p_2 = Paddle((paddle_distance, 0), paddle_length)
pong = Pong(ball_angle)
score_1 = Score(-game.window_width()/4+5)
score_2 = Score(game.window_width()/4+5)

game.onkeypress(p_1.move_up, 'w')
game.onkeypress(p_1.move_down, 's')
game.onkeypress(p_2.move_up, 'Up')
game.onkeypress(p_2.move_down, 'Down')

game_on = 1
while game_on:
    if pong.out:
        time.sleep(0.5)
        pong.out = 0
    pong.move_forward()
    time.sleep(pong.speed)


game.mainloop()
