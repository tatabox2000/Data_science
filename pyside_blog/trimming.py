import numpy as np 
import cv2
import os 
import glob
 
def pic_trim(pic = None,xtrim = 100,ytrim = None):
	if ytrim == None:
		ytrim = xtrim
	im = cv2.imread(pic)
	xmax = im.shape[0]-xtrim
	ymax = im.shape[1]-ytrim
	trimed_pic = im[xtrim:xmax,ytrim:ymax,:]
	root,ext = os.path.splitext(pic)
	name = "trimed_" + root + ext
 
	cv2.imwrite(name,trimed_pic)
	
if __name__ == "__main__":
	cur_dir = u"I:\jisei\STD"
	os.chdir(cur_dir)
	jpg_list = glob.glob("*jpg")
	for name in jpg_list:
		pic_trim(name,50)
	print 'finish'
