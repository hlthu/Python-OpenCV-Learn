import cv2  
import numpy as np  
  
img = cv2.imread("./cat.png")  
emptyImage = np.zeros(img.shape, np.uint8)  
emptyImage2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
  
cv2.imshow("EmptyImage", emptyImage)  
cv2.imshow("Image", img)  
cv2.imshow("EmptyImage2", emptyImage2)   
 
cv2.waitKey (0)  
cv2.destroyAllWindows()  
