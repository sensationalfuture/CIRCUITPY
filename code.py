import time
import board
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)


def fade_RGB(brightness = 0.3, flash = False, delay = 0):
    fade_x = 0
    fade_y = 0
    fade_z = 255
    print("start fade_RGB", brightness)
    pixel.brightness = brightness
        
    for i in range(0,255):
        pixel.brightness = brightness
        fade_z-=1
        fade_x+=1
        time.sleep(delay)
        pixel.fill((fade_x, fade_y, fade_z))
        if flash:
            pixel.brightness = 0
    for i in range(0,255):
        pixel.brightness = brightness
        fade_y+=1
        fade_x-=1
        time.sleep(delay)
        pixel.fill((fade_x, fade_y, fade_z))
        if flash:
            pixel.brightness = 0
    for i in range(0,255):
        pixel.brightness = brightness
        fade_y-=1
        fade_z+=1
        time.sleep(delay)
        pixel.fill((fade_x, fade_y, fade_z))
        if flash:
            pixel.brightness = 0
        return 0

def full_Bright():
    print("start full_Bright")
    pixel.brightness = 1
    pixel.fill((255,255,255))
    time.sleep(0.5)
    pixel.fill((0,0,0))
    return 0

def SOS():
    print("start SOS")
    full_Bright()
    time.sleep(1)
    full_Bright()
    time.sleep(0.25)
    full_Bright()
    time.sleep(0.25)
    full_Bright()
    time.sleep(0.25)
    full_Bright()
    time.sleep(1)
    return 0

def Strobe(times = 50):
    print("start Strobe", times)
    pixel.brightness = 1
    for i in range(0,times):
        pixel.fill((255,255,255))
        time.sleep(0.01)
        pixel.fill((0,0,0))
        time.sleep(0.1)

    return 0

def fade_to_white(brightness = 0.3):
    x = 0
    y = 0
    z = 0

    pixel.brightness = brightness

    print("start fade_to_white", brightness)
    for i in range(0,255):
        pixel.fill((x, y, z))
        x+=1
    for i in range(0,255):
        pixel.fill((x, y, z))
        y+=1
    for i in range(0,255):
        pixel.fill((x, y, z))
        z+=1
    return 0
        
    
while True:
    print("start show")
    full_Bright()
    time.sleep(1)
    fade_RGB(1, True, 0.05)
    time.sleep(1)
    Strobe(100)
    time.sleep(1)
    full_Bright()
    time.sleep(1)
    SOS()
    time.sleep(1)
    fade_RGB()
    time.sleep(1)
    fade_RGB()
    time.sleep(1)
    Strobe()
    time.sleep(1)
    fade_to_white(1)
    print("end show")


