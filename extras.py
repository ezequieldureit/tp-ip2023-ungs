import pygame
import sys
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return "a"
    elif key == K_b:
        return "b"
    elif key == K_c:
        return "c"
    elif key == K_d:
        return "d"
    elif key == K_e:
        return "e"
    elif key == K_f:
        return "f"
    elif key == K_g:
        return "g"
    elif key == K_h:
        return "h"
    elif key == K_i:
        return "i"
    elif key == K_j:
        return "j"
    elif key == K_k:
        return "k"
    elif key == K_l:
        return "l"
    elif key == K_m:
        return "m"
    elif key == K_n:
        return "n"
    elif key == K_o:
        return "o"
    elif key == K_p:
        return "p"
    elif key == K_q:
        return "q"
    elif key == K_r:
        return "r"
    elif key == K_s:
        return "s"
    elif key == K_t:
        return "t"
    elif key == K_u:
        return "u"
    elif key == K_v:
        return "v"
    elif key == K_w:
        return "w"
    elif key == K_x:
        return "x"
    elif key == K_y:
        return "y"
    elif key == K_z:
        return "z"
    elif key == K_SPACE:
        return " "
    else:
        return ""


def dibujar(
    screen,
    letraPrincipal,
    letrasEnPantalla,
    candidata,
    puntos,
    segundos,
    palabrasAcertadas,
):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), 20)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), 80)

    # Linea del piso
    pygame.draw.line(screen, (114, 123, 114), (0, ALTO - 70), (ANCHO, ALTO - 70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if segundos < 15:
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL
        )
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    # escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 90
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(
                defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_TIEMPO_FINAL),
                (pos, 90),
            )
        else:
            screen.blit(
                defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_LETRAS),
                (pos, 90),
            )
        pos = pos + TAMANNO_LETRA_GRANDE

    # ESCRIBE LAS PALABRAS QUE EL USUARIO ACERTE
    pos = 100
    pos2 = 210
    ren4 = defaultFont.render("Correctas:", 1, COLOR_TEXTO)
    for i in range(len(palabrasAcertadas)):
        if len(palabrasAcertadas[i]) > 2 and len(palabrasAcertadas[i]) < 8:
            if pos <= 700:
                screen.blit(
                    defaultFont.render(palabrasAcertadas[i], 1, COLOR_LETRAS),
                    (pos, pos2),
                )
            else:
                pos = 0
                pos2 += 25
                screen.blit(
                    defaultFont.render(palabrasAcertadas[i], 1, COLOR_LETRAS),
                    (pos, pos2),
                )
            pos += TAMANNO_LETRA_GRANDE

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))
    screen.blit(ren4, (0, 210))
