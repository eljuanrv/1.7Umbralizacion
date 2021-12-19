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
img = cv2.imread('deg2.jpg',0) #el cero es en escala de grises
#Valor umbral y tonalidad maxima
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#Valor umbral y tonalidad maxima
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#Bajo un valor umbral muestra los grises originales
#y lo demas a 255
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#Sobre un valor umbral muestra los grises originales
#y lo demas a 0
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#Bajo un valor umbral muestra los grises originales
#y lo demas a 0
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
 
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
miArray = np.arange(6)
for i in miArray:
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
 
plt.show()