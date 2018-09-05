# Fundamentos da imagem digital em Python

## Daniel Tiezzi
 
 A imagem é formada por inúmeros pontos denominados de pixel. Ou seja, o pixel é a unidade fundamental da imagem. Cada pixel é representado por um valor numérico, e quanto maior o valor maior a intensidade da luz que aparece naquele exato local. Para a formação de uma imagem como uma simples fotografia, são necessários milhares de pixels. A Figura 1 é uma fotografia com 1280 x 960 pixels. Ou seja, para a criação dessa imagem foi utilizado mais de 1 milhão de pixels.
 
### Figura 1. Essa imagem é 1280 x 960 com um total de 1228800 pixels.
 
 ![aparecida](http://143.107.196.146:3000/aparecida.jpeg)
 
 Existem diversos meios de acessar as características de uma imagem. Utilizando o Python, podemos lançar mão mão da biblioteca OpenCv. A OpenCV é uma ferramenta extremamente poderosa para manipular imagens e de grande importância para *deep learning* aplicado à imagens. Vamos ver um exemplo de como acessar e verificar as características da imagem acima:
 
 ```python
 import cv2
 
 img = cv2.imread('/Users/dtiezzi/Documents/AI/aparecida.jpeg')
 print(img.shape)
 
 ```
 
 Abaixo o retorno do código:
 
 	(960, 1280, 3)
 
 
 Veja que temos 1280 (eixo x, ou largura da imagem) e 960 (eixo y, ou altura da imagem). Adicionalmente temos o valor `3`. Imagens são matrizes multidimensionais. Neste caso, uma matriz com 3 dimensões, x, y e z. Neste caso, a imagem em cores é representada por uma combinação de 3 matrizes que chamamos de RGB. `R` de 'red' (vermelho), `G` de 'green' (verde) e `B` de 'blue' (azul). Nós podemos separar essas matrizes para temos uma melhor idéia de como ela funciona. Como estamos utilizando a biblioteca OpenCV para python, vamos ver que ela extrai as matrizes em BGR, ou seja, o inverso:
 
 ```python
 b = img.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

g = img.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = img.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

# RGB - Blue
cv2.imwrite('b_channel.png', b)
cv2.imshow('b', b) 
cv2.waitKey(0)
cv2.destroyAllWindows()
# RGB - Green
cv2.imwrite('_channel.png', g)
cv2.imshow('g', g) 
cv2.waitKey(0)
cv2.destroyAllWindows()
# RGB - Red
cv2.imwrite('r_channel.png', r)
cv2.imshow('r', r) 
cv2.waitKey(0)
cv2.destroyAllWindows()

 ```
 As imagens salvas serão as seguintes:
 
 **Blue**
 
 ![aparecidaB](http://143.107.196.146:3000/bChannelSmall.png)
 
 **Green**
 
 ![aparecidaG](http://143.107.196.146:3000/gChannelSmall.png)
 
 **Red**
 
 ![aparecidaG](http://143.107.196.146:3000/rChannelSmall.png)
 
 A sobreposição das matrizes forma a imagem final. E como são formadas essas matrizes? Elas são matrizes numéricas e representadas por valores que vão de 0 a 255. Quanto maior o valor, maior a intensidade daquela cor em um determinado pixel. Por exemplo, um pixel com os valores `(0, 0, 0)` representa a ausência de cor, que seria o preto. O valor `(255, 0, 0)`, seria o vermelho, o `(0, 255, 0)` verde e `(0, 0, 255)` azul. Assim, o `(255, 255, 255)` é o branco. Desta forma, um total de 16.777.216 combinações são possíveis e podem geram todo o espectro de color que o cérebro humano consegue entender. As cores em RGB também podem ser demonstradas em hexadecimal. São necessários somente dois caracteres para representar os valores de 0 a 255 em hexadecimal, sendo '00 = 0' 3 'FF = 255'. Desta forma, o valor `#FF0000` representa a cor vermelha. Existem outros esquemas de representação de cores como a HSV (Hue, Saturation, Lightness) ou a CMYK (Cyan, Magenta, Yellow, Key/Black) entre outros. [Clique aqui para acessar uma ferramenta *online*](http://colorizer.org).
 E como podemos acessar o valor de cada pixel? As matrizes são indexadas. Em Python, a indexação sempre começa em `0`. Então vamos ver a imagem abaixo:
 
  ![matrix](http://143.107.196.146:3000/matrix.png)
  
 Temos uma imagem com 64 pixels (8, 8, 1) para representar a letra `I`. Veja que temos os índices para as colunas `x` e as linhas `y`. Desta forma, a coordenada da matriz (4, 5) acessa o pixel da coluna de índice `x = 4` e a linha `y = 5`. A matriz da esquerda representa o valor de cada pixel que para `(4, 5) = 0`, que representa a cor preta. Em uma matriz multidimensional de uma imagem colorida teremos três valores para cada pixel. Cada valor representa a cor na escala RGB (ou BGR para o OpenCV). O OpenCV e outras bibliotecas de processamento de imagem como scikit-image para Python representam imagens RGB com uma matriz multidimensional da biblioteca NumPy (*NumPy arrays*). *NumPy arrays* são representados pela `(altura, largura, profundidade)`. Os Para exemplificar vamos acessar um pixel da imagem anterior:
 
 ```python
 print(img.shape)
 
 (b, g, r) = img[175, 225]
 print('Os valores em BGR são: {0}, {1}, {2}.'.format(b, g, r))
 print('O valor de azul é {0}.'.format(img[175, 225, 0]))
 print('O valor de verde é {0}.'.format(img[175, 225, 1]))
 print('O valor de vermelho é {0}.'.format(img[175, 225, 2]))
 ```
 O retorno deste código será:
 
 	Os valores em BGR são: 228, 182, 135.
 	O valor de azul é 228.
 	O valor de verde é 182.
 	O valor de vermelho é 135.
 	
 Podemos também extrair a matriz em escala de cinzas:
 
 ```python
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('aparecida_gray.png', img_gray)
print('O valor em escala de cinza é {0}.'.format(img_gray[175, 225]))
cv2.imshow('gray_image',img_gray) 
cv2.waitKey(0)
cv2.destroyAllWindows()
 ```
	O valor em escala de cinza é 173.

 **A imagem em escala de cinza.**
 
 ![aparecidaGray](http://143.107.196.146:3000/aparecida_gray.png)
 
 Agora, para finalizar, vamos fazer um subset da imagem e colocar uns pontos vermelhos em locais específicos:
 
 
 ```python
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
 ```
  
**A imagem recortada com a 'fumaça' vermelha**

![aparecidaGray](http://143.107.196.146:3000/aparecida_cropped1.png)
