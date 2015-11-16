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
from movie import Ui_MainWindow
from matrix_co import coordinateForCv
from pic_count import pic_count
from subwindow_CutOrTrim import Ui_cut_window

class DesignerMainWindow(QtGui.QMainWindow, Ui_MainWindow):
 def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
       	self.ui =  Ui_MainWindow()
	self.setupUi(self)
#	self.code = self.os_check()

if __name__ == '__main__':
	QtCore.QTextCodec.setCodecForCStrings( QtCore.QTextCodec.codecForLocale() )
	app = QtGui.QApplication(sys.argv)
	dmw = DesignerMainWindow()
	dmw.show()
	sys.exit(app.exec_())

