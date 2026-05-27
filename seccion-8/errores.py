def al_caudrado():
    numero = int(input("ingresa un numero: "))
    resultado = numero * numero
    print(f"el cuadrado de {numero} es {resultado}")


try: 
    # El codigo que puede fallar
    al_caudrado()
except:
    # el codigo que ddebe ejhecutarse si falla
    print("ocurrio un error imprevisto")

else: 
    # El codigo que se ejecutará si no sale error
    print("El cuadrado se ejecutó correctamente")
finally:
    # el código que se ejecutará de todos modos
    print("Gracias por usar nuestro programa")