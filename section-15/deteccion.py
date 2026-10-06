from deepface import DeepFace
import cv2

caras = DeepFace.extract_faces('section-15/cara1.png')

imagen = cv2.imread('section-15/cara1.png')

area = caras[0]['facial_area']
x = area['x']
y = area['y']
w = area['w']
h = area['h']

cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Cara detectada', imagen)

cv2.waitKey(0)