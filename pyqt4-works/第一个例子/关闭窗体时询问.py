#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from PyQt4  import QtGui

class MyQWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.resize(800,600)
        self.setWindowTitle('myapp')
        self.setWindowIcon(QtGui.QIcon\
        ('icons/myapp.ico'))
        self.setToolTip('看什么看^_^')
        QtGui.QToolTip.setFont(QtGui.QFont\
        ('微软雅黑', 12))

    def closeEvent(self, event):
        #重新定义colseEvent
        reply = QtGui.QMessageBox.question\
        (self, '信息',
            "你确定要退出吗？",
             QtGui.QMessageBox.Yes,
             QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

myapp = QtGui.QApplication(sys.argv)
mywidget = MyQWidget()
mywidget.show()
sys.exit(myapp.exec_())

