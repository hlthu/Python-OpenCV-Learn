# created by Huang Lu
# 27/08/2016 19:54:11   
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

# callbacks
def nothing(x):
	pass

if __name__ == '__main__':
	# empty image
	img = np.zeros((512, 512, 3), np.uint8)
	cv2.namedWindow('Track Bar')

	# creat track bars
	cv2.createTrackbar('R', 'Track Bar', 0, 255, nothing)
	cv2.createTrackbar('G', 'Track Bar', 0, 255, nothing)
	cv2.createTrackbar('B', 'Track Bar', 0, 255, nothing)
	cv2.createTrackbar('1:ON\n0:OFF', 'Track Bar', 0, 1, nothing)

	# while loop
	while(1):
		R = cv2.getTrackbarPos('R', 'Track Bar')
		G = cv2.getTrackbarPos('G', 'Track Bar')
		B = cv2.getTrackbarPos('B', 'Track Bar')
		F = cv2.getTrackbarPos('1:ON\n0:OFF', 'Track Bar')
		
		if F == 1:
			img[:]=[B,G,R]
		else:
			img[:]=[0,0,0]
		cv2.imshow('Track Bar', img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	cv2.destroyAllWindows()
