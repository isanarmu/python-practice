import pygame

repartidor_img = pygame.image.load("section-10/imagenes/repartidor.png")
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100))

class Repartidor:
    imagen = repartidor_img
    velocidad = 1
    vidas_iniciales = 3
    tiempo_invulnerable = 2500

    def __init__(self):
        self.x = 368
        self.y = 440
        self.cambio_x = 0
        self.cambio_y = 0
        self.imagen = self.__class__.imagen
        self.velocidad = self.__class__.velocidad
        self.vidas = self.__class__.vidas_iniciales
        self.tiempo_invulnerable = self.__class__.tiempo_invulnerable
        self.ultimo_golpe = -self.tiempo_invulnerable
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()

    def dibujar(self, pantalla, tiempo_actual, titilar):
        if titilar and self.esta_invulnerable(tiempo_actual):
            if (tiempo_actual // 150) % 2 == 0:
                pantalla.blit(self.imagen, (self.x, self.y))
        else:
            pantalla.blit(self.imagen, (self.x, self.y))

    def centro_x(self):
        return self.x + self.ancho / 2

    def centro_y(self):
        return self.y + self.alto / 2

    def punto_disparo_x(self):
        return self.x + 16

    def punto_disparo_y(self):
        return self.y + 34

    def iniciar_movimiento(self, tecla):
        if tecla == pygame.K_LEFT:
            self.cambio_x = -self.velocidad
        if tecla == pygame.K_RIGHT:
            self.cambio_x = self.velocidad
        if tecla == pygame.K_UP:
            self.cambio_y = -self.velocidad
        if tecla == pygame.K_DOWN:
            self.cambio_y = self.velocidad

    def parar_movimiento(self, tecla):
        if tecla in (pygame.K_LEFT, pygame.K_RIGHT):
            self.cambio_x = 0
        if tecla in (pygame.K_UP, pygame.K_DOWN):
            self.cambio_y = 0

    def mover(self):
        self.x += self.cambio_x
        self.y += self.cambio_y

        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736
        if self.y < 0:
            self.y = 0
        elif self.y > 500:
            self.y = 500

    def detener(self):
        self.cambio_x = 0
        self.cambio_y = 0

    def esta_invulnerable(self, tiempo_actual):
        return tiempo_actual - self.ultimo_golpe < self.tiempo_invulnerable

    def perder_vida(self, tiempo_actual):
        if not self.esta_invulnerable(tiempo_actual):
            self.vidas -= 1
            self.ultimo_golpe = tiempo_actual
            return True

        return False