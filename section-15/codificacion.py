from deepface import DeepFace

resultado = DeepFace.represent(img_path='section-15/cara1.png')

codificacion = resultado[0]['embedding']

