import turtle
import random as r
turtel = turtle.Turtle()
turtel.hideturtle()
turtel.up()
turtel_box = turtle.Screen()
turtel_box.tracer(1000, 0) # update window every 1000 steps to speed up drawing
turtel_box.colormode(255) # use RGB

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
        turtel.setx(turtel.xcor() - grid_length/2)
        turtel.sety(turtel.ycor() - grid_length/2 + row*dot_distance)
        for dot in range(grid_size):
            pencolor_random()
            turtel.dot(dot_size)
            turtel.forward(dot_distance)


# placeholder()
# polygons(10, 25)
# sand_bug(1000, 10)
# slinky(5000)
dot_grid(9, 100, 40)

turtel_box.exitonclick()
