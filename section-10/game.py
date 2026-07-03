import pygame
import random
import math
from perro import Perro
from gato import Gato
from pizza import Pizza
from repartidor import Repartidor
from interfaz import Interfaz

# iniciar a pygame
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

# repartidor
repartidor_jugador = Repartidor()

# interfaz
interfaz = Interfaz()

# enemigos
enemigos = []
ultimo_enemigo = pygame.time.get_ticks()
tiempo_entre_enemigos = 3000

# pizzas disparadas
pizzas = []
ultimo_disparo = pygame.time.get_ticks()
tiempo_entre_disparos = 1000

# puntaje y tiempo transcurrido
puntaje = 0
tiempo_inicio = pygame.time.get_ticks()
tiempo_final = 0
estado_juego = "jugando"


def crear_enemigo():
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    tipo_enemigo = random.choice(["perro", "gato"])

    if borde == "arriba":
        enemigo_x = random.randint(0, 746)
        enemigo_y = -64
    elif borde == "abajo":
        enemigo_x = random.randint(0, 746)
        enemigo_y = 600
    elif borde == "izquierda":
        enemigo_x = -54
        enemigo_y = random.randint(0, 536)
    else:
        enemigo_x = 800
        enemigo_y = random.randint(0, 536)

    if tipo_enemigo == "perro":
        enemigo_nuevo = Perro(enemigo_x, enemigo_y)
    else:
        enemigo_nuevo = Gato(enemigo_x, enemigo_y)

    enemigos.append(enemigo_nuevo)


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
    global enemigos

    tiempo_actual = pygame.time.get_ticks()
    enemigos_sobrevivientes = []

    for enemigo_actual in enemigos:
        distancia_x = enemigo_actual.centro_x() - repartidor_jugador.centro_x()
        distancia_y = enemigo_actual.centro_y() - repartidor_jugador.centro_y()
        distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5

        if distancia < 45:
            perdio_vida = repartidor_jugador.perder_vida(tiempo_actual)

            if perdio_vida:
                sonido_vida_perdida.play()

                if repartidor_jugador.vidas <= 0:
                    terminar_juego()
        else:
            enemigos_sobrevivientes.append(enemigo_actual)

    enemigos = enemigos_sobrevivientes


def enemigo_mas_cercano():
    enemigo_cercano = None
    distancia_menor = 999999

    for enemigo_actual in enemigos:
        dx = enemigo_actual.centro_x() - repartidor_jugador.centro_x()
        dy = enemigo_actual.centro_y() - repartidor_jugador.centro_y()
        distancia = math.sqrt(dx ** 2 + dy ** 2)

        if distancia < distancia_menor:
            distancia_menor = distancia
            enemigo_cercano = enemigo_actual

    return enemigo_cercano


def disparar_pizza():
    if len(enemigos) > 0:
        enemigo_objetivo = enemigo_mas_cercano()

        pizza_x = repartidor_jugador.punto_disparo_x()
        pizza_y = repartidor_jugador.punto_disparo_y()

        pizza_nueva = Pizza(
            pizza_x,
            pizza_y,
            enemigo_objetivo.centro_x(),
            enemigo_objetivo.centro_y()
        )

        pizzas.append(pizza_nueva)
        sonido_disparo.play()


def detectar_colisiones():
    global enemigos, puntaje, pizzas

    pizzas_sobrevivientes = []
    enemigos_sobrevivientes = list(enemigos)

    for pizza_actual in pizzas:
        pizza_choco = False

        for enemigo_actual in enemigos_sobrevivientes:
            dx = pizza_actual.x - enemigo_actual.x
            dy = pizza_actual.y - enemigo_actual.y
            distancia = (dx ** 2 + dy ** 2) ** 0.5

            if distancia < 30:
                enemigos_sobrevivientes.remove(enemigo_actual)
                pizza_choco = True
                puntaje += 1
                sonido_golpe.play()
                break

        if not pizza_choco:
            pizzas_sobrevivientes.append(pizza_actual)

    pizzas = pizzas_sobrevivientes
    enemigos = enemigos_sobrevivientes


# crear el primer enemigo
crear_enemigo()
ultimo_enemigo = pygame.time.get_ticks()

# loop juego para cerrar y que se quede abierto
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

        # crear un enemigo nuevo cada tres segundos
        if tiempo_actual - ultimo_enemigo >= tiempo_entre_enemigos:
            crear_enemigo()
            ultimo_enemigo = tiempo_actual

        # movimiento de los enemigos hacia el repartidor
        for enemigo_actual in enemigos:
            enemigo_actual.mover_hacia(repartidor_jugador.x, repartidor_jugador.y)

        # movimiento de la pizza
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

    for enemigo_actual in enemigos:
        enemigo_actual.dibujar(pantalla)

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