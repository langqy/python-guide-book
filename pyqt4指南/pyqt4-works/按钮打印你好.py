#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from PyQt4  import QtGui

class Mybutton(QtGui.QPushButton):
    def __init__(self,parent=None):
        super().__init__("nihao",parent)
        self.resize(150, 90)
        self.center()
        self.setWindowTitle('你好')
        self.clicked.connect(self.hello)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,\
         (screen.height()-size.height())/2)



    def hello(self):
        print('你好')

myapp = QtGui.QApplication(sys.argv)
mywidget = Mybutton()
mywidget.show()

myapp.exec_()
sys.exit()

