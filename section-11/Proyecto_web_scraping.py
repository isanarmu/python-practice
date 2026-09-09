from bs4 import BeautifulSoup
import requests

libros_con_cuatro_o_cinco_estrellas = []

for numero_pagina in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{numero_pagina}.html"
    resultado = requests.get(url)
    sopa = BeautifulSoup(resultado.text, 'lxml')

    for libro in sopa.select('article.product_pod'):
        clases_estrellas = libro.select_one('p.star-rating')['class']
        cantidad_estrellas = clases_estrellas[-1]

        if cantidad_estrellas in ('Four', 'Five'):
            titulo = libro.select_one('h3 a')['title']
            libros_con_cuatro_o_cinco_estrellas.append(titulo)

print(libros_con_cuatro_o_cinco_estrellas)