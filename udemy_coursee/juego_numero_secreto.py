from random import *

numero_secreto = randint(1, 100)
nombre_jugador= input("escribe tu nombre aqui: ")
print(f"Bueno, {nombre_jugador}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

intento = input("Cual crees que es el numero secreto? ")
guessed_number = int(intento)
numero_intentos = 8


while numero_intentos > 1 and numero_secreto != guessed_number:
    
    if guessed_number < 1 or guessed_number > 100: 
        print("El numero que elijas tiene que estar entre 1 y 100")
    elif guessed_number < numero_secreto:
        print("El numero elegido es menor al secreto")
    else:
        print("El numero elegido es mayor que el secreto")
    
    numero_intentos -=1
    guessed_number = int(input(f"Prueba otra vez, te quedan {numero_intentos} intentos: "))
if guessed_number == numero_secreto:
    intentos_usados = 9 - numero_intentos
    print(f"Acertaste enorabuena!! LO acertaste en {intentos_usados}")  
else:
    print(f"Perdiste, se te acabaron los intentos. El numero secreto era {numero_secreto}")