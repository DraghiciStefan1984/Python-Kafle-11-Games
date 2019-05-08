# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:26:34 2019

@author: Stefan Draghici
"""

import turtle
import random
from base import line

def draw():
    turtle.color('black')
    turtle.width(5)
    
    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random.random()>0.5:
                line(x, y, x+40, y+40)
            else:
                line(x, y+40, x+40, y)
                
    turtle.update()
    
def tap(x, y):
    if abs(x)>198 or abs(y)>198:
        turtle.up()
    else:
        turtle.down()
    turtle.width(2)
    turtle.color('red')
    turtle.goto(x, y)
    turtle.dot(4)
    
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
draw()
turtle.onscreenclick(tap)
turtle.done()