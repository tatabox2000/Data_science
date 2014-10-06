import numpy as np
from matplotlib import pylab as plt
import cv2
from PIL import Image as pil

class coordinateForCv:
 def __init_(self,parent=None):        
	self.pyqt_pic = None
	self._x = None
	self._y = None

 def cv2open(self,file=None):
	im = cv2.imread(file)
	return im

 def cv2pyqtgraph(self,im,num = -90):
	if len(im.shape) == 3:
		im_c = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
		im = im_c
	else:
		pass
	im_pil=pil.fromarray(im)
	im_pil_rotate=im_pil.rotate(-90)
	self.pyqt_pic= np.asarray(im_pil_rotate)
	return self.pyqt_pic

 def coordinate2cv(self,x,y,rect_x,rect_y):
	temp_coor =  np.zeros((rect_x,rect_y),np.uint8)
	temp_coor[x,y] = 255
	im_pil=pil.fromarray(temp_coor)
	im_pil_rotate = im_pil.rotate(90)
	cv_pic_coor = np.asarray(im_pil_rotate)
	index = np.where(cv_pic_coor==255)
	return index

 def contour_data(self,cnt):
	leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
	rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
	topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
	bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
	left_top = (topmost[0],leftmost[1])
	right_top = (topmost[0],rightmost[1])
	right_bottom = (bottommost[0],rightmost[1])
	left_bottom  = (bottommost[0],leftmost[1])
	#cut_area = [topmost[0]:bottommost[0],leftmost[1]:rightmost[1]]
	return topmost[1],bottommost[1],leftmost[0],rightmost[0]

if __name__ == '__main__':
	file = "lena.jpg"
	a = coordinateForCv()
	im = a.cv2open(file)
	im2 = a.cv2pyqtgraph(im)
	x = np.arange(10,100,1)
	y = np.arange(30,130,1)
	before,after,calc = a.coordinate2cv_test(x,y,im.shape[0],im.shape[1])
	calc_pic = np.zeros((im2.shape[0],im2.shape[1]),np.uint8)

	for i,j in calc:
		calc_pic[i,j]=255
	plt.subplot(1,3,1),plt.imshow(before,'gray')
	plt.subplot(1,3,2),plt.imshow(after,'gray')
	plt.subplot(1,3,3),plt.imshow(calc_pic,'gray')
	plt.show()
