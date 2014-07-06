#!/usr/bin/env python3
#-*-coding:utf-8-*-

import shelve

if __name__ == '__main__':
    db=shelve.open('test.db')
    for key in sorted(db):
        print(db[key])
    db.close()

