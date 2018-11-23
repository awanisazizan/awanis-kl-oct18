# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:35:41 2018

@author: awanis.azizan
"""

fileName = "GuestList.txt"
accessMode = "w"

myFile = open(fileName, accessMode)
myFile.write("Hi there!! \n")
myFile.write("How are you??")