# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:41:07 2018

@author: awanis.azizan
"""

import datetime

#birthday = input("What is your birthday? (dd/mm/yyyy)" )
#birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

#print("Your birth month is " +birthdate.strftime('%B'))

nextBirthday = datetime.datetime.strptime('11/26/2018',"%m/%d/%Y").date()
currentDate = datetime.date.today()

print(nextBirthday - currentDate)