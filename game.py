import os
import pygame
from pygame.locals import *

from configuracion import *
from extras import *

# Importo funciones auxiliares de la logica del juego
from funcionesAUXILIARES import *


# Funcion del juego
def game():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    # Preparar la ventana
    pygame.display.set_caption("Adivina la Palabra")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # Cargar la imagen de fondo
    imagen_fondo = pygame.image.load("assets/background_game.jpeg")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0
    candidata = ""
    diccionario = []
    palabrasAcertadas = []

    # lee el diccionario
    lectura(diccionario)

    # elige las 7 letras al azar y una de ellas como principal
    letrasEnPantalla = dame7Letras()
    letraPrincipal = dameLetra(letrasEnPantalla)

    # se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
    while (
        len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))
        < MINIMO
    ):
        letrasEnPantalla = dame7Letras()
        letraPrincipal = dameLetra(letrasEnPantalla)

    print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))

    # Dibujar la pantalla la primera vez
    screen.blit(
        imagen_fondo, (0, 0)
    )  # Dibujar la imagen de fondo en la posición (0, 0)
    dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)
    pygame.display.update()

    while segundos > fps / 1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()
        segundos = TIEMPO_MAX - totaltime / 1000

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():
            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                candidata += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    candidata = candidata[0 : len(candidata) - 1]  # borra la ultima
                if e.key == K_RETURN:  # presionó enter
                    puntos += procesar(
                        letraPrincipal,
                        letrasEnPantalla,
                        candidata,
                        diccionario,
                        palabrasAcertadas,
                    )
                    candidata = ""

        segundos = TIEMPO_MAX - pygame.time.get_ticks() / 1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        screen.blit(
            imagen_fondo, (0, 0)
        )  # Dibujar la imagen de fondo en la posición (0, 0)
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)
        pygame.display.update()

    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

                return
