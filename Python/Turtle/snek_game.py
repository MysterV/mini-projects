import time
import turtle
import random as r
import turtle_snake_creature

'''
TODO
- [x] snake movement
- [x] snake body
    - [x] count snake size
- [x] snake food
- [ ] collisions
    - [ ] food
    - [ ] wall
    - [ ] self
'''

game = turtle.Screen()
game.setup(800, 800)
game.tracer(1, 0)
game.listen()

# spawn snake
segments = []

def summon_segment(init=False):
    global segments
    segments.append(turtle.Turtle())
    segments[-1].shape('square')
    segments[-1].up()
    if len(segments) > 1:
        segments[-1].goto(segments[-2].xcor(), segments[-2].ycor())
        if init:
            segments[i].back(40)

for i in range(3):
    summon_segment(init=True)


# configure snake head
head = segments[0]
head.shapesize(2)
head.color('#00eeff')


# add a scoreboard
score = turtle.Turtle()
score.up()
score.hideturtle()
score.sety(game.window_height()/2-30)

def update_score(text):
    global score
    score.clear()
    score.write(text, False, align='center', font=('Arial', 20, 'normal'))

update_score(len(segments))


# spawn food
food = turtle.Turtle()
food.up()
food.shape('circle')
food.color('red')

def move_food():
    food.setpos(r.randint(-9, 9)*40, r.randint(-9, 9)*40)

move_food()


# to bring it all together
def move_snake():
    global game_running
    for i in range(len(segments) - 1, 0, -1):
        segments[i].setpos(segments[i - 1].xcor(), segments[i - 1].ycor())

    if segments[0].pos() == food.pos():
        summon_segment()
        move_food()
        update_score(len(segments))
    head.forward(40)
    print(head.pos(), food.pos())


    #for i in range(1, len(segments)):
    #    if head.xcor() == segments[i].xcor() and head.ycor() == segments[i].ycor():
    #        game_running = False


# snake movement functions to make the "onkey" method work (it doesn't accept arguments)
def head_left():
    if head.heading() != 0:
        head.setheading(180)


def head_right():
    if head.heading() != 180:
        head.setheading(0)

def head_down():
    if head.heading() != 90:
        head.setheading(-90)

def head_up():
    if head.heading() != 270:
        head.setheading(90)


game.onkey(head_up, 'w')
game.onkey(head_down, 's')
game.onkey(head_left, 'a')
game.onkey(head_right, 'd')


while game_running := True:
    time.sleep(0.5)
    move_snake()
else:
    update_score(f'You died, final score: {len(segments)}')

game.mainloop()

