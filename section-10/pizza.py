import pygame
import math

pizza_img = pygame.image.load("section-10/imagenes/pizza.png")
pizza_img = pygame.transform.scale(pizza_img, (32, 32))

class Pizza:
    imagen = pizza_img
    velocidad = 1

    def __init__(self, x, y, objetivo_x, objetivo_y):
        self.x = x
        self.y = y
        self.imagen = self.__class__.imagen
        self.velocidad = self.__class__.velocidad
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()

        dx = objetivo_x - (self.x + self.ancho / 2)
        dy = objetivo_y - (self.y + self.alto / 2)
        distancia = math.sqrt(dx ** 2 + dy ** 2)

        if distancia > 0:
            self.cambio_x = (dx / distancia) * self.velocidad
            self.cambio_y = (dy / distancia) * self.velocidad
        else:
            self.cambio_x = 0
            self.cambio_y = 0

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def mover(self):
        self.x += self.cambio_x
        self.y += self.cambio_y

    def fuera_de_pantalla(self):
        return self.x < -32 or self.x > 800 or self.y < -32 or self.y > 600