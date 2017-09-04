# created by Huang Lu
# 2016/8/22 23:02
# Depart. of EE, Tsinghua Univ.

import cv2
import numpy

def get_red(img):
	redImg = img[:,:,2]
	return redImg
	
def get_green(img):
	greenImg = img[:,:,1]
	return greenImg
	
def get_blue(img):
	blueImg = img[:,:,0]
	return blueImg
	
if __name__ == '__main__':
	img = cv2.imread("test.png")
	b, g, r = cv2.split(img)
	cv2.imshow("Blue 1", b)
	cv2.imshow("Green 1", g)
	cv2.imshow("Red 1", r)
	b = get_blue(img)
	g = get_green(img)
	r = get_red(img)
	cv2.imshow("Blue 2", b)
	cv2.imshow("Green 2", g)
	cv2.imshow("Red 2", r)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	
	
	
	
