---
title: Controlling Servos with the Servo Expansion
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---

// TODO: many places are sloppy. pls reread articles after finishing them and look for typos, spelling errors, and grammar issues

// TODO: always capitalize Onion products: PWM Expansion, Expansion Dock, on the Dock, etc

// TODO: Expansion Dock GPIOs should be referred to as Omega GPIOx, can include 'on the Expansion Header' to make it clear
// TODO: the 5V, 3.3V, and GND pins should be referred to as 5V, 3.3V, and GND pins on the Expansion Header

## Controlling Servos {#maker-kit-servo-controlling-servo}

// TODO: you can do better on this intro, let's make these people stoked!

In this tutorial we will learn how to control servo motors using the PWM Expansion with Python. First, let's get to know our servos.

// TODO: makes more sense to have the PWM description first and then the servo description. update the last sentence above to flow with the article


<!-- servo -->
``` {r child = '../../shared/servos.md'}
```

For our experiment, we'll demonstrate how servos can be controlled through PWM signals. We'll connect them to the expansion, then write some code to make them rotate. We touched on PWM very briefly before, but to operate servos, we'll have to go a bit deeper.

<!-- pwm -->
``` {r child = '../../shared/pwm.md'}
```
``` {r child = '../../shared/pwm-details.md'}
```

### Building the Circuit

// TODO: motor? maybe a typo?
// TODO: talk about how the PWM Expansion was designed with servos in mind, and that the headers allow you to plug standard servos straight into the expansion

For this experiment, we'll be wiring a circuit that allows us to control the motors directly through the PWM expansion. This circuit is relatively simple because the motor and the PWM Expansion are both plug and play. If you haven't already, it is highly recommended that you read over the [PWM Expansion](#pwm-expansion) article in our documentation for safety tips.

#### What You'll Need

Gather the following from your kit:

* 1x Omega2 plugged into Expansion Dock
* 1x PWM Expansion plugged into Expansion Dock above
* Servo Motors
    * 1x Standard Size
    * 1x Micro Size


#### Hooking up the Components


1. Plug the PWM Expansion into your Expansion Dock.
1. Plug the power cord of the Standard Size servo motor into the `S0` channel of the PWM Expansion
	* make sure the orange wire from the motor is connected to the pin with the white base on the Expansion!
1. Repeat the step above with the Micro Servo connecting to channel `S1`.

// TODO: let's make a 'Going Further' section at the end of the guide and move this point down there. The issue is not that you would draw too much current from the Dock (note it's drawing current from the regulator circuit, not the Omega), the issue is that the Dock just can't supply enough current for servos under high loads. So if you want to do dope things with servos (robot arms, rovers, etc), you'll need an external power supply. This section should also talk about how the Omega cannot be powered by this external power supply since the dc barrel jack supply is isolated. See https://github.com/OnionIoT/Onion-Docs/blob/master/Omega2/Documentation/Hardware-Overview/Expansions/PWM-Expansion.md for details
**Note 1:** If you're driving a large load on your servo, you should provide an external power supply to the PWM Expansion to avoid drawing too much current through the Omega!

<!-- // DONE (killed it): mmmm this is super unlikely/hard to do and I don't wanna scare the users. In the off chance that it does happen, it's all good since only the GND row will make contact, and the USB receptacle is grounded anyway. no harm, no foul. -->

### Writing the Code

<!-- //DONE: insert a link to the previous article -->

Let's write another class to represent a servo motor based on the class we wrote in the [previous experiment](#maker-kit-servo-dimming-led). Create a file called `motors.py` and paste the following code in it:

``` python
from omegaPwm import OmegaPwm

# define the minimum and maximum pulse widths that will suit most servos (in us)
SERVO_MIN_PULSE = 1000
SERVO_MAX_PULSE = 2000

# Servo motor
class Servo:
    """Class that uses PWM signals to drive a servo"""

    def __init__(self, channel, minPulse=SERVO_MIN_PULSE, maxPulse=SERVO_MAX_PULSE):
        # initialize a pwm channel
        self.channel = channel
        self.frequency = 50
        self.pwmDriver = OmegaPwm(self.channel, self.frequency)

        # note the min and max pulses (in microseconds)
        self.minPulse = minPulse
        self.maxPulse = maxPulse

        # calculate the total range
        self.range = self.maxPulse - self.minPulse

        # calculate the us / degree
        self.step = self.range / float(180)

        # calculate the period (in us)
        self.period = (1000000 / self.pwmDriver.getFrequency())

        # initialize the min and max angles
        self.minAngle     = 0
        self.maxAngle     = 180

    def setAngle(self, angle):
        """Move the servo to the specified angle"""
        # check against the minimum and maximium angles
        if (angle < self.minAngle):
            angle     = self.minAngle
        elif (angle > self.maxAngle):
                angle   = self.maxAngle

        # calculate pulse width for this angle
        pulseWidth = angle * self.step + self.minPulse

        # find the duty cycle percentage of the pulse width
        duty = (pulseWidth * 100) / float(self.period)

        # program the duty cycle
        ret = self.pwmDriver.setDutyCycle(duty)
        return ret

    def setDutyCycle(self, duty):
        """Set duty cycle for pwm channel"""
        ret = pwmExp.setupDriver(self.channel, duty, 0)
        if (ret != 0):
            print 'ERROR: pwm-exp setupDriver not successful!'

        return ret
```

Paste the code below into a file called `MAK02-servoControl.py`, make sure your circuit is set up, then run it and see what happens!

``` python
from motors import Servo
import time

def main():
    # instantiate objects for the two servos
    standardServo = Servo(0, 500, 2400)
    microServo = Servo(1, 500, 2400);

    # set both servos to the neutral position
    standardServo.setAngle(90.0)
    microServo.setAngle(90.0)
    time.sleep(2)

    # infinite loop
    while(True):
        # Turn servos to the 0 angle position
        standardServo.setAngle(0.0)
        microServo.setAngle(0.0)
        time.sleep(2)
        # Turn servos to the neutral position
        standardServo.setAngle(90.0)
        microServo.setAngle(90.0)
        time.sleep(2)
        # Turn servos to the 180 angle position
        standardServo.setAngle(180.0)
        microServo.setAngle(180.0)
        time.sleep(2)


if __name__ == '__main__':
    main()
```

### What to Expect

<!--
// TODO: IMAGE gif of a servo connected to the omega doing this
//  - make sure in the gif it's oriented in the same way as above in the servo section
-->

// TODO: this section was written sloppily. Please

The script will first set the servo motors to the 90 degree position.

Then a repeating pattern will happen continuously. First, the motor shaft move to the `0` degree position staying there for two seconds. Next the shaft will move to the `90` degree (neutral) positon and stay there for two seconds. Finally it will move to the `180` degree positon and stay there for two seconds. The pattern will then repeat itself.

Since the pattern will repeat infinitely, you will need to break by entering `Ctrl-C`.

// TODO: why is it highly recommended to turn the oscillator off?
//	* this is another example of something that will scare newbies.
//	* explain that the PWM Expansion is free-running and that it will keep sending the last programmed PWM signal. go on to explain that if the servos aren't really doing anything, to decrease the potential wear, we can disable the PWM Expansion's oscillator to allow the servos to be idle when they're not in use
**Note**: Due to the nature of the servo motors in the kit, it's highly recommended to turn the oscillator off after killing the script by running the following in ssh or terminal:
```
pwm-exp -s
```

### A Closer Look at the Code

<!--// this code introduced
// * doing math in Python
// * brought back the idea of using a class within a class (link back to the first time this was introduced in the 7seg article)
// * brought back the infinite loop-->

In this experiment, we encountered some classic ways to control devices with software. More techniques exist, but they're almost all based off these three things:

* Infinite loops - a way to repeat actions over and over again
* Python math - integers, floats, and conversions
* Delays - simple delay

#### Infinite Loops
As you may know by now, infinite loops in Python (and many other languages) can be implemented with a loop that always evaluates true:

``` python
while(True):
	#Code To Be Repeated Forever Goes Here
```

// TODO: most software based systems won't actually run infinite loops. it will either be code that gets triggered by an interrupt or a cron daemon.
//	however, we can just say that thermostats, digital clocks, etc, CAN BE implemented with infinite loops.

The reason anyone would use an infinite loop is so we can create programs that will always run. Practically, thermostats, digital clocks, and even computers all rely on infinite loops to work. During the an infinite loop, conditions and states can be evaluated over and over again. After the conditions are checked, actions that require those conditions are performed. For example, a thermostat would evaluate the temperature of the room over and over again. When it detects the temperature to be lower than some number, it turns on the heat; and if it's higher than some number, it should turn off the heat accordingly.

In this example the loop doesn't check anything, only progressing through the commands one-by-one. Be prepared for that to change in the upcoming tutorials though!

#### Math in Python

In this code example, you can find integer numbers along with decimal points (eg. `3.0`). The reason `3.0` is used instead of `3` is to tell Python to interpret the number as a decimal, or **floating point** number. This makes it behave like a number in a calculator.

If we dropped the decimal point (simply using `3`), we'd be doing **integer math**. In this case, Python will literally **drop the decimal part** of any calculation. This is desired behaviour in some cases, such as when counting objects or iterating through loops. But this behaviour can be the source of large errors if you need to do precise calculations!

To see the difference for yourself, we'll add some fractions together but we'll write them in what *should* be equivalent forms. Start the interactive Python interpreter on the command line by simply typing `python`, then run each of the `print` commands below:

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

You can see in the first two examples that the decimal part is dropped from the answer. In the last two you can see this error can carrying forward and end up making a significant difference!

Due to the way decimal and integer numbers are handled by computers, this applies to many other programming languages as well. Be careful!

#### Timing

// TODO: mmmm while this is technically correct, it feels like it would be hella confusing to a novice user. let's change it to talk about how:
//	* The Omega has a microprocessor which executes code hella fast
//	* Servos are mechanical, meaning (there's no possible way that you can just bombard them with commands) that they need time to actually move to the positions that we've programmed
// Also keep in mind: the commands are being transmitted to the PWM Expansion, which then generates the PWM signals to the servos

The Python `time` library is used here to provide a way to delay the signals transmitted to the servo. ()// TODO: technically, the commands are being transmitted to the PWM Expansion, which then generates the PWM signals to the servos) Without the `time.sleep()` function calls, the code would be executed as fast as the Omega can possibly handle, which is pretty much faster than the servo motor can handle.

The Omega2 runs at over 500MHz while the servo receives commands from 50~1kHz, which is over 50,000 times faster than the servo can react! So we use the `time.sleep()` function to give the command some time to take effect on the servo.



### Hardware Calibration
// TODO: is this section h3 on purpose?

// TODO: make sure to point out that we're calibrating mechanical hardware, not the Onion hardware.

In reality, there's always going to be some minor differences in the hardware we use even if they're of the same make and model.

For this reason, we can't send the same signals to the different motors and expect them to behave exactly the same. The minimum and maximum pulses we used to instantiate our servo objects - `500`, `2000`, `500`, `2500` - are values we've found to work with servos in our lab.

// TODO: this sounds a little condescending. make it more fun like, something like 'You've just calibrated your code to play nice with your particular servos', along those lines
Due to these reasons, you should do some testing to find the numbers that work for your particular hardware. This process is called calibration. See if you can use the command line tools or the libraries to figure out what duty cycles correspond to what kind of movement in your own servos.

// TODO: this is a sentence fragment. please fix
>Manufacturers almost always provide data sheets to let you know what the limits of your hardware is, they're definitely the best place to start when calibrating.

Next time, we [spin a motor](#maker-kit-servo-h-bridge).
