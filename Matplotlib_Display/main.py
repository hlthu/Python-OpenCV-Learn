# created by Huang Lu
# 27/08/2016 16:05:20
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np
import matplotlib.pyplot as plot

# test for a gray image
img1 = cv2.imread("test1.jpg")
# using opencv
cv2.imshow("Gray(opencv)", img1)
# using matplotlib
plot.imshow(img1)
plot.show()

# test for a color image
img2 = cv2.imread("test2.jpg")
b, g, r = cv2.split(img2)
img2_c = cv2.merge([r, g, b])
# using opencv
cv2.imshow("Color(opencv, img2)", img2)
cv2.imshow("Color(opencv, img2_c)", img2_c)
# using matplotlib
plot.subplot(121);plot.imshow(img2)
plot.subplot(122);plot.imshow(img2_c)
plot.show()

cv2.waitKey(0)    
cv2.destroyAllWindows() 
