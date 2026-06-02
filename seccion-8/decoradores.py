def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


operacion = cambiar_letras("min")

operacion("Palabra")


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")

    return otra_funcion


operacion("Palabra")



@decorar_saludo
def mayuscula(texto):
    print(texto.upper())


@decorar_saludo
def minuscula(texto):
    print(texto.lower())


mayuscula("Python")

