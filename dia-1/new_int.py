# sacare el segundo numero mas grande
entrada = [4, 8, 2, 10, 6]

def second_biggest(lista):
    mayor = lista[0]
    segundo = lista[1]

    if segundo > mayor:
        mayor, segundo = segundo, mayor

    for numero in lista[2:]:
        if numero > mayor:
            segundo = mayor
            mayor = numero
        elif numero > segundo and numero != mayor:
            segundo = numero

    return segundo

print(second_biggest(entrada))

# Dada una lista de números y un número objetivo, escribe una función que indique si ese número está dentro de la lista.

lista = [3, 7, 2, 9, 1]

def find_number(list, n):
    
    for number in list:
        if number == n:
            return True, list.index(n)
    return False
print(find_number(lista, 1))

# Dado un número entero positivo, escribe una función que sume todos sus dígitos.

def add_all_numbers(number):
    suma = 0
    number = str(number)
    for digit in number:
        suma =suma + int(digit)
    return suma
print(add_all_numbers(123))

# contar vocales
def contar_vocales(palabra):
    conteo = 0
    vocales = "aeiouAEIOU"
    for letra in palabra:
        if letra in vocales:
            conteo += 1
    return conteo
print (contar_vocales("hola mundo"))

# Dada una lista de números, devuelve una nueva lista sin elementos repetidos
numeros = [1, 2, 2, 3, 4, 4, 5]
def erase_duplicates(list):
    clean_list = []
    for number in list:
            if number not in clean_list:
               clean_list.append(number)
    return clean_list
   
print(erase_duplicates(numeros))
