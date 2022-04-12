from turtle import Turtle, mainloop
from random import randint, choice
t = Turtle()
t.screen.bgcolor("black")
t.color("red")



def square(length=50):
    for steps in range(4):
        t.fd(length)
        t.left(90)


def slanted_rectangle(length=50,width=50,angle=50):
    t.setheading(angle)
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)


def triangle(length=50,angle=120):
    for steps in range(3):
        t.fd(length)
        t.left(angle)


def star():
    for i in range(5):
        t.forward(150)
        t.right(144)



figures = [square, slanted_rectangle, triangle, star]


for i in range(10):
    x = randint(-200, 200)
    y = randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    figure = choice(figures)
    figure()



mainloop()