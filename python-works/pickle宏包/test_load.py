#!/usr/bin/env python3
#-*-coding:utf-8-*-

import pickle

class Test:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=1
        self.d=1

    def __str__(self):
        return str(self.__dict__)

if __name__ == '__main__':
    testfile=open('data.pkl','rb')
    test001=pickle.load(testfile)
    print(test001)
    testfile.close()



















