mi_archivo = open("prueba1.txt", "w") #metdo "a" R", a es para caudnoe scribe un archivo comenzar a escribir solo al final de lo que ya tenia hecho

mi_archivo.write("Nueva linea")





archivo = open("prueba1.txt", "a")

archivo.write("Nuevo inicio de sesión")
archivo = open("prueba1.txt", "r")
print(archivo.read())

archivo.close()



mi_archivo.close()

registro_ultima_sesion = ["Federico", "\t20/12/2021", "\t08:17:32 hs", "\tSin errores de carga"]

archivo = open("registro.txt", "a")
archivo.writelines(registro_ultima_sesion)
archivo = open("registro.txt", "r")

print(archivo.read())

archivo.close()
