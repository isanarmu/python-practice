def calcular_cuadrado(n):
    return n ** 2
print(calcular_cuadrado(5)) 

def count_digits(n):
    return len(str(n))
print(count_digits(12345))

def partir_numero(texto_numero, posicion):
    posicion = len(texto_numero) // 2
    izquierda = texto_numero[:posicion]
    derecha = texto_numero[posicion:]
    suma = int(izquierda) + int(derecha)
    return suma
print(partir_numero("1234", 2))

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
  
  cuadrado = n ** 2
  cuadrado_str = str(cuadrado)
  
  for num in range(1, len(cuadrado_str)):
    izquierda = cuadrado_str[:num]
    derecha = cuadrado_str[num:]
    if izquierda != 0 and derecha != 0:
      if int(izquierda) + int(derecha) == n:
        return True
  
  return False

print(is_kaprekar(2))


# Escribe una función que reciba una lista de números y devuelva una nueva
#  lista donde cada elemento sea la suma de todos los anteriores más él mismo.
def suma(list):
   result = []
   suma_total = 0
   for number in list:
      a = number
      b = suma_total
      siguiente = b + a
      suma_total = siguiente
      result.append(siguiente)
   return result

print(suma([1, 2, 3, 4]))