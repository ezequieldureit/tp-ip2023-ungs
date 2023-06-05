from principal import *
from configuracion import *
import random
import math

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    return ['programacion', 'ungs', 'universidad', 'juego', 'palabras', 'laboratorio', 'cadenas', 'adanida', 'adrian', 'aduana', 'aduanar', 'adunar', 'adunia', 'adan', 'ahina', 'ana', 'anadina', 'anana', 'anda', 'andada', 'andadura', 'andana', 'andanada', 'andar', 'andarina', 'andarin', 'andriana', 'andrina', 'anidar', 'anidiar', 'anudadura', 'anudar', 'anuria', 'arana', 'arduran', 'arna', 'arnadi', 'arruinar', 'aran', 'aun', 'aunar', 'aina', 'aun', 'dan', 'dandi', 'diana', 'din', 'dina', 'dinar', 'dinarada', 'duna', 'durina', 'harina', 'hin', 'hindi', 'hindu', 'hirundinaria', 'hundir', 'inanidad', 'india', 'indiada', 'indiana', 'indinar', 'inri', 'inundar', 'irani', 'nada', 'nadadura', 'nadar', 'nadi', 'nadir', 'nahua', 'nana', 'narina', 'narra', 'narrar', 'narria', 'niara', 'nidada', 'nin', 'nudrir', 'nadir', 'nia', 'radian', 'rain', 'rana', 'randa', 'ranina', 'ranura', 'rin', 'rinran', 'ruana', 'ruin', 'ruina', 'ruinar', 'ruindad', 'runa', 'runrun', 'ruan', 'unidad', 'unir', 'urna']

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():
    return "diuahrn"

def dameLetra(letrasEnPantalla): #elige una letra de las letras en pantalla
    return "n"

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    return Puntos(candidata)

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    return True

#devuelve los puntos
def Puntos(candidata):
    return(5)

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    return ['adanida', 'adrian', 'aduana', 'aduanar', 'adunar', 'adunia', 'adan', 'ahina', 'ana', 'anadina', 'anana', 'anda', 'andada', 'andadura', 'andana', 'andanada', 'andar', 'andarina', 'andarin', 'andriana', 'andrina', 'anidar', 'anidiar', 'anudadura', 'anudar', 'anuria', 'arana', 'arduran', 'arna', 'arnadi', 'arruinar', 'aran', 'aun', 'aunar', 'aina', 'aun', 'dan', 'dandi', 'diana', 'din', 'dina', 'dinar', 'dinarada', 'duna', 'durina', 'harina', 'hin', 'hindi', 'hindu', 'hirundinaria', 'hundir', 'inanidad', 'india', 'indiada', 'indiana', 'indinar', 'inri', 'inundar', 'irani', 'nada', 'nadadura', 'nadar', 'nadi', 'nadir', 'nahua', 'nana', 'narina', 'narra', 'narrar', 'narria', 'niara', 'nidada', 'nin', 'nudrir', 'nadir', 'nia', 'radian', 'rain', 'rana', 'randa', 'ranina', 'ranura', 'rin', 'rinran', 'ruana', 'ruin', 'ruina', 'ruinar', 'ruindad', 'runa', 'runrun', 'ruan', 'unidad', 'unir', 'urna']
