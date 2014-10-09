#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from PyQt4  import QtGui


class MyQWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(0, 0, 800, 600)
        #坐标0 0 大小800 600
        self.setWindowTitle('myapp')


myapp = QtGui.QApplication(sys.argv)
mywidget = MyQWidget()
mywidget.show()
sys.exit(myapp.exec_())
