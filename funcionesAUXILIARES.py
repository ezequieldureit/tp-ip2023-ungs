from configuracion import *
import random


def lectura(diccionario=[]):
    archivos = [
        "diccionario1.txt",
        "diccionario2.txt",
        "diccionario3.txt",
        "diccionario4.txt",
    ]
    archivo_seleccionado = random.choice(archivos)

    with open(archivo_seleccionado, "r") as archivo:
        for palabra in archivo:
            palabra = palabra.strip()
            diccionario.append(palabra)

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


# chequea que se use la letra principal, solo use letras de la pantalla y
# exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    for i in range(len(candidata)):
        if candidata[i] not in letrasEnPantalla:
            return False
        if not candidata[0] == letraPrincipal:
            return False
        if candidata not in diccionario:
            return False
    return True


# devuelve los puntos
def Puntos(candidata):
    longPalabra = len(candidata)

    if longPalabra == 3:
        return 1
    elif longPalabra == 4:
        return 2
    elif longPalabra == 5 or longPalabra == 7:
        return longPalabra
    else:
        return 0


# busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    palabras_correctas = []
    for palabra in diccionario:
        if esValida(letraPrincipal, letrasEnPantalla, palabra, diccionario):
            palabras_correctas.append(palabra)
    return palabras_correctas
