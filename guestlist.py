# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:29:16 2018

@author: awanis.azizan
"""

names = []
name = ''

while name != 'done':
    name = input("Please enter 10 guest name. Enter 'done' if you have no other names to add")
    #names.append(names)
    if(name != "done"):
        names.append(name)
    
names.sort()

for num in names:
    print(num)
