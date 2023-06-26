import os
import pygame
from pygame.locals import *

from configuracion import *
from extras import *

# Importo funciones auxiliares de la logica del juego
from funcionesAUXILIARES import *



# Funcion del juego
def game(DIFICULTAD):
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("Adivina la Palabra")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # Cargar la imagen de fondo
    imagen_fondo = pygame.image.load("assets/img/background_game.jpeg")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

    # Cargar de musica de fondo - leo
    pygame.mixer.music.load("assets/sounds/mision-imposible-peliculas-.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    # Variables para el contador del tiempo
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
    dibujar(
        screen,
        letraPrincipal,
        letrasEnPantalla,
        candidata,
        puntos,
        segundos,
        palabrasAcertadas,
    )

    pygame.display.update()
    # Iniciar el contador de tiempo

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
                        DIFICULTAD,
                    )
                    correctas(
                        palabrasAcertadas,
                        letraPrincipal,
                        letrasEnPantalla,
                        candidata,
                        diccionario,
                    )
                    candidata = ""

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        screen.blit(
            imagen_fondo, (0, 0)
        )  # Dibujar la imagen de fondo en la posición (0, 0)
        dibujar(
            screen,
            letraPrincipal,
            letrasEnPantalla,
            candidata,
            puntos,
            segundos,
            palabrasAcertadas,
            
        )

        pygame.display.update()
        
    if(len(palabrasAcertadas) > 0):
        cierre(
            palabrasAcertadas,puntos
            )
        
    pygame.mixer.quit()

