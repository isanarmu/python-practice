
def mi_funcion():
    lista = []

    for x in range(1, 5):
        lista.append(x * 10)

    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))

def generar_numeros():
    numero = 1

    while True:
        yield numero
        numero += 1


generador = generar_numeros()
print(next(generador))


def multiplos_siete():
    numero = 7

    while True:
        yield numero
        numero += 7


generador = multiplos_siete()

def perder_vidas():
    vidas = 3

    while vidas > 1:
        yield f"Te quedan {vidas} vidas"
        vidas -= 1

    yield "Te queda 1 vida"
    yield "Game Over"


perder_vida = perder_vidas()
print(next(perder_vida))
print(next(perder_vida))