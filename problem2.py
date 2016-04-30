# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:36:06 2016

@author: bikeshkawan
"""
#from openpyxl import load_workbook
import xlrd

file_path = '/Users/BIKESHKAWAN/pythonworkshop/data/climate_change_download_0.xls'

#wb = load_workbook(file_path)

wb = xlrd.open_workbook(file_path)

#print(wb.sheets)
print(wb.sheets())

sheet = wb.sheets()[0]

print(sheet)
print(sheet.cell(9,3))
print(sheet.cell(4,1))
cell = sheet.cell(0,5)

print(dir(cell))
print(cell)

print(sheet.nrows)
print(sheet.ncols)

#write

import xlwt

book = xlwt.Workbook()

sheet1 = book.add_sheet("hello")

sheet1.write(0,0, "Fisrt Cell")
sheet1.write(2,6, "Another cell")
book.save('test.xls')


