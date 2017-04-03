---
title: Changing OLED Settings
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 5
---

## Changing the Display's Behavior {#maker-kit-oled-change-settings}

In this expriment, we will use text-based input from the user to change the OLED display's settings. We'll be scrolling the display contents as well as dimming and inverting the display colours, let's jump in.

### The OLED's Settings

The OLED configurations which we will adjust are:

  * Screen brightness
  * Color inversion
  * Horizontal & diagonal scrolling

The brightness refers to the intensity at which the pixels of the display are illuminated. The brightness can be set to value between `0` and `255`, from complete darkness to maximum brightness. By default the brightness is set to `207`. Just like on a phone or laptop, reducing the brightness will decrease the energy draw of the screen, increasing battery life.

<!-- // DONE: GIF of min brightness to max brightness -->
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/2fx-JNhYsno" frameborder="0" allowfullscreen></iframe>


Color inversion refers to switching all of the illuminated pixels to dark and all of the dark pixels to illuminated, giving us a kind of negative image.

<!-- // DONE: GIF of normal -> inverted -->
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xq2GpoNDItE" frameborder="0" allowfullscreen></iframe>

<!-- // DONE: beginner users won't be clear on the meaning of 'wrapping fashion' -->
The scrolling setting allows you to scroll the contents of the screen in either the horizontal or diagonal direction.

<!-- // DONE: GIF of content scrolling on OLED screen -->
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/51ZgFM746mA" frameborder="0" allowfullscreen></iframe>


### Building the Circuit

Plug your Omega2 and the OLED Expansion into the Expansion Dock like in the previous expriment and let's get started!

### Writing the Code

The code we'll write for this experiment is going to go a bit more in depth into the workings of the OLED screen. We'll take a look at all the utility functions of [the `oledExp` class](https://docs.onion.io/omega2-docs/relay-expansion-python-module.html) and how they modify the screen and its contents. Specificically, we'll be fiddling with the brightness, inverting the display, and scrolling the contents.

To make it happen, create a file called `MAK05-oledChangeSettings.py` and paste the following code in it:

```python
from OmegaExpansion import oledExp

# global variable that stores if the screen is in the inverted color mode or not
bInvert = 0

# This functions toggles the inverted color state of the OLED screen - if it's regular, it will invert it, if it's inverted, it will reset to regular
def toggleColor():
	global bInvert
	if(bInvert == 0):
		bInvert = 1
	else:
		bInvert = 0
	oledExp.setDisplayMode(bInvert)

# This function prints all the commands available to change the settings of the screen
def printCommands():
	print "Enter any of the following to change display"
	print "toggleColor: This will invert the color setting of the display"
	print "dimDisplay : This will dim the brightness of the display"
	print "brightenDisplay: This will brighten the display"
	print "scrollHorizontal : This will scroll display to the left"
	print "scrollDiagonal: This will diagonally scroll the display up to the right"
	print "scrollStop: This will stop the scroll"


# This function sets the brightness of the display to the lowest possible - 0
def dimDisplay():
	lowIntensity = 0
	oledExp.setBrightness(lowIntensity)

# Sets the brightness of the display to max when called
def brightenDisplay():
	highIntensity = 255
	oledExp.setBrightness(highIntensity)

# Scrolls the entire to the left at a speed of 5 frames
def scrollHorizontal():
	oledExp.scroll (0, 0, 0, 7)


# Scroll the entire screen upwards to the left at 5 frames per second
def scrollDiagonal():
	oledExp.scrollDiagonal(0, 5, 0, 128-1, 1, 0, 8-1)

# Stops scrolling the screen - note it doesn't reset the screen to the original state!
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
	# initialize the OLED Expansion
	oledExp.driverInit()

	# Lists out all the commands available
	printCommands()

	# This loop first captures raw input, and then attempts to run the function that is typed by the user by looking it up in the 'commandFunctions' dictionary above
	while(True):
		userInput = raw_input(">> ")
		try:
			# run the function based on the user's input
			commandFunctions[userInput]()
		except KeyError as e:
			pass

if __name__ == '__main__':
	main()
```

Save it to the root directory on your Omega, and run `python /root/MAK05-oledChangeSettings.py` to see it in action.

### What to Expect

When you run the program, the different possible commands that can be entered will be printed out on the command line. The commands will interactively change the display settings. For example, to dim the display, enter `dimDisplay`.

To stop the program enter `Ctrl+C`

Here it is running on our setup:

<!-- // DONE: IMAGE Add gif -->
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/uuJDwl7Fg6w" frameborder="0" allowfullscreen></iframe>


### A Closer Look at the Code

In this script, we use the lookup table once again to codify valid inputs. However this time, we're reading arbitrary input from the command line. This means we'll have to do some **error checking**. Additionally, we're operating with more interactivity now, so some sort of **user interface** is required to help the user with entering correct commands.

#### Error Checking

User input is a core part of any product - from cars to carpets. For this expriment, we use Python's command line as the source of user input. In Python, we can request input via the `raw_input()` function. This function pauses the Python interpreter and reads keyboard commands until it sees the enter key being pressed (in most languages it's represented by the return character, `\n`). Reading user input doesn't help much if we can't interpret it and then perform the desired actions. This is where error checking becomes necessary.

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

<!-- // DONE: make it something like 'the next expriment on displaying images on the OLED further builds on this concept.' -->
If you want to learn more about user input, the next expriment ([displaying images on the OLED](#drawing-on-the-oled-screen)) builds right on this concept.

#### User interface

<!-- // DONE: the content here is decent, but the writing could use some work. Let's be more descriptive about user interfaces. the first sentence is esp weak -->

A user interface is the main way we interact with software. Here, the user interface is the list of commands we output and the prompt we print afterwards (`>>`). The command list lets us know what we can do here, and the prompt lets us know where our input will happen.

Why don't we print out 'type in your command, and then press enter to send it'? There's a hint already present in the list of commands - 'Enter the following...' implies we'll have to enter some text. Additionally, just like smart-phone apps don't need to tell us to touch the screen, we already know the context requires text-based input because we ran our program in the commandline!

Having you UI communicate clearly and effectively is important not only if you want to share your work, but also for future-you! When you make a cool project and come back to it later, you could have forgotten how to use it - having a clear and concise UI can let you know how to make your project work even if you don't remember at all.

### Comments

For developers another major way to communicate is through the code itself - with comments! The code above is sprinkled with comments that try to describe what each piece is doing. So even if just the source code is presented, we can get some understanding of how the program works by reading the comments.

<!-- // DONE: add a note about how the same goes for comments in your code! -->

Next time, we [draw some lines](#maker-kit-oled-displaying-images).
