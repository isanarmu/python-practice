numero_secreto = 99
nombre_jugador= input("escribe tu nombre aqui: ")
print(f"Bueno, {nombre_jugador}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

intento = input("Cual crees que es el numero secreto? ")
guessed_number = int(intento)

while guessed_number != numero_secreto:
    if guessed_number < 1 and guessed_number > 100: 
        print("El numero que elijas tiene que estar entre 1 y 100")
    elif guessed_number < numero_secreto:
        print("El numero elegido es menor al secreto")
    else:
        print("El numero elegido es mayor que el secreto")
print("Acertaste enorabuena!!")