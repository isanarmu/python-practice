print("---------------------------------------------------------")

def saludar(nombre):
    """
    estafuncion sirve para saludar
    """
    print("Hola " + nombre)
saludar("Brunno")
saludar("THor")

print("---------------------------------------------------------")

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!" )
nombre_persona = "Laura"
bienvenida(nombre_persona)

print("---------------------------------------------------------")


def cuadrado(numero):
    return numero ** 2

print(cuadrado(2))

print("---------------------------------------------------------")

def multiplicar(num1, num2):
    return num1 * num2

reusltado = multiplicar(5, 10)

print(reusltado)

print("---------------------------------------------------------")

def usd_a_eur(valor_usd):
    return valor_usd * 0.90

dolares = 4
print(usd_a_eur(dolares))

print("---------------------------------------------------------")

def invertir_palabra(palabra):
    return palabra[::-1].upper()
word = "Brunno"

print(invertir_palabra(word))