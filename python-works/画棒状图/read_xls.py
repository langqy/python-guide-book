#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *
import xlrd

workbook =xlrd.open_workbook('test.xls')
sheet1=workbook.sheet_by_index(0)

print(sheet1.nrows,sheet1.ncols)

data=[[sheet1.cell_value(r,c) for c in range(sheet1.ncols)] for r in range(sheet1.nrows)]

print(data)
print(len(data))





#if __name__ == '__main__': #if run as script


















