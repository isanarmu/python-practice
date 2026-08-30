from bs4 import BeautifulSoup
import requests

resultado = requests.get('https://irenes-portfolio.vercel.app/about')
sopa = BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title'))
# para contarlos usaria len(sopa.....)
# para el indice  al final despues de ('h2')[0]

# para buscar con id necesto poenr hastagh

# print(sopa.select('#Introduction'))

for titulo in sopa.select('title'):
    print(titulo.get_text())

# para descargar la imagen

imagen = sopa.select('link[as="image"]')[0]

url_base = "https://irenes-portfolio.vercel.app"
ruta_imagen = imagen.get("href")

print(url_base + ruta_imagen)

imagenes = sopa.select('img')
print(imagenes)

# para descargarlo

imagen = sopa.select('link[as="image"]')[0]
ruta_imagen = imagen.get("href")

url_imagen = url_base + ruta_imagen

respuesta_imagen = requests.get(url_imagen)

archivo = open("imagen_descargada.png", "wb")
archivo.write(respuesta_imagen.content)
archivo.close()

print("Imagen descargada correctamente")