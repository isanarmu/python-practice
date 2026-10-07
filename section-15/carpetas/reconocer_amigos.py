"""Reconoce las caras de las fotos de pruebas y muestra los resultados."""

from pathlib import Path

import cv2
from deepface import DeepFace
from deepface.modules.exceptions import FaceNotDetected


BASE = Path(__file__).resolve().parent
MODELO = 'VGG-Face'
EXTENSIONES = {'.png', '.jpg', '.jpeg', '.bmp', '.webp'}


def listar_fotos(carpeta):
    if not carpeta.is_dir():
        raise FileNotFoundError(f'No existe la carpeta: {carpeta}')
    return sorted(
        archivo for archivo in carpeta.iterdir()
        if archivo.is_file()
        and archivo.suffix.lower() in EXTENSIONES
        and not archivo.name.startswith('.')
    )


def extraer_caras(imagen):
    try:
        return DeepFace.extract_faces(
            img_path=imagen,
            detector_backend='opencv',
            enforce_detection=True,
            color_face='bgr',
            normalize_face=False,
        )
    except FaceNotDetected:
        return []


def obtener_embedding(cara):
    # La cara ya se ha detectado y alineado; no hay que detectarla otra vez.
    return DeepFace.represent(
        img_path=cara,
        model_name=MODELO,
        detector_backend='skip',
        enforce_detection=False,
    )[0]['embedding']


def cargar_conocidos():
    conocidos = {}
    for archivo in listar_fotos(BASE / 'conocidos'):
        imagen = cv2.imread(str(archivo))
        if imagen is None:
            print(f'No se puede leer {archivo.name}; se omite.')
            continue
        caras = extraer_caras(imagen)
        if len(caras) != 1:
            print(f'{archivo.name}: se necesita exactamente una cara; se omite.')
            continue
        conocidos[archivo.stem] = obtener_embedding(caras[0]['face'])
        print(f'Referencia cargada: {archivo.stem}')
    return conocidos


def reconocer_cara(cara, conocidos):
    embedding = obtener_embedding(cara)
    nombre = 'Desconocido'
    menor_distancia = float('inf')
    for persona, referencia in conocidos.items():
        resultado = DeepFace.verify(
            img1_path=embedding,
            img2_path=referencia,
            model_name=MODELO,
            distance_metric='cosine',
            silent=True,
        )
        if resultado['verified'] and resultado['distance'] < menor_distancia:
            nombre = persona
            menor_distancia = resultado['distance']
    return nombre


def procesar_foto(imagen, conocidos):
    resultado = imagen.copy()
    encontrados = set()
    caras = extraer_caras(imagen)
    for cara in caras:
        nombre = reconocer_cara(cara['face'], conocidos)
        color = (0, 0, 255)
        if nombre != 'Desconocido':
            color = (0, 255, 0)
            encontrados.add(nombre)

        area = cara['facial_area']
        x, y, ancho, alto = area['x'], area['y'], area['w'], area['h']
        cv2.rectangle(resultado, (x, y), (x + ancho, y + alto), color, 2)
        cv2.putText(
            resultado, nombre, (x, max(20, y - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2,
        )
    if not caras:
        print('  No se detectaron caras en esta foto.')
    return resultado, encontrados


def main():
    carpeta_resultados = BASE / 'resultados'
    carpeta_resultados.mkdir(exist_ok=True)
    conocidos = cargar_conocidos()
    if not conocidos:
        print('No hay referencias con una cara detectable en conocidos.')
        return

    total = 0
    personas_encontradas = set()
    try:
        for archivo in listar_fotos(BASE / 'pruebas'):
            imagen = cv2.imread(str(archivo))
            if imagen is None:
                print(f'No se puede leer {archivo.name}; se omite.')
                continue
            print(f'Analizando {archivo.name}...')
            resultado, encontrados = procesar_foto(imagen, conocidos)
            destino = carpeta_resultados / archivo.name
            if not cv2.imwrite(str(destino), resultado):
                raise OSError(f'No se pudo guardar el resultado: {destino}')
            print(f'  Resultado guardado: {destino.name}')
            total += 1
            personas_encontradas.update(encontrados)

            # Ajusta las fotos grandes para que entren en la pantalla.
            alto, ancho = resultado.shape[:2]
            escala = min(1.0, 1200 / ancho, 800 / alto)
            if escala < 1:
                resultado = cv2.resize(
                    resultado, (int(ancho * escala), int(alto * escala))
                )
            cv2.imshow('Reconocer amigos', resultado)
            print('Pulsa una tecla para pasar a la siguiente foto.')
            cv2.waitKey(0)
    finally:
        cv2.destroyAllWindows()

    print(f'\nFotos analizadas en total: {total}')
    print(f'Personas conocidas distintas encontradas: {len(personas_encontradas)}')
    if personas_encontradas:
        print('Nombres: ' + ', '.join(sorted(personas_encontradas)))


if __name__ == '__main__':
    main()
