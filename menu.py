import pygame
import sys
from button import Button
from game import *
from configuracion import *
from funcionesAUXILIARES import *

pygame.init()
pygame.display.init()

SCREEN = pygame.display.set_mode((800, 600))
WINDOW_WIDTH, WINDOW_HEIGHT = SCREEN.get_size()

pygame.display.set_caption("Juego de palabras")

BG = pygame.image.load("assets/img/background_game.jpeg")
BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))


def get_font(size):
    return pygame.font.Font("assets/fonts/font.ttf", size)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(30).render("Juego Grupo 2", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(390, 60))

        PLAY_BUTTON = Button(
            image=pygame.image.load("assets/img/Play Rect.png"),
            pos=(390, 170),
            text_input="JUGAR",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(390, 290),
            text_input="DIFICULTAD",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )
        INSTRUCTIONS_BUTTON = Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(390, 410),
            text_input="INSTRUCCIONES",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load("assets/img/Quit Rect.png"),
            pos=(390, 530),
            text_input="SALIR",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play():
    while True:
        game("easy")  # Pasa la dificultad seleccionada a la función game()
        main_menu()
        pygame.display.update()



def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(30).render("SELECCIONE DIFICULTAD", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(390, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        EASY_BUTTON = Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(390, 170),
            text_input="FACIL",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )
        MEDIUM_BUTTON = Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(390, 290),
            text_input="MEDIO",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )
        HARD_BUTTON = Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(390, 410),
            text_input="DIFICIL",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )

        EASY_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        MEDIUM_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        HARD_BUTTON.changeColor(OPTIONS_MOUSE_POS)

        EASY_BUTTON.update(SCREEN)
        MEDIUM_BUTTON.update(SCREEN)
        HARD_BUTTON.update(SCREEN)

        OPTIONS_BACK = Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(390, 530),
            text_input="VOLVER",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, OPTIONS_BACK]:
            button_rect = button.rect
            text_surface = button.text_surface
            text_rect = text_surface.get_rect(center=button_rect.center)
            SCREEN.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    game(DIFICULTAD="easy")
                if MEDIUM_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    game(DIFICULTAD="medium")
                if HARD_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    game(DIFICULTAD="hard")
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def instructions():
    while True:
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()
        BG_I = pygame.image.load("assets/img/Instrucciones.png")
        BG_I = pygame.transform.scale(BG_I, (WINDOW_WIDTH, WINDOW_HEIGHT))

        SCREEN.blit(BG_I, (0, 0))

        INSTRUCTIONS_TEXT = get_font(30).render("INSTRUCCIONES", True, "Black")
        INSTRUCTIONS_RECT = INSTRUCTIONS_TEXT.get_rect(center=(WINDOW_WIDTH / 2, 60))
        SCREEN.blit(INSTRUCTIONS_TEXT, INSTRUCTIONS_RECT)

        INSTRUCTIONS_BACK = Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 70),
            text_input="VOLVER",
            font=get_font(30),
            base_color="Black",
            hovering_color="Green",
        )
        INSTRUCTIONS_BACK.changeColor(INSTRUCTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
