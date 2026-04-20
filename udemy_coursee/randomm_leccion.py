from random import *

aleatorio = randint(1, 5)
print(aleatorio)

print("---------------------------")
aleatorio = uniform(1, 5) 
redondeado = round(aleatorio)
print(f"Numero aleatorio con decimales: {aleatorio}")
print(f"Numero aleatorio redondeado: {redondeado}")

print("---------------------------")

num_al = random()
print(f"Numero aleatorio entre 0 y 1: {num_al}")

print("------------elegir aleatorio de una lista---------------")

colores = ['auzul', 'rojo', 'amarillo']

elegir_aleatorio = choice(colores)
print(elegir_aleatorio)


print("-------------mezclar--------------")

numeros = list(range(5, 50))
mezclar = shuffle(numeros)
print(numeros)

