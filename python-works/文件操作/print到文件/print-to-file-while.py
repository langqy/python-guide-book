#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys

string =''
while True :
    x=input('请输入文字：')
    string= string+x
    if x=='quit':
        break

pyout=open(sys.argv[1] ,"w")
print(string , file=pyout)

pyout.close()


#if __name__ == '__main__': #if run as script



















