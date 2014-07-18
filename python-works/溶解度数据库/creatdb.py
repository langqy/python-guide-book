#!/usr/bin/env python3
#-*-coding:utf-8-*-

import xlrd
import sqlite3

workbook =xlrd.open_workbook('溶解度.xls')
sheet1=workbook.sheet_by_index(0)

data=[[sheet1.cell_value(r,c) for c in range(sheet1.ncols)] for r in range(sheet1.nrows)]

#create database
dbname='溶解度.db'
maindb=sqlite3.connect(dbname)

#create table inwater
try:
    maindb.execute('''create table inwater(formular text primary key, name text, solubility real)''')
except:
    print('dbname already exist')

#insert 一行
def insert(a,b,c):
    maindb.execute('insert into inwater values(?,?,?) ' , (a,b,c))



if __name__ == '__main__':
    for row in range(1,len(data)):
        insert(data[row][0],data[row][1],data[row][2])
    maindb.commit()
    maindb.close()
