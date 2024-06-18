import turtle
import random as r
turtel = turtle.Turtle()
turtel.hideturtle()
turtel.up()
turtel_box = turtle.Screen()
turtel_box.tracer(1000, 0)  # update window every 1000 steps to speed up drawing
turtel_box.colormode(255)  # use RGB

# circle drawing parameters
scale = 54
angle = 180 + 1


def circle(length):
    turtel.pensize(length / 40)
    turtel.setheading(0)
    turtel.back(length/2)
    turtel.down()
    for i in range(180):
        if i in range(90): turtel.pencolor('black')
        else: turtel.pencolor('magenta')
        turtel.forward(length)
        turtel.left(angle)
    turtel.up()


def draw_4_circles(radius, distance, shift=0):
    for i in range(4):
        turtel.home()
        turtel.left(90 * i + shift)
        turtel.forward(distance)
        circle(radius)


def placeholder():
    # center one
    circle(scale * 50)
    # perpendicular
    draw_4_circles(scale / 2, scale / 2)
    draw_4_circles(scale, scale)
    draw_4_circles(scale * 1.5, scale * 2)
    draw_4_circles(scale * 2, scale * 2.5)
    draw_4_circles(scale * 3, scale * 3.5)
    draw_4_circles(scale * 4, scale * 4.5)
    draw_4_circles(scale * 5, scale * 6)
    draw_4_circles(scale * 6.5, scale * 8)
    # diagonal
    draw_4_circles(scale / 2, scale * 1.0625, 45)
    draw_4_circles(scale, scale * 1.25, 45)
    draw_4_circles(scale * 1.5, scale * 1.25 * 1.41, 45)
    draw_4_circles(scale * 2, scale * 2.25 * 1.41, 45)
    draw_4_circles(scale * 3, scale * 3.25 * 1.41, 45)
    draw_4_circles(scale * 4, scale * 5.25 * 1.41, 45)
    draw_4_circles(scale * 5, scale * 7 * 1.41, 45)
    turtel.home()


def polygons(n, side_length):
    # move the center point using circle math
    radius = n * side_length / 6.28
    turtel.sety(radius)
    turtel.down()
    for sides in range(3, n+1):
        for i in range(sides):
            turtel.forward(side_length)
            turtel.right(360/sides)
    turtel.up()
    turtel.home()


def pencolor_random():
    turtel.pencolor(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))


def sand_bug(steps, length):
    turtel.down()
    turtel.pensize(5)
    for i in range(steps):
        pencolor_random()
        turtel.right(90 * r.randint(0, 3))
        turtel.forward(length)
    turtel.up()


def slinky(n):
    turtel.down()
    pencolor_random()
    turtel.pensize(3)
    for i in range(n):
        turtel.circle(r.randint(50, 150), 4)
        turtel.left(360/n)
    turtel.up()


def dot_grid(grid_size, dot_distance, dot_size):
    grid_length = (grid_size-1) * dot_distance
    for row in range(grid_size):
        turtel.home()
        turtel.setx(-grid_length/2)
        turtel.sety(-grid_length/2 + row*dot_distance)
        for dot in range(grid_size):
            pencolor_random()
            turtel.dot(dot_size)
            turtel.forward(dot_distance)

def paint():
    turtel_box.tracer(1, 0)
    turtel.down()
    turtel.showturtle()
    turtel.shape('turtle')
    turtel.pensize(5)

    def mv_w():
        turtel.forward(10)

    def mv_s():
        turtel.back(10)

    def mv_a():
        turtel.left(10)
        pencolor_random()

    def mv_d():
        turtel.right(10)
        pencolor_random()

    def clear():
        turtel.home()
        turtel.clear()

    turtel_box.listen()
    turtel_box.onkeypress(mv_w, 'w')
    turtel_box.onkeypress(mv_s, 's')
    turtel_box.onkeypress(mv_a, 'a')
    turtel_box.onkeypress(mv_d, 'd')
    turtel_box.onkeypress(clear, 'c')



def race(turtle_count, window_length, window_height):
    turtles = []
    turtel_box.tracer(max(1, turtle_count**1.5/10), 0)
    turtel_box.setup(window_length + 50, window_height)

    for i in range(turtle_count):
        turtles.append(turtle.Turtle())
    for ttl_index in range(len(turtles)):
        ttl = turtles[ttl_index]
        ttl.up()
        ttl.shape('turtle')
        ttl.shapesize(2)
        ttl.fillcolor(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        ttl.goto(-window_length/2, -window_height/2 + (ttl_index+0.5) * window_height / turtle_count)

    while True:
        for ttl in turtles:
            ttl.forward(r.randint(0, 10))
            if ttl.xcor() >= window_length/2 - 10:
                print(f'Turtle number {turtles.index(ttl)+1} won!')
                return




# placeholder()
# polygons(10, 25)
# sand_bug(1000, 10)
# slinky(5000)
# dot_grid(9, 100, 40)
paint()
# race(10, 1800, 1000)

turtel_box.exitonclick()
