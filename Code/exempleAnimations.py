from time import sleep
import utilitairesLed
import animations
import wifiEtServeur
import state

ssid = 'LesIngeniaux'
password = 'IngX27rpG#$'

wifiEtServeur.connect(ssid,password)
wifiEtServeur.init()
utilitairesLed.clear()

animations_list = [
    animations.animage_1,
    animations.animage_2,
    animations.animage_3,
    animations.animage_4
]
nbAnimages = len(animations_list)
compteurAnimation = 0

while True:
    if state.allumage == 1:
        print(compteurAnimation)
        animations_list[compteurAnimation]()
        sleep(0.25)
        compteurAnimation = (compteurAnimation+1) % nbAnimages
        
    else:
        utilitairesLed.clear()
    wifiEtServeur.poll()