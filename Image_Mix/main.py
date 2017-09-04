# created by Huang Lu
# 28/08/2016 13:44:54   
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')

img_mix = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img_mix', img_mix)

cv2.waitKey(0)
cv2.destroyAllWindows()
