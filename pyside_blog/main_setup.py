# -*- coding: cp932 -*-
from __future__ import with_statement

import numpy as np
import sys
from PySide import QtCore,QtGui
import os
from pyqt_Opencv import Ui_Qt_CV_MainWindow
from opencv_test import opencv_test

class DesignerMainWindow(QtGui.QMainWindow,Ui_Qt_CV_MainWindow):
 def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
       	self.ui = Ui_Qt_CV_MainWindow()
	self.setupUi(self)
	QtCore.QObject.connect(self.file_button, QtCore.
SIGNAL("clicked()"), self.open_file)
	QtCore.QObject.connect(self.exec_button,QtCore.SIGNAL("clicked()"),self.canny)
	"""
    	QtCore.QObject.connect(self.open_button, QtCore.
SIGNAL("clicked()"), self.select_file)

        QtCore.QObject.connect(self.actionQuit, QtCore.
SIGNAL("triggered()"), QtGui.qApp, QtCore.SLOT("quit()"))
	QtCore.QObject.connect(self.quit_button, QtCore.
SIGNAL("clicked()"), self.close_event)

	QtCore.QObject.connect(self.folder_button, QtCore.
SIGNAL("clicked()"), self.select_folder)

	QtCore.QObject.connect(self.th1_slider, QtCore.
SIGNAL("valueChanged(int)"), self.change_slider_th1)

	QtCore.QObject.connect(self.th1_edit, QtCore.
SIGNAL("textEdited(const QString&)"), self.change_txt)
 """
 """
	self.imagewidget.installEventFilter(self)
 """
 """
 def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonPress and source is self.pic_view):
            pos = event.pos()
	    msgbox = QtGui.QMessageBox(self)
	    #msgbox.setText(QtCore.QString(str(pos.x())))
	    msgbox.setText('mouse move: (%d, %d)' % (pos.x(), pos.y()))
	    msgbox.setModal(True)
	    ret = msgbox.exec_()
	    #print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return QtGui.QWidget.eventFilter(self, source, event)
 """

 def open_file(self):
	file = QtGui.QFileDialog.getOpenFileName()
        if file:
	    self.file_edit.setText(file[0])
	    print file
	    scene = QtGui.QGraphicsScene()
	    pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(file[0]))
	    __width = pic_Item.boundingRect().width()
	    __height = pic_Item.boundingRect().height()
	    __x = self.pic_View.x()
	    __y = self.pic_View.y()
	    print __y
	    self.pic_View.setGeometry(QtCore.QRect(__x, __y, __width, __height))

	    __main_x = int(__x + __width + 20)
	    __main_y = int(__y + __height + 50)
	    self.resize(__main_x,__main_y)
	    scene.addItem(pic_Item)
	    self.pic_View.setScene(scene)
	    return file
 def canny(self,file):
	    file = str(self.file_edit.text())
	    print file[0]
	    pic,pic2 = opencv_test.open_pic(file[0])
	    self.cv_img = opencv_test.canny(pic)


            height, width, bytesPerComponent = cv_img.shape
            bytesPerLine = bytesPerComponent * width;

            cv2.imshow("Show Image with Opencv", self.cv_img)

            # Convert to RGB for QImage.
            cv2.cvtColor(self.cv_img, cv.CV_BGR2RGB, self.cv_img)
            self.image = QImage(self.cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
	    pic_Item = QtGui.QGraphicsPixmapItem(self.image)
	    scene.addItem(pic_Item)
	    self.pic_View.setScene(scene)

 def change_txt(self,value):
	self.th1_slider.setValue(float(self.th1_edit.text()))

 def change_slider_th1(self,value):
	self.th1_edit.setText(str(value))
	str_1 = float(self.th1_edit.text())

 def select_folder(self):
        folder = QtGui.QFileDialog.getExistingDirectory(self,'Open Dorectory',os.path.expanduser('~'))
        if folder:
            self.folder_edit.setText(folder)

 def select_file(self):
        file = QtGui.QFileDialog.getOpenFileName()
        if file:
            self.ini_line.setText(file)
 
 """
 def closeEvent(self,event):
        confirmquit = QtGui.QMessageBox.question(self,'Message',
        'Are you sure to quit?',QtGui.QMessageBox.Yes |
        QtGui.QMessageBox.No,QtGui.QMessageBox.No)

 def close_event(self):
	reply = QtGui.QMessageBox.question(self,'Message',
        'Are you sure to quit?',QtGui.QMessageBox.Yes |
        QtGui.QMessageBox.No,QtGui.QMessageBox.No)
	if reply == QtGui.QMessageBox.Yes:
		QtCore.QCoreApplication.instance().quit()
	else:
		pass
 """
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	dmw = DesignerMainWindow()
	dmw.show()
	sys.exit(app.exec_())
