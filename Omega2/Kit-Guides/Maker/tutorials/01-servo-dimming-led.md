---
title: Dimming LEDs with the Servo
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---


# Dimming LEDs with the PWM Expansion

In this tutorial, we will be learning how to use the PWM Expansion with python and animating 16 LEDs along the way. To do this we will create a generic class for all channels on the PWM Expansion, and instantiate many channel specfic objects of that class to control 16 individual LEDs.


## What is Pulse Width Modulation?

<!-- pwm -->
```{r child = '../../shared/pwm.md'}
```

## Building the Circuit

// 16 LEDs connected to the Servo Expansion

Connect the cathodes of the LED serially through a resistor to the signal pin of the desired pwm channel and connect the LEDs anode to the omega's ground.

### Hooking up the Components

// 16 example of the most basic LED circuit
// - use M-F jumper wires to connect from the servo expansion
// - make sure to use 5V from the pwm expansion channel header


## Writing the Code

Prior to running the code you will need to have python and the OmegaExpansion libraries installed. You can install with the following commands

```
opkg update
opkg install python-light
opkg install pyPwmExp
```
Run the following python code and observe your LEDS
```
from OmegaExpansion import pwmExp
import math
import time

SERVO_FREQUENCY = 2000
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

### What to Expect

// explanation of the something interesting that you decide to do, add a gif

You should see a wave like effect across the LEDs when they are placed beside each other.


### A Closer Look at the Code

// making a new class - this should be familiar if you've gone through all of the starter kit experiments

We are making a generic class for a pwm channel. This generic class has one function, `setDutyCycle` that sets the particular duty cycle on the particular channel that the class has been instantiated with.


#### Using the Onion PWM Expansion Python Module

// introduce the pwm module, written by Onion to facilitate easy usage of the pwm expansion
// give a brief overview of the functions that we used and point them to the documentation reference (need to include docs.onion.io link, not markdown tag)

// description of how we use it here, in an array, talk about arrays a little bit

We are using the pwm module written by onion to easily control the pwm expansion. The module comes with a set of functions to control and modify the pwm expansion channels and properties. To read more about the module refer to the link //TODO: ADD LINK TO PWM LIBRARY IN PYTHON DOC.

#### Creating a class

As a refresher, in Object Oriented Programming, classes are essentially templates or an abstraction. An object is a unique instantiation of a given template with its own unique properties. As an example, a "four sided polygon" may be a class, and an instantiation or object of that class may be a "square".

To see another example of another example of classes in python, check out the shift register article where we first introduced //TODO:HYPERLINK TO SHIFT REGISTER ARTICLE.

In our case, wes are making a generic class for a pwm channel. This generic class has one function, `setDutyCycle` that sets the particular duty cycle on the selected channel that the class has been instantiated with. Once we instantiate each of the objects we store the objects inside of a list, such that their index corresponds to the channel number. This makes our coding a little simpler.

#### Initializing the PWM Expansion

If you look at the constructor, you will notice the line:
```
pwmExp.driverInit()
```
This line initializes the pwm expansion for usage. This starts the oscillator on the Pwm expansion which is necessary to produce the pwm signals
