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
fondo = pygame.transform.scale(fondo, (800, 900))


# loop juego para cerrar y que se qeude abierto

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
    pantalla.blit(fondo, (0, 0))
    pygame.display.update()
    
pygame.quit()
