#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from PyQt4  import QtGui

class Mywidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.center()
        self.setWindowTitle('myapp')

        button1=QtGui.QPushButton("文件")
        button2=QtGui.QPushButton("颜色")
        button3=QtGui.QPushButton("字体")
        button4=QtGui.QPushButton("关于")
        button5=QtGui.QPushButton("关于Qt")
        mainlayout=QtGui.QHBoxLayout()
        mainlayout.addWidget(button1)
        mainlayout.addWidget(button2)
        mainlayout.addWidget(button3)
        mainlayout.addWidget(button4)
        mainlayout.addWidget(button5)
        self.setLayout(mainlayout)
        button1.clicked.connect(self.openfile)
        button2.clicked.connect(self.choosecolor)
        button3.clicked.connect(self.choosefont)
        button4.clicked.connect(self.about)
        button5.clicked.connect(self.aboutqt)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,\
         (screen.height()-size.height())/2)

    def openfile(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,"打开文件...",".","")
        print('文件'+str(filename)+'已选择')

    def choosecolor(self):
        colorname=QtGui.QColorDialog.getColor()
        print('颜色'+str(colorname)+'已选择')

    def choosefont(self):
        fontname=QtGui.QFontDialog.getFont()
        print('字体'+str(fontname)+'已选择')

    def about(self):
        QtGui.QMessageBox.about(self,"关于本程序","本程序用于测试按钮和对话框。")
    def aboutqt(self):
        QtGui.QMessageBox.aboutQt(self)

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
mywidget = Mywidget()
mywidget.show()
myapp.exec_()
sys.exit()

