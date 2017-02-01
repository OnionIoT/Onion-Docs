---
title: Changing OLED Settings
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 5
---

## Changing the Display's Behavior {#changing-the-displays-behaviour}

This tutorial will show how to change how the OLED displays based on text-based user input. We'll be scrolling the display contents as well as dimming and inverting the display, let's jump in.

### The OLED's Settings

 The OLED settings which we will adjust are:
  * brightness
  * color inversion
  * horizontal+diagonal scrolling

The brightness refers to the intensity that a given pixel can be illuminated at. The brightness can be set to value between `0` and `255`, from complete darkness to maximum brightness. By default the brightness is set to `207`.

Color inversion refers to setting all illumating pixel to dark and vice versa.

The scrolling setting allows you to move the content across the screen in a wrapping fashion in either the horizontal or diagonal direction.

### Building the Circuit

Plug your Omega2 and the OLED Expansion into the Expansion Dock like in the previous tutorial.

#### Writing the Code

Create a file called `oledChangeSettings.py` and paste the following code in it:

``` python
from OmegaExpansion import oledExp
bInvert = 0

def toggle():
	global bInvert
	if(bInvert == 0):
		bInvert = 1
	else:
		bInvert = 0

def printCommands():
	print "Enter any of the following to change diplsay"
	print "toggleColor: This will invert the color setting of the display"
	print "dimDisplay : This will dim the brightness of the display"
	print "brightenDisplay: This will brighten the display"
	print "scrollHorizontal : This will scroll display to the left"
	print "scrollDiagonal: This will diagonally scroll the display up to the right"
	print "scrollStop: This will stop the scroll"

def toggleColor():
	toggle()
	oledExp.setDisplayMode(bInvert)

def dimDisplay():
	lowIntensity = 0
	oledExp.setBrightness(lowIntensity)

def brightenDisplay():
	highIntensity = 255
	oledExp.setBrightness(highIntensity)

def scrollHorizontal():
	# Scrolls the entire to the left at a speed of 5 frames
	oledExp.scroll (0, 0, 0, 7)

def scrollDiagonal():
	# Scroll the entire screen upwards to the left at 5 frames per second
	oledExp.scrollDiagonal(0, 5, 0, 128-1, 1, 0, 8-1)

def scrollStop():
	oledExp.scrollStop()

commandFunctions  = {
    'toggleColor': toggleColor,
    'dimDisplay': dimDisplay,
    'brightenDisplay': brightenDisplay,
    'scrollHorizontal': scrollHorizontal,
    'scrollDiagonal': scrollDiagonal,
    'scrollStop': scrollStop
}

def main():
	oledExp.driverInit()
	oledExp.write("Test Message")
	printCommands()
	while(True):
		userInput = raw_input(">> ")
		commandFunctions[userInput]()

if __name__ == '__main__':
	main()
```

#### What to Expect


When you run the program, the different possible commands that can be entered will be printed out on the command line. The commands will interactively change the display settings. For example, to dim the display, enter `dimDisplay`.

To stop the program enter `ctrl`+`c`

<!-- // TODO: IMAGE Add gif -->

### A Closer Look at the Code

In this code we used a dictionary structure to call a particular function based on the input. This is advantageous to us, because we don't need an if statement to decide which function to call based on input.

// TODO: reading user input was introduced in 03, so remove it from here
#### Reading User Input

Python allows us the ability to receive user input from the command line via the `raw_input()` function. Adding user input functionality can create an interactive user experience, where the program does different things depending on the input argument. If you want to learn more about user input, the [displaying images on the OLED](#drawing-on-the-oled-screen) tutorial developes this further.
