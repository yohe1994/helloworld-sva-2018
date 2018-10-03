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
    a.circle(2*i)
    a.left(i)
    if (i<100):
        a.pencolor('#DAEFF5')
    elif (i>100 and i<200):
        a.pencolor('#91E0F4')
    elif (i>200 and i<300):
        a.pencolor('#0C90AD')
    elif (i>300 and i<400):
        a.pencolor('#B1AFCD')
ws.exitonclick()
