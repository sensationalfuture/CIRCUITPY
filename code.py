import time
import board
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)


def fade_RGB(brightness = 0.3, flash = False, speed = 0):
    # This function takes arguments:
    # brightness: changes how bright the lights are going to appear
    # flash: changes whether the RGB fades in each loop with periodically flash, True/False
    # speed: speed between each color addition, i.e. how fast it fades from color to color

    # This function is an implementation of the rainbow() effect, utilizing loops for 
    # increasing both the red, green and blue elements of the neopixel in every loop. 
    # However, this function allows the colors to be turned on and off periodically 
    # using the flash argument

    fade_x = 0
    fade_y = 0
    fade_z = 255 # initially start it at 100% blue, so it subtracts in first loop
    print("start fade_RGB Brightness:", brightness, "Speed", speed)
    pixel.brightness = brightness
        
    # add more of red to neopixel, remove the initial blue
    for i in range(0,255):
        # how bright neopixel will be based on brightness argument, must be reset if flash = True
        pixel.brightness = brightness
        fade_z-=1
        fade_x+=1
        time.sleep(speed)
        pixel.fill((fade_x, fade_y, fade_z))
        # This if statement checks bool flash, makes light strobe periodically
        if flash:
            pixel.fill((0,0,0)) # flashes light, needs to turn off neopixel 
            time.sleep(0.05)     # short delay for neopixel

    # add more of green, remove red from earlier
    for i in range(0,255):
        pixel.brightness = brightness
        fade_y+=1
        fade_x-=1
        time.sleep(speed)
        pixel.fill((fade_x, fade_y, fade_z))
        if flash:
            pixel.fill((0,0,0))
            time.sleep(0.05)
    
    # add more of blue, remove green from earlier
    for i in range(0,255):
        pixel.brightness = brightness
        fade_y-=1
        fade_z+=1
        time.sleep(speed)
        pixel.fill((fade_x, fade_y, fade_z))
        if flash:
            pixel.fill((0,0,0))
            time.sleep(0.05)
        return 0

def full_Bright():
    # Function that fully turns on the neopixel to white
    print("start full_Bright")
    pixel.brightness = 1
    pixel.fill((255,255,255)) # white
    return 0

def SOS():
    # SOS function that flashes the white morse code sequence for SOS
    # uses the full_Bright() function to emitt light
    print("start SOS")
    full_Bright()
    time.sleep(1) # For - dash, long pulse
    pixel.fill((0,0,0))
    time.sleep(0.25) # For . dot, short pulse
    full_Bright()
    time.sleep(0.25)
    pixel.fill((0,0,0))
    time.sleep(0.25)
    full_Bright()
    time.sleep(0.25)
    pixel.fill((0,0,0))
    time.sleep(0.25)
    full_Bright()
    time.sleep(0.25)
    pixel.fill((0,0,0))
    time.sleep(1)
    full_Bright()
    time.sleep(1)
    pixel.fill((0,0,0))
    time.sleep(1)
    return 0

def Strobe(times = 50):
    # Strobes light periodically using full_Bright() function for white light
    # and uses loops and sleep function to strobe
    print("start Strobe", times)
    pixel.brightness = 1
    for i in range(0,times):
        full_Bright() # white
        time.sleep(0.01)
        pixel.fill((0,0,0)) # turns off light / black
        time.sleep(0.1)
    return 0

def fade_to_white(brightness = 0.3):
    # Transitions the light from red -> green -> white
    # Does this by using loops and adding more red, then more green, and finally blue
    # brightness argument sets brightness, default is 0.3

    # initial r,g,b variables to zero
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
        
def police_lights(bright = 1, delay = 0.1, times = 25):
    # alterates through police lights, with time.sleep(1)
    # being the delay between each flashing light
    pixel.brightness = bright
    for i in range(0, times):
        pixel.fill((255, 0, 0)) # red
        time.sleep(delay)
        full_Bright() # white
        time.sleep(delay) 
        pixel.fill((0,0,255))  # blue
        time.sleep(delay)
    return 0

def heartbeat(fade = False, steps = 50, bpm = 60):
    # This is the representation of the heartbeat, with the fade being its lifeforce
    # fade lowers the brightness after each iteration, calculating the step in brightness_step
    # steps are the amount of times the heartbeat shows in the neopixel + calculates the fade
    # bpm is how fast the heart is going, dividing 60 seconds by bpm to get the gap between beats
    pixel.brightness = 1
    brightness_step = 1/steps   # need to calculate step for the brightness
    bps = 60/bpm                # the actual delay between beats

    # Example: 60 bpm means 1 second per beat, or 1 bps

    for i in range(0,steps):
        if (fade == True):
            pixel.brightness -= brightness_step     #for each iteration, decrease brightness by step
        time.sleep(bps)
        pixel.fill((255,0,0))   # red
        time.sleep(bps)
        pixel.fill((0,0,0))     # black
    return 0
    
while True:
    print("start night")
    full_Bright()           # the start of the party, all lights first turn on
    time.sleep(1)
    fade_RGB(1, False, 0.01) # disco lights start being put on, party starts
    time.sleep(1)
    heartbeat(False, 5, 120) # normal heartbeat
    time.sleep(1)
    fade_to_white()         # something happenes in party, lights cut back to white
    time.sleep(1)
    Strobe(30)              # someone is having a medical issue
    time.sleep(1)
    SOS()                   # help is needed
    time.sleep(0.5)
    heartbeat(True, 5, 170)  # their heartbeat is too high and irregular, starts fading, someone is dying
    time.sleep(0.5)
    police_lights(times=10)  # police are called and the party stops
    time.sleep(0.5)
    print("end night")
    

