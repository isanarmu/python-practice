def remove_dashes(phone_number):
    texto_limpio= ""
    for char in phone_number:
        if char.isdigit():
            texto_limpio += char
    return texto_limpio
print(remove_dashes("+34 612-345-678"))