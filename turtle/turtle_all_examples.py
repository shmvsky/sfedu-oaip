### Пример 1
from turtle import *
t=Turtle()
t.screen.bgcolor("black")
t.color("red")
t.hideturtle()

def change_pos(x,y):
    t.up()
    t.right(x)
    t.forward(y)
    t.right(x)
    t.pendown()

def square(length):
    for steps in range(4):
        t.fd(length)
        t.left(90)

def slanted_rectangle(length,width,angle):
    t.setheading(angle)
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)

def triangle(length,angle=120):
    for steps in range(3):
        t.fd(length)
        t.left(angle)

def star():
    for i in range(5):
        t.forward(150)
        t.right(144)

slanted_rectangle(length=200,angle=45,width=100)

change_pos(90, 300)
t.color('blue')

square(100)


change_pos(90, 450)
t.color('green')
t.begin_fill()
triangle(120)
t.end_fill()

change_pos(-180, 100)
t.color('white')

t.circle(50,180)

change_pos(90, -500)

t.color('purple')

t.write("Turtle is cool! ",move=True,align="center",font=("Freestyle Script",50,"normal"))

change_pos(500, -400)
star()

mainloop()

### Пример 2
import random
from turtle import *
t=Turtle()
t.screen.bgcolor("black")
 
def random_drawing(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(["blue","red","green", "purple", "white"]))
        random.choice([right,left])
        t.fd(distance)
 
 
 
random_drawing(100,50)

exitonclick()

### Пример 3

from turtle import *


def tree(sz, level, angle):   
  
    if level > 0:
        colormode(255) 
          
        pencolor(0, 255//level, 0) # установим какой-то оттенок зелёного
          
        fd(sz) # движение вперед на sz пикселей
        rt(angle) # 
        tree(0.8 * sz, level-1, angle) # отрисовка правого поддерева
        
        pencolor(0, 255//level, 0)
        lt( 2 * angle ) # поворот налево на angle градусов
        tree(0.8 * sz, level-1, angle) # отрисовка левого поддерева
          
        pencolor(0, 255//level, 0)
          
        rt(angle) # поворот направо на angle градусов
        fd(-sz) # движение вперед на -sz пикселей (т.е. назад)

  
speed('fastest') # установка скорости движения черепашки
rt(-90) # поворот на 90 градусов влево (направление движения вверх)
angle = 50 # угол отклонения при отрисовке
size = 80 # начальная длина одной "ветки"
rec_level = 20 # глубина рекурсии 

tree(size, rec_level, angle)
rt(180)
tree(size, rec_level, angle)




