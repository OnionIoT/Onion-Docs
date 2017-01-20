---
title: Controlling Servos with the Servo Expansion
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---
// TODO: fix capitalization

## Controlling Servos with the PWM Expansion {#controlling-servos-with-the-pwm-expansion}

In this tutorial we will learn how to control the channels on our servo expansion using python. But first, a brief introduction to servo motors is required

<!-- servo -->
```{r child = '../../shared/servos.md'}
```

### Building the Circuit

This circuit is relatively simple, as the motor and the PWM Expansion are both plug and play. Do note that if you haven't already, it is highly recommended that you read over the [PWM Expansion](#pwm-expansion) article in our documentation for safety instructions.

#### What You'll Need

* 1x Servo Motor (Standard size)
* 1x PWM Expansion


#### Hooking up the Components

<!-- // - talk about how to connect a servo to the pwm expansion
// - make sure to mention that an external power supply is required for more servos and larger loads
// can totally rip off large chunks of the pwm expansion hardware article from the documentation
//  * should isolate that text from the pwm hw article into markdown files that can be included here -->

1. Plug the PWM Expansion into your Expansion Dock.
1. Plug the power cord of the servo motor into the `S0` channel of the PWM Expansion
	* make sure the white white wire from the motor is connected to the pin with the white base on the Expansion!

**Note 1:** If you're driving a large load on your servo, you should provide an external power supply to the PWM Expansion to avoid drawing too much current through the Omega!

**Note 2:** If you own an Omega2 or Omega2+ and intend to use the PWM expansion with a DC power supply, please take note there is likely to be a short circuit between the barrel jack and the metal case of the Omega itself. We recommend inserting a thin plastic sheet between the expansion and the omega to break this short. For more information, see the [PWM Expansion](#pwm-expansion) article.


#### Writing the Code

<!-- // Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * create a class that uses the omegapwm class from the previous example to drive a servo
//    * essentially create the servo class (from the file above), can skip the getSettings, setupMinAngle, and setupMaxAngle functions for the purposes of this example
//    * make sure the class follows the angle described in the servo section above ie 0˚->180˚ as opposed to -90-˚>90˚
// * the program should be something along the lines of setting the servo to 0˚, 45˚, 90˚, 135˚, 180˚, and then back down by 45˚ steps, have a noticeable but not annoyingly long delay between the steps
//  * have it run in an infinite loop -->

Before running the code you will need to have python and the OmegaExpansion libraries installed. You can install with the following commands

```
opkg update
opkg install python-light
opkg install pyPwmExp
```

Run the following python code and see what happens:
```
from OmegaExpansion import pwmExp
import math
import time

class servoChannel:
	def __init__(self,channel,minPulse,maxPulse):
		self.channel = channel
		self.frequecy = SERVO_FREQUENCY
		self.minPulse = minPulse
		self.maxPulse = maxPulse
		self.neutralPulse = (self.maxPulse - self.minPulse)/2
		self.pulseScale = 90/self.neutralPulse

		bInit = pwmExp.checkInit()
		if (bInit == 0):
			ret = pwmExp.driverInit()
			if (ret != 0):
				print "Error initializing expansion"

	def setAngle(self,angle):
		dutyCycle = angle/self.pulseScale + self.minPulse
                print ('dc = ' + str(dutyCycle))
		self.setDutyCycle(dutyCycle)

	def setDutyCycle(self,dutyCycle):
		ret = pwmExp.setupDriver(self.channel, dutyCycle, 0)
		if(ret != 0):
			print "Error setting channel duty cycle"


def main():
	servoControl = servoChannel(0, 3.0, 11.5)

	servoControl.setAngle(90.0)
	time.sleep(2)

	while(True):
		# Turn motor to the 0 angle position
		servoControl.setAngle(0.0)
		time.sleep(2)
		# Turn motor to the neutral position
		servoControl.setAngle(90.0)
		time.sleep(2)
		# Turn motor to the 180 angle position
		servoControl.setAngle(180.0)
		time.sleep(2)
if __name__ == '__main__':
	main()
```

#### What to Expect

<!-- // TODO: IMAGE gif of a servo connected to the omega doing this
//  - make sure in the gif it's oriented in the same way as above in the servo section -->

The script should initialize the servo motor to the 0 degree position.

Then a repeating pattern happens. First, the motor shaft move to the 0 degree position staying there for two seconds. Next the shaft will move to the 90 degree (neutral) positon and stay there for two seconds. Finally it will move to the 180 degree positon and stay there for two seconds. Then the pattern will repeat itself.

Since the pattern will repeat infinitely, you will need to break by entering `ctrl`+`c`.

>Due to the nature of the servo motors in the kit, it's highly recommended to turn the oscillator off after killing the script by running the following in ssh or terminal:
```
pwm-exp -s
```

### A Closer Look at the Code

<!--// this code introduced
// * doing math in python
// * brought back the idea of using a class within a class (link back to the first time this was introduced in the 7seg article)
// * brought back the infinite loop-->

For this tutorial:
* infinite loops - a way to repeat actions over and over again
* python math - integers, floats, and conversions
* timing - simple delay

#### Infinite Loops
As you may know by now, infinite loops in python (and many other languages) can be simply implemented with a loop that always evaluates true:
```
while(True):
	#Code To Be Repeated Forever Goes Here
```

The reason to use an infinite loop is so we can create programs that will always run. Practically, thermostats, digital clocks, and even computers all rely on infinite loops to work. During the an infinite loop, conditions and states can be evaluated over and over again and actions that rely on the state being at some value executed. For example, a thermostat would evaluate the temperature of the room over and over again, and when it detects the temperature to be lower than some number, it turns on the heat, and if it's higher than some number, it should turn off the heat accordingly.

In this example, the loop does a simple progression of commands, but the concept remains the same.


#### Math in Python

In this code example, as well as others, you will notice that integer numbers including a decimal place, regardless if it is necessary. The reason is that python will interpret the number as a floating point number and not an integer type. The former allows for decimal point precision in calculation unlike the latter. Of course occasions will arise when integer math is more preferable - but we'll leave that as an excercise for the reader.

To see the difference for yourself, run the following code:

```
print 4/3
# will print "1"
print 4.0/3
# will print "1.33333333"
```

#### Timing

The time python library is used here to provide a way to delay the signals transmitted to the servo. Should the `time.sleep()` functions be removed, the code would be executed as fast as the Omega can possibly handle, which more or less translates to 'much faster than the servo motor can handle' - the Omega2 runs at over 500MHz, while the servo recieves commands from 50~1kHz, that's over 50,000x faster than the servo can react! So we use the `time.sleep()` function to give the command some time to take effect on the servo.


### Moving Beyond

Since each servo motor is slightly different, we instantiate our class with the channel that motor is connected to along with the duty cycle for the 0 degree position and the duty cycle for the 180 degree position. The numbers we used (3.0 and 11.5) are values we've tested and found to work with our particular servo. Due to manufacturing imperfections, design flaws, and a whole host of other issues, you would often need to test and find the numbers that work for your particular servo at the angles you need - this is called calibration. Moving beyond, see if you can use the command line tools or the libraries to figure out what duty cycles correspond to what kind of movement in your own servo.
