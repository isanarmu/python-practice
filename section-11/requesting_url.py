from bs4 import BeautifulSoup
import requests

resultado = requests.get('https://irenes-portfolio.vercel.app/about')
sopa = BeautifulSoup(resultado.text, 'lxml')

# print(sopa.select('title'))
# para contarlos usaria len(sopa.....)
# para el indice  al final despues de ('h2')[0]

# para buscar con id necesto poenr hastagh

print(len(sopa.select('#Introduction')))