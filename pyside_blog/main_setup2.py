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
from PIL import Image as pil 
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
	self.all_cnt = None
	self.all_con = None
	self.cur_cnt = None
	self.cur_cnt_number = None
	self.erase_num = []
	undoicon = QtGui.QIcon.fromTheme("edit-undo")
	#print undoicon
	#self.centralwidget.setWindowIcon(QtGui.QIcon(undoicon))

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
	self.pic_view.installEventFilter(self)
	  
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

 def erase_area(self):
	 self.erase_num.append(self.cur_cnt_number)
	 cou = pic_count()
	 erased_mask_cv = cou.re_draw_contour(self.im,self.all_num,self.all_cnt,self.erase_num)
	 coor = coordinateForCv()
	 erased_mask_qt = coor.cv2pyqtgraph(erased_mask_cv)

	 self.open_or_add_pic(self.pyqt_pic,erased_mask_qt,0.7,0.7)
	 self.all_con = self.add
 def add_area(self):
	 
	 self.erase_num.remove(self.cur_cnt_number)

	 cou = pic_count()
	 erased_mask_cv = cou.re_draw_contour(self.im,self.all_num,self.all_cnt,self.erase_num)
	 coor = coordinateForCv()
	 erased_mask_qt = coor.cv2pyqtgraph(erased_mask_cv)

	 self.open_or_add_pic(self.pyqt_pic,erased_mask_qt,0.7,0.7)
	 self.all_con = self.add

 def recover_area(self):
	 self.erase_num.pop()
	 cou = pic_count()
	 erased_mask_cv = cou.re_draw_contour(self.im,self.all_num,self.all_cnt,self.erase_num)
	 coor = coordinateForCv()
	 erased_mask_qt = coor.cv2pyqtgraph(erased_mask_cv)

	 self.open_or_add_pic(self.pyqt_pic,erased_mask_qt,0.7,0.7)
	 self.all_con = self.add

 def edge_chekbox(self):
	for h,con in enumerate[self.all_cnt]:
		top,bottom,left,right =coo.contour_data(cnt)
		if top == 0 or bottom == 0 or left == 0 or right == 0:
			pass
		else:
			pass

 def mouseMoved(self,pos):
	pyqt_pos = self.pic_item.mapFromScene(pos.pos())
	item = self.pic_item.boundingRect()
	co = coordinateForCv()
	_w,_h = int(item.width()),int(item.height()) 
	if pyqt_pos.x() < 0 or pyqt_pos.y() < 0 or pyqt_pos.x() > _w or pyqt_pos.y() > _h:
		pass
	else :
		pic_coordinate = co.coordinate2cv(int(pyqt_pos.x()),int(pyqt_pos.y()),_w,_h)
		x = np.ndarray.tolist(pic_coordinate[1])
		y = np.ndarray.tolist(pic_coordinate[0])
		self.curPos= (x[0]+4,y[0]+4)

 def normal_contour(self):
	ret,thresh = cv2.threshold(self.imgray,5,255,0)
	self.all_cnt, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for h,cnt in enumerate(self.all_cnt):
    		mask = np.zeros(self.imgray.shape,np.uint8)
    		cv2.drawContours(mask,[cnt],0,255,-1)
		#self.open_or_add_pic(mask,mask,1,1)
 def cut_area(self):
	 if self.cur_cnt is None:
		 pass
	 else:
	 	coo = coordinateForCv()
	 	top,bottom,left,right =coo.contour_data(self.cur_cnt)
		im_con = self.im[top-5:bottom+20,left-5:right+5,:]
		filename = self.last_dir + '/' + 'contour.jpg' + '\'' 
		temp_file = QtGui.QFileDialog.getSaveFileName(self,directory = filename,filter="Image Files (*.png *.bmp *jpg)")
		if temp_file == None:
			pass
		else:
			cv2.imwrite(temp_file[0],im_con)
			self.pic_item.setImage(im_con)
 def write_scale(self,im):
	 im.shape[0]

 def contour_select(self):
	if self.all_cnt is None :
		pass
	else:
		for i ,cnt in enumerate(self.all_cnt):
			in_out = cv2.pointPolygonTest(cnt,(self.curPos[0],self.curPos[1]),False)
			if in_out == 1 or in_out == 0:
				self.cur_contour = np.zeros_like(self.im)
				cv2.drawContours(self.cur_contour,[cnt],0,(0,255,0),-1)	 
				coor = coordinateForCv()
				self.cur_cnt = cnt
				self.cur_cnt_number = i
				self.cv_img = coor.cv2pyqtgraph(self.cur_contour)
				self.open_or_add_pic(self.pyqt_pic,self.cv_img,0.2,1)
			else :
				pass

 def contextMenue(self,event):
        menu = QtGui.QMenu()
        menu.addAction('Canny',self.make_canny)
	menu.addAction('All_drow',self.all_drowcontour)
	menu.addAction('Threshold_only',self.normal_contour)
	menu.addAction('Clear',self.clear)
	menu.addAction('Save Contour',self.cut_area)
	menu.addAction('Erase contour',self.erase_area)
	menu.addAction('Add contour',self.add_area)
	menu.addAction('Recover a erased contour',self.recover_area)

	self.contour_select()
	menu.exec_(QtGui.QCursor.pos())

	#menu.addAction('All_area',self.all_area)
 def all_area(self):
	 print "i"
 def clear(self):
	 self.pic_item.setImage(self.pyqt_pic)

 def all_drowcontour(self):
	 count = pic_count()
	 self.imgray=cv2.bilateralFilter(self.imgray,10,20,5)
	 imgray,im_color = count.gray_range_select(self.imgray,80,160)
	 imgray_mask,all_1,self.all_num,self.all_cnt = count.all_contour(imgray)

	 coor = coordinateForCv()
	 self.cv_img = coor.cv2pyqtgraph(imgray_mask)
	 
	 imgray_mask_bool = np.asarray(self.cv_img,np.bool8)
	 self.all_mask = np.zeros_like(self.pyqt_pic)
	 self.all_mask[imgray_mask_bool]=(255,255,0)
	 self.open_or_add_pic(self.pyqt_pic,self.all_mask,0.7,0.7)
	 self.all_con = self.add

 def open_or_add_pic(self,pic1,pic2=None,weight1=1,weight2=0.5):
	 self.pic_item = pg.ImageItem()
	 self.vb.addItem(self.pic_item)
	 if pic2 == None:
		self.add =pic1
	 else:
	 	self.add = cv2.addWeighted(pic1,weight1,pic2,weight2,0)
	 self.pic_item.setImage(self.add)

 def eventFilter(self, source, event):
	if (type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_A) :
		pass
	if (event.type() == (QtCore.QEvent.MouseButtonDblClick) and source is self.pic_view):
		pass
	if (event.type() == QtCore.QEvent.MouseButtonPress and source is self.pic_view):
		if event.button() == QtCore.Qt.RightButton:
			pass

		if event.button() == QtCore.Qt.LeftButton:
			if self.all_con is None :
				pass

			else :
				self.pic_item.setImage(self.all_con)
	
	#if (event.type() == QtCore.QEvent.MouseButtonRelease and source is self.pic_view):
	#	if event.button() == QtCore.Qt.RightButton:
	#		print "ok" 

	return QtGui.QWidget.eventFilter(self, source, event)

 def open_file(self):
	self.filename = QtGui.QFileDialog.getOpenFileName(self,filter="Image Files (*.png *.bmp *jpg)")
        if self.filename is not None:
		if self.pic_item == None:
			pass
		else:
			self.vb.removeItem(self.pic_item)
		self.file_edit.setText(self.filename[0])
		self.im = cv2.imread(self.filename[0])
		self.all_con = None
		self.last_dir = os.path.dirname(unicode(self.filename))

		if len(self.im.shape) == 3:
			self.imgray = cv2.cvtColor(self.im,cv2.COLOR_BGR2GRAY)
		else:
			self.imgray = self.im
		coor = coordinateForCv()
	 	self.pyqt_pic = coor.cv2pyqtgraph(self.im)
		if self.vb == None:
			self.vb = self.pic_view.addViewBox(enableMenu=False)
			self.vb.setAspectLocked(True)
		else:
			pass
		self.open_or_add_pic(self.pyqt_pic)
		self.pic_view.scene().sigMouseClicked.connect(self.mouseMoved)
		self.adjust_view()
	return file

 def adjust_view(self):
	 bar = 8
	 __width = self.pic_item.boundingRect().width()+bar
	 __height = self.pic_item.boundingRect().height()+bar
	 __x = self.pic_view.x()
	 __y = self.pic_view.y()
	 if __width <= 512 or __height <= 512:
 		__width, __height  = 512,512
	 else:
		 pass
	 self.pic_view.setGeometry(QtCore.QRect(__x, __y, __width, __height))
	 __main_x = int(__x + __width + 80)
	 __main_y = int(__y + __height + 80)
	 self.resize(__main_x,__main_y)
	 self.all_con
 def make_canny(self):
	 cv_test = opencv_test()
	 cv_img = cv_test.canny(self.im)
	 coor = coordinateForCv()
	 self.canny = coor.cv2pyqtgraph(cv_img)
	 self.open_or_add_pic(self.canny)

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
