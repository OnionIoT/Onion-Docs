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

Create a file called `MAK05-oledChangeSettings.py` and paste the following code in it:

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
		try:
			commandFunctions[userInput]()
		except KeyError as e:
			pass

if __name__ == '__main__':
	main()
```

#### What to Expect

When you run the program, the different possible commands that can be entered will be printed out on the command line. The commands will interactively change the display settings. For example, to dim the display, enter `dimDisplay`.

To stop the program enter `Ctrl+C`

<!-- // TODO: IMAGE Add gif -->

### A Closer Look at the Code

In this script, we use the lookup table once again to codify valid inputs. However this time, we're reading arbitrary input from the command line. This means we'll have to do some **error checking**. Additionally, we're operating with more interactivity now, so some sort of **user interface** is required to help the user with entering correct commands.

#### Error Checking

User input is a core part of any product - from cars to carpets. For this tutorial, we use Python's command line as the source of user input. In Python, we can request input via the `raw_input()` function. This function pauses the Python interpreter and reads keyboard commands until it sees the enter key being pressed (in most languages it's represented by the '\n' characters). Taking in user input doesn't help much if we can't interpret it and send the desired signals. This is where error checking becomes necessary.

If you typed in `asdf` to the command line when prompted, nothing would happen to the screen. This is expected behavior! If the code was not error checked, we'd see something entirely different. To try it out, replace the following section in the code:

``` python
		try:
			commandFunctions[userInput]()
		except KeyError as e:
			pass
```

With this:

``` python
		commandFunctions[userInput]()
```

If you did it 'right', the next time you run the code and enter an invalid command like `asdf`, the script should crash. The `try:/except:` structure prevents crashing by catching the error when it's 'thrown'. In effect, it lets you continue to type commands and change the behaviour of the OLED screen no matter how badly you mistyped them.

If you want to learn more about user input, the [displaying images on the OLED](#drawing-on-the-oled-screen) tutorial developes this further.

#### User interface

User interfaces are the way software communicates to us. Here, the user interface is the list of commands we output and the prompt we print afterwards (`>>`). These come together to communicate how the software can be operated. Having you UI communicate clearly and effectively is important not only if you want to share your work, but also for future-you! When you make a cool project and come back to it later, you could have forgotten how to use it - the UI will let you know how to operate it even if you don't remember at all.
