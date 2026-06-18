import pygame
import random
import math

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
# pizza
pizza_img = pygame.image.load("pizza.png")
pizza_img = pygame.transform.scale(pizza_img, (32, 32))

# repartirdor
repartidor_img = pygame.image.load("repartidor.png")
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100))
repartidor_x = 368
repartidor_y = 440
repartidor_cambio_x = 0
repartidor_cambio_y = 0
velocidad_repartidor = 1

# perro enemigo
perro_img = pygame.image.load("perro.png")
perro_img = pygame.transform.scale(perro_img, (54, 64))
# para que el perro aparezca en una posicion aleatoria
perros_x = [random.randint(0, 746)]
perros_y = [0]
velocidad_perro = 0.1
# pizzas disparadas
pizzas_x = []
pizzas_y = []
pizzas_cambio_x = []
pizzas_cambio_y = []
velocidad_pizza = 1
ultimo_disparo = pygame.time.get_ticks()
tiempo_entre_disparos = 1000

    
def repartidor(x, y):
    pantalla.blit(repartidor_img, (x, y))

def perro(x, y):
    pantalla.blit(perro_img, (x, y))

def pizza(x, y):
    pantalla.blit(pizza_img, (x, y))

def perro_mas_cercano():
    perro_cercano = 0
    distancia_menor = 999999
    for i in range(len(perros_x)):
        dx = (perros_x[i] + 27) - (repartidor_x + 32)
        dy = (perros_y[i] + 32) - (repartidor_y + 50)
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        if distancia < distancia_menor:
            distancia_menor = distancia
            perro_cercano = i
    return perro_cercano

def disparar_pizza():
    if len(perros_x) > 0:
        indice_perro = perro_mas_cercano()
        pizza_x = repartidor_x + 16
        pizza_y = repartidor_y + 34
        dx = (perros_x[indice_perro] + 27) - (pizza_x + 16)
        dy = (perros_y[indice_perro] + 32) - (pizza_y + 16)
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        if distancia > 0:
            pizzas_x.append(pizza_x)
            pizzas_y.append(pizza_y)
            pizzas_cambio_x.append((dx / distancia) * velocidad_pizza)
            pizzas_cambio_y.append((dy / distancia) * velocidad_pizza)


# loop juego para cerrar y que se qeude abierto

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                repartidor_cambio_x = -velocidad_repartidor
            if evento.key == pygame.K_RIGHT:
                repartidor_cambio_x = velocidad_repartidor
            if evento.key == pygame.K_UP:
                repartidor_cambio_y = -velocidad_repartidor
            if evento.key == pygame.K_DOWN:
                repartidor_cambio_y = velocidad_repartidor
        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                repartidor_cambio_x = 0
            if evento.key in (pygame.K_UP, pygame.K_DOWN):
                repartidor_cambio_y = 0

    repartidor_x += repartidor_cambio_x
    repartidor_y += repartidor_cambio_y

    # para que no se salga de la pantalla
    if repartidor_x < 0:
        repartidor_x = 0
    elif repartidor_x > 736:
        repartidor_x = 736
    if repartidor_y < 0:
        repartidor_y = 0
    elif repartidor_y > 500:
        repartidor_y = 500

# disparar pizza automaticamente cada segundo
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_disparo >= tiempo_entre_disparos:
        disparar_pizza()
        ultimo_disparo = tiempo_actual

    # Movimiento del perro hacia el repartidor(formula pitagoras)
    for i in range(len(perros_x)):
        dx = repartidor_x - perros_x[i]
        dy = repartidor_y - perros_y[i]
        distancia = (dx **2 + dy ** 2) ** 0.5
        if distancia > 0:
            perros_x[i] += (dx / distancia) * velocidad_perro
            perros_y[i] += (dy / distancia) * velocidad_perro

    # Movimiento de la pizza
    for i in range(len(pizzas_x) - 1, -1, -1):
        pizzas_x[i] += pizzas_cambio_x[i]
        pizzas_y[i] += pizzas_cambio_y[i]
        if pizzas_x[i] < -32 or pizzas_x[i] > 800 or pizzas_y[i] < -32 or pizzas_y[i] > 600:
            pizzas_x.pop(i)
            pizzas_y.pop(i)
            pizzas_cambio_x.pop(i)
            pizzas_cambio_y.pop(i)

    pantalla.blit(fondo, (0, 0))
    repartidor(repartidor_x, repartidor_y)

    for i in range(len(perros_x)):
        perro(perros_x[i], perros_y[i])

    for i in range(len(pizzas_x)):
        pizza(pizzas_x[i], pizzas_y[i])
    
    pygame.display.update()
    
pygame.quit()