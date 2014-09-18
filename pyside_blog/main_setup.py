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
	QtCore.QObject.connect(self.exec_button,QtCore.SIGNAL("clicked()"),self.make_canny)
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
        pic_view = self.pic_View
        pic_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        pic_view.customContextMenuRequested.connect(self.contextMenue) 
	self.pic_View.installEventFilter(self)
	  
	self.pic_View.setHorizontalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOff )
        self.pic_View.setVerticalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOff )
	self.pic_View.setTransformationAnchor( QtGui.QGraphicsView.NoAnchor )
	self.scaleRatio = 1.0
	self.scaleRatio_add = 0.02
	self.pic_item = None

 def contextMenue(self,event):
        menu = QtGui.QMenu()
        menu.addAction('canny',self.make_canny)
	menu.addAction('test1',self.make_canny)
	menu.exec_(QtGui.QCursor.pos())

 def eventFilter(self, source, event):
	if (type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_A) :
		self.scaleRatio += self.scaleRatio_add
		self.change_size()
	elif (event.type() == (QtCore.QEvent.MouseButtonDblClick) and source is self.pic_View):
		self.scaleRatio = 1
		self.change_size(event.pos())
		print "1"

	elif (event.type() == QtCore.QEvent.MouseButtonPress and source is self.pic_View):
		if event.button() == QtCore.Qt.RightButton:
			pass
		
		#elif event.button() == QtCore.Qt.LeftButton:
		#	curPos = event.posF()
		#	print curPos
		#	print "from"
		#	print self.pic_View.mapFromScene( curPos.x(), curPos.y())
		#	print "to"
		#	print self.pic_View.mapToScene( curPos.x(), curPos.y())
		#	print "end"
		

		else:
			pos = event.pos()
			print pos
			msgbox = QtGui.QMessageBox(self)
			msgbox.setText('mouse position: (%d, %d)' % (pos.x(), pos.y()))
			ret = msgbox.exec_()
	elif (event.type() == QtCore.QEvent.Wheel and source is self.pic_View):
		
		if event.delta() > 119 :
			self.scaleRatio += self.scaleRatio_add
			self.change_size(event.pos())
		elif event.delta() < -119 :
			if self.scaleRatio == 1  :
				pass
			else:
				self.scaleRatio -= self.scaleRatio_add
				self.change_size(event.pos())
		else:
			pass

	return QtGui.QWidget.eventFilter(self, source, event)

 def change_size(self,curPos=None):
	if curPos == None :
		scene_size = self.scene.itemsBoundingRect()
		self.pic_item.setTransform(QtGui.QTransform().translate(\
				scene_size.width()/2,scene_size.height()/2)\
				.scale(self.scaleRatio, self.scaleRatio)\
				.translate(-scene_size.width()/2,-scene_size.height()/2))
	else:
	 	localRect = self.pic_View.mapFromScene( curPos.x(), curPos.y() )
	 	self.pic_item.setTransform(QtGui.QTransform().translate( float(localRect.x()), float(localRect.y()) ).scale(float(self.scaleRatio), float(self.scaleRatio)).translate( float(-localRect.x()),float( -localRect.y() )))
	self.scene.setSceneRect(self.scene.itemsBoundingRect())
	print self.scaleRatio
 def open_file(self):
	self.file = QtGui.QFileDialog.getOpenFileName()
        if file:
	     
	    self.file_edit.setText(self.file[0])
	    self.scene = QtGui.QGraphicsScene()
	    self.scene.clear() 
	    pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.file[0]))
	    self.pic_item =  pic_Item

	    __width = pic_Item.boundingRect().width()
	    __height = pic_Item.boundingRect().height()
	    __x = self.pic_View.x()
	    __y = self.pic_View.y()
	    self.pic_View.setGeometry(QtCore.QRect(__x, __y, __width, __height))

	    __main_x = int(__x + __width + 50)
	    __main_y = int(__y + __height + 50)
	    self.resize(__main_x,__main_y)
	    self.scene.addItem(pic_Item)
	    self.pic_View.setScene(self.scene)
	    return file
 def make_canny(self):
	    cv_test = opencv_test()
	    pic,pic2 = cv_test.open_pic(self.file[0])
	    self.cv_img = cv_test.canny(pic2)
            height, width, dim = self.cv_img.shape
            bytesPerLine = dim * width
            self.image = QtGui.QImage(self.cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
	    pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(self.image))
	    self.pic_item = pic_Item
	    self.scene.addItem(pic_Item)

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
