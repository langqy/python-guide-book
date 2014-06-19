#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from PyQt4  import QtGui

class Mybutton(QtGui.QPushButton):
    def __init__(self,parent=None):
        QtGui.QPushButton.__init__(self,"打开文件",parent)
        self.resize(150, 90)
        self.center()
        self.setWindowTitle('打开文件')
        self.clicked.connect(self.openfile)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,\
         (screen.height()-size.height())/2)


    def openfile(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,"打开文件...",".","")
        print('文件'+str(filename)+'已选择')

myapp = QtGui.QApplication(sys.argv)
mywidget = Mybutton()
mywidget.show()

myapp.exec_()
sys.exit()

