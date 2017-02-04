---
title: PWM Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

## PWM Expansion {#pwm-expansion}

<!-- // intro to the pwm exp - allows you to generate 16 distinct PWM signals
// can be used to control anything that can be controlled by pwm: leds, servos, motors, etc

// mention this expansion is controlled with i2c -->

The PWM Expansion allows you to generate up to 16 different Pulse Width Modulated (PWM) signals to control anything from Servo Motors (servos), DC Motor speed, LED brightness, etc.

This Expansion communicates with the Omega using the I2C protocol. If you're curious, check out the [article on I2C](#communicating-with-i2c-devices).

### The Hardware

<!-- // Overview of the Hardware
//  - the 16 channels
//  - the dc barrel jack -->
The PWM Expansion has 16 channels that can output individual PWM signals to drive motors and servos. The expansion can either be powered through the dock, or through a DC barrel jack to enable driving of motors up to 12V. 

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-expansion-illustration.png)

### Connecting to a Dock

<!-- // plugged into the expansion Header
// have photos of it plugged into the Exp dock, power dock, and arduino dock 2

// mention that other expansions can be safely stacked on top of it - just be mindful of wires connected to the headers

// maybe a good place to mention that only 1 pwm expansion per omega will work -->

To use the PWM Expansion, plug it into a Dock that has Expansion header pins (Expansion Dock, Power Dock, Arduino Dock R2).

You can safely stack other Expansions on top of it. **However, be mindful of wires that are connected to the header pins underneath.**

>Note: You may only have one PWM Expansion stacked onto an Omega at a time.


![expansion-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-expansion-dock.jpg)

![power-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-power-dock.jpg)

![arduino-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-arduino-dock.jpg)



### The PWM Channels

<!-- // explanation of channel ordering - which channel is 0, which is 1

// Explanation that each channel has male headers for Vcc, ground, and the pwm signal; the important part here is the signal header - thats the pwm signal -->

The PWM Expansion has 16 channels (outputs) that can be controlled simultaneously. Each channel has the following male header pins from top to bottom:

* **GND** - ground
* **Vcc** - 5V output
* **SIGNAL** - the wire that carries the PWM signal
    * This channel is marked with a white header pin.

### Connecting Servos

<!-- // mention that we made the headers this way so that servo connectors can be plugged right in - add photo of a servo expansion on a dock with a servo plugged in, maybe also a photo of the pwm expansion on the spider robot -->
<!-- TODO: add photos -->

We've placed the PWM pins in the same order that most\* servo motors have them, so you can plug them right in!

>One exception we've found is Airtronics servos, which may have the Vcc and SIGNAL pins on the outside.

Take a look at your servo's connector. Typically the GND wire is black; line it up with the black GND pin on the servo channel's header. The SIGNAL wire will then plug into the white header pin on the bottom. The photo below shows a Hitec servo properly plugged into channel 1 (SIGNAL is the yellow wire).

![pwm-servomotor](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-servomotor.jpg)

Check out the PWM Expansion hooked up to the servos on our Spiderbot!

![pwm-spiderbot](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-spiderbot.jpg)

### The Barrel Jack adapter

<!-- // highlight that the omega can only provide enough power to move one or two servos under light load, in order to power projects with a bunch of servos, we've included a barrel jack adapter
// the DC voltage that comes in will be provided on the Vcc and GND pins on the channels, the PWM signal will also be stepped up to this voltage

// mention that they shouldn't go too nuts, say that we've tested up to 12V
// also mention that this does not provide power to the Omega, it will still need to be powered a different way

// see existing doc for reference -->

The Omega supplies enough power to move only one or two servos under light load. In order to power projects with a bunch of servos, we've included an onboard DC barrel jack connector that can be used to supply power to any connected servos.

>It is not recommended to attempt to power more than 2 servos without an external power supply.

![barrel-jack](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-barrel-jack.jpg)

The DC voltage supplied through the barrel jack will be provided on the Vcc (and GND) pins. The PWM voltage will also be stepped up to this voltage. We've safely tested up to 12V, so try not to go beyond that or you risk damaging your Expansion. To get more power at this stage, look for power supplies with higher current ratings rather than higher voltages.

Note that the Omega cannot be powered through this connector and still requires its own power supply.

>**Note**: on the Arduino Dock, the barrel jack's bottom tabs have been found to make contact with the metal case of the Omega2 and Omega2+ creating a **short circuit**. We recommend inserting a thin plastic layer between the top of the Omega and the bottom of the PWM Expansion to break this short. If the DC connector is shorted, it may cause damage to any components connected to the PWM Expansion.

![The fix to the short](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-barrel-jack-fix.jpg)

### The Oscillator

<!-- // the chip that generates the pwm signals has an internal oscillator that controls the frequency of the generated pwm signals
// since there is one oscillator, all of the pwm signals will run on the same frequency. make sure to make the distinction that they just operate on the same frequency but their pwm duty cycles can be different
// mention the frequency range - see existing doc -->

The onboard chip has an oscillator that can generate PWM signals with a frequency in the range of 24 Hz to 1526 Hz. The default frequency is 50 Hz which is set to match most servomotors.

All signals generated by the PWM Expansion run at the same frequency set by the one oscillator, so you will not be able to control servos using different frequencies.

### Mechanical Drawings

We've made available a detailed [diagram](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-E-PWM.PDF) of the dimensions and geometry of the PWM Expansion.

### Using the PWM Expansion

<!-- // examples of use: robotics, making led light shows, anything involving pwm signals -->
<!-- TODO: this little list and intro is weak! you can do better! -->

Some of the things you can do with the PWM Expansion are as follows:

* Robotics
* LED light shows

Read our [guide to using the PWM Expansion](#using-pwm-expansion) to learn how to control it using software.
