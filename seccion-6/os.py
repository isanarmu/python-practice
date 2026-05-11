import os

# ruta = os.getcwd()
# print(ruta)

os.chdir("C:\\Users\\Irene\\Desktop\\Probando rutas")

archivo = open("vesina.txt.txt")

print(archivo.read())

archivo.close()
