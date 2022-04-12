from turtle import Turtle, mainloop
t = Turtle()
t.screen.bgcolor("black")
t.color("red")



def make_sq_spirale(step, decrease):
    while step > 0:
        t.forward(step)
        t.left(90)
        step -= decrease


make_sq_spirale(100, 4)

mainloop()