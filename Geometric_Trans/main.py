# created by Huang Lu
# 2016/8/26 17:35
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

# read the original
img = cv2.imread('../test2.jpg')
cv2.imshow('original', img)

# expand
rows, cols, channels = img.shape
img_ex = cv2.resize(img, (2*cols, 2*rows), interpolation=cv2.INTER_CUBIC)
cv2.imshow('expand', img_ex)

# zoom
img_zo = cv2.resize(img, (cols/2, rows/2), interpolation=cv2.INTER_AREA)
cv2.imshow('zoom', img_zo)

# trans
M = np.array([[1, 0, 50],[0, 1, 50]], np.float32)
img_tr =cv2.warpAffine(img, M, img.shape[:2])
cv2.imshow('trans', img_tr)

# Rotation
M=cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
img_ro =cv2.warpAffine(img, M, img.shape[:2])
cv2.imshow('rotation', img_ro)

# wait the key and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
