import pygame
import random
import math
from perro import Perro

#iniciar a pygame
pygame.init()
pygame.mixer.init()

# crear la pantalla
pantalla = pygame.display.set_mode((800, 600))
# para el nombre que aparece al abrirse
pygame.display.set_caption("Pizza survivor")
# para el icono del juego
icono = pygame.image.load("section-10/imagenes/pizza.png")
pygame.display.set_icon(icono)
# para el fondo
fondo = pygame.image.load("section-10/imagenes/fondo.png")
fondo = pygame.transform.scale(fondo, (800, 600))
# pizza
pizza_img = pygame.image.load("section-10/imagenes/pizza.png")
pizza_img = pygame.transform.scale(pizza_img, (32, 32))
# corazones
corazon_img = pygame.image.load("section-10/imagenes/corazon.png")
corazon_img = pygame.transform.scale(corazon_img, (32, 32))

# sonidos
pygame.mixer.music.load("section-10/sonidos/MusicaFondo.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)
sonido_disparo = pygame.mixer.Sound("section-10/sonidos/disparo.mp3")
sonido_golpe = pygame.mixer.Sound("section-10/sonidos/golpe.mp3")
sonido_vida_perdida = pygame.mixer.Sound("section-10/sonidos/vida_perdida.mp3")
sonido_disparo.set_volume(0.8)
sonido_golpe.set_volume(0.8)
sonido_vida_perdida.set_volume(0.8)

# repartirdor
repartidor_img = pygame.image.load("section-10/imagenes/repartidor.png")
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100))
repartidor_x = 368
repartidor_y = 440
repartidor_cambio_x = 0
repartidor_cambio_y = 0
velocidad_repartidor = 1
vidas = 3
tiempo_invulnerable = 2500
ultimo_golpe = -tiempo_invulnerable

# para que el perro aparezca en una posicion aleatoria
perros = [Perro(random.randint(0, 746), 0)]
ultimo_perro = pygame.time.get_ticks()
tiempo_entre_perros = 3000
# pizzas disparadas
pizzas_x = []
pizzas_y = []
pizzas_cambio_x = []
pizzas_cambio_y = []
velocidad_pizza = 1
ultimo_disparo = pygame.time.get_ticks()
tiempo_entre_disparos = 1000

# puntaje y tiempo transcurrido

puntaje = 0
fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 90)
fuente_mediana = pygame.font.Font(None, 40)
tiempo_inicio = pygame.time.get_ticks()
tiempo_final = 0
estado_juego = "jugando"
    
def repartidor(x, y):
    pantalla.blit(repartidor_img, (x, y))

def crear_perro():
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if borde == "arriba":
        perros.append(Perro(random.randint(0, 746), -64))
    elif borde == "abajo":
        perros.append(Perro(random.randint(0, 746), 600))
    elif borde == "izquierda":
        perros.append(Perro(-54, random.randint(0, 536)))
    else:
        perros.append(Perro(800, random.randint(0, 536)))

def pizza(x, y):
    pantalla.blit(pizza_img, (x, y))

def dibujar_vidas():
    if vidas >= 1:
        pantalla.blit(corazon_img, (10, 10))
    if vidas >= 2:
        pantalla.blit(corazon_img, (45, 10))
    if vidas >= 3:
        pantalla.blit(corazon_img, (80, 10))

def obtener_tiempo_sobrevivido():
    if estado_juego == "jugando":
        tiempo_pasado = pygame.time.get_ticks() - tiempo_inicio
    else:
        tiempo_pasado = tiempo_final

    segundos_totales = tiempo_pasado // 1000
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    return minutos, segundos

def dibujar_tiempo():
    minutos, segundos = obtener_tiempo_sobrevivido()
    texto = fuente.render(f"Time Survived: {minutos}:{segundos:02}", False, (235, 0, 0))
    rectangulo = texto.get_rect(midtop=(400, 570))
    pantalla.blit(texto, rectangulo)

def terminar_juego():
    global estado_juego, tiempo_final, repartidor_cambio_x, repartidor_cambio_y

    if estado_juego == "jugando":
        estado_juego = "terminado"
        tiempo_final = pygame.time.get_ticks() - tiempo_inicio
        repartidor_cambio_x = 0
        repartidor_cambio_y = 0
        pygame.mixer.music.stop()

def dibujar_pantalla_fin():
    minutos, segundos = obtener_tiempo_sobrevivido()

    texto_game_over = fuente_grande.render("Game Over", False, (235, 0, 0))
    rectangulo_game_over = texto_game_over.get_rect(center=(400, 250))
    pantalla.blit(texto_game_over, rectangulo_game_over)

    texto_puntaje = fuente_mediana.render(f"Final score: {puntaje}", False, (255, 255, 255))
    rectangulo_puntaje = texto_puntaje.get_rect(center=(400, 330))
    pantalla.blit(texto_puntaje, rectangulo_puntaje)

    texto_tiempo = fuente_mediana.render(f"Time Survived: {minutos}:{segundos:02}", False, (255, 255, 255))
    rectangulo_tiempo = texto_tiempo.get_rect(center=(400, 375))
    pantalla.blit(texto_tiempo, rectangulo_tiempo)

def detectar_colision_repartidor():
    global vidas, perros, ultimo_golpe

    tiempo_actual = pygame.time.get_ticks()
    esta_invulnerable = tiempo_actual - ultimo_golpe < tiempo_invulnerable

    perros_sobrevivientes = []

    for perro_actual in perros:
        distancia_x = perro_actual.centro_x() - (repartidor_x + 32)
        distancia_y = perro_actual.centro_y() - (repartidor_y + 50)
        distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5

        if distancia < 45:
            if not esta_invulnerable:
                vidas -= 1
                sonido_vida_perdida.play()
                ultimo_golpe = tiempo_actual
                esta_invulnerable = True

                if vidas <= 0:
                    terminar_juego()
        else:
            perros_sobrevivientes.append(perro_actual)

    perros = perros_sobrevivientes

def perro_mas_cercano():
    perro_cercano = 0
    distancia_menor = 999999

    for indice_perro in range(len(perros)):
        dx = perros[indice_perro].centro_x() - (repartidor_x + 32)
        dy = perros[indice_perro].centro_y() - (repartidor_y + 50)
        distancia = math.sqrt(dx ** 2 + dy ** 2)

        if distancia < distancia_menor:
            distancia_menor = distancia
            perro_cercano = indice_perro

    return perro_cercano

def disparar_pizza():
    if len(perros) > 0:
        indice_perro = perro_mas_cercano()

        pizza_x = repartidor_x + 16
        pizza_y = repartidor_y + 34

        dx = perros[indice_perro].centro_x() - (pizza_x + 16)
        dy = perros[indice_perro].centro_y() - (pizza_y + 16)

        distancia = math.sqrt(dx ** 2 + dy ** 2)

        if distancia > 0:
            pizzas_x.append(pizza_x)
            pizzas_y.append(pizza_y)
            pizzas_cambio_x.append((dx / distancia) * velocidad_pizza)
            pizzas_cambio_y.append((dy / distancia) * velocidad_pizza)
            sonido_disparo.play()

def detectar_colisiones():
    global perros, puntaje
    pizzas = list(zip(pizzas_x, pizzas_y))

    pizzas_sobrevivientes = []
    perros_sobrevivientes = list(perros)

    for pizza_actual in pizzas:
        pizza_choco = False

        for perro_actual in perros_sobrevivientes:
            dx = pizza_actual[0] - perro_actual.x
            dy = pizza_actual[1] - perro_actual.y
            distancia = (dx **2 + dy ** 2) ** 0.5

            if distancia < 30:
                perros_sobrevivientes.remove(perro_actual)
                pizza_choco = True
                puntaje += 1
                sonido_golpe.play()
                break
        if not pizza_choco:
            pizzas_sobrevivientes.append(pizza_actual)
    pizzas = pizzas_sobrevivientes
    perros = perros_sobrevivientes

def dibujar_puntaje():
    texto = fuente.render(f"Points: {puntaje}", False, (235, 0, 0))
    pantalla.blit(texto, (650, 10))

# loop juego para cerrar y que se qeude abierto

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if estado_juego == "jugando":
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

    tiempo_actual = pygame.time.get_ticks()

    if estado_juego == "jugando":
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
        if tiempo_actual - ultimo_disparo >= tiempo_entre_disparos:
            disparar_pizza()
            ultimo_disparo = tiempo_actual
        # crear un perro nuevo cada tres segundos
        if tiempo_actual - ultimo_perro >= tiempo_entre_perros:
            crear_perro()
            ultimo_perro = tiempo_actual

        # Movimiento del perro hacia el repartidor(formula pitagoras)
        for indice_perro in range(len(perros)):
            perros[indice_perro].mover_hacia(repartidor_x, repartidor_y)
        # Movimiento de la pizza
        for indice_pizza in range(len(pizzas_x) - 1, -1, -1):
            pizzas_x[indice_pizza] += pizzas_cambio_x[indice_pizza]
            pizzas_y[indice_pizza] += pizzas_cambio_y[indice_pizza]
            if pizzas_x[indice_pizza] < -32 or pizzas_x[indice_pizza] > 800 or pizzas_y[indice_pizza] < -32 or pizzas_y[indice_pizza] > 600:
                pizzas_x.pop(indice_pizza)
                pizzas_y.pop(indice_pizza)
                pizzas_cambio_x.pop(indice_pizza)
                pizzas_cambio_y.pop(indice_pizza)

        detectar_colisiones()
        detectar_colision_repartidor()

    pantalla.blit(fondo, (0, 0))

    esta_invulnerable = tiempo_actual - ultimo_golpe < tiempo_invulnerable

    if estado_juego == "jugando":
        if esta_invulnerable:
            if (tiempo_actual // 150) % 2 == 0:
                repartidor(repartidor_x, repartidor_y)
        else:
            repartidor(repartidor_x, repartidor_y)
    else:
        repartidor(repartidor_x, repartidor_y)


    for indice_perro in range(len(perros)):
        perros[indice_perro].dibujar(pantalla)

    for indice_pizza in range(len(pizzas_x)):
        pizza(pizzas_x[indice_pizza], pizzas_y[indice_pizza])
    
    dibujar_vidas()
    dibujar_puntaje()

    if estado_juego == "jugando":
        dibujar_tiempo()
    else:
        dibujar_pantalla_fin()

    pygame.display.update()

pygame.quit()
