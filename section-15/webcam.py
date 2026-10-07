from deepface import DeepFace
import cv2
from deepface.modules.exceptions import FaceNotDetected

camara = cv2.VideoCapture(0)

print("Mira de frente a la cámara. Pulsa ESPACIO para hacer la foto.")

exito = False

while True:
    leido, frame = camara.read()

    if not leido:
        print("No se pudo leer la cámara.")
        break

    cv2.imshow('Vista previa', frame)
    tecla = cv2.waitKey(1) & 0xFF

    if tecla == 32:  # ESPACIO
        exito = True
        break
    elif tecla == 27:  # ESC para cancelar
        break

camara.release()
cv2.destroyAllWindows()

if exito:
    cv2.imwrite('captura.jpg', frame)

    try:
        resultado = DeepFace.verify(
            img1_path='captura.jpg',
            img2_path='section-15/cara2.jpg'
        )

        if resultado['verified']:
            texto = 'Irene'
            color = (0, 255, 0)
        else:
            texto = 'No coinciden'
            color = (0, 0, 255)

    except ValueError as error:
        if not isinstance(error.__cause__, FaceNotDetected):
            raise

        texto = 'No se detecto una cara'
        color = (0, 0, 255)
        print("No se pudo detectar una cara. Prueba otra captura.")

    cv2.putText(
        frame,
        texto,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    cv2.imshow('Resultado', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()