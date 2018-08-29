import numpy as np
import cv2
import argparse
from skimage.exposure import rescale_intensity


def convolution(image, K):
	(imgH, imgW) = image.shape[:2]
	(kH, kW) = K.shape[:2]

	pad = (kW - 1) // 2
	img = cv2.copyMakeBorder(image, pad, pad, pad, pad, 
		cv2.BORDER_REPLICATE)
	output = np.zeros((imgH, imgW), dtype='float')

	for y in np.arange(pad, imgH + pad):
		for x in np.arange(pad, imgW + pad):
			roi = img[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * K).sum()
			output[y - pad, x - pad] = k

	output = rescale_intensity(output, in_range=(0,255))
	output = (output * 255).astype("uint8")

	return output

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())


#Convolutions kernels
smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype='int')

laplacian = np.array((
	[0, 1, 0],
	[-1, -4, -1],
	[0, 1, 0]), dtype='int')

sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype='int')

sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype='int')

embross = np.array((
	[-2, -1, 0],
	[-1, 1, 1],
	[0, 1, 2]), dtype='int')

kernelBank = (
	("small_Blur", smallBlur),
	("large_Blur", largeBlur),
	("sharpen", sharpen),
	("laplacian", laplacian),
	("sobelX", sobelX),
	("sobelY", sobelY),
	("embross", embross))

img_original = cv2.imread(args["image"])
img_rs = cv2.resize(img_original, (0,0), fx=0.25, fy=0.25) 
img_gray = cv2.cvtColor(img_rs, cv2.COLOR_BGR2GRAY)

for (kerneName, K) in kernelBank:
	print("[INFO] applying {0} kernel".format(kerneName))
	convOutput = convolution(img_gray, K)
	cvOutput = cv2.filter2D(img_gray, -1, K)

	cv2.imshow("Orignal", img_gray)
	cv2.imshow("{0} - convolution".format(kerneName), convOutput)
	cv2.imshow("{0} - opencv".format(kerneName), cvOutput)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

