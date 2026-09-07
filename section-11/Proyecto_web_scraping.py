from bs4 import BeautifulSoup
import requests

resultado = requests.get('https://books.toscrape.com/')
sopa = BeautifulSoup(resultado.text, 'lxml')