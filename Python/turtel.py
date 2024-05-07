import turtle
turtel = turtle.Turtle()
# turtel.shape('turtle')
# turtel.color('aquamarine')
turtel.hideturtle()
turtel_box = turtle.Screen()
turtel_box.delay(0)

size = 54
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

# when generating things, the turtle gets slow very quickly, and can take a long time to finish
# but if you minimize the window, the turtle speeds up like 30x and finishes the whole thing in under 20 seconds

# center one
circle(size*50)
# perpendicular
draw_4_circles(size/2, size/2)
draw_4_circles(size, size)
draw_4_circles(size*1.5, size*2)
draw_4_circles(size*2, size*2.5)
draw_4_circles(size*3, size*3.5)
draw_4_circles(size*4, size*4.5)
draw_4_circles(size*5, size*6)
draw_4_circles(size*6.5, size*8)
# diagonal
draw_4_circles(size/2, size * 1.0625, 45)
draw_4_circles(size, size * 1.25, 45)
draw_4_circles(size * 1.5, size * 1.25 * 1.41, 45)
draw_4_circles(size*2, size * 2.25 * 1.41, 45)
draw_4_circles(size*3, size * 3.25 * 1.41, 45)
draw_4_circles(size*4, size * 5.25 * 1.41, 45)
draw_4_circles(size*5, size * 7 * 1.41, 45)

turtel.home()
turtel_box.exitonclick()
