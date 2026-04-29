from random import *


lista_cafes = [("capuchino", 2.30), ("latte", 2.80), ("espresso", 1.50), ("mocha", 3.20), ("americano", 2.00), ("flat white", 3.00), ("macchiato", 2.40)]

# for elemento, precio in lista_cafes:
#     print(elemento)

# print("------------------------probando---------------------")

def encontrar_mas_caro(lista):
    precio_mayor = 0
    nombre_cafe_mas_caro = ""

    for nombre, precio in lista:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe_mas_caro = nombre
    return nombre_cafe_mas_caro, precio_mayor
cafe, precio = encontrar_mas_caro(lista_cafes)
    # return (f"el cafe mas caro es {nombre_cafe_mas_caro} y su precio {precio_mayor}€")
print(f"el cafe mas caro es {cafe} y su precio {precio}€")

print("------------------------ejercicio palitos---------------------")



# lista inicial
palitos = ["-", "--", "---", "-----"]
# mezclar palitos
def mezclar(lista):
    shuffle(palitos)
    return lista


# pedir al usuario qeu elija palito

def probar_suerte():
    intento = ""
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

# comprobar el intento del usuario

def probar_intento(lista, intentoo):
    seleccion_usuario = intentoo - 1
    if lista[seleccion_usuario] == "-":
        print("A lavar los platos!!")
    else:
        print("Te salvaste")

    print(f"Te ha tocado {lista[seleccion_usuario]}")

palitos_mezclados = mezclar(palitos)
numero_elegido = probar_suerte()
probar_intento(palitos_mezclados, numero_elegido)
