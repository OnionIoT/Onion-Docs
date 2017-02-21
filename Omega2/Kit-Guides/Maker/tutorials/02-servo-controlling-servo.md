---
title: Controlling Servos with the Servo Expansion
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---

## Controlling Servos with the PWM Expansion {#MAK02-servo-controlling-servo}

In this tutorial we will learn how to control servo motors using the PWM Expansion with Python. But first, let's briefly introduce servo motors.

<!-- servo -->
```{r child = '../../shared/servos.md'}
```

### Building the Circuit

This circuit is relatively simple, as the motor and the PWM Expansion are both plug and play. Do note that if you haven't already, it is highly recommended that you read over the [PWM Expansion](#pwm-expansion) article in our documentation for safety instructions.

#### What You'll Need

Grab the following from your kit:

* 1x Omega2 plugged into Expansion Dock
* 1x PWM Expansion plugged into Expansion Dock above
* Servo Motors
    * 1x Standard Size
    * 1x Micro Size

#### Hooking up the Components

<!-- // TODO: update this whole article to use both of the included servos -->

<!-- // - talk about how to connect a servo to the pwm expansion
// - make sure to mention that an external power supply is required for more servos and larger loads
// can totally rip off large chunks of the pwm expansion hardware article from the documentation
//  * should isolate that text from the pwm hw article into markdown files that can be included here -->

1. Plug the PWM Expansion into your Expansion Dock.
1. Plug the power cord of the Standard Size servo motor into the `S0` channel of the PWM Expansion
	* make sure the white white wire from the motor is connected to the pin with the white base on the Expansion!
1. Repeat the step above to connect the Micro Servo into channel `S1`.

**Note 1:** If you're driving a large load on your servo, you should provide an external power supply to the PWM Expansion to avoid drawing too much current through the Omega!

**Note 2/follow up:** When the Servo Expansion is plugged in as the bottom of the Expansion stack, the pins on the underside of the board may be short circuited by contact with the USB receptacle directly underneath when pressure is applied to the top of the Expansion. We recommend inserting a thin plastic sheet between the expansion and the omega to break this short. For more information, see the [PWM Expansion](#pwm-expansion) article.

#### Writing the Code

<!-- // * create a class that uses the omegapwm class from the previous example to drive a servo
//    * essentially create the servo class (from the file above), can skip the getSettings, setupMinAngle, and setupMaxAngle functions for the purposes of this example
//    * make sure the class follows the angle described in the servo section above ie 0˚->180˚ as opposed to -90-˚>90˚
// * the program should be something along the lines of setting the servo to 0˚, 45˚, 90˚, 135˚, 180˚, and then back down by 45˚ steps, have a noticeable but not annoyingly long delay between the steps
//  * have it run in an infinite loop

// TODO: implement this servo class in a separate file, include the file from the previous exp -->

Let's write another class to represent a servo motor based on the class we wrote in the first experiment. Create a file called `motors.py` and paste the following code in it:

``` python
from omegaPwm import OmegaPwm

# Servo motor
class Servo:
	"""Class that uses PWM signals to drive a servo"""

	def __init__(self, channel, minPulse=1000, maxPulse=2000):
		# initialize a pwm channel
		self.channel 	= channel
        self.frequency	= 50
		self.pwmDriver 	= OmegaPwm(self.channel, self.frequency)

		# note the min and max pulses (in microseconds)
		self.minPulse 	= minPulse
		self.maxPulse 	= maxPulse

		# calculate the total range
		self.range 		= self.maxPulse - self.minPulse

		# calculate the us / degree
		self.step 		= self.range / float(180)

		# calculate the period (in us)
		self.period 	= (1000000 / self.pwmDriver.getFrequency())

		# initialize the min and max angles
		self.minAngle 	= 0
		self.maxAngle 	= 180

	def setAngle(self, angle):
		"""Move the servo to the specified angle"""
		# check against the minimum and maximium angles
		if angle < self.minAngle:
			angle 	= self.minAngle
		elif angle > self.maxAngle:
			angle 	= self.maxAngle

		# calculate pulse width for this angle
		pulseWidth 	= angle * self.step + self.minPulse

		# find the duty cycle percentage of the pulse width
		duty 		= (pulseWidth * 100) / float(self.period)

		# program the duty cycle
		ret = self.pwmDriver.setDutyCycle(duty)
		return ret

    def setDutyCycle(self, duty):
		"""Set duty cycle for pwm channel"""
		ret 	= pwmExp.setupDriver(self.channel, duty, 0)
		if (ret != 0):
			print 'ERROR: pwm-exp setupDriver not successful!'

		return ret
```

Paste the code below into a file called `MAK02-servoControl.py`, make sure your circuit is set up, then run it and see what happens!

``` python
from motors import Servo
import time

def main():

	standardServo = Servo(0, 500, 2500)
	microServer = Servo(1, 500, 2000);


	standardServo.setAngle(90.0)
	microServo.setAngle(90.0)
	time.sleep(2)

	while(True):
		# Turn motor to the 0 angle position
		standardServo.setAngle(90.0)
		microServo.setAngle(90.0)
		time.sleep(2)
		# Turn motor to the neutral position
		standardServo.setAngle(90.0)
		microServo.setAngle(90.0)
		time.sleep(2)
		# Turn motor to the 180 angle position
		standardServo.setAngle(90.0)
		microServo.setAngle(90.0)
		time.sleep(2)
if __name__ == '__main__':
	main()
```

#### What to Expect

<!--
// TODO: IMAGE gif of a servo connected to the omega doing this
//  - make sure in the gif it's oriented in the same way as above in the servo section
-->

The script should first initialize the servo motor to the 90 degree position.

Then a repeating pattern happens. First, the motor shaft move to the `0` degree position staying there for two seconds. Next the shaft will move to the `90` degree (neutral) positon and stay there for two seconds. Finally it will move to the `180` degree positon and stay there for two seconds. Then the pattern will repeat itself.

Since the pattern will repeat infinitely, you will need to break by entering `Ctrl-C`.

**Note**: Due to the nature of the servo motors in the kit, it's highly recommended to turn the oscillator off after killing the script by running the following in ssh or terminal:
```
pwm-exp -s
```

### A Closer Look at the Code

<!--// this code introduced
// * doing math in Python
// * brought back the idea of using a class within a class (link back to the first time this was introduced in the 7seg article)
// * brought back the infinite loop-->

For this tutorial:
* Infinite loops - a way to repeat actions over and over again
* Python math - integers, floats, and conversions
* Timing - simple delay

#### Infinite Loops
As you may know by now, infinite loops in Python (and many other languages) can be simply implemented with a loop that always evaluates true:

``` python
while(True):
	#Code To Be Repeated Forever Goes Here
```

The reason to use an infinite loop is so we can create programs that will always run. Practically, thermostats, digital clocks, and even computers all rely on infinite loops to work. During the an infinite loop, conditions and states can be evaluated over and over again and actions that rely on the state being at some value executed. For example, a thermostat would evaluate the temperature of the room over and over again, and when it detects the temperature to be lower than some number, it turns on the heat, and if it's higher than some number, it should turn off the heat accordingly.

In this example, the loop does a simple progression of commands, but the concept remains the same.

#### Math in Python

In this code example, you can find integer numbers with decimal points (eg. `3.0`). The reason `3.0` is used instead of `3` is to tell Python to interpret the number as a decimal, or **floating point** number. This makes it behave like a number in a calculator.

If we dropped the decimal point (simply using `3`), we'd be doing **integer math**. In this case, Python will literally **drop the decimal part** of any calculation. This is desired behaviour in some cases, such as when counting objects or iterating through loops. But this behaviour can be the source of numerous errors if you need to do precise calculations!

To see the difference for yourself, start the interactive Python interpreter on the command line by simply typing `python`, then run each of the `print` commands below:

``` python
# simple examples of floating point vs integer math
print 4.0/3
# will print "1.3333333..."
print 4/3
# will print "1"

# difference between floating point and integer math in expressions
print 5.0/3 + 8.0/3
# will print "4.3333333..."
print 5/3 + 8/3
# will print "3"
```

You can see in the first two examples how the decimal part is dropped from the answer, and in the last two you can see that this error can carry forward(!!!).

Due to the way decimal and integer numbers are handled by computers, this also applies to most other programming languages as well. Be careful!

#### Timing

The time Python library is used here to provide a way to delay the signals transmitted to the servo. Without the `time.sleep()` function calls, the code would be executed as fast as the Omega can possibly handle, which is pretty much faster than the servo motor can handle. The Omega2 runs at over 500MHz while the servo receives commands from 50~1kHz, which is over 50,000 times faster than the servo can react! So we use the `time.sleep()` function to give the command some time to take effect on the servo.


### Hardware Calibration

In reality, there's always going to be differences in the hardware we use even if they're of the same make and model.

For this reason, we can't send the same signals to the different motors and expect them to behave exactly the same. The minimum and maximum pulses we used to instantiate our servo objects - `500`, `2000`, `500`, `2500` - are values we've found to work with servos in our lab.

Due to these reasons, you should do some testing to find the numbers that work for your particular hardware. This proccess is called calibration. See if you can use the command line tools or the libraries to figure out what duty cycles correspond to what kind of movement in your own servos.

Next time, we [spin a motor](#MAK03-servo-h-bridge).
