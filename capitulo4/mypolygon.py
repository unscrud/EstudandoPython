import turtle


def square(t):
    bob = turtle.Turtle()
    for i in range(4):
        bob.fd(t)
        bob.lt(90)
    print(bob)
    turtle.mainloop()


square(300)
