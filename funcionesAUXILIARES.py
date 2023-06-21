from configuracion import *
import random
import pygame

pygame.mixer.init()


# lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario=[]):
    with open("data/diccionario.txt", "r") as archivo:
        palabras = [palabra.strip() for palabra in archivo]
    diccionario.extend(palabras)
    return diccionario


# Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz) >> OK
def dame7Letras():
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"

    # Seleccionar 2 o 3 vocales al azar sin repetir
    num_vocales = random.randint(2, 3)
    letras_vocales = random.sample(vocales, num_vocales)

    # Seleccionar el resto de letras como consonantes sin repetir
    num_consonantes = 7 - num_vocales
    letras_consonantes = random.sample(consonantes, num_consonantes)

    # Combinar las letras de forma aleatoria
    letras = letras_vocales + letras_consonantes
    random.shuffle(letras)

    return "".join(letras)


def dameLetra(letrasEnPantalla):  # elige una letra de las letras en pantalla
    return random.choice(letrasEnPantalla)


# si es valida la palabra devuelve puntos sino resta.
def procesar(
    letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas
):
    if (
        esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario)
        and candidata in diccionario
    ):
        if candidata not in palabrasAcertadas:
            palabrasAcertadas.append(
                candidata
            )  # Agrega la palabra a la lista de palabras acertadas

            return Puntos(candidata)
        else:
            return 0
    else:
        return -1


# chequea que la letra seleccionada esté dentro de la palabra, use solo letras de la pantalla y exista en el diccionario
def esValida(letraSeleccionada, letrasEnPantalla, candidata, diccionario):
    if letraSeleccionada not in candidata:
        return False
    if not set(candidata).issubset(set(letrasEnPantalla)):
        return False
    if candidata not in diccionario:
        return False
    return True


# devuelve los puntos
def Puntos(candidata):
    longPalabra = len(candidata)

    if longPalabra == 3:
        val = 1
        sonidosVarios(val)
        return 1
    elif longPalabra == 4:
        val = 1
        sonidosVarios(val)
        return 2
    elif longPalabra == 7:
        val = 1
        sonidosVarios(val)
        return 10
    elif longPalabra == 5 or longPalabra == 6:
        val = 1
        sonidosVarios(val)
        return longPalabra
    else:
        val = 0
        sonidosVarios(val)
        return 0


# busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    palabras_correctas = []
    for palabra in diccionario:
        if esValida(letraPrincipal, letrasEnPantalla, palabra, diccionario):
            palabras_correctas.append(palabra)
    return palabras_correctas


# sonidos que se ejecutan con palabras correctas e incorrectas EXTRA
def sonidosVarios(valores):
    if valores == 1:
        sonidoCorrecto = pygame.mixer.Sound("Sonidos/woohoo-text-sms.mp3")
        sonidoCorrecto.set_volume(0.8)
        sonidoCorrecto.play()

    elif valores == 0:
        sonidoIncorrecto = pygame.mixer.Sound("Sonidos/perder-incorrecto-no-valido.mp3")
        sonidoIncorrecto.set_volume(0.8)
        sonidoIncorrecto.play()
