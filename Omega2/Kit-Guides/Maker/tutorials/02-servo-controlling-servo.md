---
title: Controlling Servos with the Servo Expansion
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---


# Controlling Servos with the Servo Expansion


In this tutorial we will learn how to control the channels on our servo expansion using python.

## Servo-Motors

<!-- servo -->
```{r child = '../../shared/servos.md'}
```

## Building the Circuit

<!-- // - talk about how to connect a servo to the pwm expansion
// - make sure to mention that an external power supply is required for more servos and larger loads
// can totally rip off large chunks of the pwm expansion hardware article from the documentation
//  * should isolate that text from the pwm hw article into markdown files that can be included here -->

```{r child = '../../shared/servo-setup.md'}
```

## Writing the Code

<!-- // Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * create a class that uses the omegapwm class from the previous example to drive a servo
//    * essentially create the servo class (from the file above), can skip the getSettings, setupMinAngle, and setupMaxAngle functions for the purposes of this example
//    * make sure the class follows the angle described in the servo section above ie 0˚->180˚ as opposed to -90-˚>90˚
// * the program should be something along the lines of setting the servo to 0˚, 45˚, 90˚, 135˚, 180˚, and then back down by 45˚ steps, have a noticeable but not annoyingly long delay between the steps
// * have it run in an infinite loop -->

Prior to running the code you will need to have python and the OmegaExpansion libraries installed. You can install with the following commands

```
opkg update
opkg install python-light
opkg install pyPwmExp
```
Run the following python code and observe your your motor

```
from OmegaExpansion import pwmExp
import math
import time

PWM_FREQUENCY = 50
class servoChannel:
	def __init__(self,channel,minPulse,maxPulse):
		self.channel = channel
		self.frequecy = PWM_FREQUENCY
		self.minPulse = minPulse
		self.maxPulse = maxPulse
		bInit = pwmExp.checkInit()
		if (bInit == 0):
			ret = pwmExp.driverInit()
			if (ret != 0):
				print "Error initializing expansion"
			else:
				bSetFrequency = pwmExp.setFrequency(SERVO_FREQUENCY)	
				if(bSetFrequency != 0):
					print "Error setting oscillator frequecy"

	def setAngle(self,angle):
		pulseWidth = ((self.maxPulse - self.minPulse)/180) + self.minPulse
		dutyCycle = self.calcDutyCycle(pulseWidth);
		self.setDutyCycle(dutyCycle)

	def calcDutyCycle(self,pulseWidth):
		return pulseWidth * PWM_FREQUENCY * 100

	def setDutyCycle(self,dutyCycle):
		ret = pwmExp.setupDriver(self.channel, dutyCycle, 0)
		if(ret != 0):
			print "Error setting channel duty cycle"


def main():
	# Construct servoPin object
	servoControl = servoChannel(0,.001,.002)
	while(true):
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

### What to Expect

// gif of a servo connected to the omega doing this
//  - make sure in the gif it's oriented in the same way as above in the servo section


You should see a repeating pattern. First,the motor shaft move to the 0 degree position, stay there for two seconds.
Next it will move to the 90 degree(neutral) positon and stay two seconds. Then it will move to the 180 degree positon and stay there for two seconds. Then the pattern will repeat itself.

Since the pattern will repeat infinitely, you will need to break by entering `ctrl`+`c`.

### A Closer Look at the Code

<!-- // this code introduced
// * doing math in python
// * brought back the idea of using a class within a class (link back to the first time this was introduced in the 7seg article)
// * brought back the infinite loop -->

As in the servo-dimming-tutorial, we have created a class that allows us to instantiate a servo controlling object for each channel. This allows us to create as many channel objects from the same class template and control each channel as a seperate entity. 

We have also employed an infinite loop. These can be easily constructed with the following code block:

```
while(True):
	#Code To Be Repeated Forever Goes Here
```

Since each servo motor is slightly different, we instantiate our class with the channel that motor is connected to along with the pulse width for the 0 degree position and the pulse width or the 180 degree position. This not only allows us to control the position on different servo motors on different channels but also allows us to interpolate
for pulse width between 0 and 180 degrees.

#### Math in Python

In this code example, as well as others, you may notice that integer numbers include a decimal place. The reason is that python will interpret the number as a floating point number and not an integer type. For precision calculations involving decimals, interpreting numbers as integers can cause lots of errors.

To see the difference for yourself, run the following code in python:

```
print 4/3
# will print "1"
print 4.0/3
# will print "1.33333333"
```

