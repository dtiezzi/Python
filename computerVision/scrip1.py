import cv2
import numpy as np
 
img = cv2.imread('/Users/dtiezzi/Documents/AI/aparecida.jpeg')
print(img.shape)

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

# RGB - Blue
cv2.imwrite('b_channel.png', b)
# RGB - Green
cv2.imwrite('_channel.png', g)
# RGB - Red
cv2.imwrite('r_channel.png', r)
print(img.shape)
 
(b, g, r) = img[175, 225]
print('Os valores em BGR são: {0}, {1}, {2}.'.format(b, g, r))
print('O valor de azul é {0}.'.format(img[175, 225, 0]))
print('O valor de verde é {0}.'.format(img[175, 225, 1]))
print('O valor de vermelho é {0}.'.format(img[175, 225, 2]))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('aparecida_gray.png', img_gray)
print('O valor em escala de cinza é {0}.'.format(img_gray[175, 225]))
cv2.imshow('gray_image',img_gray) 
cv2.waitKey(0)
cv2.destroyAllWindows()

img_subset = img[175:350, 100:300]
red = [0,0,255]
# Converte em escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Faz um subset da imagem
img_subset = img_gray[175:350, 100:300]
#Seleciona pixels com coloração perto do branco
indices = np.where(img_subset>210)

img_subset1 = img[175:350, 100:300]
#substitui os pontos por vermelho
img_subset1[indices[0], indices[1], :] = [0, 0, 255]
cv2.imwrite('aparecida_cropped1.png', img_subset1)

cv2.imshow('crop_image',img_subset1) 
cv2.waitKey(0)
cv2.destroyAllWindows()