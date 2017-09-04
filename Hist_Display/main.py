# created by Huang Lu
# 2016/8/26 17:35
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

# get the hist graph of a gray image
def HistGraphGray(image, color):    
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])       
    histGraph = np.zeros([256,256,3], np.uint8)
    m = max(hist)
    hist = hist * 220 / m
    for h in range(256): 
       	n = int(hist[h])
        cv2.line(histGraph,(h,255), (h,255-n), color)        
    return histGraph; 
  
# get the hist graph of a color image
def HistGraphColor(image):
	histGraph = np.zeros([256,256,3], np.uint8)
	colorBlue = [255, 0, 0]
	colorGreen = [0, 255, 0]
	colorRed = [0, 0, 255]
	b, g, r = cv2.split(image)
	bhist = cv2.calcHist([b], [0], None, [256], [0.0,255.0])
	ghist = cv2.calcHist([g], [0], None, [256], [0.0,255.0]) 
	rhist = cv2.calcHist([r], [0], None, [256], [0.0,255.0])
	bm = max(bhist)
	gm = max(ghist)
	rm = max(rhist)
	bhist = bhist * 220 / bm
	rhist = rhist * 220 / rm
	ghist = ghist * 220 / gm
	for h in range(256):
		bn = int(bhist[h])
		gn = int(ghist[h])
		rn = int(rhist[h])
		if h != 0:
			cv2.line(histGraph,(h-1,255-bStart), (h,255-bn), colorBlue)
			cv2.line(histGraph,(h-1,255-gStart), (h,255-gn), colorGreen)
			cv2.line(histGraph,(h-1,255-rStart), (h,255-rn), colorRed)
		bStart = bn
		gStart = gn
		rStart = rn
	return histGraph

# main fuction
if __name__ == '__main__':
	# test for a gray image
	img1 = cv2.imread("test1.jpg", 0)
	color = [255, 255, 255]
	histGraph1 = HistGraphGray(img1, color)
	cv2.imshow("Hist Gray", histGraph1)

	# test for a color image
	img2 = cv2.imread("test2.jpg")
	# first tset for three channels
	colorRed = [0, 0, 255]
	colorGreen = [0, 255, 0]
	colorBlue = [255, 0, 0]
	b, g, r = cv2.split(img2)
	# blue channel
	bhistGraph = HistGraphGray(b, colorBlue)
	cv2.imshow("Hist Blue", bhistGraph)
	# green channel
	ghistGraph = HistGraphGray(g, colorGreen)
	cv2.imshow("Hist Green", ghistGraph)
	# red channel
	rhistGraph = HistGraphGray(r, colorRed)
	cv2.imshow("Hist Red", rhistGraph)
	# get three channels together
	histGraph2 = HistGraphColor(img2)
	cv2.imshow("Hist Color", histGraph2)
	cv2.waitKey(0)    
	cv2.destroyAllWindows() 
