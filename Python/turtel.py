import turtle
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


placeholder()

turtel_box.exitonclick()
