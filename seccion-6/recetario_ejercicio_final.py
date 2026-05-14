from pathlib import Path


# crear una ruta para las categorias donde el usuario elige una seccion
def elegir_categoria(carpeta):
    categorias = []
    for elemento in carpeta.iterdir():
        if elemento.is_dir():
            categorias.append(elemento.name)
    for numero, categoria in enumerate(categorias, start=1):
        print(f"{numero} - {categoria}")

    eleccion = int(input("Elige una categoria: "))
    categoria_elegida = categorias[eleccion - 1]

    return categoria_elegida


carpeta = Path(r"C:\Users\Irene\Desktop\Recetas")
print("Bienvenido, estas son nuestras recetas ")

categoria_elegida = elegir_categoria(carpeta)
print(f"Elegista {categoria_elegida.upper()}")

# crear una ruta para las recetas donde el usuario ve la receta

ruta_categoria = carpeta / categoria_elegida

def elegir_receta(carpeta_elegida):
    recetas = []
    for archivo in carpeta_elegida.iterdir():
        if archivo.is_file() and archivo.suffix == ".txt":
            recetas.append(archivo.name)
    for numero, receta in enumerate(recetas, start=1):
        print(f"{numero} - {receta}")
    eleccion_receta = int(input("Elige una receta: "))
    receta_elegida = recetas[eleccion_receta - 1]

    return receta_elegida

def leer_receta(ruta_receta):
    archivo = open(ruta_receta, "r")
    print(archivo.read())
    archivo.close()

receta_elegida = elegir_receta(ruta_categoria)
ruta_receta = ruta_categoria / receta_elegida

