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

    #动作和连接
        act_exit = QtGui.QAction('退出', self)
        act_exit.setStatusTip('退出程序')
        act_exit.triggered.connect(self.close)

        act_about = QtGui.QAction('关于本程序', self)
        act_about.triggered.connect(self.about)

        act_aboutqt = QtGui.QAction('关于Qt', self)
        act_aboutqt.triggered.connect(self.aboutqt)

    #菜单栏
        self.menubar = self.menuBar()
        menu_file=self.menubar.addMenu('文件')
        menu_file.addAction(act_exit)
        menu_edit=self.menubar.addMenu('编辑')
        menu_help=self.menubar.addMenu('帮助')
        menu_help.addAction(act_about)
        menu_help.addAction(act_aboutqt)

#函数
    def about(self):
        QtGui.QMessageBox.about(self,"关于本程序","本程序是一个用于教学的程序。\n\nFell free to use it\n(including it's source code).")
    def aboutqt(self):
        QtGui.QMessageBox.aboutQt(self)

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
mainwindow.statusBar().showMessage('程序已就绪...')
sys.exit(myapp.exec_())
