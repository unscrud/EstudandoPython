import turtle
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


square(bob, 200)


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    n = 100
    length = (2*3.14*r)/n
    polygon(t, length, n)


def arc(angle, t, r):
    n = 100
    length = (2*3.14*r)/n
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)


#polygon(bob, 50, 7)
#circle(bob, 50)
#arc(30, bob, 25)
turtle.mainloop()
