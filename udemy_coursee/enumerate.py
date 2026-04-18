mi_lista = ["a", "b", "c"]
indice = 0 

for item in mi_lista:
    print(indice, item)
    indice = indice + 1

print("--------------------lo mismo que arriba pero con enumerate----------------------------")
lista = ["a", "b", "c"]

for item in enumerate(lista):
    print(item)

for indice, item in enumerate(lista):
    print(indice, item)

enumerate(range(50, 54))
print("----------------------------other--------------------indice--------------")

lsita = ["a", "b", "c"]

mis_elementos = list(enumerate(lsita))
print(mis_elementos[1][1])