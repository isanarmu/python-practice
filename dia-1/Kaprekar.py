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
    cuadrado_str = str(cuadrado)
    if (len(cuadrado_str) == 1):
        cuadrado_str = "0" + cuadrado_str
    mitad = len(cuadrado_str) // 2
    izquierda = cuadrado_str[:mitad]
    derecha = cuadrado_str[mitad:]
    suma = int(izquierda) + int(derecha)
    return suma == n
print(es_kaprekar(9))
    
def is_kaprekar(n):
    if n == 1:
        return True
    # calculamos el cuadrado y lo convertimos a texto
    squared = n ** 2
    squared_str = str(squared)
    if len(squared_str) == 1:
        squared_str = "0" + squared_str
    # Paso 3: Buscamos la mitad de la palabra
    mitad = len(squared_str) // 2 
    # Paso 4: Cortamos con tijeras el texto por la mitad
    trozo_izquierdo = squared_str[:mitad]
    trozo_derecho = squared_str[mitad:]
    # Paso 5: Convertimos los trozos de nuevo a números y los sumamos
    suma = int(trozo_izquierdo) + int(trozo_derecho)
    # Paso 6: Comprobamos si la suma de los trozos da el número original
    return suma == n
print(is_kaprekar(9)) 