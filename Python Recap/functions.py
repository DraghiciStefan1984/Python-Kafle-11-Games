# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:00:22 2019

@author: Stefan Draghici
"""


def info(name="", age=0, likes=0):
    print("I am {0}, I am {1} years old, and have {2} likes on FB.".format(name, age, likes))
    
info()
info("Stefan", 35, 10000000)

#arguments unpacking
l=[1,2,3,4,5]
print(*l)
print('asdfghjkl')

def add(*args):
    s=0
    for number in args:
       s+=number
    return s

print(add(4,8,6,3,1,5,3,2))

#keyword argument unpacking
def about(**kwargs):
    for key, value in kwargs.items():
        print("{} - {}".format(key, value))

about(python="easy", cpp="hard")