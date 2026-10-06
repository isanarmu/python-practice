from deepface import DeepFace

resultado = DeepFace.verify(img1_path='section-15/cara3.png', img2_path='section-15/cara2.jpg')

for c, v in resultado.items():
    print(f'{c}: {v}')