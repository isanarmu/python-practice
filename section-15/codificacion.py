from deepface import DeepFace

resultado = DeepFace.represent(img_path='section-15/cara1.png')

for k in resultado[0]:
    print(k)