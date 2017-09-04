import cv2
import numpy

# add n salt noise to an image
def salt(img, n):
	for k in range(n):
		i = int(numpy.random.random() * img.shape[1])
		j = int(numpy.random.random() * img.shape[0])
		if img.ndim == 2:
			img[j, i] = 255
		elif img.ndim == 3:
			img[j, i, 0] = 255
			img[j, i, 1] = 255
			img[j, i, 2] = 255
	return img

if __name__ == '__main__':
	img = cv2.imread("test.png")
	saltImage = salt(img, 1000)
	cv2.imshow("salt", saltImage)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

