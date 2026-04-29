from random import *

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
    maximo = max(lista)
    lista.remove(maximo)
    lista_sin = set(lista)
    return lista_sin
lista_reducida = reducir_lista(lista_numeros)

def promedio(lista):
    media = sum(lista) / len(lista)
    return media

promedio_lista = promedio(lista_reducida)
print(promedio_lista)
