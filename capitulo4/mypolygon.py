import turtle
bob = turtle.Turtle()


def square(t):
    for i in range(4):
        t.fd(150)
        t.lt(90)
    print(t)
    turtle.mainloop()


square(bob)
