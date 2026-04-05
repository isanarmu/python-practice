mis_telefonos = ["612-345-678", "34 600 000 000", "+34 (654) 321"]

def remove_dashes(phone_number, country_code):
    result = []
    for telefono in phone_number:
        telefono_limpio = ""
        for char in telefono:
            if char.isdigit():
                telefono_limpio += char
        if not telefono_limpio.startswith(country_code):
            telefono_limpio = country_code + telefono_limpio
        result.append(telefono_limpio)
    return result
print(remove_dashes(mis_telefonos[0], "34"))


# mis_telefonos = ["612-345-678", "34 600 000 000", "+34 (654) 321"]

# def limpiar_telefonos(lista_telefonos, codigo_pais):
#     resultado = []
#     for telefono in lista_telefonos:
#         # 1. Limpiamos el teléfono: dejamos solo los números
#         telefono_limpio = ""
#         for caracter in telefono:
#             if caracter.isdigit(): # ¿Es un número del 0 al 9?
#                 telefono_limpio += caracter   
#         # 2. Comprobamos si ya empieza por el código del país
#         if not telefono_limpio.startswith(codigo_pais):
#             # Si no lo tiene, se lo pegamos delante
#             telefono_limpio = codigo_pais + telefono_limpio
#         # 3. Lo guardamos en nuestra lista final
#         resultado.append(telefono_limpio)

#     return resultado

# print(limpiar_telefonos(mis_telefonos, "34"))
