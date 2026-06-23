

class Enemigo:
    imagen = None
    velocidad = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imagen = self.__class__.imagen
        self.velocidad = self.__class__.velocidad
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def centro_x(self):
        return self.x + self.ancho / 2

    def centro_y(self):
        return self.y + self.alto / 2

    def mover_hacia(self, objetivo_x, objetivo_y):
        dx = objetivo_x - self.x
        dy = objetivo_y - self.y
        distancia = (dx **2 + dy ** 2) ** 0.5

        if distancia > 0:
            self.x += (dx / distancia) * self.velocidad
            self.y += (dy / distancia) * self.velocidad