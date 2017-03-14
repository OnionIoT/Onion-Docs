---
title: Dimming LEDs with the Servo
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---

// TODO: give this a read-through before diving into editing, some typos and gramatical errors need to be fixed

// TODO: always capitalize Onion products: PWM Expansion, Expansion Dock, on the Dock, etc

// TODO: Expansion Dock GPIOs should be referred to as Omega GPIOx, can include 'on the Expansion Header' to make it clear
// TODO: the 5V, 3.3V, and GND pins should be referred to as 5V, 3.3V, and GND pins on the Expansion Header

## Dimming LEDs {#maker-kit-servo-dimming-led}

<!-- // DONE: need to capitalize Python EVERYWHERE -->

// TODO: this first sentence is pretty awkward even though we're doing something pretty awesome

In this tutorial, we will be learning how to use the PWM Expansion with Python and animating 16 LEDs along the way. We'll be wiring LEDs to the PWM expansion using a breadboard, then we'll write some code to light up the LEDs for a mini light show.


<!-- pwm -->
``` {r child = '../../shared/pwm.md'}
```

// TODO: let's include a section on LEDs. No need to include the whole led.md thing, just a small refresher on the anode, cathode, and need for a current limiting resistor. make sure to link back to the first experiment from the starter kit

### Building the Circuit

<!-- // 16 LEDs connected to the Servo Expansion -->

For this circuit, we will connect one LED to each of the 16 channels (0-15) on the PWM Expansion. Using the breadboard here will keep things organised.

#### What You'll Need

Grab the following from your kit:

* 1x Omega plugged into Expansion Dock
* 1x Breadboard
* 1x PWM Expansion plugged into the Expansion Dock
* 16x LEDs of any color
* 16x 200Ω Resistors
* Jumper wires
    * 16x M-F
    * 1x  M-M

#### Hooking up the Components

Each LED will be connected to the board in the same way, so we'll cover wiring a single LED first. Then you can repeat this process for all 16 and you should be good to go.

1. Find the anode and the cathode of your LED, make note of which one is where, then plug the LED across the channel of your breadboard on any row you wish (on columns `e` and `f`)
    * The most reliable way to find the anode/cathode isn't the length of the pins, it's by examining the [diode](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/LED%2C_5mm%2C_green_%28en%29.svg/432px-LED%2C_5mm%2C_green_%28en%29.svg.png) inside the plastic head.
1. Take a 200Ω resistor and use it to bridge the LED's cathode row with the column next to it (labelled `-`).
    * We'll call the `-`labelled column the **`GND` rail**.
1. Now connect the `GND` rail to the `GND` header (TODO: let's call it 'a `GND` pin everywhere), this might be confusing) on your PWM Expansion with one M-M jumper
1. Find the signal pin of any channel. We'll start at channel 0 (`S0` on the PWM Expansion).
    * The signal pin is marked by a white plastic base. For channel `S0`, it should be clearly labelled as `SIGNAL` to the left side. We'll call this the `SIG` pin.
1. Connect the `SIG` pin to a pin in column `a` in one of the rows on the left side of the breadboard using a M-F jumper wire. (eg. `1a`)
    * We'll start at row 1 for the first one, and so on.

If your circuit now looks like this:

<!-- // TODO: IMAGE picture and/or circuit diagram -->

Then we're all set!


// TODO: why do we need an external DC supply? would this make more sense to be introduced when using servos?
**Note**: If you decided to connect a DC supply to the barrel jack that supplies **something other than 5V**, you need to change the resistor to match the DC supply voltage. For 12V supplies, connecting a second 200Ω resistor in series works well.

>If you have a different supply, you just need to divide the voltage output of your supply by 5V and multiply that number by 200Ω to get the new resistance value. If it's a weird number, take the closest resistor you have, or add them in series to get the resistance you need.


### Writing the Code

Let's write a class to abstract methods for a PWM pin on the Omega. Create a file called `omegaPwm.py` and paste the following code in it:

``` python
from OmegaExpansion import pwmExp

class OmegaPwm:
    """Base class for PWM signal"""

    def __init__(self, channel, frequency=50):
        self.channel     = channel
        self.frequency     = frequency

        # check that pwm-exp has been initialized
        bInit     = pwmExp.checkInit()

        if (bInit == 0):
            # initialize the expansion
            ret     = pwmExp.driverInit()
            if (ret != 0):
                print 'ERROR: pwm-exp init not successful!'

            # set to default frequency
            self._setFrequency(self.frequency)

    def _setFrequency(self, freq):
        """Set frequency of pwm-exp oscillator"""
        self.frequency     = freq
        ret     = pwmExp.setFrequency(freq);
        if (ret != 0):
            print 'ERROR: pwm-exp setFrequency not successful!'

        return ret

    def getFrequency(self):
        """Get frequency of pwm-exp oscillator"""
        return self.frequency

    def setDutyCycle(self, duty):
        """Set duty cycle for pwm channel"""
        ret     = pwmExp.setupDriver(self.channel, duty, 0)
        if (ret != 0):
            print 'ERROR: pwm-exp setupDriver not successful!'

        return ret
```

Now let's write the script for the experiment. Create a file called `MAK01-pwmLed.py` and throw the following code in it. Then run it and keep an eye on your LEDs:

// TODO: the code is good, just need comments to describe what we're actually doing!

``` python
from omegaPwm import OmegaPwm
import math
import time

# define constants
PWM_FREQUENCY = 1000

# TODO: need a small description comment of this function
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
		# instantiate an object tied to the i channel 	// TODO: fix up this comment
        obj = OmegaPwm(i, PWM_FREQUENCY)
		# add the object into our array of objects
        ledObjectArray.append(obj)

    phaseIncrement = (2 * math.pi)/16
    actualIncrement = (2 * math.pi)/160

    i = 0
    duty = 0
    while(True):
        for index,element in enumerate(ledObjectArray):
            duty = calcDutyCycle(( (index) * phaseIncrement ) + (i * actualIncrement))
            element.setDutyCycle(duty)
        i += 1
        i = i % 160
        time.sleep(.005)

if __name__ == '__main__':
    main()
```


### What to Expect

You should see a wave like effect across the LEDs when they are placed beside each other in order from 0 to 15.

// TODO: IMAGE add gif/video of LEDs working

This code uses an infinite loop, so you'll have to terminate the script with `Ctrl-C`.


### A Closer Look at the Code

// TODO: this second sentence tries to do many things, let's split it up and talk about how each object is tied to a particular channel when it is instantiated. can also move that last sentence up to the description of the class. and THEN talk about what the setDutyCycle class does
This code does two major things. First, it specifies a generic class for a PWM channel. This generic class has a function `setDutyCycle()` that sets the specified duty cycle on the particular channel that the class has been instantiated with. By creating an object for each output channel, we can set the brightness of each LED individually.

Some points of interest here:

* Creating objects from classes
* Using the PWM Python Module

Additionally, this code has a lot of mathematical operators, if you're confused, here's a cheat-sheet of what do the operators do:

|    Operator   | Effect                                       |
|:-------------:|----------------------------------------------|
|    `a * b`    | Multiplies a and b                           |
|    `a / b`    | Divides a by b                               |
|    `a % b`    | Returns the remainder of a divided by b      |
| `math.sin(a)` | Returns the sine of a, where a is in radians |
|   `math.pi`   | Returns the value of pi                      |
|    `a += b`   | Assigns the value of a plus b to a           |

> // TODO: include a link to a page that describes sines, radians, etc


#### Creating a class

// TODO: bask in your glory, this paragraph is great!

As a refresher, in Object Oriented Programming, classes are essentially blueprints or an abstraction. An **object** is a set of data created from the class blueprint with its own unique properties. For example, a class blueprint for a "four sided polygon" can be used to create objects such as a "square" or a "rectangle". Creating an object from a class is called **instantiation**, and objects created from a class are called **instances**.

<!-- DONE: link properly to shift register article when lazar's finished -->

To see another example of another example of classes in Python, check out the [shift register](#shift-register-creating-classes) article where we first introduced them.

In our case, we used the class `OmegaPwm` as a blueprint for a single PWM output channel. By creating objects of this class, we can represent and control an actual PWM channel on the board. When we call the `OmegaPwm()` function with arguments `i` and `PWM_FREQUENCY` we're initializing an object of the `OmegaPwm` class representing channel `i` on the expansion. Once we instantiate each channel object we store the objects inside of a list, such that their index corresponds to the channel number. This makes the rest of our code a little simpler. // TODO: include a small teaser of how it makes it simpler, or just say, 'as you'll see below'

#### Using the Onion PWM Expansion Python Module

Python's functionality can be expanded with modules and packages - like extra lego sets allowing you to build more complex things. Here we use the PWM module (pyPwmExp) to control the PWM expansion. The module comes with a set of functions to control and modify the PWM expansion channels and properties. By running a script to control the expansion, you don't need to manually need to enter or trigger any commands through the terminal. You can simply leave it running, and it would automatically do its job!

You can find a detailed guide to this module in the [pyPwmExp library](#pwm-expansion-python-module) reference in the Onion docs.

Specifically, we use the following functions:

* `setFreqency()`
* `setupDriver()`
* `checkInit()`
* `driverInit()`


##### Controlling the PWM Outputs

In `omegaPwm.py`, you'll notice the servo frequency was set to 1000 Hz. This is to ensure the LED doesn't flicker no matter what duty cycle we set the channel to output. This is done in the class' constructor function by passing `PWM_FREQUENCY` as the 2nd argument. For each channel, we can change the duty cycle on the fly by calling `setupDriver()` and sending in the channel, and the duty cycle (recall that this is between 0% and 100%). By changing the duty cycle, we change the average voltage sent to the LED connected to the channel - this is how the LEDs dim and brighten.

Instantiating an `OmegaPwm` object requires a channel number and frequency. Note that if you change the frequency of one channel (through initialization or `setFrequency()`), you change it for **all** channels. This is because the PWM expansion only has one oscillator shared between all the outputs.

##### Initializing the PWM Expansion

If you look at the constructor (the `__init__` function), you will notice the line:

``` python
pwmExp.driverInit()
```

This line initializes the PWM expansion for usage. This starts the oscillator on the PWM expansion which actually produces the signals sent through the pins. Without this line, the oscillator will be off and the expansion won't respond! //TODO: technically, it would respond, but it wouldn't produce any pwm signals

Before we initialize the oscillator, we can check if it's already on with `pwmExp.checkInit()`. By checking the return value we can avoid initializing it multiple times. For the PWM expansion in particular, initializing it multiple times doesn't really matter much. However initialization for other hardware devices may take quite a while, so it's a pretty good habit to get into to save you some time.

### What's Math?

You'll notice a lot of mathematical operations going on with the math module in Python. Combined, this allows the brightness of the LEDs to vary sinusoidally. Python's built in mathematical operations are pretty powerful, but it does have some pitfalls which we'll go over next tutorial.

// TODO: maybe include a graphic and/or more text to explain what you mean by vary sinusoidally. We don't want to make the readers feel dumb

Next time, we will [control servos](#maker-kit-servo-controlling-servo) with the PWM Expansion.
