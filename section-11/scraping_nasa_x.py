from bs4 import BeautifulSoup
import requests

url = "https://x.com/NASA"

respuesta = requests.get(url)
sopa = BeautifulSoup(respuesta.text, "lxml")

print(sopa.prettify())