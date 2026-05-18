# metodos de clase es con cls. 
# 
# Metodo de instancia pueden acceder a otros metodos. Self se le aplcia solo a las instancias

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

    def pintar_negro(self):
        self.color = "negro"
        print(f"El pajaro ahora es {self.color}")

    # metodo de clase
    
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Pone {cantidad} huevos.")

    #metodo estatico
    @staticmethod
    def mirar():
        print("El pajaro mira")


mi_pajaro = Pajaro("amarillo", "pollo")
print(mi_pajaro.color)
mi_pajaro.pintar_negro()
Pajaro.poner_huevos(3)
Pajaro.mirar()