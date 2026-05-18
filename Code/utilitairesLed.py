"""
Ce module contient des fonctions pour vous faciliter la manipulation de votre matrice de LEDs.
Vous êtes libres d'ajouter les fonctions que vous voulez, ou de modifier celles qui sont déjà écrites.
Pour vous en servir dans main.py, il vous suffit d'importer ce module en écrivant import utilitairesLed et d'appeler les fonctions avec utilitairesLed.nomDeLaFonction() 
Par exemple : utilitairesLed.clear() pour éteindre toutes les LEDs
"""


import machine
import neopixel
from time import sleep

NB_LEDS = 64
COULEUR = (22, 50, 66)
WIDTH = 8
HEIGHT = 8
NUM_PIXELS = WIDTH * HEIGHT

np = neopixel.NeoPixel(machine.Pin(4), NB_LEDS)

"""Cette fonction retourne la matrice de LEDs pour que vous puissiez la manipuler plus facilement dans main.py"""
def pixels()->neopixel.NeoPixel:
    return np

"""Cette fonction met toutes les LEDs à 0 et applique le résultat sur la matrice"""
def clear()->None:
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)
    np.write()

"""Cette fonction met toutes les LEDs à 0 sans l'appliquer sur la matrice, pour que vous puissiez faire d'autres modifications avant de les appliquer avec utilitairesLed.show()"""
def clearNoShow()->None:
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)


"""Cette fonction applique les modifications faites sur la matrice de LEDs"""
def show()->None:
    np.write()
    
