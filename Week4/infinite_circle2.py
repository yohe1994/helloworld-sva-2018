# -*- coding: utf-8 -*-
import turtle
#import random
#random.randint(0,9)
ws = turtle.Screen()
turtle.screensize(960, 720, "black")
a = turtle.Turtle()
#b = turtle.Turtle()
a.speed(0)
#b.speed(0)
for i in range(400): # this "for" loop will repeat these functions 500 times
    a.circle(i)
    a.left(i)
    if (i<100):
        a.pencolor('#E3F2F9')
    elif (i>100 and i<200):
        a.pencolor('#A1BEE6')
    elif (i>200 and i<300):
        a.pencolor('#E3F3D1')
    elif (i>300 and i<400):
        a.pencolor('#D97CA8')
ws.exitonclick()
