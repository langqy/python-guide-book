#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt4  # just to tell pyqode we want to use PyQt4.
from PyQt4  import QtGui
from PyQt4  import QtCore
import pyqode.core

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
#基本UI
        self.resize(800,600)
        self.center()
        self.setWindowTitle('myapp')
        self.setWindowIcon(QtGui.QIcon\
        ('icons/myapp.ico'))
        self.setToolTip('<b>看什么看、、</b>')
        QtGui.QToolTip.setFont(QtGui.QFont\
        ('微软雅黑', 12))
        self.statusBar().showMessage('这是状态栏')

#动作和连接
        exit = QtGui.QAction('退出', self)
        exit.setStatusTip('退出程序')
        exit.triggered.connect(self.close)

        about = QtGui.QAction('关于本程序', self)
        about.triggered.connect(self.about)

        aboutqt = QtGui.QAction('关于Qt', self)
        aboutqt.triggered.connect(self.aboutqt)

        newfile=QtGui.QAction('新建',self)
        newfile.triggered.connect(self.newfile)

        openfile=QtGui.QAction('打开',self)
        openfile.triggered.connect(self.openfile)

        savefile=QtGui.QAction('保存',self)
        savefile.triggered.connect(self.savefile)

        saveasfile=QtGui.QAction('另存为',self)
        saveasfile.triggered.connect(self.saveasfile)

#菜单栏
        menubar = self.menuBar()
        menu001 = menubar.addMenu('文件')
        menu001.addAction(newfile)
        menu001.addAction(openfile)
        menu001.addAction(savefile)
        menu001.addAction(saveasfile)
        menu001.addAction(exit)
        menu002 = menubar.addMenu('编辑')
        menu003 = menubar.addMenu('查看')
        menu004 = menubar.addMenu('工具')
        menu005 = menubar.addMenu('设置')
        menu006 = menubar.addMenu('帮助')
        menu006.addAction(about)
        menu006.addAction(aboutqt)
#工具栏
        toolbar001=self.addToolBar("新建")
        toolbar001.addAction(newfile)
        toolbar001.addAction(openfile)
        toolbar001.addAction(savefile)
#编辑器
        self.editor = pyqode.core.QGenericCodeEdit(self)
        self.setCentralWidget(self.editor)
        self.setCurrentFileName()
        print(self.editor.fileName)


#函数
    def setCurrentFileName(self, fileName=''):
        self.fileName = fileName
        self.editor.document().setModified(False)
        if not fileName:
            shownName = 'untitled.txt'
        else:
            shownName = QtCore.QFileInfo(fileName).fileName()
        self.setWindowTitle(self.tr("%s[*] - %s" % (shownName, "Rich Text")))
        self.setWindowModified(False)

    def about(self):
        QtGui.QMessageBox.about(self,"关于本程序","本程序是一个教学用的编辑器。")
    def aboutqt(self):
        QtGui.QMessageBox.aboutQt(self)

    def newfile(self):
        self.editor.clear()

    def openfile(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,"打开文件...",".","")
        self.editor.openFile(filename)
        self.fileName=filename

    def savefile(self):
        s = open(self.fileName,'w')
        s.write(self.editor.toPlainText())
        s.close()

    def saveasfile(self):
        filename=QtGui.QFileDialog.getSaveFileName(self,'另存为...','ultitle.name','')
        self.fileName=filename
        s = open(self.fileName,'w')
        s.write(self.editor.toPlainText())
        s.close()



    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        #接受屏幕几何
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,
        (screen.height()-size.height())/2)
#左侧点绝对位置坐标move
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

def main():
    myapp = QtGui.QApplication(sys.argv)
    mymainwindow = MainWindow()
    mymainwindow.show()
    sys.exit(myapp.exec_())


if __name__ == '__main__':
    main()
