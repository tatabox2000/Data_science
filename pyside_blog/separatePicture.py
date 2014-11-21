# -*- coding: cp932 -*-
import numpy as np
import os 
import cv2
import pylab as plt
from pic_count import pic_count

class separate_pic():
	def adjust_pic(self,im,num):
		x = im.shape[0]
		y = im.shape[1]
		if x % num == 0:
			pass
		else:
			x = int( x / num) * num 
		if y % num == 0:
			pass
		else:
			y = int( y / num) * num
		return x,y
	def sepalate_pic(self,x,y,num,name):
		x1 = 0
		y1 = 0
		save_pic = np.zeros((x/num,y/num,3),np.uint8)
		for i in np.arange(1,num+1):
			for j in np.arange(1,num+1):
				x2 = x / num * i
				y2 = y / num * j
				save_x = x / num
				save_y  = y / num
				file_name = name + str(i) + '-' +str( j ) +'.jpg'
				print file_name
				save_pic[0:save_x,0:save_y]= im[x1:x2,y1:y2]
				
				y1 = y2
				cv2.imwrite(file_name,save_pic)
			y1 = 0
			x1 = x2
if __name__ == '__main__':
	os.chdir(u"I:/picture/mills/Amill/")
	pass_name= u"I:/picture/mills/Amill/A_1150_1.jpg"
	name = os.path.basename(pass_name)
	im = cv2.imread(pass_name)
	sep = separate_pic()
	x,y = sep.adjust_pic(im,9)
	sep.sepalate_pic(x,y,9,name)

