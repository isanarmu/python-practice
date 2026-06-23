import pygame

corazon_img = pygame.image.load("section-10/imagenes/corazon.png")
corazon_img = pygame.transform.scale(corazon_img, (32, 32))

class Interfaz:
    def __init__(self):
        self.corazon_img = corazon_img
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 90)
        self.fuente_mediana = pygame.font.Font(None, 40)

    def dibujar_vidas(self, pantalla, vidas):
        if vidas >= 1:
            pantalla.blit(self.corazon_img, (10, 10))
        if vidas >= 2:
            pantalla.blit(self.corazon_img, (45, 10))
        if vidas >= 3:
            pantalla.blit(self.corazon_img, (80, 10))

    def dibujar_tiempo(self, pantalla, minutos, segundos):
        texto = self.fuente.render(f"Time Survived: {minutos}:{segundos:02}", False, (235, 0, 0))
        rectangulo = texto.get_rect(midtop=(400, 570))
        pantalla.blit(texto, rectangulo)

    def dibujar_puntaje(self, pantalla, puntaje):
        texto = self.fuente.render(f"Points: {puntaje}", False, (235, 0, 0))
        pantalla.blit(texto, (650, 10))

    def dibujar_pantalla_fin(self, pantalla, puntaje, minutos, segundos):
        texto_game_over = self.fuente_grande.render("Game Over", False, (235, 0, 0))
        rectangulo_game_over = texto_game_over.get_rect(center=(400, 250))
        pantalla.blit(texto_game_over, rectangulo_game_over)

        texto_puntaje = self.fuente_mediana.render(f"Final score: {puntaje}", False, (255, 255, 255))
        rectangulo_puntaje = texto_puntaje.get_rect(center=(400, 330))
        pantalla.blit(texto_puntaje, rectangulo_puntaje)

        texto_tiempo = self.fuente_mediana.render(f"Time Survived: {minutos}:{segundos:02}", False, (255, 255, 255))
        rectangulo_tiempo = texto_tiempo.get_rect(center=(400, 375))
        pantalla.blit(texto_tiempo, rectangulo_tiempo)