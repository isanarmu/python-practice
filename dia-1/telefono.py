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
print(remove_dashes(mis_telefonos, "34"))


mis_telefonos = ["612-345-678", "34 600 000 000", "+34 (654) 321"]