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
# bucle del 10 al 0 con un while
numero = 10

while numero >= 0: 
     print(numero)
     numero -= 1

print("---------------------------------multiplos 5 en serie 50---------------------------------------------------")
# solo imprimir los multiplos de 5 desde 50 hasta 0
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero = numero - 1

print("-------------------------------------interrumpir flujo cuando llegue a numeros negativos-----------------------------------------------")
# loopinterrumpir flujo cuando llegue a un valor negativo

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)
    