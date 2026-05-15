class Pajaro:

    alas = True #atributo de clase

    def __init__(self, color, especie): #constructor seimrpe self y init. Esto es atributo de instancia
        self.color = color
        self.especie = especie

    def piar(self):
        print("PIO")
    
mi_pajaro = Pajaro("blanco", "pollo")
mi_pajaro.piar()
