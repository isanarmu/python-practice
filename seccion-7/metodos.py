class Pajaro:

    alas = True #atributo de clase

    def __init__(self, color, especie): #constructor seimrpe self y init. Esto es atributo de instancia
        self.color = color
        self.especie = especie

    def piar(self):
        print("PIO")
    
    def caracteristicas(self):
        print(f"Mi color es {self.color} y soy {self.especie}")

    def volar(self, metros):
        print(f"Este pajaro ha volado {metros} metros")
    
mi_pajaro = Pajaro("amarillo", "pollo")
mi_pajaro.piar()
mi_pajaro.caracteristicas()
mi_pajaro.volar(0)
