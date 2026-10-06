from deepface import DeepFace
import cv2

caras = DeepFace.extract_faces('section-15/cara1.png')

print(caras)