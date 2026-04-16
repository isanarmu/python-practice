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