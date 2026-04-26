
for n in range(0, 10):
    print(n)
print("---------------------")
for n in range(5):
    print(n)

print("---------------------")

for n in range(0, 10,2):
    print(n)

print("---------------------")
lista = list(range(1, 11))

print(lista)

print(".--------------------------.")

suma_cuadrados = 0
for n in range(1, 16):
    
    suma_cuadrados = n ** 2
    n = suma_cuadrados
    print(n) 