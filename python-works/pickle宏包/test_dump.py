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
    test001=Test()
    print(test001)
    testfile=open('data.pkl','wb')
    pickle.dump(test001,testfile)
    testfile.close()



















