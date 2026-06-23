import pygame
import random
import math
from perro import Perro
from pizza import Pizza
from repartidor import Repartidor
from interfaz import Interfaz

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
repartidor_jugador = Repartidor()

# interfaz
interfaz = Interfaz()

# para que el perro aparezca en una posicion aleatoria
perros = [Perro(random.randint(0, 746), 0)]
ultimo_perro = pygame.time.get_ticks()
tiempo_entre_perros = 3000
# pizzas disparadas
# pizzas disparadas
pizzas = []
ultimo_disparo = pygame.time.get_ticks()
tiempo_entre_disparos = 1000

# puntaje y tiempo transcurrido

puntaje = 0
tiempo_inicio = pygame.time.get_ticks()
tiempo_final = 0
estado_juego = "jugando"
    
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

def obtener_tiempo_sobrevivido():
    if estado_juego == "jugando":
        tiempo_pasado = pygame.time.get_ticks() - tiempo_inicio
    else:
        tiempo_pasado = tiempo_final

    segundos_totales = tiempo_pasado // 1000
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    return minutos, segundos

def terminar_juego():
    global estado_juego, tiempo_final

    if estado_juego == "jugando":
        estado_juego = "terminado"
        tiempo_final = pygame.time.get_ticks() - tiempo_inicio
        repartidor_jugador.detener()
        pygame.mixer.music.stop()

def detectar_colision_repartidor():
    global perros

    tiempo_actual = pygame.time.get_ticks()

    perros_sobrevivientes = []

    for perro_actual in perros:
        distancia_x = perro_actual.centro_x() - repartidor_jugador.centro_x()
        distancia_y = perro_actual.centro_y() - repartidor_jugador.centro_y()
        distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5

        if distancia < 45:
            perdio_vida = repartidor_jugador.perder_vida(tiempo_actual)

            if perdio_vida:
                sonido_vida_perdida.play()

                if repartidor_jugador.vidas <= 0:
                    terminar_juego()
        else:
            perros_sobrevivientes.append(perro_actual)

    perros = perros_sobrevivientes

def perro_mas_cercano():
    perro_cercano = None
    distancia_menor = 999999

    for perro_actual in perros:
        dx = perro_actual.centro_x() - repartidor_jugador.centro_x()
        dy = perro_actual.centro_y() - repartidor_jugador.centro_y()
        distancia = math.sqrt(dx ** 2 + dy ** 2)

        if distancia < distancia_menor:
            distancia_menor = distancia
            perro_cercano = perro_actual

    return perro_cercano

def disparar_pizza():
    if len(perros) > 0:
        perro_objetivo = perro_mas_cercano()

        pizza_x = repartidor_jugador.punto_disparo_x()
        pizza_y = repartidor_jugador.punto_disparo_y()

        pizza_nueva = Pizza(pizza_x, pizza_y, perro_objetivo.centro_x(), perro_objetivo.centro_y())
        pizzas.append(pizza_nueva)
        sonido_disparo.play()

def detectar_colisiones():
    global perros, puntaje, pizzas

    pizzas_sobrevivientes = []
    perros_sobrevivientes = list(perros)

    for pizza_actual in pizzas:
        pizza_choco = False

        for perro_actual in perros_sobrevivientes:
            dx = pizza_actual.x - perro_actual.x
            dy = pizza_actual.y - perro_actual.y
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

# loop juego para cerrar y que se qeude abierto

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if estado_juego == "jugando":
            if evento.type == pygame.KEYDOWN:
                repartidor_jugador.iniciar_movimiento(evento.key)
            if evento.type == pygame.KEYUP:
                repartidor_jugador.parar_movimiento(evento.key)

    tiempo_actual = pygame.time.get_ticks()

    if estado_juego == "jugando":
        repartidor_jugador.mover()

# disparar pizza automaticamente cada segundo
        if tiempo_actual - ultimo_disparo >= tiempo_entre_disparos:
            disparar_pizza()
            ultimo_disparo = tiempo_actual
        # crear un perro nuevo cada tres segundos
        if tiempo_actual - ultimo_perro >= tiempo_entre_perros:
            crear_perro()
            ultimo_perro = tiempo_actual

         # Movimiento del perro hacia el repartidor(formula pitagoras)
        for perro_actual in perros:
            perro_actual.mover_hacia(repartidor_jugador.x, repartidor_jugador.y)
                # Movimiento de la pizza
        pizzas_sobrevivientes = []

        for pizza_actual in pizzas:
            pizza_actual.mover()

            if not pizza_actual.fuera_de_pantalla():
                pizzas_sobrevivientes.append(pizza_actual)

        pizzas = pizzas_sobrevivientes

        detectar_colisiones()
        detectar_colision_repartidor()

    pantalla.blit(fondo, (0, 0))

    if estado_juego == "jugando":
        repartidor_jugador.dibujar(pantalla, tiempo_actual, True)
    else:
        repartidor_jugador.dibujar(pantalla, tiempo_actual, False)


    for perro_actual in perros:
        perro_actual.dibujar(pantalla)
    for pizza_actual in pizzas:
        pizza_actual.dibujar(pantalla)
    
    interfaz.dibujar_vidas(pantalla, repartidor_jugador.vidas)
    interfaz.dibujar_puntaje(pantalla, puntaje)

    minutos, segundos = obtener_tiempo_sobrevivido()

    if estado_juego == "jugando":
        interfaz.dibujar_tiempo(pantalla, minutos, segundos)
    else:
        interfaz.dibujar_pantalla_fin(pantalla, puntaje, minutos, segundos)

    pygame.display.update()

pygame.quit()