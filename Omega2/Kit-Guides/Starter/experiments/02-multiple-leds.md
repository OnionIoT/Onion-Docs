---
title: Controlling Many LEDs
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---

# Controlling Many LEDs

"We've blinked one LED sure, but what about a second LED?" 

In this experiment, we're going to use what we learned in the first experiment and wire up a bunch of LEDs. Then we're gonna make some visual effects.

## Building the Circuit

Let's dive right into building our circuit. It's going to be essentially the same thing as the first experiment, but repeated six times over!

// list of gpios that are going to be used: 0, 1, 2, 3, 18, 19



### Hooking up the Components

While the individual LEDs will be connected in exactly the same way as in the first experiment, we're going to be using the power rail on the breadboard to make the wiring a little simpler. You'll see what I mean in a second. 

Grab six LEDs and let's do the following for each one:
1. Plug in the LED into the breadboard, making sure to plug the anode and cathode into different rows.
2. Connect one end of a (// TO DO: figure out resistance)kΩ resistor to the the cathode row, and the other end into the power rail marked `-`

Now that you have all six LEDs plugged in, let's connect a jumper wire from the `-` power rail on the breadboard to a Ground pin on the Omega{{#if Omega2}}2{{/if}}. Since the power rail is connected vertically, what we've done is **connect all of the LED cathodes to the Ground on the Omega{{#if Omega2}}2{{/if}} using just one pin on the Expansion Dock!**

// TO DO: FRITZING: fritzing diagram of the experiment

To finish off the circuit, we need to connect the anodes of our LEDs to GPIOs on the Omega{{#if Omega2}}2{{/if}} using jumper wires. We'll be using GPIOs 0, 1, 2, 3, 18, and 19 to control our six LEDs. To make our lives easy when writing the code to control the circuit, wire the left-most LED to GPIO0, the next one to GPIO1, and so on, with the right-most LED connected to GPIO19.

The circuit diagram for our first experiment looks like this:
// TO DO: CIRCUIT DIAGRAM: circuit showing this experiment
Like I said, it's just six copies of our first experiment together.

## Writing the Code

// need to run omega2-ctrl gpiomux to put 18 and 19 in gpio mode

Here's where this experiment is different from the previous, the code we write will be significantly different since we now have five more LEDs to control. We'll also be making a little animation instead of just blinking!

Create a new file `lineUp.py` to hold the code:
``` python
import onionGpio
import time

# create and populate an array to hold the GPIO pin numbers that control the LEDs
gpioPins = [0, 1, 2, 3, 18, 19]
# create an empty array that will hold the GPIO objects to control the LEDs
gpioObjects = []	

# print which GPIOs are being used
print 'Using GPIOs:'
for gpioElement in gpioPins:
	print gpioElement

# populate the gpioObjects array
for gpioElement in gpioPins:
	ledObj = onionGpio.OnionGpio(gpioElement)		# instatiate a GPIO object for this gpio pin
	ledObj.setOutputDirection(0)		# set to output direction with zero being the default value
	gpioObjects.append(ledObj)	# add the GPIO object to our array

	// LAZAR: alternative code
	# add a GPIO object to the array that's initialized with the current GPIO pin number
	gpioObjects.append( onionGpio.OnionGpio(gpioElement) )
	# set the GPIO to the output direction
	gpioObjects[-1].setOutputDirection(0)


ledValue 	= 1

while 1:
	# program all of the GPIOs to the ledValue
	for gpio in gpioObjects:
		gpio.setValue(ledValue)
		thime.sleep(0.5)

	# flip the value variable
	if ledValue == 1:
		ledValue = 0
	else:
		ledValue = 1
```

And run the code:
```
python lineUp.py
```

### What to Expect

Your line-up of LEDs will be essentially chasing it's tail: the left-most LED will turn on, and then the next one, and the next and so on. When all of them turn on, the left-most one will turn off, and the rest will follow suit.

// TO DO: GIF: Showing this experiment with the LEDs lighting up one after another and then turning off one after another

This will repeat until you exit the program.

### A Closer Look at the Code

This program looks pretty different from the code in the first experiment, but it does very similar things, just for six LEDs this time. Let's take a look at some of the new stuff that was introduced.

#### Arrays

The very first line of code after importing the modules is new to us: it's creating an array. An array variable is a list of variables, with the ability to access each individual variable. A single variable in an array is referred to as an element. Arrays are a very common data structure used in programming and you'll soon see why. 

The `gpioPins` array is meant to hold the GPIO pin numbers that control our LEDs. So this array will hold a bunch of integers, and we're *populating* the array as soon as we declare it.

The `gpioObjects` array is a little different; we're going to be using it to hold six GPIO objects that will control the GPIOs to which our LEDs are connected. More on that a little later, for now, we're just creating it as an empty array.


#### For Loop

A `for loop` is used when you have code that needs to be repeated a known number of times, like in our example how we want to print each GPIO from our `gpioPins` array. The line that starts with `for` will define how many times the loop will be run, our example will run the loop body once for each element in the `gpioPins` array, with the value of the current element being stored in the `gpioElement` variable. The indented line below makes up the body of the loop, here we are only printing the contents of the gpio variable. 

The loop will go through the array from start to finish, with the `gpioElement` variable taking on the value of the current array element. We will see the following being printed:
```
Using GPIOs:
0
1
2
3
18
19
```

#### Arrays of Objects

The second `for loop` in the program is used to populate the `gpioObjects` array with objects of the GPIO class that will control the six GPIOs connected to the LEDs in our circuit. The loop will run for each of the elements in the `gpioPins` array, meaning for each of the GPIOs that we will be using. 

The loop body will instantiate an object of the GPIO class to control the GPIO pin the `gpioElement` variable contains and add it to the end of the `gpioObjects` array. It will also set each of the GPIOs to the output direction. 

By the end of the for loop, the `gpioObjects` array will contain six GPIO class objects, each setup to control one of the GPIOs listed in the `gpioPins` array.


#### For Loops Revisited

The very last `for loop` in the program will use the GPIO objects to turn the LEDs on or off to create our animation. It will loop through all of GPIO class objects in the `gpioObjects` array and use them to set the associated GPIO to the value in the `ledValue` variable. The first time through it will turn our LEDs on one by one: it will first set GPIO0 to `ledValue` (which was initialized to 1), and then GPIO1, then GPIO2, GPIO3, GPIO18, and finally, GPIO19. The half second delay was added so the animation is actually visible by the human eye.

Similar to the previous experiment, the code that changes the LED states is in an infinite loop, so once the for loop is completed, the `ledValue` variable will be changed to hold the opposite value, and the for loop will be repeated, this time turning the LEDs off one by one. This cycle will continue, turning the LEDs on, and then off until the program is terminated.


