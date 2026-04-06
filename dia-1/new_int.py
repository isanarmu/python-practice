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

def summ_all(n):
        
    return len(n)
    
print(summ_all(10))