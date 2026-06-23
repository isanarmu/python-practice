import pygame
from enemigo import Enemigo

perro_img = pygame.image.load("section-10/imagenes/perro.png")
perro_img = pygame.transform.scale(perro_img, (54, 64))

class Perro(Enemigo):
    imagen = perro_img
    velocidad = 0.2