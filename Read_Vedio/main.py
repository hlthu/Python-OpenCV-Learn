# created by Huang Lu
# 27/08/2016 17:24:55
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

cap = cv2.VideoCapture("../test.avi")
while(1):
	# get a frame
	ret, frame = cap.read()
	# show a frame
	cv2.imshow("capture", frame)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows() 

