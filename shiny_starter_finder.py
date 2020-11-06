import time
import sys

import numpy as np

import pynput

import mss
import mss.tools

from pynput.mouse import Button, Controller
from pynput import keyboard

from PIL import Image

mouse = pynput.mouse.Controller()

def select_pokemon(speed):
    time.sleep(.5)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(2/speed)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(1/speed)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(.5)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(.5)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(1/speed)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(1/speed)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(1/speed)
    keyboard.Controller().press(keyboard.Key.esc)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.esc)

def skip_through_startup():
    time.sleep(2)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(1)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(1)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(1)
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(.5)

def screen_shot(debug, fname):
    with mss.mss() as sct:
        #The region to capture
        monitor = {"top": 170, "left": 170, "width": 160, "height": 135}
        output = fname + ".png"

        #Screen shot
        sct_img = sct.grab(monitor)

        if debug == True:
            #Save the picture to a file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        img_arr = np.array(img)
        return img_arr


def setup(debug, speed):
    print("Setting up.")
    #Move mouse to game window and select window so it reads the keyboard
    mouse.position=(50,50)
    time.sleep(.2)
    mouse.press(Button.left)
    time.sleep(.2)
    mouse.release(Button.left)

    #select the pokemon 
    select_pokemon(speed)

    #Get screen shots for later comparison
    #We need multiple screen shots because of small variants in the timings
    # means the sometimes the pokemon sprite is in a different animation
    # state. If the initial image does not match the new one
    # taken when the find_shiny loop is running, it will stop the loop
    # in case there is a shiny pokemon.
    initial_img_arrs = list()
    for i in range(0, 20):
        initial_img_arrs.append(screen_shot(debug, "initial" + str(i)))

    #Restart the game
    time.sleep(1)
    keyboard.Controller().press(keyboard.Key.f12)
    time.sleep(.3)
    keyboard.Controller().release(keyboard.Key.f12)

    return initial_img_arrs

def find_shiny(initial_img_arrs, debug, speed):
    shiny_found = False
    count = 0

    while shiny_found == False:
        skip_through_startup()
        print("Started Game.")

        select_pokemon(speed)
        print("Selected Pokemon.")

        count += 1

        img_arr = screen_shot(debug, "check_shiny")

        print('Comparing to original to see if pokemon is shiny.')
        #Loop through the initial img set and see if any of them match the current screen shot
        #If there is a match found, then there is no shiny
        img_found = False
        for i in initial_img_arrs:
            if np.array_equal(i, img_arr, False):
                img_found = True

        print(f"Checked {count} pokemon so far.")
        
        #No matching image found, then there might be a shiny.
        if img_found == False:
            print("Possible shiny found, stoping script.")
            shiny_found = True
        else:
            #Restart the game
            time.sleep(.5)
            keyboard.Controller().press(keyboard.Key.f12)
            time.sleep(.3)
            keyboard.Controller().release(keyboard.Key.f12)

if __name__ == "__main__":
    debug = False
    speed = 5
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            debug = True
            print("Running in debug mode...")
    
    initial_img_arrs = setup(debug, speed)
    find_shiny(initial_img_arrs, debug, speed)
