# -*- coding: cp932 -*-
from __future__ import with_statement
import PySide
import pyqtgraph as pg
import cv2
import numpy as np
import sys
import math
from PySide import QtCore,QtGui
import os
from pygraph_Opencv import Ui_Qt_CV_MainWindow
from opencv_test import opencv_test
from matrix_co import coordinateForCv

class DesignerMainWindow(QtGui.QMainWindow,Ui_Qt_CV_MainWindow):
 def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
       	self.ui = Ui_Qt_CV_MainWindow()
	self.setupUi(self)
	QtCore.QObject.connect(self.file_button, QtCore.SIGNAL("clicked()"), self.open_file)
	QtCore.QObject.connect(self.exec_button,QtCore.SIGNAL("clicked()"),self.make_canny)
	self.vb = None
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
        self.pic_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pic_view.customContextMenuRequested.connect(self.contextMenue) 
	#self.pic_view.installEventFilter(self)
	  
	self.pic_view.setHorizontalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOff )
	self.pic_view.setVerticalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOff )
	self.pic_item = QtGui.QGraphicsPixmapItem()
	self.pic_view.setTransformationAnchor( QtGui.QGraphicsView.NoAnchor )
	self.pic_view.setResizeAnchor(QtGui.QGraphicsView.NoAnchor)
	self.scaleRatio = 1.0
	self.scaleFacter = 0.02
	self.scale = 1
	self.pic_item = None
 def mouseMoved(self,pos):
	curPos = self.pic_item.mapFromScene(pos.pos())
	print int(curPos.x()),int(curPos.y())


 def contextMenue(self,event):
        menu = QtGui.QMenu()
        menu.addAction('canny',self.make_canny)
	menu.addAction('test1',self.make_canny)
	menu.exec_(QtGui.QCursor.pos())

 def eventFilter(self, source, event):
	if (type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_A) :
		self.scaleRatio += self.scaleRatio_add
		self.change_size()
	elif (event.type() == (QtCore.QEvent.MouseButtonDblClick) and source is self.pic_view):
		self.scaleRatio = 1
		self.change_size(event.pos())
		print "1"

	elif (event.type() == QtCore.QEvent.MouseButtonPress and source is self.pic_view):
		_x0,_y0,pic_x,pic_y = self.pic_coordinate(event.pos())
		if event.button() == QtCore.Qt.RightButton:
			self.pic_item.resetTransform()
			self.scene.setSceneRect(self.scene.itemsBoundingRect())

		elif event.button() == QtCore.Qt.LeftButton:
			self.scaleRatio = 2
			self.change_size(event.pos(),_x0,_y0,pic_x,pic_y)
	
		else:
			pos = event.pos()
			msgbox = QtGui.QMessageBox(self)
			scenepos = self.pic_item.mapToScene( pos.x(), pos.y() )
			scenepos2 = self.pic_item.mapFromScene( pos.x(), pos.y() )
			msgbox.setText('mouse position: (%d, %d) \r\nto :(%d,%d) \r\nfrom:(%d,%d)'\
					% (pos.x()/self.scaleRatio, pos.y()/self.scaleRatio,\
					scenepos.x()/self.scaleRatio, scenepos.y()/self.scaleRatio,\
					scenepos2.x()/self.scaleRatio, scenepos2.y()/self.scaleRatio\
					))
			ret = msgbox.exec_()
			x,y = self.pic_coordinate(event.pos())
			print x,y
			"""
			print self.pic_item.pos()
			print self.pic_item.scenePos()
			a=  self.pic_item.sceneBoundingRect()
			print a.width()
			print a
			print self.scale
			"""
	elif (event.type() == QtCore.QEvent.Wheel and source is self.pic_view):
		if event.delta() > 119 :
			self.scaleRatio = 1.1
			#self.scaleRatio += self.scaleRatio_add
			self.change_size(event.pos())
		elif event.delta() < -119 :
			if self.scaleRatio == 1  :
				pass
			else:
				self.scaleRatio =0.8
				#self.scaleRatio -= self.scaleRatio_add
				self.change_size(event.pos())
		else:
			pass
	return QtGui.QWidget.eventFilter(self, source, event)

 def pic_coordinate(self,curPos=None):
	scenepos = self.pic_view.mapToScene(curPos.x(),curPos.y())
	item_position = self.pic_item.sceneBoundingRect()
	_x0,_y0,_h,_w = item_position.x(),item_position.y(),item_position.height(),item_position.width()
	#print 	_x,_y,_h,_w
	#print scenepos
	#print self.scale
	pic_x = (scenepos.x() - _x0 )/self.scale
	pic_y = (scenepos.y() - _y0 )/self.scale
	return _x0,_y0,pic_x,pic_y
	
 def change_size(self,curPos=None,_x0=None,_y0=None,pic_x=None,pic_y=None):
	if curPos == None :
		scene_size = self.scene.itemsBoundingRect()
	else:	
		print pic_x,pic_y
		localRect = self.pic_item.mapToScene(curPos.x(),curPos.y())
		print localRect
		localRect2 = self.pic_view.mapToScene(curPos.x(),curPos.y())
		print localRect

		new_x = pic_x * self.scale * self.scaleRatio +_x0
		new_y = pic_y * self.scale * self.scaleRatio +_y0
		ch_x = new_x - localRect.x()
		ch_y = new_y - localRect.y()
		#self.pic_item.setPos(float(1),float(1))
		#self.pic_item.translate(float(5),float(5))
		self.pic_item.translate(float(localRect.x()),float(localRect.y()))
		self.pic_item.scale(float(self.scaleRatio),float(self.scaleRatio))
		self.pic_item.translate(-float(localRect.x()),-float(localRect.y()))
		#print new_y,localRect.y()
		print self.pic_item.sceneBoundingRect()
		#self.pic_view.ensureVisible(200*2*scaleFacter,200*2*self.scaleFacter,300,300)
		#self.pic_view.centerOn(100*self.scaleRatio,100*self.scaleRatio)
	self.scene.setSceneRect(self.scene.itemsBoundingRect())
	self.scale = self.scale*self.scaleRatio

	
 def open_file(self):
	
	self.file = QtGui.QFileDialog.getOpenFileName()
        if file:
		if self.pic_item == None:
			pass
		else:
			pass
		#self.pic_vie.removeItem(self.pic_item)
		self.file_edit.setText(self.file[0])
		im = cv2.imread(self.file[0])
		im_c = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
		rows,cols,dim = im_c.shape
		M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
		self.pyqt_pic = cv2.warpAffine(im_c,M,(cols,rows))
		if self.vb == None:
			self.vb = self.pic_view.addViewBox()
		else:
			pass

		self.pic_item = pg.ImageItem(self.pyqt_pic)
		self.vb.addItem(self.pic_item)
		self.vb.setAspectLocked(True)
		self.pic_view.scene().sigMouseClicked.connect(self.mouseMoved) 
	    	self.adjust_view()
	    	self.scaleRatio = 1
	return file

 def adjust_view(self):
	 bar = 8
	 __width = self.pic_item.boundingRect().width()+bar
	 __height = self.pic_item.boundingRect().height()+bar
	 __x = self.pic_view.x()
	 __y = self.pic_view.y()
	 self.pic_view.setGeometry(QtCore.QRect(__x, __y, __width, __height))

	 __main_x = int(__x + __width + 100)
	 __main_y = int(__y + __height + 50)
	 self.resize(__main_x,__main_y)
	 
 def make_canny(self):
	    cv_test = opencv_test()
	    pic,pic2 = cv_test.open_pic(self.file[0])
	    self.cv_img = cv_test.canny(pic2)
            height, width, dim = self.cv_img.shape
            bytesPerLine = dim * width
            self.image = QtGui.QImage(self.cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
	    pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(self.image))
	    self.pic_item = pic_Item
	    self.scene.clear()
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
