# Juan Rivera Vargas

#Notas importantes del codigo
#1No pongan palabras reservadas
#en el nombre del archivo
#2No poner cosas como acentos o enies
#3Python no usa llaves, en su lugar
#se usan identaciones de 4 espacios
#4En TODO un archivo solo usar o
#tabulaciones o 4 espacios
#5Las fotos deben estar en la misma
#carpeta que el codigo

import cv2
import numpy as np
from matplotlib import pyplot as plt
#255 blanco
#0 negro 

img = cv2.imread('tree_1.jpg',0) #el cero es en escala de grises

#Bajo un valor umbral muestra los grises originales
#y lo demas a 255
ret,thresh1 = cv2.threshold(img,135,255,cv2.THRESH_TRUNC)

#Valor umbral y tonalidad maxima
ret,thresh2 = cv2.threshold(img,140,255,cv2.THRESH_BINARY)


titles = ['Original','TRUNC','BINARY']
images = [img, thresh1, thresh2]
miArray = np.arange(3)
for i in miArray:
	plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
 
plt.show()