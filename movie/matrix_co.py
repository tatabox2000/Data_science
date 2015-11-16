import numpy as np
import os 
import cv2
from PIL import Image as pil
import glob
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

 def get_list_and_index(self,filename):
	 print filename
	 root, ext = os.path.splitext(filename)
	 dirname  = os.path.dirname(filename)
	 name  = os.path.basename(filename)

	 search_name = dirname + '/*' + ext
	 namelist = glob.glob(search_name)
	 namelist_uni=[]
	 i = 0
	 for i in np.arange(0,len(namelist),1):
		 name = namelist[i].replace('\\','/')
		 namelist_uni.append(name)
	 files_len = len(namelist) - 1
	 filename_pos = namelist_uni.index(filename)

	 return namelist_uni,files_len,filename_pos
 

 def check_edge(self,im,all_num,all_cnt,all_cnt_area,edge_pix=2):
	edge_num=[]
	edge_cnt=[]
	edge_area=[]
	no_edge_all_num =[]
	no_edge_all_cnt =[]
	no_edge_all_area=[]
	bottom = im.shape[0]
	right = im.shape[1]
	edge =np.zeros((im.shape[0],im.shape[1]),np.uint8)
	edge[:,0:edge_pix] =255
	edge[:,right-edge_pix:right] =255
	edge[0:edge_pix,:] =255
	edge[bottom-edge_pix:bottom,:] =255
	edge_bool = (edge > 254)
	edgeSum = np.sum(edge)/255
	
	for h,cnt,area in zip(all_num,all_cnt,all_cnt_area):
		area_mask = np.zeros((im.shape[0],im.shape[1]),np.uint8)
		cv2.drawContours(area_mask,[cnt],0,255,-1)
		#area_mask2 = area_mask - edge
		area_mask[edge_bool] = 0
		cnt_edge= np.sum(area_mask)/255

		if area > cnt_edge:
			edge_num.append(h)
			edge_cnt.append(cnt)
			edge_area.append(cnt_edge)
		elif area == cnt_edge :
			no_edge_all_num.append(h)
			no_edge_all_cnt.append(cnt)
			no_edge_all_area.append(area)
	
	return no_edge_all_num,no_edge_all_cnt,no_edge_all_area,edge_num,edge_cnt,edge_area,edgeSum
	print len(no_edge_all_num),len(edge_cnt)

 def contour_data(self,cnt):
	leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
	rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
	topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
	bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
	left_top = (topmost[1],leftmost[0])
	right_top = (topmost[1],rightmost[0])
	right_bottom = (bottommost[1],rightmost[0])
	left_bottom  = (bottommost[1],leftmost[0])
	#cut_area = [topmost[0]:bottommost[0],leftmost[1]:rightmost[1]]
	return topmost[1],bottommost[1],leftmost[0],rightmost[0]
 def eba_calc(self,all_num,all_cnt,all_cnt_area,imgray_mask,imgray):
	no_edge_all_num,no_edge_all_cnt,no_edge_all_area,edge_num,edge_cnt,edge_area = self.check_edge(imgray_mask,all_num,all_cnt,all_cnt_area,10)
	for num,cnt in zip(no_edge_all_num,no_edge_all_cnt):

		list_num = self.coordinate_of_cnt(cnt,imgray,num)
		#topmost[1],bottommost[1],leftmost[0],rightmost[0]=self.contour_data(cnt)
		imgray_mask_bool = imgray_mask == 255

		for x,y,num in list_num:
			xstart = x - 10
			xend   = x + 10
			ystart = y - 10
			yend   = y + 10
		pass
 def coordinate_of_cnt(self,cnt,imgray,num):
	 coordinate_list=[]
	 y = imgray.shape[0]
	 x = imgray.shape[1]
	 area_mask = np.zeros((y,x),np.uint8)
	 cv2.drawContours(area_mask,[cnt],0,255,-1)
	 for x in np.arange(0,x,1):
		 for y in np.arange(0,y,1):
			if (area_mask[y,x] ==255):
				coordinate_list.append((x,y,num))
			else:
				pass
	 print coordinate_list
	 return coordinate_list

	 

if __name__ == '__main__':
	from matplotlib import pylab as plt
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
