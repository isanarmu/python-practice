# def calcular_cuadrado(n):
#     return n ** 2
# print(calcular_cuadrado(5)) 

# def count_digits(n):
#     return len(str(n))
# print(count_digits(12345))

# def partir_numero(texto_numero, posicion):
#     posicion = len(texto_numero) // 2
#     izquierda = texto_numero[:posicion]
#     derecha = texto_numero[posicion:]
#     suma = int(izquierda) + int(derecha)
#     return suma
# print(partir_numero("1234", 2))

def es_kaprekar(n):
    if n == 1:
        return True
    cuadrado = n ** 2
    cuadrado = str(cuadrado)
    if (len(cuadrado) == 1):
        cuadrado = "0" + cuadrado
    mitad = len(cuadrado) // 2
    izquierda = cuadrado[:mitad]
    derecha = cuadrado[mitad:]
    suma = int(izquierda) + int(derecha)
    return suma == n
print(es_kaprekar(81))
    