def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg es igual a {arg}")

    for clave, valor in kwargs.items():
        print(f"La clave {clave} es igual a {valor}")


prueba(3, 4, 5, 6, x=7, y=8, z=9)

print("---------------------cantidad_atributos --------------")

def cantidad_atributos(**kwargs):
    return len(kwargs)

print(cantidad_atributos(x=7, y=8, z=9))

print("---------------------lista_atributos --------------")

def lista_atributos(**kwargs):
    return list(kwargs.values())
print (lista_atributos(x=7, y=8, z=9))


print("_---------------------describir_persona --------------")
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")
describir_persona("María", color_ojos="azules", color_pelo="rubio")