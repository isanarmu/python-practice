print("-----------------------------------------------------------------")

def chequear_3_cifras(n1, n2):
    suma = n1 + n2
    return suma in range(100, 1000)

resultado = chequear_3_cifras(999, 0)
print(resultado)

print("--------------------tiene 3 cifras un numero?---------------------------------------------")

mi_lista = [55, 954, 100]

def chequear_3_cifras(lista):
    lsita_3_cifras = []
    for numero in lista:
        if numero in range(100, 1000):
            lsita_3_cifras.append(numero)
    return lsita_3_cifras

result = chequear_3_cifras(mi_lista)
print(result)

print("---------------------------hay algun numero negatvo?--------------------------------------")

lista_numeros = [1, 5, 59, 7]

def todos_positivos(lista):
    for numero in lista:
        if numero < 0:
            return False
    return True
result = todos_positivos(lista_numeros)
print(result)

print("-----------------------------sumar todos los menores a1000 y mayor que  0------------------------------------")

lista_numeros = [1, 10, 1009]

def suma_menores(lista):
    total = 0
    for numero in lista:
        if numero in range(0, 1000):
            total += numero
    return total

print(suma_menores(lista_numeros))

print("------------------------------contar cantidad numeros pares-----------------------------------")


lista_numeros = [1, 10, 1009, 2,2,2,2,2]

def cantidad_pares(lista):
    total = 0
    for numero in lista:
        if numero % 2 == 0:
            total += 1
    return total
            
print(cantidad_pares(lista_numeros))
