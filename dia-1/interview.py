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


# Ejercicio 2 – Palíndromo

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

# Ejercicio 3 – Filtrar mayores de edad
users = [
    {"name": "Ana", "age": 20},
    {"name": "Luis", "age": 17},
    {"name": "Marta", "age": 25}
]

def older_filter(users):
    return [user for user in users if user["age"] >= 18]
print(older_filter(users))

# Ejercicio 4 – Números de Kaprekar
def is_kaprekar(n):
    if n == 1:
        return True
    # calculamos el cuadrado y lo convertimos a texto
    squared = n ** 2
    squared_str = str(squared)
    # Paso 3: Buscamos la mitad de la palabra
    mitad = len(squared_str) // 2 
    # Paso 4: Cortamos con tijeras el texto por la mitad
    trozo_izquierdo = squared_str[:mitad]
    trozo_derecho = squared_str[mitad:]
    # Paso 5: Convertimos los trozos de nuevo a números y los sumamos
    suma = int(trozo_izquierdo) + int(trozo_derecho)
    # Paso 6: Comprobamos si la suma de los trozos da el número original
    if suma == n:
        return True
    else:
        return False
print(is_kaprekar(2))  # True

# Ejercicio 5 – Limpiar números de teléfono
def limpiar_telefonos(lista_telefonos, codigo_pais):
    resultado = []
    for telefono in lista_telefonos:
        # 1. Limpiamos el teléfono: dejamos solo los números
        telefono_limpio = ""
        for caracter in telefono:
            if caracter.isdigit(): # ¿Es un número del 0 al 9?
                telefono_limpio += caracter   
        # 2. Comprobamos si ya empieza por el código del país
        # (Por ejemplo, si el código es "34")
        if not telefono_limpio.startswith(codigo_pais):
            # Si no lo tiene, se lo pegamos delante
            telefono_limpio = codigo_pais + telefono_limpio
        # 3. Lo guardamos en nuestra lista final
        resultado.append(telefono_limpio)

    return resultado

# Ejemplo de cómo se usaría:
mis_telefonos = ["612-345-678", "34 600 000 000", "+34 (654) 321"]
print(limpiar_telefonos(mis_telefonos, "34"))