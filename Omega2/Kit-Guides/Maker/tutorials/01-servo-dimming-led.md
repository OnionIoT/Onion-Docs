---
title: Dimming LEDs with the Servo
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---


## Dimming LEDs with the PWM Expansion

In this tutorial, we will be learning how to use the PWM Expansion with python and animating 16 LEDs along the way. We'll be wiring the LEDs to the PWM expansion through the breadboard, then we'll write some code to light up the LEDs for a mini light show.


<!-- pwm -->
```{r child = '../../shared/pwm.md'}
```

### Building the Circuit

// 16 LEDs connected to the Servo Expansion

For this circuit, we will connect one LED to each of the 16 channels (0-15) on the PWM Expansion. Using the breadboard here will keep things organised.

#### What You'll Need

* 1x Breadboard
* 1x PWM Expansion
* LEDs
	* 16x any color
* Jumper Wires
	* 16x M-M
	* 16x M-F
	* 16x F-F
* Resistors
	* 16x 200 Ohm


#### Hooking up the Components

// 16 example of the most basic LED circuit
Each LED will be connected to the board in the same way, so we'll cover wiring a single LED here the n you can repeat this proccess for all 16 and you should be good to go.

1. Find the anode of the LED and the signal pin of any channel, we started at chanel 0 (`S0` on the expansion board) to avoid confusion. 
	* The signal pin is the only pin out of the three with a white base, for channel `S0`, it should be clearly labelled to the left side, we'll call this the **SIG** pin in the future
1. Stake out three rows in your breadboard - we'll used these to connect the LED and resistor together, and lead them to the PWM Expansion
1. Stick the LED into two rows out of the three, we started at row 1 and 2 on the A-E side. We chose to stick the anode into the lower numbered row for consistency.
1. Connect the anode row (row 1 for our first LED) to the SIG pin with a male-to-female jumper wire.
	* Connect the male end to any column in row 1 of your breadboard.
	* Connect the female end to the SIG pin of channel 0 (`S0`) of the PWM expansion.
1. Take a resistor and bend both pins so it forms a really square 'U' shape. Plug the two ends one into row 2, and one into row 3. Your circuit should look something like this:
// TODO: IMAGE picture and/or circuit diagram
1. Take one male-to-male and one female-to-female jumper wire, and connect them to form one long male-to-female jumper.
1. Connect the franken-jumper between row 3 and the ground pin (we'll call this **GND** in the future) of `S0` on the PWM expansion, it is the pin labelled `GND`, and the one furthest from the `SIG` pin

Now we're all set!

Here's a photo of our finished circuit:
// TODO: IMAGE photo of finished circuit
// - use M-F jumper wires to connect from the servo expansion
// - make sure to use 5V from the pwm expansion channel header


### Writing the Code

Prior to running the code you will need to have python-light and the OmegaExpansion libraries installed. You can install with the following commands

```
opkg update
opkg install python-light
opkg install pyPwmExp
```
Run the following python code and observe your LEDS.
```
from OmegaExpansion import pwmExp
import math
import time

SERVO_FREQUENCY = 1000
class pwmPin:
	def __init__(self,channel):
		self.channel = channel
		self.frequecy = SERVO_FREQUENCY
		bInit = pwmExp.checkInit()
		if (bInit == 0):
			ret = pwmExp.driverInit()
			if (ret != 0):
				print "Error initializing expansion"
			else:
				bSetFrequency = pwmExp.setFrequency(SERVO_FREQUENCY)
				if(bSetFrequency != 0):
					print "Error setting oscillator frequecy"

	def setDutyCycle(self,dutyCycle):
		ret = pwmExp.setupDriver(self.channel, dutyCycle, 0)
		if(ret != 0):
			print "Error setting channel duty cycle"

def calcDutyCycle(rad):
	result = 50.0*(math.sin(rad)) + 50.0
	if(result > 100.0):
		result = 100.0
	if(result < 0.0):
		result = 0.0
	return result

def main():
	# Construct pwmLED object array
	ledObjectArray = []
	for i in range(16):
		obj = pwmPin(i)
		ledObjectArray.append(obj)

	# Construct pwmLED wave array:

	phaseIncrement = (2 * math.pi)/16
	actualIncrement = (2 * math.pi)/160
	i = 0
	while(True):
		for idx,element in enumerate(ledObjectArray):
			element.setDutyCycle(calcDutyCycle(((idx)*phaseIncrement)+(i*actualIncrement)))
		i = i + 1
		time.sleep(.005)

if __name__ == '__main__':
	main()
```

#### What to Expect

// TODO: IMAGE add gif/video of LEDs working

You should see a wave like effect across the LEDs when they are placed beside each other in order from 0 to 15.


### A Closer Look at the Code

This code does two major things, first it it specifies a generic class for a PWM channel. This generic class has one function, `setDutyCycle` that sets the particular duty cycle on the particular channel that the class has been instantiated with. By creating an object for each output channel, we can set the brightness of each LED individually.

Some points of interest here:

* Creating objects from classes
* Using the PWM Python Module


#### Creating a class

As a refresher, in Object Oriented Programming, classes are essentially blueprints or an abstraction. An object is a collection of data made according to the class blueprint with its own unique properties. For example, for a class created as "four sided polygon", an object created from this class may be "square". Creating an object is often called 'instantiation' and an object can alternatively be called an 'instance'

To see another example of another example of classes in python, check out the [shift register](// TODO: LINK TO SHIFT REGISTER ARTICLE.) article where we first introduced classes.

In our case, wes are making a class for a PWM channel. This class represents a single PWM output channel, and objects of this class will represent and control an actual PWM channel on the board. The function `setDutyCycle` sets the particular duty cycle on whichever channel the object represents. Once we instantiate each channel object we store the objects inside of a list, such that their index corresponds to the channel number. This makes our coding a little simpler.


#### Using the Onion PWM Expansion Python Module

Python's functionality can be expaned with modules and packages - like extra lego sets allowing you to build more complex things. Here we use the PWM module (pyPwmExp) to control the PWM expansion. The module comes with a set of functions to control and modify the PWM expansion channels and properties. By running a script to control the expansion, you don't need to manually need to enter or trigger any commands through the terminal. You can simply leave it running, and it would automatically do its job! 

To find a detailed description of the module, refer to [pyPwmExp library](//TODO: LINK TO PWM LIBRARY IN PYTHON DOC) reference in the Onion docs.

Specifically, we use the following functions:

* `setFreqency()`
* `setupDriver()`
* `checkInit()`
* `driverInit()`

##### Controlling the PWM Outputs

In the code, you'll notice the servo frequency set to 1000Hz, this is to ensure the LED doesn't flicker no matter what duty cycle we set the channel to output. To accomplish this, we call `setFrequency()` and give it `SERVO_FREQUENCY` as the argument. For each channel, we can change the duty cycle on the fly by calling `setupDriver()` and sending it the channel and duty cycle number (recall this is between 0% and 100%), by changing the duty cycle, we change the average voltage sent to the LED connected to the channel - this is how the LEDs dim and brighten.


##### Initializing the PWM Expansion

If you look at the constructor (the `__init__` function), you will notice the line:
```
pwmExp.driverInit()
```
This line initializes the PWM expansion for usage. This starts the oscillator on the PWM expansion which actually produces the signals sent through the pins. 
