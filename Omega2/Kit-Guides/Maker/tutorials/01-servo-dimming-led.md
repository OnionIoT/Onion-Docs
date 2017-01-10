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

For this circuit, we will connect one LED to each of the 16 channels (0-15) on the PWM Expansion. 16 LEDs are required of any colour you wish along with 16 200Ohm resistors. Using the breadboard here will keep things organised.

### Hooking up the Components

// 16 example of the most basic LED circuit
Each LED will be connected to the board in the same way.

To connect a single LED, the anode of the LED will need to be wired to the signal pin of any channel, then wire a resistor to the cathode of the LED, and finally the other end of the resistor must be wired to the ground (GND) pin of the *same* channel as the anode of the LED. 

// TODO: picture and/or circuit diagram

// - use M-F jumper wires to connect from the servo expansion
The PWM expansion uses male pins for connectivity, while the breadboard uses female sockets. The LED is connected to the resistor through the breadboard already, so we'll need 32 female to male jumpers. The kit has 20, but we can connect a female-female and a male-male jumper together to get a female-male.

// - make sure to use 5V from the pwm expansion channel header


## Writing the Code

Prior to running the code you will need to have python-light and the OmegaExpansion libraries installed. You can install with the following commands

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

// TODO: add gif/video of LEDs working

You should see a wave like effect across the LEDs when they are placed beside each other in order from 0 to 15.


### A Closer Look at the Code

This code does two major things, first it it specifies a generic class for a pwm channel. This generic class has one function, `setDutyCycle` that sets the particular duty cycle on the particular channel that the class has been instantiated with. By creating an object for each output channel, we can set the brightness of each LED individually.


#### Creating a class

As a refresher, in Object Oriented Programming, classes are essentially blueprints or an abstraction. An object is a collection of data made according to the class blueprint with its own unique properties. For example, for a class created as "four sided polygon", an object created from this class may be "square". Creating an object is often called 'instantiation' and an object can alternatively be called an 'instance'

To see another example of another example of classes in python, check out the shift register article where we first introduced //TODO:HYPERLINK TO SHIFT REGISTER ARTICLE.

In our case, wes are making a class for a pwm channel. This class represents a single pwm output channel, and objects of this class will represent and control an actual pwm channel on the board. The function `setDutyCycle` sets the particular duty cycle on whichever channel the object represents. Once we instantiate each channel object we store the objects inside of a list, such that their index corresponds to the channel number. This makes our coding a little simpler.


#### Using the Onion PWM Expansion Python Module

Here we use the pwm module (pyPwmExp) to easily control the PWM expansion. The module comes with a set of functions to control and modify the pwm expansion channels and properties. To find a detailed description of the module, refer to [pyPwmExp library link].

//TODO: ADD LINK TO PWM LIBRARY IN PYTHON DOC.

Specifically, we use the following functions:
```
checkInit()
driverInit()
setFreqency()
setupDriver()
```
The init functions will be discussed later, the last two are more immediately relevant to how this circuit works. In the code, you'll notice the servo frequency set to 2000Hz, this is to ensure the LED doesn't flicker no matter what duty cycle we set the channel to output. To accomplish this, we call setFrequency() and give it SERVO_FREQUENCY as the argument. For each channel, we can change the duty cycle on the fly by calling setupDriver() and sending it the channel and duty cycle number (recall this is between 0% and 100%), by changing the duty cycle, we change the average voltage sent to the LED connected to the channel - this is how the LEDs dim and brighten.


#### Initializing the PWM Expansion

If you look at the constructor (the __init__ function), you will notice the line:
```
pwmExp.driverInit()
```
This line initializes the pwm expansion for usage. This starts the oscillator on the Pwm expansion which is necessary to produce the pwm signals
