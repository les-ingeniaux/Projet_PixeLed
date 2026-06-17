"""
Ce code est le point d'entrée de votre PixeLed
Il se connecte au réseau Wi-Fi et initialise le serveur.
A vous de le compléter pour qu'il se charge de l'animation des LEDs
"""

from time import sleep
import wifiEtServeur
import state
from neopixel import NeoPixel
from machine import Pin
nb_pixels = 64
mesLeds = NeoPixel(Pin(4), nb_pixels)

ssid = 'LesIngeniaux'
password = 'IngX27rpG#$'

wifiEtServeur.connect(ssid,password)
wifiEtServeur.init()



while True:
    if state.allumage == 1:
        xy=(state.x+1)+(state.y)*8-1
        mesLeds[xy] = (state.rouge, state.vert, state.bleu) 
        mesLeds.write()

    wifiEtServeur.poll()


