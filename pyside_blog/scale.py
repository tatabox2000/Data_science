import cv2

def make_scale(im,length=40,from_edge = 15,thick = 2,hight = 6,font_size = 0.6 ,pix = 10):

	w = im.shape[0]
	h = im.shape[1]

	cv2.line(im,(w-length-from_edge,h-from_edge),(w-from_edge,h-from_edge),(180,255,100),thick)
	cv2.line(im,(w-length-from_edge,h-from_edge-hight/2),(w-length-from_edge,h-from_edge+hight/2),(180,255,100),thick)
	cv2.line(im,(w-from_edge,h-from_edge-hight/2),(w-from_edge,h-from_edge+hight/2),(180,255,100),thick)
	
	size = pix*length
	text = str(size) + ' ' + 'micro m'
	#font = cv2.FONT_HERSHEY_COMPLEX_SMALL
	#font = cv2.FONT_HERSHEY_SIMPLEX
	font = cv2.FONT_HERSHEY_PLAIN
	cv2.putText(im,text,(w-length-from_edge*2,h-from_edge-hight),font, font_size,(180,255,100))

	return im
if __name__ == '__main__':
	im = cv2.imread("lena.jpg")
	im2 = make_scale(im)
	cv2.imshow("",im2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
