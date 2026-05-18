"""
Ce code est le point d'entrée de votre PixeLed
Il se connecte au réseau Wi-Fi et initialise le serveur. 
A vous de le compléter pour qu'il se charge de l'animation des LEDs
"""

from time import sleep
import utilitairesLed
import wifiEtServeur
import state

ssid = 'LesIngeniaux'
password = 'IngX27rpG#$'

wifiEtServeur.connect(ssid,password)
wifiEtServeur.init()
utilitairesLed.clear()


while True:
    if state.allumage == 1:
        pass
    else:
        utilitairesLed.clear()
    wifiEtServeur.poll()