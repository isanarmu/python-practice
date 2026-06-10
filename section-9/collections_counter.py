from collections import Counter, defaultdict

numeros = [1, 2, 32, 5, 4, 5,55,87,7, 7, 56]
print(Counter(numeros))
print(Counter("hhoohhlla"))

mi_diccionario = defaultdict(lambda: "Valor no hallado")

mi_diccionario["edad"] = 44
print(mi_diccionario)

from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

print(lista_ciudades)