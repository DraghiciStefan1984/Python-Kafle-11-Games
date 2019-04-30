# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:10:17 2019

@author: Stefan Draghici
"""

from base import Vector
import random
import turtle

def value():
    return (3+random.random()*2)*random.choice([-1,1])

ball=Vector(0,0)
aim=Vector(value(), value())

def draw():
    ball.move(aim)
    x=ball.x
    y=ball.y
    
    if x<-200 or x>200:
        aim.x=-aim.x
        
    if y<-200 or y>200:
        aim.y=-aim.y
        
    turtle.clear()
    turtle.goto(x, y)
    turtle.dot(10)
    turtle.ontimer(draw, 50)
    
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.up()
draw()
turtle.done()