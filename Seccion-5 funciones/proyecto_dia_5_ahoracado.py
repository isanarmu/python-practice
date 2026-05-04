import random


palabras = ["abundante", "brunno", "felicidad", "prosperidad", "riqueza"]
palabra_oculta = random.choice(palabras)
vidas = 6
print(palabra_oculta)                      
def ocultar_palabra(word):
    oculta = []
    for letter in word:
        oculta.append("_")
    return oculta

hidden_word = ocultar_palabra(palabra_oculta)

def comprobar_letra(hidden_palabra):
    pedir_letra = input("Elige una letra: ")
    palabra =[]
    for letra in hidden_palabra:
        if letra == pedir_letra:        
            letra.append(palabra)
        else:
            return f"La letra no está, te quedan {vidas} vidas."
    return hidden_palabra

print(comprobar_letra(hidden_word))



def restar_vidas(numero):
    pass


