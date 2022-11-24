import numpy as np
import cv2 as cv

img = cv.imread('sample.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print('Image load failed!')
    exit()

mean = np.mean(img)
dst = img.copy()

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if (img[y,x] < mean):
            dst[y,x] = 0

cv.imwrite('output.jpg', dst)

#print(mean)
#cv.imshow('image', img)
#cv.imshow('output', dst)
#cv.waitKey()



