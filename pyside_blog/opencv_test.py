import numpy as np
import cv2
import scipy.ndimage as nd

class opencv_test:
	def __init__(self,parent = None):
		self.file = file
	def open_pic(self,file):
		pic = cv2.imread(file)
		pic_color = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)

		return pic,pic_color
	def canny(self,pic):
		img =cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(img,100,200)
		edges2 = np.zeros_like(pic)
		for i in (0,1,2):
			edges2[:,:,i] = edges
		add = cv2.addWeighted(pic,1,edges2,0.4,0)
		return add
        def find_contour(self,pic):
                im_gray =cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
                print im_gray
                im_gray_smooth=cv2.medianBlur(im_gray,5)
                bubbles = (im_gray_smooth <= 50) 
                sand = (im_gray_smooth > 50) & (im_gray_smooth <= 110)
                glass = (im_gray_smooth > 110)

                kernel = np.ones((5,5),np.uint8)
                
                for img in (bubbles,sand,glass):
                    img[:] = nd.binary_opening(img, iterations=3)
                    img[:] = nd.binary_closing(img, iterations=3)
                    
                    """
                    img[:] = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
                    img[:] = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
                    """
                colors = np.zeros((pic.shape[0],pic.shape[1],3),np.uint8)
                colors[bubbles]= (100,100,200)
                colors[sand]= (255,0,0)
                colors[glass]= (0,255,0)

                return colors

if __name__ == '__main__':
	file = "lena.jpg"
        a = opencv_test()
	b,c = a.open_pic(file)
        d = a.find_contour(b)
	cv2.imshow("",d)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	



