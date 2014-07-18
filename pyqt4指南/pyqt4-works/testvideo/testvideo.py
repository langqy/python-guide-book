#!/usr/bin/env python3
#-*-coding:utf-8-*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import videoplay_ui
from PyQt4 import phonon
import wget

class Test(QtGui.QFrame,
        videoplay_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


    def download(self):
        source='http://hc.yinyuetai.com/uploads/videos/common/1687014667AA6B34EF66673A5BB529F5.flv?sc=6cccab50c32b29a5'
        wget.download(source, bar=wget.bar_thermometer)

    def openvideo(self):
        self.video=QtGui.QFileDialog.getOpenFileName(self,"打开视频...",".","")
        media = phonon.Phonon.MediaSource(self.video)
        self.videoPlayer.load(media)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question\
        (self, '信息',
            "你确定要退出吗？",
             QtGui.QMessageBox.Yes,
             QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.videoPlayer.stop()
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = Test()
    form.show()
    app.exec_()
    sys.exit()






#if __name__ == '__main__':
