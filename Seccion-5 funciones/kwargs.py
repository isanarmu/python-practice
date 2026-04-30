def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg es igual a {arg}")

    for clave, valor in kwargs.items():
        print(f"La clave {clave} es igual a {valor}")


prueba(3, 4, 5, 6, x=7, y=8, z=9)