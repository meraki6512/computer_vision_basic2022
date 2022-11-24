import numpy as np
import cv2 as cv

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value

img = cv.imread('sample.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print('Image load failed')
    exit()

mean = np.mean(img)
s = 2.0
dst = img.copy()

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        dst[y,x] = saturated(img[y,x] + (img[y,x] - mean) * s)

#cv.imshow('img', img)
cv.imshow('dst', dst)
cv.waitKey()
cv.imwrite('contrast.jpg', dst)



