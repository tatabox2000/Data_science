# -*- coding: utf-8 -*-
from __future__ import with_statement
import PySide
import pyqtgraph as pg
import cv2
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import math
from PySide import QtCore,QtGui
import os
from PIL import Image as pil 
from pygraph_Opencv import Ui_Qt_CV_MainWindow
from opencv_test import opencv_test
from matrix_co import coordinateForCv
from pic_count import pic_count
from subwindow_CutOrTrim import Ui_cut_window
class CustomPlotItem(pg.ImageItem):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        # Need to switch off the "has no contents" flag
        self.setFlags(self.flags() & ~self.ItemHasNoContents)

    def mouseDragEvent(self, ev):
        print("drag")
        if ev.button() != QtCore.Qt.LeftButton:
            ev.ignore()
            return

        if ev.isStart():
            print("start")
        elif ev.isFinish():
            print("finish")

    def shape(self):
        # Inherit shape from the curve item
        return self.curve.shape()

    def boundingRect(self):
        # All graphics items require this method (unless they have no contents)
        return self.shape().boundingRect()

    def paint(self, p, *args):
        # All graphics items require this method (unless they have no contents)
        return

    def hoverEvent(self, ev):
        # This is recommended to ensure that the item plays nicely with 
        # other draggable items

        print("hover")
        ev.acceptDrags(QtCore.Qt.LeftButton)

class SubWindow_for_cut_or_trim(QtGui.QDialog,Ui_cut_window):
 def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

class DesignerMainWindow(QtGui.QMainWindow,Ui_Qt_CV_MainWindow):
 def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
       	self.ui = Ui_Qt_CV_MainWindow()
	self.setupUi(self)
	self.code = self.os_check()
	
###########################################################
# Table Settings
###########################################################
        vheader = QtGui.QHeaderView(QtCore.Qt.Orientation.Vertical)
        vheader.setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.tableWidget.setVerticalHeader(vheader)
        hheader = QtGui.QHeaderView(QtCore.Qt.Orientation.Horizontal)
        hheader.setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeader(hheader)
        #self.tableWidget.setHorizontalHeaderLabels(title)

        QtCore.QObject.connect(self.file_button, QtCore.SIGNAL("clicked()"), self.push_file_button)
	#QtCore.QObject.connect(self.exec_button,QtCore.SIGNAL("clicked()"),self.make_canny)
	QtCore.QObject.connect(self.EBA_button,QtCore.SIGNAL("clicked()"),self.calc_eba)

	self.init_var()
	self.pic_item = None
	#self.size = 0.0361
	#self.size = 2.15
	self.size = int(self.size_edit.text())
	self.imgray = None
	self.sub_vb = None
	self.vb = None
	self.pyqt_pic =None
	self.plt1 = None
	self.largeRange = int(self.threshold1_edit.text())
	self.smallRange = int(self.threshold2_edit.text())
	self.maxArea =int(self.max_area_edit.text())
	self.minArea =int(self.min_area_edit.text())
	self.namelist = None
	undoicon = QtGui.QIcon.fromTheme("edit-undo")
	#print undoicon
	#self.centralwidget.setWindowIcon(QtGui.QIcon(undoicon))
	"""
        QtCore.QObject.connect(self.actionQuit, QtCore.
SIGNAL("triggered()"), QtGui.qApp, QtCore.SLOT("quit()"))
	QtCore.QObject.connect(self.quit_button, QtCore.
SIGNAL("clicked()"), self.close_event)
	"""
	QtCore.QObject.connect(self.exec_button, QtCore.SIGNAL("clicked()"), self.push_execute_box)
	QtCore.QObject.connect(self.threshold1_slider, QtCore.SIGNAL("valueChanged(int)"), self.change_threshold1_slider)
	QtCore.QObject.connect(self.threshold2_slider, QtCore.SIGNAL("valueChanged(int)"), self.change_threshold2_slider)
	QtCore.QObject.connect(self.threshold1_edit, QtCore.SIGNAL("textEdited(const QString&)"), self.change_threshold1_edit)
	QtCore.QObject.connect(self.threshold2_edit, QtCore.SIGNAL("textEdited(const QString&)"), self.change_threshold2_edit)
	QtCore.QObject.connect(self.max_area_slider, QtCore.SIGNAL("valueChanged(int)"), self.change_max_area_slider)
	QtCore.QObject.connect(self.min_area_slider, QtCore.SIGNAL("valueChanged(int)"), self.change_min_area_slider)
	QtCore.QObject.connect(self.max_area_edit, QtCore.SIGNAL("textEdited(const QString&)"), self.change_max_area_edit)
	QtCore.QObject.connect(self.min_area_edit, QtCore.SIGNAL("textEdited(const QString&)"), self.change_min_area_edit)
	QtCore.QObject.connect( self.color_combo, QtCore.SIGNAL('activated(int)'), self.setCurrentIndex)
	QtCore.QObject.connect( self.save_mode_combo, QtCore.SIGNAL('activated(int)'), self.set_save_modeIndex)
	QtCore.QObject.connect( self.smooth_combo, QtCore.SIGNAL('activated(int)'), self.setsmooth)
	QtCore.QObject.connect(self.actionSeparate_picture, QtCore.SIGNAL("triggered()"), self.separate_picture)

	#QtCore.QObject.connect(self.threshold1_edit, QtCore.SIGNAL("textEdited(const QString&)"), self.change_text)
	QtCore.QObject.connect(self.size_edit, QtCore.SIGNAL("textEdited(const QString&)"), self.change_size_edit)

        self.pic_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pic_view.customContextMenuRequested.connect(self.contextMenue) 
	self.pic_view.installEventFilter(self)
	#self.pic_item = QtGui.QGraphicsPixmapItem()
	self.pic_view.setTransformationAnchor( QtGui.QGraphicsView.NoAnchor )
	self.pic_view.setResizeAnchor(QtGui.QGraphicsView.NoAnchor)
	self.eject_edge_or_not.stateChanged.connect(self.all_drowcontour)
	#self.file_scrollbar.valueChanged.connect(self.cur_position)

	#self.form_view_or_image.stateChanged.connect(self.open_or_add_pic)
	
 
 def separate_picture(self):
	 self.cut_or_trim_window = SubWindow_for_cut_or_trim(self)
	 self.cut_or_trim_window.show()
 def change_size_edit(self):
	self.size = float(self.size_edit.text())
 
 def calc_eba(self):
	edgePix = int(5000 / self.size)
	coor = coordinateForCv()



	if self.eject_edge_or_not.isChecked():
		coor = coordinateForCv()
		coor.eba_calc(self.all_num_with_edge,self.all_cnt_with_edge,self.all_cnt_area_with_edge,self.imgray_mask,self.imgray)
	else:
		coor = coordinateForCv()
		coor.eba_calc(self.all_num,self.all_cnt,self.all_cnt_area,self.imgray_mask,self.imgray)

 def cur_position(self):
	self.vb.clear()
	self.sub_vb.clear()
	i =  self.file_scrollbar.value()
	name2 = self.namelist[i].encode(self.code)
	self.im = cv2.imread(name2)
	self.file_edit.setText(name2)
        name = QtGui.QTableWidgetItem(os.path.basename(name2))
        self.tableWidget.setItem(0,0,name)
	self.pic_set()
        self.all_con = None

 def init_var(self):
	self.all_cnt_area =None
	self.all_cnt = None
 	self.all_con = None
	self.cur_cnt = None
	self.cur_cnt_number = None
	self.cur_contour_area = None
	self.erase_num = []
	self.all_num = None
	self.all_con = None
	self.erase_num = []
	self.all_num_with_edge=None
	self.all_cnt_with_edge=None
	self.all_area_with_edge=None
	self.files_len = None
	self.filename_pos = None
	self.imgray_mask = None
	self.all_cnt_area_with_edge = None
	self.edgeSum = None

 def check_edge(self):
	 if self.all_num == None:
		 return
	 else:
		count = pic_count()
	 	if self.eject_edge_or_not.isChecked():
			self.all_num_with_edge=self.all_num
			self.all_cnt_with_edge=self.all_cnt
			self.all_area_with_edge = self.all_cnt
			self.imgray_mask_with_edge = self.imgray_mask
			coordinate = coordinateForCv()
			self.all_num,self.all_cnt,self.all_cnt_area,self.edge_num,self.edge_cnt,self.edge_area,self.edgeSum =coordinate.check_edge(self.im,self.all_num,self.all_cnt,self.all_cnt_area)

			erased_mask,cur_contour_area = count.mono_re_draw_contour(self.im,self.all_num,self.all_cnt,self.all_cnt_area,self.erase_num)
			return erased_mask,cur_contour_area
		else:
			erased_mask,cur_contour_area = count.mono_re_draw_contour(self.im,self.all_num,self.all_cnt,self.all_cnt_area,self.erase_num)
			return erased_mask,cur_contour_area
 def result_calculate(self):
    if self.cur_contour_area is None:
        if self.all_cnt_area is None:
            return
	else :
	    vals = self.all_cnt_area
    else:
	vals = self.cur_contour_area
    if vals == []:
        return
    else:
        calc = []
	areavals = np.array(vals)
        sizevals = self.size * self.size * areavals
	sizevals_list = sizevals.tolist()
        _sum = np.sum(sizevals)
        average = round(np.mean(sizevals),3)
        median = np.median(sizevals)
        var = round(np.var(sizevals),3)
        std = round(np.std(sizevals),3)
        count = len(vals)

        
        calc.append(count)

	if self.edgeSum is None:
	    print "None Edge"
	    ppm = int(np.sum(vals)*1000000/(self.im.shape[0]*self.im.shape[1]))
	    mperm = ppm * 1000
	    calc.append(ppm)
	    over100,over250 = self.pixcel_separate()
	    over100_contour = areavals[areavals>=over100]
	    
	    ppm_over100 = int(np.sum(over100_contour)*1000000/(self.im.shape[0]*self.im.shape[1]))
	    calc.append(len(over100_contour))
	    calc.append(ppm_over100)
	    over250_contour = areavals[areavals>=over250]
	    ppm_over250 = int(np.sum(over250_contour)*1000000/(self.im.shape[0]*self.im.shape[1]))
	    calc.append(len(over250_contour))

	    calc.append(ppm_over250)
	    #calc.append(mperm)
    	else:
	    print "Eject Edge"
	    ppm =int(np.sum(vals)*1000000/(self.im.shape[0]*self.im.shape[1]-(np.sum(self.edge_area)+self.edgeSum)))
	    mperm = ppm * 1000
	    calc.append(ppm)
	    over100,over250 = self.pixcel_separate()
	    over100_contour = areavals[areavals>=over100]
	    ppm_over100 = int(np.sum(over100_contour)*1000000/(self.im.shape[0]*self.im.shape[1]-(np.sum(self.edge_area)+self.edgeSum)))
	    calc.append(len(over100_contour))
	    calc.append(ppm_over100)
	    over250_contour = areavals[areavals>=over250]
	    ppm_over250 = int(np.sum(over250_contour)*1000000/(self.im.shape[0]*self.im.shape[1]-(np.sum(self.edge_area)+self.edgeSum)))
	    calc.append(len(over250_contour))

	    calc.append(ppm_over250)
	    #calc.append(mperm)
        calc.append(_sum)
        calc.append(average)
        calc.append(median)
	calc.append(var)
        calc.append(std)
	calc.append(sizevals_list)
        return calc

 def table_set(self):
     if self.cur_contour_area is None and self.all_cnt_area is None:
         return
     
     calc = self.result_calculate()
     title = ["File Name","counts","ppm","100_count","100_ppm","250_count","250_ppm","sum","average","median","var","std"]
     num = int(len(calc))
     self.tableWidget.setHorizontalHeaderLabels(title)
     for i in np.arange(0,num-1,1):
         item = QtGui.QTableWidgetItem(str(calc[i]))
         self.tableWidget.setItem(0,i+1,item)
     
 def make_histogram(self):
     if self.cur_contour_area is None and self.all_cnt_area is None:
         return
     else:
         calc = self.result_calculate()
         if calc == None:
             return
     if self.plt1 == None:
		 self.plt1 = self.hist_view.plotItem
		 #self.plt1.clear()
     else:
		 self.plt1.clear()
         
     self.plt1.hideAxis('left')
     self.plt1.showAxis('right')

     #vals = np.hstack([np.random.normal(size=500), np.random.normal(size=260, loc=4)])
     y,x = np.histogram(calc[0],bins=100)
     curve = pg.PlotCurveItem(x, y, stepMode=True, fillLevel=0, brush=(0, 0, 255, 80))
     curve.rotate(90)
     self.plt1.addItem(curve)
     self.table_set()
 def make_scale(sefl,im,length=10,from_edge = 5,thick = 1,hight = 4,font_size = 0.6 ,pix = 10):
	w = im.shape[1] *2
	h = im.shape[0] *2
	im2 = cv2.resize(im,(w,h))
	cv2.line(im2,(w-length-from_edge,h-from_edge),(w-from_edge,h-from_edge),(180,255,100),thick)
	cv2.line(im2,(w-length-from_edge,h-from_edge-hight/2),(w-length-from_edge,h-from_edge+hight/2),(180,255,100),thick)
	cv2.line(im2,(w-from_edge,h-from_edge-hight/2),(w-from_edge,h-from_edge+hight/2),(180,255,100),thick)
	size = pix*length /2
	text = str(size) + ' ' + 'micro m'
	#font = cv2.FONT_HERSHEY_COMPLEX_SMALL
	#font = cv2.FONT_HERSHEY_SIMPLEX
	font = cv2.FONT_HERSHEY_PLAIN
	cv2.putText(im2,text,(w-length-from_edge*2,h-from_edge-hight),font, font_size,(180,255,100))
	cv2.imshow("",im2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return im2


 def contextMenue(self,event):
        menu = QtGui.QMenu()
	submenu = QtGui.QMenu()
	submenu.setTitle("Contour menu")
	if self.all_con is not None: 
		menu.addMenu(submenu)
        menu.addAction('Canny',self.make_canny)
	menu.addAction('Fourier transform',self.FFT)
	menu.addAction('All_drow',self.all_drowcontour)
	menu.addAction('Clear',self.clear)
	
	submenu.addAction('Save Contour',self.cut_area)
	submenu.addAction('Erase contour',self.erase_area)
	submenu.addAction('Add contour',self.add_area)
	submenu.addAction('Recover a erased contour',self.recover_area)

	self.contour_select()
	menu.exec_(QtGui.QCursor.pos())
 def FFT(self):
	 if self.imgray is None :
		 pass
	 else:
	 	count = pic_count()
	 	im = count.FFT(self.imgray)
		self.open_or_add_pic(im)
	
 def sub_window_pic(self,im):
	if self.sub_vb == None:
		self.sub_vb = self.sub_view.addViewBox()
	else:
		self.sub_vb.clear()
	self.sub_vb.setAspectLocked(True)
	self.sub_item = pg.ImageItem()
	self.sub_vb.addItem(self.sub_item)
	coor = coordinateForCv()
	self.pyqt_imgray = coor.cv2pyqtgraph(im)
	self.sub_item.setImage(self.pyqt_imgray)

 def open_or_add_pic(self,pic1=None,pic2=None,weight1=1,weight2=0.5):
	 self.pic_item = pg.ImageItem()
	 if self.vb is None:
		 pass
	 else:
	 	self.vb.clear()
	 	self.vb.addItem(self.pic_item)
	 if pic1 is None:
		if self.pyqt_pic is None:
			return
		else:
			self.add = self.pyqt_pic
	 elif pic1 is not None and pic2 is None:
		self.add =pic1
	 else:
	 	self.add = cv2.addWeighted(pic1,weight1,pic2,weight2,0)
	 self.View_or_Image()
	 self.pic_item.setImage(self.add)
 def mouseDragEvent(self, event):
	 print pos

 def eventFilter(self, source, event):
	if (type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_A) :
		pass
	if (event.type() == (QtCore.QEvent.MouseButtonDblClick) and source is self.pic_view):
		print '???'
	if (event.type() == (QtCore.QEvent.MouseButtonRelease) and source is self.pic_view):
		#if event.button() == QtCore.Qt.LeftButton:
		print event.globalX()

	if (event.type() == QtCore.QEvent.MouseButtonPress and source is self.pic_view):
		if event.button() == QtCore.Qt.RightButton:
			pass

		if event.button() == QtCore.Qt.LeftButton:
			if self.all_con is None :
				return
			else :
				self.pic_item.setImage(self.all_con)
	
	return QtGui.QWidget.eventFilter(self, source, event)
 def scrollbar_set(self,files_len,filename_pos):
	self.file_scrollbar.setProperty("value", files_len)
	self.file_scrollbar.setValue(filename_pos)
	self.file_scrollbar.setMaximum(files_len)
	self.file_scrollbar.valueChanged.connect(self.cur_position)

 def push_file_button(self):
	 self.open_file()
	 self.pic_set()
	 self.scrollbar_before()

 def open_file(self):
	self.init_var()
	self.filename = QtGui.QFileDialog.getOpenFileName(self,filter="Image Files (*.png *.bmp *jpg)")
        if self.filename is not None:
		if self.pic_item is not None:
			self.vb.clear()
		if self.plt1 is not None:
			self.plt1.clear()
		self.file_edit.setText(self.filename[0])
                name = QtGui.QTableWidgetItem(os.path.basename(self.filename[0]))
                self.tableWidget.setItem(0,0,name)
		self.filename2 = self.filename[0].encode(self.code)
                self.im = cv2.imread(self.filename2)

 def pic_set(self): 
	if len(self.im.shape) == 3:
       		color = self.setCurrentIndex()
		smooth = self.setsmooth()

		count = pic_count()
		blur = count.smoothing(self.im,smooth)
		self.imgray = count.color_filter(blur,color)
		self.sub_window_pic(blur)
		#cv2.imshow("",self.imgray)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
	else:
		self.imgray = self.im
	coor = coordinateForCv()
	self.pyqt_pic = coor.cv2pyqtgraph(self.im)
	if self.vb == None:
		self.vb = self.pic_view.addViewBox(enableMenu=False)
		self.vb.setAspectLocked(True)
		#self.vb.setMouseEnabled(y=False)
		#self.vb.setMouseEnabled(x=False)
	else:
		pass
	self.open_or_add_pic(self.pyqt_pic)
	
 def scrollbar_before(self):
	self.pic_view.scene().sigMouseClicked.connect(self.mouseMoved)
	coor = coordinateForCv()
	self.namelist, self.files_len, self.filename_pos = coor.get_list_and_index(self.filename[0])
	self.scrollbar_set( self.files_len, self.filename_pos)

 def mouseReleased(self,event):
	 #QtGui.qApp.restoreOverrideCursor()
	 self.update()
         QtGui.QGraphicsItem.mouseReleaseEvent(self, event)
	 print '>>>>'
	 #super(pg.GraphicsLayoutWidget, self).mouseReleaseEvent( event)

 def make_canny(self):
	 cv_test = opencv_test()
	 cv_img = cv_test.canny(self.im)
	 coor = coordinateForCv()
	 self.canny = coor.cv2pyqtgraph(cv_img)
	 self.open_or_add_pic(self.canny)

 def select_folder(self):
        folder = QtGui.QFileDialog.getExistingDirectory(self,'Open Dorectory',os.path.expanduser('~'))
        if folder:
		self.folder_edit.setText(folder)
 ###############################################
 # check box & combobox
 ###############################################
 def set_save_modeIndex(self):
	if self.save_mode_combo.currentIndex () == 0:
		save = 'CSV_hist'
		return save
	if self.save_mode_combo.currentIndex () == 1:
		save = 'CSV_count'
		return save
 def os_check(self):
	 if os.name is 'nt':
		 code = 'cp932'
		 return code
	 if os.name is not 'nt':
		 code = 'utf-8'
		 return code

 def setCurrentIndex(self):
	if self.color_combo.currentIndex () == 0:
		color = 'gray'
		return color
	if self.color_combo.currentIndex () == 1:
		color = 'r'
		return color

	if self.color_combo.currentIndex () == 2:
		color = 'g'
		return color

	if self.color_combo.currentIndex () == 3:
		color = 'b'
		return color
	if self.color_combo.currentIndex () == 4:
		color = 'y'
		return color
 def setsmooth(self):
	if self.smooth_combo.currentIndex () == 0:
		smooth = 'None'
		return smooth
	if self.smooth_combo.currentIndex () == 1:
		smooth = 'Bilateral'
		return smooth
	if self.smooth_combo.currentIndex () == 2:
		smooth = 'GaussianBlur'
		return smooth
	if self.smooth_combo.currentIndex () == 3:
		smooth = 'medianBlur'
		return smooth
	if self.smooth_combo.currentIndex () == 4:
		smooth = 'Blur'
		return smooth
 def setextention(self):
	if self.extention_combo.currentIndex () == 0:
		smooth = '*.jpg'
		return smooth
	if self.extention_combo.currentIndex () == 1:
		smooth = '*.bmp'
		return smooth
	if self.extention_combo.currentIndex () == 2:
		smooth = '*.tiff'
		return smooth
 def Save_Image(self):
	if self.save_picture_combo.currentIndex () == 0:
		pic_save = None
		return pic_save
	if self.save_picture_combo.currentIndex () == 1:
		pic_save = 'Contour'
		return pic_save
	if self.save_picture_combo.currentIndex () == 2:
		pic_save = 'Picture with Contour'
		return pic_save

 
 def View_or_Image(self):
	if self.form_view_or_image.isChecked():
		self.adjust_view()
	else:
		self.adjust_pic()

 #########################################
 #adjust view & picture scale
 #########################################
 def adjust_pic(self):
	 __x = self.pic_view.x()
	 __y = self.pic_view.y()

	 self.pic_view.setGeometry(QtCore.QRect(__x, __y, 551, 561))

	 _view_x = self.pic_view.width()
	 _view_y = self.pic_view.height()

	 __width = float(self.add.shape[0])
	 __height = float(self.add.shape[1])
	 if __width > __height :
		 scale = _view_x/__width
	 else:
		 scale = _view_y/__height
	 self.pic_item.scale(scale,scale)
	 __main_x = int(__x + 512 + 80)
	 __main_y = int(__y + 512 + 80)
	 self.resize(__main_x,__main_y)


 def adjust_view(self):
	 bar = 8
	 __width = float(self.add.shape[0])
	 __height = float(self.add.shape[1])
	 __x = self.pic_view.x()
	 __y = self.pic_view.y()
	 if __width <= 512 or __height <= 512:
 		__width, __height  = 512,512
	 else:
		 pass
	 self.pic_view.setGeometry(QtCore.QRect(__x, __y, __width, __height))
	 __main_x = int(__x + __width )
	 __main_y = int(__y + __height )
	 self.resize(__main_x,__main_y)

 #############################################
 # contour 
 #############################################
 def contour_select(self):
	if self.all_cnt is None :
		pass
	else:
		for i ,cnt in zip(self.all_num,self.all_cnt):
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
 def clear(self):
	 self.init_var()
	 self.vb.clear()
	 self.pic_item = pg.ImageItem()
	 self.vb.addItem(self.pic_item)
	 self.pic_item.setImage(self.pyqt_pic)
	 self.all_con = None
	 self.all_cnt = None
 def push_execute_box(self):
	 save_csv = self.set_save_modeIndex()
	 folder = QtGui.QFileDialog.getExistingDirectory(self,'Open Dorectory',os.path.expanduser('~'))
	 if folder == u'':
		 return
	 import glob
	 ext = self.setextention()
	 os.chdir(folder)

	 if save_csv == 'CSV_hist':
		calc_cnt =[]
		for name in glob.glob(ext):
			 self.im = cv2.imread(name)
			 cnt = self.execute(self.im)
			 calc_cnt.extend(cnt)
		import codecs
		import csv
		fol_name = ["Folder place:", folder ]
		code = self.os_check()
		with codecs.open("all_pic_hist.csv",'ab',code) as pic:
			 csvWriter = csv.writer(pic)
			 csvWriter.writerow(fol_name)
			 csvWriter.writerow(calc_cnt)  
	 if save_csv == 'CSV_count':
		import codecs
		import csv
		self.pixcel_separate()
		settings = ["1pixel Size","Max threshold","Min threshold","Max Area[pix]","Min Area[pix]","100 over[pix]","250 over[pix]"]
		settings_num = [self.size * self.size,self.largeRange,self.smallRange,self.maxArea,self.minArea,self.over100_pix,self.over250_pix]
                csvtitle = ["File Name","counts","ppm","100_count","100_ppm","250_count","250_ppm","sum","average","median","var","std","contours"]
		with codecs.open("pic_count.csv",'w',self.code) as pic:
			csvWriter = csv.writer(pic)
			csvWriter.writerow(settings)
			csvWriter.writerow(settings_num) 
                        csvWriter.writerow(csvtitle)  
			for name in glob.glob(ext):
				self.im = cv2.imread(name)
                                calc = self.exec_each_pic(self.im,name)
				if calc == None:
					pass
				else:
					calc.insert(0,name)
					contour = calc[12]
					del calc[12]
					if contour == None:
						pass
					else :
						calc.extend(contour)
					csvWriter.writerow(calc) 
                                
 def pixcel_separate(self):
##########################
# r1 = 250/2.0
# over100 = np.pi* r1**2
# r2 = 100/2
# over250 = np.pi*r1**2
##########################
  over100 = 7853.981633974483
  over250 = 49087.385212340516
  import math
  self.over100_pix = math.ceil(over100/(self.size*self.size))
  self.over250_pix = math.ceil(over250/(self.size*self.size))
  return self.over100_pix,self.over250_pix

 def save_picture(self,im,name):
         mask = self.imgray_mask == 255
         im_mask_color = np.zeros_like(im)
         im_mask_color[mask]= (0,0,255)
	 save_pic = self.Save_Image()

	 if save_pic == 'Contour':
         	name1 = "contour_" + name
         	cv2.imwrite(name1,im_mask_color)
	 if save_pic == 'Picture with Contour':
         	alpha = 1.0
         	beta = 0.8
         	add = cv2.addWeighted(im,alpha,im_mask_color,beta,0)
         	name2 = "picture_with_contour_" + name
         	cv2.imwrite(name2,add)

 def exec_each_pic(self,im,name):
	 self.init_var()
 	 color = self.setCurrentIndex()
	 count = pic_count()
	 _imgray = count.color_filter(im,color)
	 smooth = self.setsmooth()
	 blur = count.smoothing(_imgray,smooth)
	 imgray,im_color = count.gray_range_select(blur,self.smallRange,self.largeRange) 
	 self.imgray_mask,self.all_num,self.all_cnt,self.all_cnt_area = count.all_contour(imgray,self.maxArea,self.minArea)
	 self.imgray_mask,self.all_cnt_area = self.check_edge()
	 save = self.Save_Image()
	 if save == None:
		 pass
	 else:
            image = self.save_picture(im,name)  

            #cv2.imshow("",add)
	    #cv2.waitKey(0)
	    #cv2.destroyAllWindows() 

	 calc = self.result_calculate()
	 if calc == None:
		 calc = ['0','0','0','0','0','0','0','0','0','0','0','0']
	 else:
		 pass
	 if self.vb == None:
		 pass
	 else:
		 self.vb.clear()
		 self.sub_vb.clear()
         return calc

 def execute(self,im):
	 self.init_var()
 	 color = self.setCurrentIndex()
	 count = pic_count()
	 _imgray = count.color_filter(im,color)
	 smooth = self.setsmooth()
	 blur = count.smoothing(_imgray,smooth)
	 imgray,im_color = count.gray_range_select(blur,self.smallRange,self.largeRange) 
	 self.imgray_mask,self.all_num,self.all_cnt,self.all_cnt_area = count.all_contour(imgray,self.maxArea,self.minArea)

	 self.imgray_mask,self.all_cnt_area = self.check_edge()
	 
	 save = self.Save_Image()
	 if save == None:
		 pass
	 else:
            image = self.save_picture(im,name)

	 #imgray_mask_bool = np.asarray(self.cv_img,np.bool8)
	 #self.all_mask = np.zeros_like(self.im)
	 #self.all_mask[imgray_mask_bool]=(255,255,0)
	 area = []
	 for i  in self.all_cnt_area:
		 j = self.size * self.size * float(i)
		 area.append(j)
	 #print area
	 if self.vb == None :
		 pass
	 else:
	 	self.vb.clear()
	 	self.sub_vb.clear()
	 return area

 def all_drowcontour(self):
	 self.init_var()
	 count = pic_count()
	 #self.imgray=cv2.bilateralFilter(self.imgray,10,20,5)
	 imgray,im_color = count.gray_range_select(self.imgray,self.smallRange,self.largeRange) 
	 #imgray,im_color = count.gray_range_select(self.imgray,80,160)
 	 """
	 cv2.imshow("",imgray)
	 cv2.waitKey(0)
	 cv2.destroyAllWindows() 
	 """
	 self.imgray_mask,self.all_num,self.all_cnt,self.all_cnt_area = count.all_contour(imgray,self.maxArea,self.minArea)

	 self.imgray_mask,self.all_cnt_area = self.check_edge()
	 coor = coordinateForCv()
	 self.cv_img = coor.cv2pyqtgraph(self.imgray_mask)
	 
	 imgray_mask_bool = np.asarray(self.cv_img,np.bool8)
	 self.all_mask = np.zeros_like(self.pyqt_pic)
	 self.all_mask[imgray_mask_bool]=(255,255,0)
	 self.open_or_add_pic(self.pyqt_pic,self.all_mask,0.7,0.7)
 	 self.make_histogram()
	 self.all_con = self.add

 def erase_area(self):
	 self.erase_num.append(self.cur_cnt_number)

	 count = pic_count()
	 erased_mask_cv,self.cur_contour_area = count.re_draw_contour(self.im,self.all_num,self.all_cnt,self.all_cnt_area,self.erase_num)
	 coor = coordinateForCv()
	 erased_mask_qt = coor.cv2pyqtgraph(erased_mask_cv)
	 self.open_or_add_pic(self.pyqt_pic,erased_mask_qt,0.7,0.7)
	 self.all_con = self.add
	 
	 self.make_histogram() 
 def add_area(self):
	 self.erase_num.remove(self.cur_cnt_number)
	 cou = pic_count()

	 erased_mask_cv,self.cur_contour_area = cou.re_draw_contour(self.im,self.all_num,self.all_cnt,self.all_cnt_area,self.erase_num)
	 coor = coordinateForCv()
	 erased_mask_qt = coor.cv2pyqtgraph(erased_mask_cv)

	 self.open_or_add_pic(self.pyqt_pic,erased_mask_qt,0.7,0.7)
	 self.all_con = self.add
	 self.make_histogram()

 def recover_area(self):
	 self.erase_num.pop()
	 cou = pic_count()
	 erased_mask_cv,self.cur_contour_area = cou.re_draw_contour(self.im,self.all_num,self.all_cnt,self.all_cnt_area,self.erase_num)
	 coor = coordinateForCv()
	 erased_mask_qt = coor.cv2pyqtgraph(erased_mask_cv)

	 self.open_or_add_pic(self.pyqt_pic,erased_mask_qt,0.7,0.7)
	 self.all_con = self.add
	 self.make_histogram() 

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
		self.curPos= (x[0]+2,y[0]+2)

 def cut_area(self):
	 if self.cur_cnt is None:
		 pass
	 else:
	 	coo = coordinateForCv()
	 	top,bottom,left,right =coo.contour_data(self.cur_cnt)
		if top-5 >= 0 :
			top = top - 5
		if bottom + 10 <= self.im.shape[0]:
			bottom = bottom +10
		if left - 5 >= 0:
			left = left - 5
		if right + 10 <= self.im.shape[1]:
			right = right  + 10

		im_con = self.im[top:bottom,left:right,:]
		scale_pic = self.make_scale(im_con)
		filename = self.last_dir + '/' + 'contour.jpg' + '\'' 
		temp_file = QtGui.QFileDialog.getSaveFileName(self,directory = filename,filter="Image Files (*jpg *.png *.bmp )")
		if temp_file == None:
			pass
		else:
			cv2.imwrite(temp_file[0],scale_pic)

 ###############################################################
 # slider
 ###############################################################
 def change_max_area_slider(self,value):
	self.max_area_edit.setText(str(value))
	self.maxArea = int(value)
	if self.imgray is None :
		pass
	else:
		self.all_drowcontour()

 def change_min_area_slider(self,value):
	self.min_area_edit.setText(str(value))
	self.minArea = int(value)
	if self.imgray is None :
		pass
	else:
		self.all_drowcontour()

 def change_max_area_edit(self,value):
	if self.max_area_edit.text() is '':
		self.max_area_slider.setValue(0)
		self.maxArea = 0

	else:
		self.max_area_slider.setValue(int(self.max_area_edit.text()))
		self.maxArea=int(self.max_area_edit.text())
		if self.imgray is None :
			pass
		else:
			self.all_drowcontour()
 def change_min_area_edit(self,value):
	if self.min_area_edit.text() is '':
		self.min_area_slider.setValue(0)
		self.minArea = 0

	else:
		self.min_area_slider.setValue(int(self.min_area_edit.text()))
		self.minArea=int(self.min_area_edit.text())
		if self.imgray is None :
			pass
		else:
			self.all_drowcontour()
 def change_threshold1_slider(self,value):
	self.threshold1_edit.setText(str(value))
	self.largeRange = int(value)
	if self.imgray is None :
		pass
	else:
		self.all_drowcontour()

 def change_threshold2_slider(self,value):
	self.threshold2_edit.setText(str(value))
	self.smallRange = int(value)
	if self.imgray is None :
		pass
	else:
		self.all_drowcontour()

 def change_threshold1_edit(self,value):
	if self.threshold1_edit.text() is '':
		self.threshold1_slider.setValue(0)
		self.smallRange = 0

	else:
		self.threshold1_slider.setValue(int(self.threshold1_edit.text()))
		self.largeRange =int(self.threshold1_edit.text())
		if self.imgray is None :
			pass
		else:
			self.all_drowcontour()

		self.all_drowcontour()
 def change_threshold2_edit(self,value):
	if self.threshold2_edit.text() is '':
		self.threshold2_slider.setValue(0)
		self.smallRange = 0
	else:
	 	self.threshold2_slider.setValue(int(self.threshold2_edit.text()))
		self.smallRange = int(self.threshold1_edit.text())
		if self.imgray is None :
			pass
		else:
			self.all_drowcontour()


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
	QtCore.QTextCodec.setCodecForCStrings( QtCore.QTextCodec.codecForLocale() )
	app = QtGui.QApplication(sys.argv)
	dmw = DesignerMainWindow()
	dmw.show()
	sys.exit(app.exec_())
