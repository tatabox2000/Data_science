import numpy as np
import cv2
from PIL import Image
cap = cv2.VideoCapture(1)
i = 0

for i in np.arange(1,1000,1) :
     ret, frame = cap.read()
     frame1 = frame
im0 = cv2.flip(frame1,0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    im = cv2.flip(frame,0)
    """
    im2 = np.zeros_like(im)
    im2[:,:,0] =im[:,:,2]
    im2[:,:,2]=im[:,:,0]
    im2[:,:,1]=im[:,:,1]
    im = im2
    """
    im = im - im0
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    
    cv2.imshow('frame',im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
