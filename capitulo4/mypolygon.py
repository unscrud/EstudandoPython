import turtle
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(t)
    turtle.mainloop()


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    print(t)
    turtle.mainloop()


#square(bob, 200)
polygon(bob, 50, 7)
