import numpy as np
from matplotlib import pylab as plt
import cv2

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
			rows,cols,dim = im.shape
		else:
                        rows,cols = im.shape
		
		M = cv2.getRotationMatrix2D((cols/2,rows/2),num,1)
		self.pyqt_pic = cv2.warpAffine(im,M,(cols,rows))
		return self.pyqt_pic

	def coordinate2cv_test(self,x,y,rect_x,rect_y):
		temp_coor =  np.zeros((rect_x,rect_y),np.uint8)
		index = zip(x,y)
		for i,j in index:
			#print j,i
			temp_coor[j:j+3,i] = 255
		rows,cols = temp_coor.shape
		M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
		cv_pic_coor = cv2.warpAffine(temp_coor,M,(cols,rows))
		index2 = np.where(cv_pic_coor==255)
		cv_coor = zip(index2[0],index2[1])
		return temp_coor,cv_pic_coor,cv_coor

	def coordinate2cv(self,x,y,rect_x,rect_y):
		temp_coor =  np.zeros((rect_x,rect_y),np.uint8)
		temp_coor[x,y] = 255
		rows,cols = temp_coor.shape
		M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
		cv_pic_coor = cv2.warpAffine(temp_coor,M,(cols,rows))
		index = np.where(cv_pic_coor==255)
		return index

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
