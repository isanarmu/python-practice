print("------------------------------------------------------------------------------------")
monedas = 5
while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
else:
    print("no tengo mas monedas")

print("------------------------------------------------------------------------------------")
respuesta = "s"

while respuesta == "s":
    respuesta = input("¿quieres continuar? (s/n): ")
else:
    print("Adios")

print("------------------------------------------------------------------------------------")

nombre = input("Escribe tu nombre: ")

for letra in nombre:
    if letra == "n":
        break
    print(letra)

print("------------------------------------------------------------------------------------")
# aqui no imprime la n y continua
nombre = input("Escribe tu nombre: ")

for letra in nombre:
    if letra == "n":
        continue
    print(letra)
print("------------------------------------------------------------------------------------")
number = 0

for num in number:
    number += num
    print(num)