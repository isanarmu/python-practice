from random import *
import random

def lanzar_dados():
    resultado_dado_1 = randint(1, 6)
    resultado_dado_2 = randint(1, 6)
    return resultado_dado_1, resultado_dado_2

def evaluar_jugada(dado_1, dado_2):
    suma_dados = int(dado_1 + dado_2)
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados <10 and suma_dados > 6:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

lanzar_1, lanzar_2 = lanzar_dados()
evaluar_jugada(lanzar_1, lanzar_2)



print("----------------------------sacar numeros repetidos----------")

lista_numeros = [1,2,3,2,2,5]
def reducir_lista(lista):
    lista.remove(max(lista))
    lista_sin = list(set(lista))
    return lista_sin
lista_reducida = reducir_lista(lista_numeros)

def promedio(lista):
    media = sum(lista) / len(lista)
    return media

promedio_lista = promedio(lista_reducida)
print(promedio_lista)

print("----------------------------cara o----------")

lista_numeros = [1,2,3,2,5]

def lanzar_moneda():
    opciones = ["Cara", "Cruz"]
    resultado = random.choice(opciones)
    return resultado

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        lista.clear()
        print("La lista se autodestruirá")
        return lista
    return f"La lista fue salvada {lista}"

moneda = lanzar_moneda()

print(probar_suerte(moneda, lista_numeros))