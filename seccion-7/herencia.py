class Animal:

    def __init__(self, color, especie): #constructor seimrpe self y init. Esto es atributo de instancia
        self.color = color
        self.especie = especie

    def nacer(self):
        print("nacio")


class Pajaro(Animal):
    pass

  
mi_pajaro = Pajaro("amarillo", "pollo")
print(mi_pajaro.color)