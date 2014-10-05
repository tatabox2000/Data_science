import cv2

def make_scale(im,length=20,from_edge = 10,thick = 1,hight = 4, pix = 10):

	w = im.shape[0]
	h = im.shape[1]

	cv2.line(im,(w-length-from_edge,h-from_edge),(w-from_edge,h-from_edge),(180,255,100),thick)
	cv2.line(im,(w-length-from_edge,h-from_edge-hight/2),(w-length-from_edge,h-from_edge+hight/2),(180,255,100),thick)
	cv2.line(im,(w-from_edge,h-from_edge-hight/2),(w-from_edge,h-from_edge+hight/2),(180,255,100),thick)
	
	size = pix*length
	text = str(size) + 'micro m'
	#font = cv2.FONT_HERSHEY_COMPLEX_SMALL
	#font = cv2.FONT_HERSHEY_SIMPLEX
	font = cv2.FONT_HERSHEY_PLAIN
	cv2.putText(im,text,(w-length-from_edge*3,h-from_edge-hight),font, thick/2.0,(180,255,100))

	return im
if __name__ == '__main__':
	im = cv2.imread("lena.jpg")
	im2 = make_scale(im)
	cv2.imshow("",im2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
