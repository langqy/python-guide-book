#!/usr/bin/env python3
#-*-coding:utf-8-*-
"""mymodule
我在mymodule文件夹的__init__.py文件里面"""

print('mymodule already import')

from mymodule import mymod
__all__ = ['mymod']

#if __name__ == '__main__':
