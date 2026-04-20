habla_ingles = True
sabe_python = False

if habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == True and sabe_python ==False:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Cumples con los requisitos para postularte")




