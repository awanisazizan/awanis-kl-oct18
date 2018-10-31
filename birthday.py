# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:41:07 2018

@author: awanis.azizan
"""

import datetime

birthday = input("What is your birthday?")
birthdate = datetime.datetime.strptime(birthday,"%d/%m/%y").date()

print("Your birth month is " +birthdate.strftime('%B'))