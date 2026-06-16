import pygame

#iniciar a pygame
pygame.init()

# crear la pantalla
pantalla = pygame.display.set_mode((800, 600))
# para el nombre que aparece al abrirse
pygame.display.set_caption("Pizza survivor")
# para el icono del juego
icono = pygame.image.load("pizza.png")
pygame.display.set_icon(icono)
# para el fondo
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (800, 600))

# repartirdor
repartidor_img = pygame.image.load("repartidor.png")
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100))
repartidor_x = 368
repartidor_y = 440
repartidor_cambio_x = 0
repartidor_cambio_y = 0


def repartidor(x, y):
    pantalla.blit(repartidor_img, (x, y))

# loop juego para cerrar y que se qeude abierto

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                repartidor_cambio_x = -1
            if evento.key == pygame.K_RIGHT:
                repartidor_cambio_x = 1
            if evento.key == pygame.K_UP:
                repartidor_cambio_y = -1
            if evento.key == pygame.K_DOWN:
                repartidor_cambio_y = 1
        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                repartidor_cambio_x = 0
            if evento.key in (pygame.K_UP, pygame.K_DOWN):
                repartidor_cambio_y = 0
    repartidor_x += repartidor_cambio_x
    repartidor_y += repartidor_cambio_y

    pantalla.blit(fondo, (0, 0))
    repartidor(repartidor_x, repartidor_y)
    
    pygame.display.update()
    
pygame.quit()
