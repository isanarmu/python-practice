mi_archivo = open("prueba.txt")

primera_linea = mi_archivo.readline()
print(primera_linea.upper())

siguiente_linea = mi_archivo.readline()
print(siguiente_linea)

# siempre que se abra un archivo recuerda cerrarlo para que no consuma mucha memoria
mi_archivo.close()