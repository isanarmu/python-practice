# tipos de atributos de clase y de instancia

class Pajaro:
    def __init__(self, color): #constructor seimrpe self y init
        self.color = color

mi_pajaro = Pajaro("amarillo")

print(mi_pajaro.color)