# Summary

### Pokemon Insurgence GUI automation with python

This is a GUI automation script build for finding a shiny starter pokemon in the 
community made pokemon insurgence video game.

Currently This only works with 1080p monitors since your mouse is moved and screen shots are taken at 
predefined locations based on a hight and width of a 1080p monitor.

This script forces certain mouse and keyboard inputs. You can not use your computer and this script at 
the same time and expect it to work properly.

This has not been tested on Mac or Linux but it should work.

# Installation
YOU MUST HAVE PYTHON 3 INSTALLED

### Install dependencies 
```pip install -r requirements.txt```

or

```python -m pip install -r requirements.txt```

or

```py -m pip install -r requirements.txt```

# Use

### Setup before using the script

By default this script assumes you have your in game text speed set to insane and your game speed
set to max (press m on the keyboard to cycle through the pokemon game speeds. Red is fastest.)

Make sure size of window is Normal.

Make sure you have saved the game in front of the starter pokeball you want
and that you have saved the game after setting up your game speed settings and window size settings.

### Using the script

Start Pokemon Insurgence Game.

Go through the start menu and load your save file so you are in front of the pokeball you want.

Move game window to upper left corner of your screen. It wont snap there but try to line it up.

Start script and wait.  

### Run:  
```python shiny_starter_finder.py```

or

```py shiny_starter_finder.py```

### Run with debugging:  

LOTS OF IMAGES WILL BE WRITTEN TO YOUR DIRECTORY. 

21 to be exact. 1 of those images will be overwritten constantly throughout the time the script is running.

```python shiny_starter_finder.py debug```

or

```py shiny_starter_finder.py debug```

If debug mode is on, image files will be saved in the directory and these can be used to trouble shoot issues.


This script will use keyboard inputs to select the pokemon and then screen shot the sprite after the pokemon 
appears behind your character. The initial phase of the script will capture a screen shot of the pokemon that 
it will be compared over and over again to new screen shots of the pokemon after the game restarts. 
If the screen shots are different, then something in the image has changed, you might have a shiny. YAY.

In your terminal press the key combination ctrl + c (ctrl and c) to quit the script.

# Advanced Use and Customization

If you want to play around with different game speeds you can change the speed 
variable in the ```if __name__ == "__main__"``` function. speed = 1 works well with the games default speed settings.
While it makes sense to have to deafult speed of the script be the default speed of the game, I made the script run faster by default
because it encourges users to run there game faster which decreases the time it takes to find a shiny pokemon.

If you have a different sized monitor, you can adjust the location of the screen 
shot by changing the monitor variables int the screen_shot function. Run in debug mode
so the screen shots will be written out to a file so you can view them. Make sure the 
pokemon is in the image.
