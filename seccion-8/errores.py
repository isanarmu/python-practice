def al_caudrado():
    numero = int(input("ingresa un numero: "))
    resultado = numero ** numero
    print(f"el cuadrado de {numero} es {resultado}")


try: 
    # El codigo que puede fallar
    al_caudrado()
except:
    # el codigo que ddebe ejhecutarse si falla
    print("ocurrio un error imprevisto")