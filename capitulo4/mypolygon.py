import math
import turtle
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# square(bob, 200)


def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)


#polygon(bob, n=7, length=70)


def circle(t, r):
    arc(t, r, 360)


#circle(bob, 50)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


arc(bob, 25, 300)
turtle.mainloop()
