import pyqtgraph as pg
import numpy as np
import sys
import cv2
import math
from PyQt4 import QtGui, QtCore

##########################
# Create the main window #
##########################

# This should be pretty self-explanatory if you have worked with Qt/PyQt
# before. If not, consider reading a tutorial or a book.
app = QtGui.QApplication([])
win = QtGui.QWidget()
lay = QtGui.QGridLayout()
win.setLayout(lay)

# Create a the first GraphicsView, which will contain a ViewBox for easier
# image zoom/pan/rotate operations, which will in turn contain the ImageItem
# responsible for displaying the image.
pg1 = pg.GraphicsView()
vb1 = pg.ViewBox()
im1 = pg.ImageItem()
vb1.addItem(im1)
vb1.setAspectLocked(True)    # No aspect distortions
pg1.setBackground(None)      # Transparent background outside of the image
pg1.setCentralWidget(vb1)    # Autoscale the image when the window is rescaled

# Do the same for the second GraphicsView
pg2 = pg.GraphicsView()
vb2 = pg.ViewBox()
im2 = pg.ImageItem()
vb2.addItem(im2)
vb2.setAspectLocked(True)
pg2.setBackground(None)
pg2.setCentralWidget(vb2)

# Add both GraphicsView to the Qt window
lay.addWidget(pg1, 0, 0, 1, 1)
lay.addWidget(pg2, 0, 1, 1, 1)

########################
# Load the first image #
########################

# Read the image, and only take the first channel if it has multiple channels
image = cv2.imread("C:\\Users\\analyst\\Documents\\Data_science\\pyside_blog\\lena.jpg",0)

# Transpose and mirror the image because PyQtGraph doesn't seem to use and
# display image arrays the same way OpenCV usually does.
#
#                              J
#    O------------->J          ^.....
#    |              .          |    .
#    |    OpenCV    .          |    . PyQtGraph
#    V              .          |    .
#    I...............          O--->I
#

###########################
# Create the second image #
###########################

# Simulate another image with a perspective transformation relative to the
# first image, by rotating it by 45 around its center and adding a little 
# perspective.

# Rotate it by 45...
angle = math.pi / 4
rotation = np.matrix([
    [np.cos(angle), np.sin(angle), 0.0],
    [-np.sin(angle), np.cos(angle), 0.0],
    [0.001, 0., 1.]])
# snuck in a little perspective here.

# ...around its center
tr = image.shape[1] / 2, image.shape[0] / 2
translation = np.matrix([
    [1.0, 0.0, tr[0]],
    [0.0, 1.0, tr[1]],
    [0.0, 0.0, 1.0]])

# Compose the two previous matrices and warp the image
warpmat = translation * rotation * translation.I
invwarp = warpmat.I
warpimage = cv2.warpPerspective(image, warpmat, (image.shape[1], image.shape[0]))

##################
# Display images #
##################

# Load the first image and autoscale it to be displayed entirely on the screen
im1.setImage(image)
vb1.autoRange()

# Do the same for the warped image
im2.setImage(warpimage)
vb2.autoRange()

################
# Add the ROIs #
################

size = min(image.shape) / 3
posx = (image.shape[0] - size) / 2
posy = (image.shape[1] - size) / 2

roi1 = pg.RectROI((posx, posy), size, pen=9)
roi2 = pg.RectROI((posx, posy), size, pen=9)

roi1.addScaleHandle([0, 0], [1, 1])
roi2.addScaleHandle([0, 0], [1, 1])
roi1.addScaleRotateHandle([1, 0], [1, 1])
roi2.addScaleRotateHandle([1, 0], [1, 1])

# Convert OpenCV-style transform to Qt-style.
# First, swap x <=> y
qtmat = warpmat[[1,0,2]][:,[1,0,2]]
# Transpose and build QTransform:
elements = np.array(qtmat).T.flatten()
roitrans = pg.QtGui.QTransform(*elements)
transitem = pg.ItemGroup()
transitem.setTransform(roitrans)
roi2.setParentItem(transitem)

vb1.addItem(roi1)
vb2.addItem(transitem)




# This method will handle ROI region changes
def regionChanged(source):
    """This method will handle ROI region changes."""

    # 'source' refers to the ROI that was moved by the user; 
    # 'target' will be the other ROI.
    target = roi2 if source == roi1 else roi1
    
    # Copy the ROI state from source to target.
    try:
        target.sigRegionChanged.disconnect(regionChanged)
        target.setState(source.saveState())
    finally:
        target.sigRegionChanged.connect(regionChanged)
        

# Connect the ROI's regionChanged signals to the method above
roi1.sigRegionChanged.connect(regionChanged)
roi2.sigRegionChanged.connect(regionChanged)

# Run it once to load the ROI positions
regionChanged(roi1)

###################
# Show the window #
###################

win.showMaximized()
win.setWindowTitle("PyQtGraph Examples - Linked ROIs")
app.exec_()
