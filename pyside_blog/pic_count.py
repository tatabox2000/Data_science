# -*- coding: utf-8 -*-
from __future__ import with_statement
import cv2
import os

import numpy as np
import glob
import re
import codecs

class pic_count:
 def __init__(self,parent = None):
	self.file = file
	self.pix = 9
	self.gray =re.compile('Snapshot[2-3]')
	#self.maxArea = 5000
	self.maxArea = 80000
	#self.minArea = 120
	self.minArea = 10
	self.filename = "picture.csv"
	self.min_number =120
	#self.min_number =254
	self.largeRange = 200
	self.smallRange = 0
	#self.smallRange = 50
	#self.largeRange = 185
	self.erase_num = []

 def picture_make(self,before,dim=3 ):
    	bak=[]
    	i = 0
    	while i < dim:
        	zeros = np.zeros((before.shape[0],before.shape[1],i+1),np.uint8)
        	bak.append(zeros)
        	i = i+2
    	return bak

 def all_contour(self,im,maxArea,minArea):
	contours,hierarch =cv2.findContours(im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        mask = np.zeros((im.shape[0],im.shape[1]),np.uint8)
	all_num =[]
	all_cnt =[]
	i = 0
	all_cnt_area = []
        for h,cnt in enumerate(contours):
		area = cv2.contourArea(cnt)
		if area > maxArea:
			pass
		elif area < minArea:
			pass
		else:
			calc_mask_temp = np.zeros((im.shape[0],im.shape[1]),np.uint8)
			cv2.drawContours(calc_mask_temp,[cnt],0,255,-1)
			#print (np.sum(calc_mask_temp)/255)
			all_cnt_area.append(np.sum(calc_mask_temp)/255)

			cv2.drawContours(mask,[cnt],0,255,-1)
			all_num.append(i)
			i += 1
			all_cnt.append(cnt)
    	return mask,all_num,all_cnt,all_cnt_area
  
 def re_draw_contour(self,im,all_num,all_cnt,all_cnt_area,erase_num ):
	 erased_mask = np.zeros_like(im)
	 cnt_area = []
	 for h,cnt,area in zip(all_num,all_cnt,all_cnt_area):
                if h  not in erase_num :
			 cv2.drawContours(erased_mask,[cnt],0,(0,255,255),-1)
			 #print (np.sum(calc_mask_temp)/255)
			 cnt_area.append(area)

			 #cv2.imshow("",calc_mask_temp)
			 #cv2.waitKey(0)
			 #cv2.destroyAllWindows()  
		else:
			 pass
			 
	 return erased_mask, cnt_area
 def mono_re_draw_contour(self,im,all_num,all_cnt,all_cnt_area,erase_num ):
	 erased_mask = np.zeros((im.shape[0],im.shape[1]),np.uint8)
	 cnt_area = []
	 for h,cnt,area in zip(all_num,all_cnt,all_cnt_area):
		 if h  not in erase_num :
			 cv2.drawContours(erased_mask,[cnt],0,255,-1)
			 #print (np.sum(calc_mask_temp)/255)
			 cnt_area.append(area)

			 #cv2.imshow("",calc_mask_temp)
			 #cv2.waitKey(0)
			 #cv2.destroyAllWindows()  
		 else:
			 pass
			 
	 return erased_mask, cnt_area

 def make_name(self,name = None,i=1):
	 name4,name5 =re.split(r'/',name)
         name6 = name4 + '_' + str(i)
         name7 = name6 + '_mask'
         name6_jpg = name6 + '.jpg'
         name7_jpg = name7 + '.jpg'
	 name_UV = re.sub(r'Snapshot1',r'Snapshot2',name)
	 return name6_jpg,name7_jpg,name_UV
 
 def color_filter(self,im,color = 'r'):
	 if  len(im.shape) == 2:
		 return im
	 elif color == 'gray':
		 imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		 return imgray
	 elif color == 'r' :
		 select_color = np.zeros((im.shape[0],im.shape[1]),np.uint8)
		 select_color[:,:] = im[:,:,2]
		 return select_color
	 elif color == 'g' :
		 select_color = np.zeros((im.shape[0],im.shape[1]),np.uint8)
		 select_color[:,:] = im[:,:,1]
		 return select_color
	 elif color == 'b' :
		 select_color = np.zeros((im.shape[0],im.shape[1]),np.uint8)
		 select_color[:,:] = im[:,:,0]
		 return select_color
	 elif color == 'y' :
		 select_color = np.zeros((im.shape[0],im.shape[1]),np.uint8)
		 select_color2 = select_color.copy()

		 select_color[:,:] = im[:,:,1]
		 select_color = select_color/2
		 select_color2[:,:] = im[:,:,2]
		 select_color2 = select_color2/2
		 select_color = select_color+ select_color2
		 return select_color



 def smoothing(self,imgray,smooth = 'None'):
	 #if  len(imgray.shape) == 3:
	#	 print  'gray scale only'
	#	 return
	 if smooth == 'None':
		 return imgray
	 elif smooth == 'Bilateral' :
		 blur = cv2.bilateralFilter(imgray,10,20,5)
		 return blur
	 elif smooth == 'GaussianBlur' :
		 blur = cv2.GaussianBlur(imgray,(5,5),0)
		 return blur
 	 elif smooth == 'medianBlur' :
		 median = cv2.medianBlur(imgray,5)
		 return median
	 elif smooth == 'Blur' :
		 blur = cv2.blur(imgray,(5,5))
		 return blur


 def gray_range_select(self,im,_min=None,_max=None):
	 im_gray,im_color =self.picture_make(im)
 	 if _max == None:
		th_bool=(im >= _min)
         	im_gray[th_bool]= 255
         	im_color[th_bool]=(255,255,0)
	 elif _min == None:
		th_bool=(im <= _max)
         	im_gray[th_bool]= 255
         	im_color[th_bool]=(255,255,0)	
	 else :
		th_bool=(im >= _min)&(im <= _max)
         	im_gray[th_bool]= 255
         	im_color[th_bool]=(0,255,0)
		#cv2.imshow("",im_color)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows() 

	 return  im_gray,im_color


 def pic_calc(self,color_final,all_1):
	red_area =np.sum(color_final)
	float_red_area =float(red_area)
	red_area_exe = float_red_area/255*self.pix/1000/1000*(1000*1000/1.55/1.55)

	return red_area,red_area_exe

 def bool_mask(self,imgray_mask,UV_mask,color_final):
	imgray_mask_bool = np.asarray(imgray_mask,np.bool8)
	UV_mask_bool = np.asarray(UV_mask,np.bool8)
	mask_bool =imgray_mask_bool + UV_mask_bool
	mask =imgray_mask + UV_mask
	color_final[mask_bool]=(0,0,0)

	return mask_bool,mask,color_final,imgray_mask_bool,mask_bool
 
 def get_pic_names(self,name_ext = '*.jpg',dir = None):
	 if dir == None :
		 pos_name  = glob.glob(name_ext)
	 else :
		 name_ext = dir + '/' + name_ext
		 print name_ext
		 pos_name  = glob.glob(name_ext)
	 return pos_name
 


 def FFT(self,imgray):

    F= np.fft.fft2(imgray)
    F_= np.log(5 + np.fft.fftshift(np.abs(F)))
    
    return F_

 def open_files(self,dir = None):
	if dir is not None :
		os.chdir(dir)
	else:
		pass
	with codecs.open(self.filename,'ab','cp932') as pic:
		all_color = []
    		i = 1
    		pic.write(u"サンプル名,ファイル名,面積,数\n")
    		for name in glob.glob('*/*.jpg'):
        		if self.gray.search(name) is None:
				name2 = re.sub(r'/',',',name) + ','
	         		name3 = re.sub('\n',',',name2)
				pic.write(name3)
				name6_jpg,name7_jpg,name_UV = self.make_name(name,i)
				i =i+1	
				im0 = cv2.imread(name)
				im_UV0 =cv2.imread(name_UV)
				im_UV = cv2.cvtColor(im_UV0,cv2.COLOR_BGR2GRAY)
				red_pic = self.color_filter(im0,'r')
				imgray,color = self.gray_range_select(red_pic ,self.min_number )
				color_final = color.copy() 

				th_UV,im_UV3 = self.gray_range_select(bila_UV,self.smallRange,self.largeRange )
				imgray_mask,all_1,self.all_num1,self.all_cnt1 = self.picture_mask(imgray)
				UV_mask,all_2,self.all_num1,self.all_cnt1 = self.picture_mask(th_UV)

				mask_bool,mask,color_final,imgray_mask_bool,mask_bool = self.bool_mask(imgray_mask,UV_mask,color_final)
				red_area,count,red_area_exe = self.pic_calc(color_final,all_1)
				print >> pic,red_area,',',
				
				#印刷、描画用画像処理と書き出し
				im_gray,im_color=self.picture_make(im0)
				im_1 =im_color.copy()
				im_2 =im_color.copy()
				im_1[imgray_mask_bool]=(255,0,0)
				im_2[mask_bool]=(0,255,255)
				im_color =255 - color[:,:,0]
				cv2.imwrite(name6_jpg,im_color)
				color_add=color.copy()
				color_add[mask_bool]=(0,0,255)
				add = cv2.addWeighted(im_UV0,1,color_add,0.5,0)
				return color,im0,add,im_UV0,im_1,im_UV,im_UV3,UV_mask,color_final,all_2,im_2
			else:
				pass
if __name__ == '__main__':
	import matplotlib.pyplot as plt
	a = pic_count()
	_dir = os.path.abspath(__file__)
	name = '*.jpg'
	print a.get_pic_names(name,_dir)

	color,im0,add,im_UV0,im_1,im_UV,im_UV3,UV_mask,color_final,all_2,im_2  =a.open_files()
	
	im_c = cv2.cvtColor(im0,cv2.COLOR_BGR2RGB)

	plt.subplot(3,4,1),plt.imshow(im_c)
	plt.title('blank')
	plt.subplot(3,4,2),plt.hist(im_c.flatten(),300,range=(1,300))
	plt.title('red histgram')
	plt.subplot(3,4,3),plt.imshow(color,'gray')
	plt.title('threshold > 220 ')
	plt.subplot(3,4,4),plt.imshow(im_1,'gray')
	plt.title('mask from red(Area>120pix=1080micro)')
	plt.subplot(3,4,5),plt.imshow(im_UV,'gray')
	plt.title('UV')
	plt.subplot(3,4,6),plt.hist(im_UV.flatten(),300,range=(1,300))
	plt.title('UV histgram')
	plt.subplot(3,4,7),plt.imshow(im_UV3)
	plt.title('185 > threshold > 50')
	plt.subplot(3,4,8),plt.imshow(UV_mask,'gray')
	plt.title('mask from UV (Area>120pix=1080micro)')
	plt.subplot(3,4,9),plt.imshow(color_final)
	plt.title('final')
	plt.subplot(3,4,10),plt.hist(all_2,100,range=(1,100))
	plt.title('distribution')
	plt.subplot(3,4,11),plt.imshow(add)
	plt.title('Color like image')
	plt.subplot(3,4,12),plt.imshow(im_2)
	plt.title('sum_mask')
	plt.show()
