# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subwindow_CutOrTrim.ui'
#
# Created: Sun Mar 01 20:28:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_cut_window(object):
    def setupUi(self, cut_window):
        cut_window.setObjectName("cut_window")
        cut_window.resize(471, 177)
        self.pushButton = QtGui.QPushButton(cut_window)
        self.pushButton.setGeometry(QtCore.QRect(350, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(cut_window)
        QtCore.QMetaObject.connectSlotsByName(cut_window)

    def retranslateUi(self, cut_window):
        cut_window.setWindowTitle(QtGui.QApplication.translate("cut_window", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("cut_window", "Exit", None, QtGui.QApplication.UnicodeUTF8))

