from bs4 import BeautifulSoup
import requests

resultado = requests.get('https://irenes-portfolio.vercel.app/about')
sopa = BeautifulSoup(resultado.text, 'lxml')

print(sopa.select(('title')))