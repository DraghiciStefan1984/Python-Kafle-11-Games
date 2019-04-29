# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:17:37 2019

@author: Stefan Draghici
"""

class Character():
    def __init__(self, name=None, age=0):
        self.name=name
        self.age=age
        
    def run(self):
        print("{} is running.".format(self.name))
        
char1=Character("Ben", 1250)
char1.run()

char2=Character("Mary")
char2.run()

class Person():
    def __init__(self, name, score):
        self.name=name
        self.score=score
        print("Person constructor called")
        
    def info(self):
        print("My name is {0}, and my score is {1}.".format(self.name, self.score))
        

class Mary(Person):
    def __init__(self, name, score, speed):
        super().__init__(name, score)
        self.speed=speed
        
    def info(self):
        super().info()
        print("My speed is {}.".format(self.speed))
        
class John():
    def __init__(self):
        pass
    
mary=Mary("Mary", 152, 8)
mary.info()