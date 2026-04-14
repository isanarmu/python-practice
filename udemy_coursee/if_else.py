# if elif elif else. Siempre dos puntso al final de cada uno.
if 10 > 99:
    print("10 es mayor que nueve")
else:
    print("no es mayor")


operacion = 5 * 2

if operacion != 10:
    print("el resultado no es 10")
elif operacion == 30:
    print("el resultado es 30")
else:
    print("no se cual es el resultado")


mi_edad = int(input("Escribe aqui tu edad: "))
calificacion = int(input("¿Qué nota has tenido?: "))

if mi_edad >= 100:
    print("Eres una momia y encima puedes conducir")
elif mi_edad >= 18:
        print("Puedes conducir un coche en España")
else:
    print("No puedes conducir un coche en españa")
if calificacion > 10 or calificacion < 0:
    print("Has introducido mal la nota, tiene que ser un numero entre 0 y 10")
elif calificacion >= 5:
    print("Has aprobado")
else:
    print("Lo siento has suspendido")