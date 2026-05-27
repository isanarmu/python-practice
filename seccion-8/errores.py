def al_caudrado():
    numero = int(input("ingresa un numero: "))
    resultado = numero * numero
    print(f"el cuadrado de {numero} es {resultado}")


try: 
    # El codigo que puede fallar
    al_caudrado()
except ValueError:
    # el codigo que ddebe ejhecutarse si falla
    print("Eso no es un numero")
except:
    print("Ocurrio un error interno")

else: 
    # El codigo que se ejecutará si no sale error
    print("El cuadrado se ejecutó correctamente")
finally:
    # el código que se ejecutará de todos modos
    print("Gracias por usar nuestro programa")

# OTRO EJEMPLO

def pedir_numero():
    while True:
        try:
            numero = int(input("ingresa un numero: "))
        except:
            print("ese no es un numero")
        else:
            print("ingresaste el numero ", numero)
            break
        print("gracias")
pedir_numero()