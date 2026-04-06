# Ejercicio 1 – Tic Toc
def tic_toc(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("TicToc")
        elif i % 3 == 90:
            print ("Tic")
        elif i % 5 == 0:
            print("Toc")
        else:
            print(i)

tic_toc(100)    

# Ejercicio 2 – Palíndromo ----------------------------

def es_palindromo(word):
    word = word.lower() # Ignorar mayúsculas
    word = ''.join(word.split()) # Ignorar espacios
    word = ''.join(char for char in word if char.isalnum()) # Ignorar signos de puntuación. Char es una variable temporal que representa cada caracter en la palabra. 
    left = 0
    right = len(word) -1
    
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
        
    return True
print(es_palindromo("Anita lava la tina"))

# Ejercicio 4 – Números de Kaprekar  --------------------------
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
print(is_kaprekar(2)) 

# Ejercicio 5 – Limpiar números de teléfono ------------------------
mis_telefonos = ["612-345-678", "34 600 000 000", "+34 (654) 321"]

def limpiar_telefonos(lista_telefonos, codigo_pais):
    resultado = []
    for telefono in lista_telefonos:
        # 1. Limpiamos el teléfono: dejamos solo los números
        telefono_limpio = ""
        for caracter in telefono:
            if caracter.isdigit(): # ¿Es un número del 0 al 9?
                telefono_limpio += caracter   
        # 2. Comprobamos si ya empieza por el código del país
        if not telefono_limpio.startswith(codigo_pais):
            # Si no lo tiene, se lo pegamos delante
            telefono_limpio = codigo_pais + telefono_limpio
        # 3. Lo guardamos en nuestra lista final
        resultado.append(telefono_limpio)

    return resultado

print(limpiar_telefonos(mis_telefonos, "34"))

# EJ 6 crear una funcion que reciba una lista de números y devuelva una nueva lista con solo los números pares
pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def only_even_n(numebrs):
    return [num for num in numebrs if num % 2 == 0]
print(only_even_n(pares))


# Ejercicio 7 – Contar letras Crea una función que reciba una palabra y devuelva cuántas veces aparece cada letra. contar_letras('casa')

def contar_letras(texto):
    conteo = {} # Creamos un diccionario vacío para almacenar el conteo de letras
    for letra in texto:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    return conteo
print(contar_letras("casa"))

# contar vocales. Crea una función que reciba una palabra y devuelva cuántas vocales tiene.
def contar_vocales(text):
    vocales = "aeiouAEIOU"
    conteo = 0
    for letra in text:
        if letra in vocales:
            conteo += 1
    return conteo
print(contar_vocales("casa"))

# Ejercicio – Filtrar mayores de edad
users = [
    {"name": "Ana", "age": 20},
    {"name": "Luis", "age": 17},
    {"name": "Marta", "age": 25}
]

def older_filter(users):
    return [user for user in users if user["age"] >= 18]
print(older_filter(users))


# Ejercicio 6 – Número más grande Dada una lista de números, devuelve el número más grande sin usar max().

numeros = [3, 7, 2, 9, 5]
def bigger_number(numebrs):
    if not numebrs:
        return None
    maximo = numebrs[0]
    for numero in numebrs:
        if numero > maximo:
            maximo = numero
    return maximo
print(bigger_number(numeros))

# ej 7 
def numeros_enteros(n1, n2):
    result = n1 * n2
    if result <= 1000:
        return result
    return n1 + n2
print(numeros_enteros(2000, 1))

# ej 8 dar vuelta a una palabra
def palabra(str):
    return str[::-1]
print(palabra("hola"))

# ej 9 encontrar el número más grande y el más pequeño de una lista de números
nums = [45, 2, 89, 12, 7]
def find_extremes(n_list):
    n1 = max(n_list)
    n2 = min(n_list)
    return n1, n2

result = find_extremes(nums)

print("El numero mas grande es:", result[0])
print("El numero mas pequeño es:", result[1])

# ej 10 borrar duplicados
data = [1, 2, 2, 3, 4, 4, 4, 5]
def erase(n):
    return list(set(n))
print(erase(data))
# ahroa sin set
def erase(n):
    unicos = []
    for num in n:
        if num not in unicos:
            unicos.append(num)
    return unicos
print(erase(data))

# ej 11 clase con atributos para arrancar un coche
class Car:
    def __init__(self, marca, modelo, año):
        self.marca= marca
        self.modelo = modelo
        self.año = año
    def start_engine(self):
        return f"The {self.año} {self.modelo} {self.marca} engine is now running!"
my_car = Car("Toyota", "Auris", 1999)
print(my_car.start_engine()) 

def fibonacci(n):
  list_of_numbers = []
  a = 1
  b = 1
  
  for num in range(n):
    list_of_numbers.append(a)
    siguiente = a + b
    a = b
    b = siguiente
  return list_of_numbers
print(fibonacci(15))

