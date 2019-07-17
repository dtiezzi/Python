import cv2 as cv
import numpy as np

im = cv.imread('p1_check.jpg')
print(im.shape)
cv.imshow('im', im)
cv.waitKey(0)
im = (cv.cvtColor(im, cv.COLOR_BGR2GRAY)/255).astype('uint8')
im = cv.resize(im, None, fx=0.2, fy=0.2)
np.savetxt('p1_check.txt', im, fmt='%d')

