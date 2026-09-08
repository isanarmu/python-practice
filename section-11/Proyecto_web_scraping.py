from bs4 import BeautifulSoup
import requests

resultado = requests.get('https://books.toscrape.com/')
sopa = BeautifulSoup(resultado.text, 'lxml')

for numero_pagina in range(1, 51):
    url = f'https://books.toscrape.com/catalogue/page-{numero_pagina}.html'
    print(url)