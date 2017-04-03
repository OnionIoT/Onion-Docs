---
title: Controlling Servos with the Servo Expansion
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---

<!-- // DONE: many places are sloppy. pls reread articles after finishing them and look for typos, spelling errors, and grammar issues -->

<!-- // DONE: always capitalize Onion products: PWM Expansion, Expansion Dock, on the Dock, etc -->

<!-- // DONE: Expansion Dock GPIOs should be referred to as Omega GPIOx, can include 'on the Expansion Header' to make it clear
// DONE: the 5V, 3.3V, and GND pins should be referred to as 5V, 3.3V, and GND pins on the Expansion Header -->

## Controlling Servos {#maker-kit-servo-controlling-servo}

<!-- // DONE: you can do better on this intro, let's make these people stoked! -->

Now let's move on from LEDs to more fun stuff! In this experiment we will learn how to control servo motors using the PWM Expansion with Python. Servos are one of the staples of any motorized project, so let's get right to it!

First, let's review the basics of PWM as we'll be using it a bit differently.

<!-- // DONE: makes more sense to have the PWM description first and then the servo description. update the last sentence above to flow with the article -->

<!-- pwm -->
``` {r child = '../../shared/pwm.md'}
```

``` {r child = '../../shared/pwm-details.md'}
```

<!-- servo -->
``` {r child = '../../shared/servos.md'}
```

For our experiment, we'll demonstrate how servos can be controlled through PWM signals. We'll connect them to the Expansion, then write some code to make them rotate. We touched on PWM very briefly before, but to operate servos, we'll have to go a bit deeper.

### Building the Circuit

<!-- // DONE: motor? maybe a typo?
// DONE: talk about how the PWM Expansion was designed with servos in mind, and that the headers allow you to plug standard servos straight into the Expansion -->

The PWM Expansion was designed with servos in mind, and its headers allow you to plug standard servos straight into the Expansion. This experiment circuit is relatively simple because you only need to plug the servos into the board. If you haven't already, it is highly recommended that you read over the [PWM Expansion](#pwm-expansion) article in our documentation for safety tips.

For completeness, here's a diagram of our circuit:

![How the servos connect to the PWM Expansion](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/diagrams/02-circuit-diagram.png)

#### What You'll Need

Gather the following from your kit:

* 1x Omega2 plugged into Expansion Dock
* 1x PWM Expansion plugged into Expansion Dock above
* Servo Motors
    * 1x Standard Size
    * 1x Micro Size

#### Hooking up the Components

1. Plug the PWM Expansion into your Expansion Dock.
1. Plug the power cord of the Standard Size servo motor into the `S0` channel of the PWM Expansion.
	* make sure the orange wire from the motor is connected to the pin with the white base on the Expansion!
1. Repeat the step above with the Micro Servo connecting to channel `S1`.

Your circuit should look like this:

![Assembled circuit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/01-assembled-circuit.jpg)

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


<!-- // DONE: this section was written sloppily. Please -->

The script will first set the servo motors to the 90 degree (neutral) position. Then it will repeat the following pattern:

1. First, the motor shaft move to the `0` degree position and stop for two seconds. 
1. Next the shaft will move back to the `90` degree (neutral) position and stop for another two seconds. 
1. Finally it will move in the other direction to the `180` degree position and stop for another two seconds.

Here it is working in the Onion Lab:

<!--
// DONE: IMAGE gif of a servo connected to the omega doing this
//  - make sure in the gif it's oriented in the same way as above in the servo section
-->
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/i2KygjFe22A" frameborder="0" allowfullscreen></iframe>

Since the pattern will repeat infinitely, you will need to break by entering `Ctrl-C`.

<!--
// DONE: why is it highly recommended to turn the oscillator off?
//	* this is another example of something that will scare newbies.
//	* explain that the PWM Expansion is free-running and that it will keep sending the last programmed PWM signal. go on to explain that if the servos aren't really doing anything, to decrease the potential wear, we can disable the PWM Expansion's oscillator to allow the servos to be idle when they're not in use
-->

**Note**: It's highly recommended to turn the oscillator off after terminating the script by running the following in ssh or terminal:

```
pwm-exp -s
```

This is because the servos will continue to be sent signals if the oscillator remains on. Although the arms won't be swinging, the motors will be running needlessly and drain power.

### A Closer Look at the Code

<!--// this code introduced
// * doing math in Python
// * brought back the idea of using a class within a class (link back to the first time this was introduced in the 7seg article)
// * brought back the infinite loop-->

In this experiment, we encountered some classic ways to control devices with software. We covered the following techniques and topics:

* **Infinite loops** - a way to repeat actions over and over again
* **Python math** - integers, floats, and conversions
* **Delays** - simple delay

#### Infinite Loops
As you may know by now, infinite loops in Python (and many other languages) can be implemented with a loop that always evaluates true:

``` python
while(True):
	#Code To Be Repeated Forever Goes Here
```

<!-- // DONE: most software based systems won't actually run infinite loops. it will either be code that gets triggered by an interrupt or a cron daemon.
//	however, we can just say that thermostats, digital clocks, etc, CAN BE implemented with infinite loops. -->

In simple experiments like ours, we can use infinite loops to make sure our program always runs. Other devices such as thermostats, and digital clocks can also be implemented using infinite loops. In these loops, conditions and states can be evaluated over and over again. After the conditions are checked, actions that require those conditions can be performed. For example, a thermostat would evaluate the temperature of the room over and over again. When it detects the temperature to be lower than some value, it can turn on the heat; and if it's higher than some value, it can also turn off the heat accordingly.

In this example, the loop doesn't check anything, only progressing through the commands one-by-one. Be prepared for that to change in the upcoming experiments though!

#### Math in Python

In this code example, you can find integer numbers along with decimal points (eg. `3.0`). The reason `3.0` is used instead of `3` is to tell Python to interpret the number as a decimal, or **floating point** number. This makes it behave like a number in a calculator.

If we dropped the decimal point (simply using `3`), we'd be doing **integer math**. In this case, Python will literally **drop the decimal part** of any calculation. Sometimes we want this behaviour, such as when counting objects or iterating through loops. But this behaviour can be the source of large errors if you need to do precise calculations!

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

You can see in the first two examples that the decimal part is dropped from the answer. In the last two you can see this error can carrying forward, causing a huge error!

This applies to many other programming languages due to the way decimal and integer numbers are handled by computers. Be careful!

#### Timing

<!-- // DONE: mmmm while this is technically correct, it feels like it would be hella confusing to a novice user. let's change it to talk about how:
//	* The Omega has a microprocessor which executes code hella fast
//	* Servos are mechanical, meaning (there's no possible way that you can just bombard them with commands) that they need time to actually move to the positions that we've programmed
// Also keep in mind: the commands are being transmitted to the PWM Expansion, which then generates the PWM signals to the servos -->

As we've mentioned in the Starter Kit experiments, the Omega has a microprocessor which executes code **extremely** quickly (500MHz), while on the other hand servos are mechanical devices and can only react to command changes up to a certain point (50Hz ~ 1kHz). If a program like ours runs on the Omega with no time delays built in, the Omega will change the servos' PWM signals faster than they can interpret them. This can cause unexpected behaviour; for example, your servos may twitch as they struggle to keep up.

The Python `time` library and `time.sleep()` function calls are crucial to make sure there's enough time for the servo to react to command changes.

#### Hardware Calibration
<!-- // DONE: is this section h3 on purpose? -->

<!-- // DONE: make sure to point out that we're calibrating mechanical hardware, not the Onion hardware. -->

In reality, there will always be minor differences in mechanical hardware between motors even if they're of the same make and model. This can be due to slight variations in manufacturing, how well it was assembled, and so on.

For this reason, sending the same signals to two of the same motor may not cause them to behave exactly the same. The pulse width values we provided - `500` and `2000`; `500` and `2500` - are values we've found to work with servos in our lab. Try playing around with these and seeing what happens; this process is called **calibration**.

See if you can use the command line tools or the libraries to figure out what duty cycles correspond to what kind of movement in your own servos!

<!-- // DONE: this sounds a little condescending. make it more fun like, something like 'You've just calibrated your code to play nice with your particular servos', along those lines
Due to these reasons, you should do some testing to find the numbers that work for your particular hardware. This process is called calibration. See if you can use the command line tools or the libraries to figure out what duty cycles correspond to what kind of movement in your own servos.-->

<!-- // DONE: this is a sentence fragment. please fix -->
>Manufacturers almost always provide data sheets to let you know the characteristics and limits of your hardware. They're definitely the best place to start when calibrating.

### Going Further


<!-- // DONE: let's make a 'Going Further' section at the end of the guide and move this point down there. The issue is not that you would draw too much current from the Dock (note it's drawing current from the regulator circuit, not the Omega), the issue is that the Dock just can't supply enough current for servos under high loads. So if you want to do dope things with servos (robot arms, rovers, etc), you'll need an external power supply. This section should also talk about how the Omega cannot be powered by this external power supply since the dc barrel jack supply is isolated. See https://github.com/OnionIoT/Onion-Docs/blob/master/Omega2/Documentation/Hardware-Overview/Expansions/PWM-Expansion.md for details -->

If you want to do more advanced projects like a robot arm or a rover, you should provide an external power supply to the PWM Expansion via the barrel jack. This is because the PWM Expansion draws power from the Expansion Dock's power circuitry. Heavy loads and multiple servos draw a lot of current, and the high power demand may exceed what the Dock is able to provide.

Also, keep in mind that the Omega cannot be powered directly by this external power supply because the DC barrel jack's positive voltage connection is isolated from the main power circuitry. For full details, see our [PWM Expansion hardware article](#pwm-expansion).

<!-- // DONE (killed it): mmmm this is super unlikely/hard to do and I don't wanna scare the users. In the off chance that it does happen, it's all good since only the GND row will make contact, and the USB receptacle is grounded anyway. no harm, no foul. -->


Next time, we [spin a motor](#maker-kit-servo-h-bridge).
