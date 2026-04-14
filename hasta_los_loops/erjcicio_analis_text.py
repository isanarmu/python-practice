text= input("Ingresa un texto: ")
texto = text.lower()

letra_1 = input("Escribe la primera letra: ").lower()
letra_2 = input("Escribe la segunda letra: ").lower()
letra_3 = input("Escribe la tercera letra: ").lower()

texto_min_1 = texto.count(letra_1)
texto_min_2 = texto.count(letra_2)
texto_min_3 = texto.count(letra_3)

contador_palabras = texto.split()

primera = texto[0]
ultima = texto[-1]
aparece_python = "python" in texto.lower()

contador_palabras.reverse()
texto_invertido = " ".join(contador_palabras)


print(f"la letra {letra_1} aparece: {texto_min_1} veces")
print(f"la letra {letra_2} aparece: {texto_min_2} veces")
print(f"la letra {letra_3} aparece: {texto_min_3} veces")
print(f"Aparecen {len(contador_palabras)} palabras.")
print(f"La primera letra es {primera} y la última es {ultima}")
print(f"el texto al reves: {texto_invertido}")
print(aparece_python)