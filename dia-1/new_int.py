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

# # palindromo o anagrama

def anagrama(word1, word2):
    word1 = word1.upper().replace(" ", "")
    word2 = word2.upper().replace(" ", "")
    return sorted(word1) == sorted(word2)
print(anagrama("carmen ", "n em car"))


# clean number telephone
mis_telefonos = ["612-345-678", "34 600 000 000", "+34 (654) 321"]
def limpiar_numeros(lista_telefono, prefijo):
    resultado = []
    for numero in lista_telefono:
        solo_numero = ""
        for caracter in numero:
            if caracter.isdigit():
                solo_numero += caracter
        if not solo_numero.startswith(prefijo):
            solo_numero = prefijo + solo_numero
        resultado.append(solo_numero)
    return resultado

print(limpiar_numeros(mis_telefonos, "34"))

#  EJ 6 crear una funcion que reciba una lista de
#  números y devuelva una nueva lista con solo los números pares
pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def only_even(list):
    lsita_pares = []
    for num in list:
        if num % 2 == 0:
            lsita_pares.append(num)
    return lsita_pares
print(f"this are even:{only_even(pares)}")

# contar letras
def count_letters(text):
    conteo = {}
    for letra in text:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    return conteo
print(count_letters("cassa"))


# Ejercicio – Filtrar mayores de edad
users = [
    {"name": "Ana", "age": 20},
    {"name": "Luis", "age": 17},
    {"name": "Marta", "age": 25}
]
def older_filter(users):
    result = []
    for user in users:
        if user["age"] >= 18:
            result.append(user)
    return result
print(older_filter(users))
        
lisa= [2, 3, 2 ,15 ,5]
def encontrar_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo
print(f"el maximo es: {encontrar_maximo(lisa)}")