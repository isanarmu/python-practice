mi_archivo = open("prueba.txt")

# primera_linea = mi_archivo.readline()
# print(primera_linea.upper())

# for linea in mi_archivo:
#     print("Aqui dice: " + linea)

todas = mi_archivo.readlines()
print(todas)




# siempre que se abra un archivo recuerda cerrarlo para que no consuma mucha memoria
mi_archivo.close()