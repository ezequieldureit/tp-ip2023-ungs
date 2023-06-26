from configuracion import *
import random
import pygame

pygame.mixer.init()


# Lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario=[]):
    with open("data/diccionario.txt", "r") as archivo:
        palabras = [palabra.strip() for palabra in archivo]
    diccionario.extend(palabras)
    return diccionario


# Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante difícil (kxyz)
def dame7Letras():
    vocales = "aeiou"
    consonantes = "bcdfghjlmnpqrstvw"
    letras_dificiles = "kxyz"

    # Seleccionar 1 o 2 vocales al azar sin repetir
    num_vocales = random.randint(1, 2)
    letras_vocales = random.sample(vocales, num_vocales)

    # Seleccionar el resto de letras como consonantes sin repetir
    num_consonantes = (
        7 - num_vocales - 1
    )  # Se reserva espacio para una posible letra difícil
    letras_consonantes = random.sample(consonantes, num_consonantes)

    # Agregar una letra difícil al azar con una probabilidad del 50%
    if random.random() < 0.5:
        letras_consonantes.append(random.choice(letras_dificiles))
    else:
        num_consonantes += (
            1  # No se agregó una letra difícil, se recupera el espacio reservado
        )

    # Seleccionar una letra aleatoria para llenar el espacio restante
    letras_restantes = letras_vocales + letras_consonantes
    letras_finales = letras_restantes + random.sample(
        vocales + consonantes, 7 - len(letras_restantes)
    )

    # Combinar las letras de forma aleatoria
    random.shuffle(letras_finales)

    return "".join(letras_finales)


# Elige una letra de las letras en pantalla
def dameLetra(letrasEnPantalla):
    return random.choice(letrasEnPantalla)


# Verifica si la letra seleccionada está dentro de la palabra, usa solo letras de la pantalla y existe en el diccionario
def esValida(letraSeleccionada, letrasEnPantalla, candidata, diccionario):
    if letraSeleccionada not in candidata:
        return False
    if not set(candidata).issubset(set(letrasEnPantalla)):
        return False
    if candidata not in diccionario:
        return False
    return True


# Procesa la palabra ingresada por el usuario y devuelve la puntuación
# Si la palabra es válida y no ha sido acertada anteriormente, se agrega a la lista de palabras acertadas
def procesar(
    letraPrincipal,
    letrasEnPantalla,
    candidata,
    diccionario,
    palabrasAcertadas,
    DIFICULTAD,
):
    if (
        esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario)
        and candidata in diccionario
    ):
        if candidata not in palabrasAcertadas:
            palabrasAcertadas.append(candidata)
            return Puntos(candidata, DIFICULTAD)
        else:
            return 0
    else:
        return -1


# Asigna una puntuación a una palabra en función de su longitud y la dificultad seleccionada
def Puntos(candidata, DIFICULTAD):
    longPalabra = len(candidata)
    puntos = 0

    # Configuración de puntuación para la dificultad EASY
    if DIFICULTAD == "easy":
        if longPalabra == 3:
            puntos = 1
        elif longPalabra == 4:
            puntos = 2
        elif longPalabra == 7:
            puntos = 10
        elif longPalabra == 5 or longPalabra == 6:
            puntos = longPalabra
        elif longPalabra >= 8:
            return 0

    # Configuración de puntuación para la dificultad MEDIUM
    elif DIFICULTAD == "medium":
        if longPalabra == 3:
            puntos = 1
        elif longPalabra == 4:
            puntos = 2
        elif longPalabra == 7:
            puntos = 7
        elif longPalabra == 5 or longPalabra == 6:
            puntos = 4
        elif longPalabra >= 8:
            return 0

    # Configuración de puntuación para la dificultad HARD
    elif DIFICULTAD == "hard":
        if longPalabra == 3:
            puntos = 1
        elif longPalabra == 4:
            puntos = 1
        elif longPalabra == 7:
            puntos = 5
        elif longPalabra == 5 or longPalabra == 6:
            puntos = 3
        elif longPalabra >= 8:
            return 0

    sonidosVarios(puntos)
    return puntos


# Busca en el diccionario las palabras correctas que se pueden formar con la letra principal y las letras en pantalla
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    palabras_correctas = []
    for palabra in diccionario:
        if esValida(letraPrincipal, letrasEnPantalla, palabra, diccionario):
            palabras_correctas.append(palabra)
    return palabras_correctas

# Funcionales adicionales

# Reproduce sonidos correspondientes a palabras correctas o incorrectas
def sonidosVarios(valores):
    if valores >= 1:
        sonidoCorrecto = pygame.mixer.Sound("assets/sounds/woohoo-text-sms.mp3")
        sonidoCorrecto.set_volume(0.5)
        sonidoCorrecto.play()

    elif valores <= 0:
        sonidoIncorrecto = pygame.mixer.Sound(
            "assets/sounds/perder-incorrecto-no-valido.mp3"
        )
        sonidoIncorrecto.set_volume(0.5)
        sonidoIncorrecto.play()


# Evita que el usuario repita palabras correctas
def correctas(
    palabrasAcertadas, letraPrincipal, letrasEnPantalla, candidata, diccionario
):
    if not candidata in palabrasAcertadas:
        if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
            palabrasAcertadas.append(candidata)
