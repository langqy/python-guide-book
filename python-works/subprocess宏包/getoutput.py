#!/usr/bin/env python3
#-*-coding:utf-8-*-

import subprocess

name=subprocess.getoutput('whoami')
print(name)
#if __name__ == '__main__':
