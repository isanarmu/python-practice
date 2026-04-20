menor=min(58, 58, 54, 152, 12 )
print(menor)

lista = [58, 58, 54, 152, 12]
print(f'el menor es: {min(lista)}, y el mayor es: {max(lista)}.')

print("-----------------------------------------------strings----------------------------")

nombres = ['Rachel', 'Marcos', 'Luis', 'Rea']
print(min(nombres))

dic = {"c1": 45, "c2": 11}

print(min(dic.values()))

print("---------------------ejercicio udemy----------------------------------")
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima, ultimo_nombre)