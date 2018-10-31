# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:12:09 2018

@author: awanis.azizan
"""

import datetime


currdate = datetime.date.today()
print(currdate) 
print(currdate.year) 
print(currdate.month) 
print(currdate.day) 
print(currdate.year) 

print(currdate.strftime('%d %b, %Y'))
print(currdate.strftime('%d-%m-%Y')) 
print(currdate.strftime('%a %A')) 