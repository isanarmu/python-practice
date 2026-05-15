# tipos de atributos de clase y de instancia

class Pajaro:

    alas = True #atributo de clase

    def __init__(self, color, especie): #constructor seimrpe self y init. Esto es atributo de instancia
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("amarillo", "pollo")
otro_pajaro = Pajaro("negro", "tucán")

print(mi_pajaro.color)
print(mi_pajaro.alas)