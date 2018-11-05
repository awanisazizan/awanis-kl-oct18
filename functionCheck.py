# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:01:36 2018

@author: awanis.azizan
"""

def say(hello):
    print(hello)
    return
1
#say('hey')
#say('hi')
#say('hello')
#say('arigatou')
#say('annyeonghaseyo')

a = int(input('Number 1:'))
b = int(input('Number 2:'))

def calculate(a, b):
    sum = a+b;
    return sum
    
print("Sum of "+str(a)+ " and " +str(b)+ " equals " +str(calculate(a,b)))
    
    