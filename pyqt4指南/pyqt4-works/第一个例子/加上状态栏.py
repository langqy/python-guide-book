#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from PyQt4  import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.resize(800,600)
        self.center()
        self.setWindowTitle('myapp')
        self.setWindowIcon(QtGui.QIcon\
        ('icons/myapp.ico'))
        self.setToolTip('看什么看^_^')
        QtGui.QToolTip.setFont(QtGui.QFont\
        ('微软雅黑', 12))

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question\
        (self, '信息',
            "你确定要退出吗？",
             QtGui.QMessageBox.Yes,
             QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,\
         (screen.height()-size.height())/2)

myapp = QtGui.QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(myapp.exec_())

