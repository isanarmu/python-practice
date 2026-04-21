palabra = "python" 
lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

print("----------------forma mas eficiente de hacer lo mismo-----------------")

lista = [letra for letra in "python" ]
print(lista)

print("----------------ahroa con numeros y rango-----------------")

numeros = [n for n in range(0, 11, 2)]
numeros_condicion_1 = [n for n in range(0, 11, 2) if n  * 2 > 10]
numeros_condicion = [n if n * 2 > 10 else "NO" for n in range(0, 11, 2)]
print(numeros)
print(numeros_condicion_1)
print(numeros_condicion)

print("-----------------------ejercicio de pies a metros-------------------------")

pies = [10, 12, 20, 55]
metros = [m / 3.281 for m in pies]

print(metros)