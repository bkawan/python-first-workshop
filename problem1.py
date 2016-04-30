# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:32:18 2016

@author: bikeshkawan

Read CSV file form disk and perform some 
"""

#print(__file__)

csv_file ='/Users/BIKESHKAWAN/pythonworkshop/data/GDP.csv'

#csvFile = open(csv_file, 'r')
import csv
output_file = open('myfile.csv', 'w')
writer = csv.writer(output_file)
with open(csv_file, 'r',
          encoding='ISO-8859-1') as csvfile:
    print(csvfile)
    readers = csv.reader(csvfile)
   #print(readers)
   # print('asd')
   # print(reader)
    for row in readers:
        #print('asdfdddd')
        print(row)
        if row[0] in ['NPL','IND', 'BGD'] and int(row[1]) < 100:
            writer.writerow(row)
output_file.close()
        
        