mi_lista = ["a", "b", "c"]

for letra in mi_lista:
    numeros_letra = mi_lista.index(letra)
    print(f"la letra es {letra} y su indice es {numeros_letra}")


# otra_lista = ["Pablo", "Pepe", "lola", "Brunno"]

# for nombre in otra_lista:
#     if nombre.startswith("B"):
#         print(nombre)
#     else:
#         print("este nombre no empieza con b")


otra_lista = ["Lola, Pepe, Brunno"]

for nombre in otra_lista:
    if nombre.startswith("B"):
        print(nombre)
    else:
        print("este nombre no empieza con b")

