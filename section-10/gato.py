import pygame
from enemigo import Enemigo

gato_img = pygame.image.load("section-10/imagenes/gato.png")
gato_img = pygame.transform.scale(gato_img, (45, 54))

class Gato(Enemigo):
    imagen = gato_img
    velocidad = 0.35