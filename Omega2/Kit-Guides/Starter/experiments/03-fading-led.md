---
title: Fading an LED
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 3
---

## Dimming an LED

So far we've been turning LEDs fully on and fully off, but it's also possible have LEDs dimmed to somewhere between on and off. And that's what we're going to do in this experiment: we're going to use Pulse Width Modulation (PWM) to create a dimming effect on an LED.

<!-- Pulse Width Modulation -->
```{r child = '../../shared/pwm.md'}
```

#### PWM and LEDs

By sending a PWM signal to an LED, we can control how bright that LED appears to shine. What's actually going on is that the LED is turning on and off many, many times in a second. For example, if we send a 50% duty cycle PWM signal at 50 Hz to an LED, it will be on for 10ms, then be off for 10ms, then be on for 10ms and so on. You won't actually see the LED turning on and off, instead you'll see that the LED looks much dimmer than when you set the duty cycle to 100%.

### Building the Circuit

We're going to be providing power to the LED just like we did in the two previous experiments. The only difference is the speed at which we turn the LED on and off!

#### What You'll Need

We'll need the same LED circuit we used in the previous two experiments, which includes at minimum:

* Omega2 plugged into Expansion Dock
* 1x LEDs
* 2x Jumper Wires
* Resistors
  * (// TODO: LED resistor) 
* Breadboard

#### Hooking up the Components

In this example we'll only be fading a single LED on GPIO 0 so go ahead and build the same circuit we used in the previous two experiments:

* Plug the LED into the breadboard, with the anode and cathode in different rows
* Connect the LED's

### Writing the Code

<!-- Going to use fast-gpio pwm to avoid any muxing nonsense-->

// use fast-pwm to slowly increment the duty cycle on a gpio and then halfway through start decrementing the pwm, so that you get a fading in, and then fading out
// make it progress slowly so you can tell that its getting brighter and dimmer

``` python
import onionGpio
import time
import os

gpio0 	= onionGpio.OnionGpio(0)	# initialize a GPIO object
gpio0.setOutputDirection(0)		# set to output direction with zero being the default value

ledValue  = 2
dutyCycle = 0
def pwmLed(pin, frequency, dutyCyclePercentage):
	command = "fast-gpio pwm %d %d %d" % (pin, frequency, dutyCyclePercentage) #Assign the arguments to the correct positions in the fast-gpio command
	os.system(command) # Send the command to the command line

## Infinite Loop Main Code
while 1:
	dutyCycle=dutyCycle+ledValue # Increment or decrement the duty cycle by the ledValue

	pwmLed(0, 50, dutyCycle) # Assign GPIO 0 to the pwm duty cycle value

	# flip the value variable
	if (dutyCycle <= 0) or (dutyCycle >= 100):
		ledValue = -ledValue # Reverse direction at 0, and 100

	time.sleep(0.1)	# sleep for a tenth of a second
```



<!-- TODO: FUTURE: Write using the Omega's PWM pins -->

#### What to Expect

// Your LED will fade in and then out, describe this and have a gif

When you run this script your LED will fade in and out. This is because we set the duty cycle to increase up to 100% (fade in to 100%), and then we begin to decrease the duty cycle down to 0% (fade out to 0%).

<!-- TODO: Insert gif of this -->


#### A Closer Look at the Code

// intro to the code that was written
//  new things introduced:
//  * function where you pass in gpio # and duty cycle and it calls fast-gpio for you
//  * fancy for loop

We've used the code from Experiment 1 as a foundation for writing the code in the experiment. We will still instantiate the GPIO and set the direction to output, but afterwards we no longer use onionGpio. Instead we use `fast-gpio` for its software based PWM function. In our infinite loop we increment the duty cycle by the ledValue, and at 100% we reverse the value and decrement to 0.

##### Functions

// explanation of why it was useful to package the fast-gpio os call into a function:
//  * useful to have a readable & simple python interface for setting the pwm duty cycle
//  * will be used a whole bunch
//  * cleaner looking code and good practice


In order to use `fast-gpio` we need to use the `os` module. This module allows us to send command-line arguments in Python using `os.system(command)`.

We then put this into it's own function so that we have a much simpler and easier to read Python interface for setting the PWM duty cycle. This function takes in the following arguments:

* GPIO pin number
* Frequency
* Duty cycle percentage

By doing this we make it really easy to reuse for other pins, frequencies, and duty cycle values.

>It's good practice to break your code into small problems, and writing single functions to solve each problem.

<!-- #### Fancy For Loops

// have a for loop that increments the PWM and then halfway through starts decrementing the PWM - when you reach halfway, multiply the value by which you increment by -1 :) -->
