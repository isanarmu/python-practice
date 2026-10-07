from deepface import DeepFace
import cv2


camara = cv2.VideoCapture(0)

camara.read()
exito, frame = camara.read()

camara.release()

if exito:
    cv2.imwrite('captura.jpg', frame)
    resultado = DeepFace.verify(img1_path='captura.jpg', img2_path='section-15/cara2.jpg')