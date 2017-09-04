# created by Huang Lu
# 27/08/2016 19:33:52  
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

# empty image
img = np.zeros((512, 512, 3), np.uint8)

# call back function
def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),100,(255,0,0),1)

cv2.namedWindow('circle')
cv2.setMouseCallback('circle', draw_circle)

while(1):
	cv2.imshow('circle', img)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
