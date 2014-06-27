#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt4  import QtGui
from PyQt4  import QtCore


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
#编辑器
        self.editor =QtGui.QTextEdit(self)
        self.fileName=''
        self.setCentralWidget(self.editor)

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

        copy=QtGui.QAction('复制',self)
        copy.triggered.connect(self.editor.copy)

        cut=QtGui.QAction('剪切',self)
        cut.triggered.connect(self.editor.cut)

        paste=QtGui.QAction('粘贴',self)
        paste.triggered.connect(self.editor.paste)

        redo=QtGui.QAction('重做',self)
        redo.triggered.connect(self.editor.redo)

        undo=QtGui.QAction('撤销上次操作',self)
        undo.triggered.connect(self.editor.undo)



#菜单栏
        menubar = self.menuBar()
        menu001 = menubar.addMenu('文件')
        menu001.addAction(newfile)
        menu001.addAction(openfile)
        menu001.addAction(savefile)
        menu001.addAction(saveasfile)
        menu001.addAction(exit)
        menu002 = menubar.addMenu('编辑')
        menu002.addAction(copy)
        menu002.addAction(cut)
        menu002.addAction(paste)
        menu002.addAction(redo)
        menu002.addAction(undo)
        menu003 = menubar.addMenu('查看')
        menu004 = menubar.addMenu('工具')
        menu005 = menubar.addMenu('格式')
        menu006 = menubar.addMenu('帮助')
        menu006.addAction(about)
        menu006.addAction(aboutqt)



#函数
    def issaved(self):
        if  self.editor.document().isModified():
            return False
        else :
            return True

    def about(self):
        QtGui.QMessageBox.about(self,"关于本程序","本程序是一个教学用的编辑器。")
    def aboutqt(self):
        QtGui.QMessageBox.aboutQt(self)

    def newfile(self):
        if  self.issaved():
            self.editor.clear()

    def openfile(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,"打开文件...",".","")
        self.fileName=filename
        f = open(self.fileName,'r')
        self.editor.setPlainText(f.read())
        f.close()


    def savefile(self):
        if self.fileName == '' :
            self.saveasfile()
        else:
            f=open(self.fileName,'w')
            f.write(self.editor.toPlainText())
            f.close()
        self.editor.document().setModified(False)


    def saveasfile(self):
        filename=QtGui.QFileDialog.getSaveFileName(self,'另存为...','untitle.txt','')
        self.fileName=filename
        f = open(self.fileName,'w')
        f.write(self.editor.toPlainText())
        f.close()
        self.editor.document().setModified(False)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        #接受屏幕几何
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,
        (screen.height()-size.height())/2)

    def closeEvent(self, event):
        if not self.issaved():
            reply = QtGui.QMessageBox.question(self, '信息',"文档还没有保存，你确定要退出吗？",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
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
