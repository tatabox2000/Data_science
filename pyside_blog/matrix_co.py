import numpy as np
from matplotlib import pylab as plt
import cv2

class coordinateForCv:
	def __init_(self,parent=None):
		self.file = file
		self._x = None
		self._y = None
	def cv2qtgraph(self,im=None):
		if im.shape[2] == 3:
			im_c = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
			im = im_c
		else:
			pass
		rows,cols,dim = im.shape
		M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
		dst = cv2.warpAffine(im,M,(cols,rows))
		return dst

if __name__ == '__main__':
	file = "lena.jpg"
	im = cv2.imread(file)
        a = coordinateForCv()
	pic = a.cv2qtgraph(im)

	test = np.zeros((pic.shape[0],pic.shape[1]),np.uint8)
	test2 = np.zeros((pic.shape[0],pic.shape[1]),np.uint8)
	test[5:8,10:30] = 255
	index = np.where(test==255)
	rows,cols = test.shape
	M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
	dst = cv2.warpAffine(test,M,(cols,rows))
	index2 = np.where(dst==255)

	coor = zip(index2[0],index2[1])
	for i,j in coor:
		test2[i,j]=254
	print coor
	#print index
	#print index2
	plt.subplot(1,3,1),plt.imshow(test,'gray')
	plt.subplot(1,3,2),plt.imshow(dst,'gray')
	plt.subplot(1,3,3),plt.imshow(test2,'gray')
	plt.show()
