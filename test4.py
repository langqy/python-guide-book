#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sigslot.py

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(lambda x: lcd.display(slider.value()))

        self.setWindowTitle('Signal & slot')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())

#if __name__ == '__main__':


















