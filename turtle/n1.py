from turtle import Turtle, mainloop
t = Turtle()
t.screen.bgcolor("black")
t.color("red")


def square(length):
    for steps in range(4):
        t.fd(length)
        t.left(90)

def make_10_squeres():
    pos = -10
    for i in range(10):
        t.penup()
        t.goto(pos, pos)
        t.pendown()
        length = abs(pos)
        square(length*2)
        pos -= 10


make_10_squeres()


mainloop()