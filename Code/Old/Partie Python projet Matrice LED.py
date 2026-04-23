import machine 
import network 
import socket 
from time import sleep
import neopixel

PIN_MATRICE = 4     # GPIO utilisé
NB_LEDS = 16        # matrice 4x4
COULEUR = (22, 50, 66)

pixel_alterne = [1,4,7,10,12,15]

led = neopixel.NeoPixel(machine.Pin(PIN_MATRICE), NB_LEDS)

sleep(2)

def matrice_off():
    for i in range(NB_LEDS):
        led[i] = (0, 0, 0)
    led.write()

def matrice_on():
    for i in range(NB_LEDS):
        led[i] = COULEUR
    led.write()
    
def matrice_alternee():
    matrice_off()
    for LED_on in pixel_alterne:
        led[LED_on] = COULEUR
    led.write()