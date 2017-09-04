# created by Huang Lu
# 27/08/2016 17:59:31  
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

# empty image
img = np.zeros((512, 512, 3), np.uint8)

# draw a line
cv2.line(img, (0,0), (511,511), (255, 0, 0), 10)

# draw a rectangle
cv2.rectangle(img, (0,0), (255,255), (0, 255, 0), 5)

# draw a circle
cv2.circle(img, (255, 255), 127, (0, 0, 255), 8)

# draw a ellipse
cv2.ellipse(img, (255, 255), (150, 75), 0, 0, 360, (0, 255, 255), 1)

# add text
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

# show image
cv2.imshow("shape", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
