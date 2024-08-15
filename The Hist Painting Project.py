from turtle import Turtle, Screen
from random import randint,choice


my_turtle = Turtle()
screen = Screen()
screen.colormode(255)

def rgb_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    return (r,g,b)


y = -500.00

for making_hirst_painting in range(0,10):  
    x = -400.00 
    my_turtle.penup()
    my_turtle.goto(x=x,y=y)
    for making_hirst_painting_2 in range(0,10):
        my_turtle.dot(50,rgb_color())
        x += 100
        my_turtle.penup()
        my_turtle.goto(x=x,y= y)
    y += 100

screen.exitonclick()