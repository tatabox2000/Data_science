import numpy as np 
import cv2
 
im = np.zeros((20,20),np.uint8)
bottom = im.shape[0]-1
right = im.shape[1]-1
im2 = np.zeros((20,20),np.uint8)
im2[:,:] = 255


im[:,0:5] =255
im[:,right] =255
im[0,:] =255
im[bottom,:] =255

im3 = im > 254

im2[im3] = 0
cv2.imshow("",im2)
cv2.waitKey(0)
cv2.destroyAllWindows() 
