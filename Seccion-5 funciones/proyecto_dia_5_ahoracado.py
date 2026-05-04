import random


palabras = ["abundante", "brunno", "felicidad", "prosperidad", "riqueza"]
palabra_oculta = random.choice(palabras)
vidas = 6
print(palabra_oculta)

def mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas):
    tablero = []
    for letra in palabra:
        if letra in letras_correctas:
            tablero.append(letra)
        else:
            tablero.append("_")
    print("\n" + "-------------")
    print(" ".join(tablero))
    print(f"Lettras incorrectas: {letras_incorrectas}")
    print("Vidas: ", vidas)
    print("\n" + "-------------")

def pedir_letra(letras_usadas):
    while True:
        letra = input("Elige una letra: ")

        if len(letra) != 1 or not letra.isalpha():
            print("Eso no es una letra válida")
        elif letra in letras_usadas:
            print("Esa letra ya la has usado")
        else:
            return letra

def comprobar_letra(letra, palabra, letras_correctas, letras_incorrectas, vidas):
    if letra in palabra:
        letras_correctas.append(letra)
    else:
        letras_incorrectas.append(letra)
        vidas -= 1
    return vidas

def victoria(palabra, letras_correctas):
    for letra in palabra:
        if letra not in letras_correctas:
            return False
    return True

def jugar():
    palabra = palabra_oculta
    letras_correctas = []
    letras_incorrectas = []
    vidas = 6
    juego_terminado = False

    while not juego_terminado:
        mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
        letras_usadas = letras_correctas + letras_incorrectas
        letra = pedir_letra(letras_usadas)
        vidas =comprobar_letra(letra, palabra, letras_correctas, letras_incorrectas, vidas)

        if victoria(palabra, letras_correctas):
           mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
           print("Ganaste!!")
           juego_terminado = True
        elif vidas == 0:
             mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
             print(f"Perdiste. La palabra era: {palabra}")
             juego_terminado = True

jugar()