# Version complète du code - ne pas donner celle-ci aux élèves en début de projet :-)
from time import sleep

import wifiEtServeur
import state

import utilitairesLed
import images_fixes

ssid = 'LesIngeniaux'
password = 'IngX27rpG#$'

imageActuelle = 1
wifiEtServeur.connect(ssid,password)
wifiEtServeur.init()
utilitairesLed.clear()

while True:
    
    if state.allumage == 1:
        if state.imageActuelle == 1:
            images_fixes.dino()
        elif state.imageActuelle == 2:
            images_fixes.glace()
        else:
            images_fixes.ghost()
    else:
        utilitairesLed.clear()
    wifiEtServeur.poll()
