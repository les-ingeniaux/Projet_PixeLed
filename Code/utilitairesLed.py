import machine
import neopixel
from time import sleep

NB_LEDS = 64
COULEUR = (22, 50, 66)
WIDTH = 8
HEIGHT = 8
NUM_PIXELS = WIDTH * HEIGHT

np = neopixel.NeoPixel(machine.Pin(4), NB_LEDS)

def pixels():
    return np

def xy_to_index(x, y):
    y = (HEIGHT - 1) - y
    x = (WIDTH - 1) - x
    return y * WIDTH + x

def clear():
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)
    np.write()

def clearNoShow():
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)

def set_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        np[xy_to_index(x, y)] = color

def show():
    np.write()
    
