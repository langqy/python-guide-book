#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os
import sys

filename = sys.argv[1]

filesize = os.stat(filename).st_size

for unit in ['字节','KB','MB','GB','TB']:
    if filesize > 1024:
        filesize = filesize/1024
    else:
        break

print(filename + '大小是' +str(int(filesize)) + unit)



#if __name__ == '__main__':
