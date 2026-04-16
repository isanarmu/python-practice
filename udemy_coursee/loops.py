mi_lista = ["a", "b", "c"]

for letra in mi_lista:
    numeros_letra = mi_lista.index(letra)
    print(f"la letra es {letra} y su indice es {numeros_letra}")


otra_lista = ["Pablo", "Pepe", "lola", "Brunno"]

for nombre in otra_lista:
    if nombre.startswith("B"):
        print(nombre)
    else:
        print("este nombre no empieza con b")

numeros = [1, 2, 3]
valor = 0
for numero in numeros:
    valor = valor + numero

    print(valor)

palabra = "python"

for letra in palabra:
    print(letra)

for a, b in [[1, 2], ["A", "X"]]:
    print(f"a = {a}")
    print(f"b = {b}")

dic = {"clave1": "A", "clave2": "B"}

for item, itam in dic:
    print(item, itam)