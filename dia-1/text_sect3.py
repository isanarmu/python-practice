text = "Probando un texto Random"
# print(text.upper())
# print(text.lower())
# print(text[2].upper())
# texto = text.split()
# texto = text.split("t")
# texto = text.find("t")
texto = text.replace("t", "y")
texto = text.replace("P", "X").replace("Random", "Cualquiera")
print(texto)

# t = "juntar"
# s = "palabras"
# r = " ".join([t,s])
# print(r)
long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print(len(long_text))
X = "Repetición"
print(X * 15)

# Listas
list= ["a", "b", "c", "d", "e"]
list[0] = "uno"
list.append("ultimo")
list.pop(0) #borrar
# list.sort() ---- ordenar
# list.reverse() ---- al revés
deleted_element = list.pop(0)
print("deleted element:", deleted_element)
print("3rd postion:", list[2])
print("backwards: ", list[::-1])
print("longitud: ", len(list))

# Diccionarios no tienen orden ni indice, van en pares, als claves tienen que ser unicas, lños valores pueden ser repetidos, estan ordenados por vclaves no uindices
dicc = {"nombre": "pepe", 
        "edad" : 396,
        "hobbies": ["conseguir plasma", "visitar castillos", "programar"],
        "mascotas": {"perro": "Colmillos", "gato": "pelusa"}
        }

dicc["miedos"] = ["ajo", "sol"] #agregar un nuevo par clave-valor
print(dicc)
print(dicc.keys()) #imprime las claves
print(dicc.values()) #imprime los valores
print(dicc.items()) #imprime los pares clave-valor
# print(dicc["hobbies"][0])
print(dicc["mascotas"]["perro"].upper())

