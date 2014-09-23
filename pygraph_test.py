import PySide
import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import cv2



pg.mkQApp()
w = pg.GraphicsLayoutWidget()
w.show()
vb = w.addViewBox()
img = pg.ImageItem(image = cv2.imread("C:\\Users\\analyst\\Documents\\Data_science\\pyside_blog\\1number.bmp"))
vb.addItem(img)
vb.setAspectLocked(True)
def mouseMoved(pos):
    print "Image position:", img.mapFromScene(pos.pos())

w.scene().sigMouseClicked.connect(mouseMoved)
#w.scene().sigMouseMoved.connect(mouseMoved)
QtGui.QApplication.instance().exec_()
