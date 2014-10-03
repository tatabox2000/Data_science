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
from pic_count import pic_count

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
	self.erase_num = []
 def mouseMoved(self,pos):
	curPos = self.pic_item.mapFromScene(pos.pos())
	item = self.pic_item.boundingRect()
	co = coordinateForCv()
	_w,_h = int(item.width()),int(item.height())
	if curPos.x() < 0 or curPos.y() < 0 or curPos.x() > _w or  curPos.y() > _h:
		pass
	else :
		pic_coordinate = co.coordinate2cv(int(curPos.x()),int(curPos.y()),_w,_h)
		print pic_coordinate[0], pic_coordinate[1]

 def contour_select(self,pic_contour ,contour, curPos):
	for i ,cnt in enemurate(contour):
		 in_out = cv2.pointPolygonTest(cnt,(curPos[0],curPos[1]),False)
		 if in_out == 1 or in_out == 0:
			 cur_contour = np.zeros_like(pic_contour)
			 cur_contour = cv2.drawContours(cur_contour,cnt,0,(255,255,0),3)
		 else :
			pass
	add_image = cv2.addWeighted(pic_contour,1,cur_contour,0.5,0)
	return add_image

 def contextMenue(self,event):
        menu = QtGui.QMenu()
        menu.addAction('canny',self.make_canny)
	menu.addAction('All_drow',self.all_drowcontour)
	self.make_canny()

	#menu.addAction('All_area',self.all_area)
	menu.exec_(QtGui.QCursor.pos())

 def all_area(self):
	 self.pic_item.scale(1,1)

 def all_drowcontour(self):
	 count = pic_count()
	 color,color2,imgray,color_final,im_c = count.red_change(self.imgray)

	 imgray_mask,all_1,mask_area1,self.all_num,self.all_cnt = count.picture_mask(imgray)
	 coor = coordinateForCv()
	 self.cv_img = coor.cv2pyqtgraph(imgray_mask)
	 
	 imgray_mask_bool = np.asarray(self.cv_img,np.bool8)
	 im_1 = np.zeros_like(self.pyqt_pic)
	 im_1[imgray_mask_bool]=(255,0,0)

	 add = cv2.addWeighted(self.pyqt_pic,1,im_1,0.5,0)
	 
	 self.pic_item = pg.ImageItem(add)
	 self.vb.addItem(self.pic_item)
	 

 def close_event(self):
	reply = QtGui.QMessageBox.question(self,'Message',
        'Are you sure to quit?',QtGui.QMessageBox.Yes |
        QtGui.QMessageBox.No,QtGui.QMessageBox.No)
	if reply == QtGui.QMessageBox.Yes:
		QtCore.QCoreApplication.instance().quit()
	else:
		pass



 def eventFilter(self, source, event):
	if (type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_A) :
		self.scaleRatio += self.scaleRatio_add
		self.change_size()
	elif (event.type() == (QtCore.QEvent.MouseButtonDblClick) and source is self.pic_view):
		self.scaleRatio = 1
		self.change_size(event.pos())
		print "1"

	elif (event.type() == QtCore.QEvent.MouseButtonPress and source is self.pic_view):
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

	elif (event.type() == QtCore.QEvent.Wheel and source is self.pic_view):
		return QtGui.QWidget.eventFilter(self, source, event)

 def open_file(self):
	
	self.file = QtGui.QFileDialog.getOpenFileName()
        if file:
		if self.pic_item == None:
			pass
		else:
			pass
		self.file_edit.setText(self.file[0])
		im = cv2.imread(self.file[0])
		self.imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		coor = coordinateForCv()
	 	self.pyqt_pic = coor.cv2pyqtgraph(im)

		if self.vb == None:
			self.vb = self.pic_view.addViewBox(enableMenu=False)
		else:
			pass
		self.pic_item = pg.ImageItem(self.pyqt_pic)
		self.vb.addItem(self.pic_item)
		self.vb.setAspectLocked(True)
		self.pic_view.scene().sigMouseClicked.connect(self.mouseMoved)
		#self.pic_view.scene().sigMouseClicked.connect(self.eventFilter)
	    	self.adjust_view()
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
	 cv_img = cv_test.canny(pic2)
	 coor = coordinateForCv()
	 self.pyqt_pic = coor.cv2pyqtgraph(cv_img)
	 self.pic_item = pg.ImageItem(self.pyqt_pic)
	 self.vb.addItem(self.pic_item)


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
