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
            print("/n" + "-------------")
            print(" ".join(tablero))
            print(f"Lettras incorrectas: {letras_incorrectas}")
            print("Vidas: ", vidas)
            print("/n" + "-------------")

def ocultar_palabra(word):
    oculta = []
    for letter in word:
        oculta.append("_")
    return oculta

hidden_word = ocultar_palabra(palabra_oculta)

def pedir_letra():
    while True:
        letra = input("Elige una letra: ")
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Eso no es una letra")

def comprobar_letra(hidden_palabra):
    pass


def restar_vidas(numero):
    pass


