# print("Tu nombre es:" + input("esccribe tu nombre:") + " " + input("escribe tu apellido: ")) 

# variables

# 1- ejercicio de comision de ventas de empleados

nombre = input("Write your name: ")

ganancia = input("cuanto has vendido en un mes: ")

resultado = (float(ganancia) * 13 / 100)
resultado_final = round(resultado, 2)

print(f"hola {nombre} tu ganancia es de : {resultado_final} euros")

