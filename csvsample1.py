# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:15:59 2018

@author: awanis.azizan
"""

import csv
#
#myCSVFile = ('python-kl-oct18/data/demo.csv','r' )
#dataFromFile = (csv.reader, myCSVFile)
fileName = 'GuestList.txt'
accessMode = 'r'

with open(fileName, accessMode) as myCSVFile:
    dataFromFile = (csv.reader, myCSVFile)

#print(dataFromFile)

for row in dataFromFile:
    print(row)


myCSVFile.close()