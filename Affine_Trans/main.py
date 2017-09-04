# created by Huang Lu
# 18/09/2016 23:35:37    
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

img = cv2.imread('test.png')
rows, cols, chanels = img.shape

# get three points in the original image and transformed image
pt1 = np.float32([[50,50],[200,50],[50,200]])
pt2 = np.float32([[10,100],[200,50],[100,250]])

# get the transformation matrix
M = cv2.getAffineTransform(pt1, pt2)

# output
out = cv2.warpAffine(img, M, (cols, rows))

# display
cv2.imshow("input", img)
cv2.imshow("output", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
