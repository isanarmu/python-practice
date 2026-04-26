lista_cafes = [("capuchino", 2.30), ("latte", 2.80), ("espresso", 1.50), ("mocha", 3.20), ("americano", 2.00), ("flat white", 3.00), ("macchiato", 2.40)]

for elemento, precio in lista_cafes:
    print(elemento)

print("------------------------probando---------------------")

def encontrar_mas_caro(lista):
    precio_mayor = 0
    nombre_cafe_mas_caro = ""

    for nombre, precio in lista:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe_mas_caro = nombre
    return nombre_cafe_mas_caro, precio_mayor
cafe, precio = encontrar_mas_caro(lista_cafes)
    # return (f"el cafe mas caro es {nombre_cafe_mas_caro} y su precio {precio_mayor}€")
print(f"el cafe mas caro es {cafe} y su precio {precio}€")