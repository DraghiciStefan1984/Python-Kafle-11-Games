# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:14:18 2019

@author: Stefan Draghici
"""

from base import Vector
import random
import turtle

ant=Vector(0,0)
aim=Vector(2,0)
running=True

def wrap(value):
    return value

def draw():
    ant.move(aim)
    ant.x=wrap(ant.x)
    ant.y=wrap(ant.y)
    aim.move(random.random()-0.5)
    aim.rotate(random.random()*10-5)
    turtle.clear()
    turtle.goto(ant.x, ant.y)
    turtle.dot(4)
    
    if running:
        turtle.ontimer(draw, 100)
    
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.up()

draw()
turtle.done()