---
title: Dimming LEDs with the Servo
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---

## Dimming LEDs with the PWM Expansion {#dimming-leds-with-pwm-expansion}

<!-- // TODO: need to capitalize Python EVERYWHERE -->

In this tutorial, we will be learning how to use the PWM Expansion with Python and animating 16 LEDs along the way. We'll be wiring the LEDs to the PWM expansion through the breadboard, then we'll write some code to light up the LEDs for a mini light show.


<!-- pwm -->
```{r child = '../../shared/pwm.md'}
```

### Building the Circuit

<!-- // 16 LEDs connected to the Servo Expansion -->

For this circuit, we will connect one LED to each of the 16 channels (0-15) on the PWM Expansion. Using the breadboard here will keep things organised.

#### What You'll Need

Grab the following from your kit:

* 1x Omega plugged into Expansion Dock
* 1x Breadboard
* 1x PWM Expansion plugged into the Expansion Dock
* LEDs
	* 16x any color
* Jumper Wires
	* 16x M-F
* Resistors
	* 16x 200 Ohm

#### Hooking up the Components

<!-- // TODO: adjust how the LEDs are wired up: servo exp -> breadboard w/ M-F jumper -> LED -> resistor -> GND -->

Each LED will be connected to the board in the same way, so we'll cover wiring a single LED here the n you can repeat this process for all 16 and you should be good to go.

1. Find the anode of the LED and the signal pin of any channel. We'll start at channel 0 (`S0` on the PWM Expansion).
	* The signal pin is marked by a white plastic base. For channel `S0`, it should be clearly labelled as `SIGNAL` to the left side. We'll call this the `SIG` pin.
1. Connect the `SIG` pin to a pin in column `a` in one of the rows on the left side of the breadboard using a M-F jumper wire. (eg. `1a`)
    * We'll start at row 1 for the first one, and so on.
1. Stick the cathode of the LED into the same row as the `SIG` jumper wire (eg. `1e`), and the anode into the pin on the other side of the middle gap in the same row (eg. `1f`).
1. Take a 200 Ohm resistor and connect it to the LED's anode and to the `-` column on the right side.
    * We'll call the `-` column the `GND` connection.
1. Your circuit should now look like this<!-- // TODO: IMAGE picture and/or circuit diagram -->

After you've wired up all the LEDs on the board, connect the breadboard's `GND` column to one of the `GND` pins on the PWM Expansion using a M-F jumper wire.

Now we're all set!

Here's a photo of our finished circuit:
<!-- // TODO: IMAGE photo of finished circuit -->

**Note**: The reason we can connect the LED to the `SIG` pin safely here is because the `SIG` pin is providing 5V from the board. **If you decided to connect a DC supply to the barrel jack that supplies more than 5V, you'd need to change the resistor value to match the DC supply voltage.**
<!-- // - use M-F jumper wires to connect from the servo expansion
// - make sure to use 5V from the pwm expansion channel header -->

### Writing the Code

Let's write a class to abstract methods for a PWM pin on the Omega. Create a file called `omegaPwm.py` and paste the following code in it:

``` python
from OmegaExpansion import pwmExp

class OmegaPwm:
	"""Base class for PWM signal"""

	def __init__(self, channel, frequency=50):
		self.channel 	= channel
		self.frequency 	= frequency

		# check that pwm-exp has been initialized
		bInit 	= pwmExp.checkInit()

		if (bInit == 0):
			# initialize the expansion
			ret 	= pwmExp.driverInit()
			if (ret != 0):
				print 'ERROR: pwm-exp init not successful!'

			# set to default frequency
			self._setFrequency(self.frequency)

	def _setFrequency(self, freq):
		"""Set frequency of pwm-exp oscillator"""
		self.frequency 	= freq
		ret 	= pwmExp.setFrequency(freq);
		if (ret != 0):
			print 'ERROR: pwm-exp setFrequency not successful!'

		return ret

	def getFrequency(self):
		"""Get frequency of pwm-exp oscillator"""
		return self.frequency

	def setDutyCycle(self, duty):
		"""Set duty cycle for pwm channel"""
		ret 	= pwmExp.setupDriver(self.channel, duty, 0)
		if (ret != 0):
			print 'ERROR: pwm-exp setupDriver not successful!'

		return ret
```

Now let's write the script for the experiment. Create a file called `pwmLed.py` and throw the following code in it. Then run it and keep an eye on your LEDs:

``` python
from omegaPwm import OmegaPwm
import math
import time

# define constants
SERVO_FREQUENCY = 1000

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
		obj = OmegaPwm(i, SERVO_FREQUENCY)
		ledObjectArray.append(obj)

	phaseIncrement = (2 * math.pi)/16
	actualIncrement = (2 * math.pi)/160
    
	i = 0
	while(True):
		for idx,element in enumerate(ledObjectArray):
			element.setDutyCycle(calcDutyCycle(((idx)*phaseIncrement)+(i*actualIncrement)))
		i += 1
		time.sleep(.005)

if __name__ == '__main__':
	main()
```

<!-- // TODO: the above main loop has the variable `i` increase without bounds, and does mapping in the function it's passed to. fix this later -->

#### What to Expect

<!-- // TODO: IMAGE add gif/video of LEDs working -->

You should see a wave like effect across the LEDs when they are placed beside each other in order from 0 to 15.

This code uses an infinite loop, so you'll have to terminate the script with `Ctrl-C`.

### A Closer Look at the Code

This code does two major things. First, it specifies a generic class for a PWM channel. This generic class has a function `setDutyCycle()` that sets the particular duty cycle on the particular channel that the class has been instantiated with. By creating an object for each output channel, we can set the brightness of each LED individually.

Some points of interest here:

* Creating objects from classes
* Using the PWM Python Module

#### Creating a class

As a refresher, in Object Oriented Programming, classes are essentially blueprints or an abstraction. An **object** is a collection of data that is defined by the class blueprint with its own unique properties. For example, for a class created as "four sided polygon", an object created from this class may be "square". Creating an objects is called **instantiation**, and copies of an object are called **instances**.

To see another example of another example of classes in Python, check out the [shift register](#shift-register-creating-classes) article where we first introduced them.

In our case, we are making a class for a PWM channel. This class represents a single PWM output channel, and objects of this class will represent and control an actual PWM channel on the board. The function `setDutyCycle()` sets the particular duty cycle on whichever channel the object represents. Once we instantiate each channel object we store the objects inside of a list, such that their index corresponds to the channel number. This makes our coding a little simpler.

#### Using the Onion PWM Expansion Python Module

Python's functionality can be expaned with modules and packages - like extra lego sets allowing you to build more complex things. Here we use the PWM module (pyPwmExp) to control the PWM expansion. The module comes with a set of functions to control and modify the PWM expansion channels and properties. By running a script to control the expansion, you don't need to manually need to enter or trigger any commands through the terminal. You can simply leave it running, and it would automatically do its job!

You can find a detailed guide to this module in the [pyPwmExp library](#pwm-expansion-python-module) reference in the Onion docs.

Specifically, we use the following functions:

* `setFreqency()`
* `setupDriver()`
* `checkInit()`
* `driverInit()`

##### Controlling the PWM Outputs

In the code, you'll notice the servo frequency was set to 1000 Hz. This is to ensure the LED doesn't flicker no matter what duty cycle we set the channel to output. This is done in the class' constructor function by passing `SERVO_FREQUENCY` as the 2nd argument. For each channel, we can change the duty cycle on the fly by calling `setupDriver()` and sending it the channel and duty cycle number (recall that this is between 0% and 100%). By changing the duty cycle, we change the average voltage sent to the LED connected to the channel - this is how the LEDs dim and brighten.

##### Initializing the PWM Expansion

If you look at the constructor (the `__init__` function), you will notice the line:

```
pwmExp.driverInit()
```

This line initializes the PWM expansion for usage. This starts the oscillator on the PWM expansion which actually produces the signals sent through the pins.
