class Animal:

    def __init__(self, color, especie): #constructor seimrpe self y init. Esto es atributo de instancia
        self.color = color
        self.especie = especie

    def nacer(self):
        print("nacio")

    def nacer(self):
        print("El animal emite un sonido")
class Pajaro(Animal):

    def hablar(self):
        print("PIO")
    
    def volar(self, metros):
        print(f"voló {metros} metros")

  
pollo = Pajaro("amarillo", "pollo")
perro = Animal("Tricolor", "Teckel")

print(pollo.color)
pollo.volar(15)