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