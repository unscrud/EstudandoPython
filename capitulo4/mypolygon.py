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
    for i in range(n):
        t.fd(length)
        t.lt(angle)


#polygon(bob, n=7, length=70)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


circle(bob, 50)


def arc(angle, t, r):
    n = 100
    length = (2*math.pi*r)/n
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)


#arc(30, bob, 25)
turtle.mainloop()
