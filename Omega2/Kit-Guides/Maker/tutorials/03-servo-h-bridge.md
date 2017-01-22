---
title: Using an H-Bridge
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---
<!-- // Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example, this (or something similar) is what the final result will be -->

## Controlling a DC Motor with an H-Bridge {#controlling-a-dc-motor-with-an-h-bridge}

<!-- // this tutorial will show us how to control a dc motor using an h-bridge. we'll also continue using the class from the first example to create classes to help us accomplish our goals -->
For this tutorial, we'll be controlling a motor using the PWM expansion. To do this, the PWM expansion will send appropriate signals to an 'H-bridge' by changing duty cycles, and the H-bridge will transmit the signal to the motor.

>If you need a refresher on how PWM (or Pulse-Width Modulation) works, you can find an explaination in the [Using PWM Expansion](#using-pwm-expansion) article.

<!-- dcmotor -->
```{r child = '../../shared/dcmotor.md'}
```

<!-- hbridge -->
```{r child = '../../shared/hbridge.md'}
```

The way a PWM signal operates a motor is by switching the power supply on and off really quickly. Normally this can be done sending the PWM signal to a transistor, and have the transistor switch ther power supply, but an H-bridge adds functionality to this control by allowing the direction of the current to be easily changed. In the H-bridge diagram above, the PWM expansion will be sending signals to open and close the four switches on the H-bridge. In our circuit, we'll be using an H-bridge integrated chip (IC) so we don't need to wire the internals ourselves, and to prevent short circuits that could arise if we directly controlled those switches.


### Building the Circuit

<!-- // omega -> h-bridge -> dc motor
// three switches as gpio inputs to the omega -->

Before we start building, we recommend familiarizing yourself with how the H-bridge chip in our kit works. The chip contains two H-bridges, allowing control of two sources at once. For this tutorial, we'll be using one of them. Specifically, the pair of inputs and outputs (`1A`, `2A` and `1Y`, `2Y`)on the left side of the chip.

// TODO: IMAGE diagram of the SN754410

The way we'll be controlling this specific H-bridge is through three pins - `1A`, `2A` and `1,2EN`. `1A` controls the polarity of `1Y`, `2A` controls the polarity to `2Y`. To further explain, at a very high level, this H-bridge chip 'assigns' the outputs (the pins labelled `Y`) according to the voltage (or signal) fed to the inputs (the pins labelled `A`). For example, sending a a 'high' signal to `1A` will lead to the same signal being sent out `1Y` the difference is the signal sent *out* uses the voltage supplied to pin `8`. Voltage acts kind of like a waterfall - it sends the current flowing from the voltage source (top) to the ground (bottom), so if the signal to `1A` is high, that means the H-bridge switches `1Y` to the top of the fall, if low is sent instead, the H-bridge switches `1Y` to the bottom of the falls. A waterfall only falls if there's a top and a bottom, so if both `1A` and `2A` see the same signal (both high, or both low) then nothing moves and the motor won't turn. If the top and the bottom of the 'falls' - or if `2A` gets sent high, and `1A` low - are swapped, the logically the the movement flips and the motor changes directions!

The `1,2EN` pin is a little bit easier to understand. It simply turns the H-bridge on or off. If `1,2EN` sees a 'high', then everything we've covered above happens as normal, if it's off, then there won't be anything sent to the outputs no matter what `1A` and `2A` are set to.

>**Note**: As can be seen above, the chip is roughly mirrored. The top right and bottom left pins are the power supply for the output (pin `8`) and the chip (pin `16`) respectively, the difference being the voltage supplied for the output can be up to 36V, while the voltage supplied to the chip is recommended to be around 5V for proper operation. This means if you want to power a large motor, and you have an external power supply, you should power the motor with the external supply and control it with the H-bridge without any fuss, you simply need to power the chip (pin `16`) and the H-bridge output (pin `8`) with the correct supplies

#### What You'll Need

* 1x PWM Expansion
* 1x DC Motor
* 1x H-bridge (SN754410)
* 1x Breadboard
* 1x Something solid to fix the motor down on
* 1x strip of tape to see the motor spinning more clearly
* Jumper wires
	* 3x M-F
	* 10x M-M

#### Hooking up the Components

<!-- // omega -> h-bridge: three channels from pwm expansion to control the two input pins and the duty cycle pin, all requisite wiring for power
//  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)
// h-bridge -> dc motor: the h-bridge motor outputs to the motor... duh

// make sure to drive home the point that the H-bridge can be burnt if improperly wired
//  make sure the pwm expansion is not producing any signals (or they're all at 0%) while you're wiring it -->


When working with ICs, setting up the breadboard's rails can be very helpful in reducing clutter. For this tutorial, we'll do this first to reduce the wires needed.

1. Connect the `-` rails on either side of the board together on one end (usually the end away from most of the wiring) with a M-M jumper, we'll call this the ground (or GND) rail.
1. Do the same with the `+` rails, we'll call these Vcc rails in this tutorial.
// TODO: IMAGE of connected rails on a breadboard
1. Now that the rails are connected, we'll plug in two M-M jumpers to the ground and Vcc rails - we recommend using and reserving red wires for Vcc and black for ground to make it easier to debug.
	* Leave the other ends dangling for now - these will go into the power output of the expansion later
	* Power is usually wired in last to keep your chips and components safe from accidental shorts when you're wiring.
1. Grab your H-bridge, pick a location on your breadboard and plug the H-bridge across the channel in the middle of your breadboard. It should be setting across with one side in column E and the other in column F. We picked rows 5 to 12 in our breadboard.
// TODO: IMAGE of H-bridge across channel with pins labelled
1. Take note of where your pins are - look for the half circle denoting the 'top' of the H-bridge to orient it correctly.
	* **Note**: This is super important, because the H-bridge could quickly fry itself if it's wired incorrectly!
1. Wire pins `4`, `5`, `12`, and `13` to the ground rail on their respective sides using four M-M jumpers.
1. Using the three M-F jumpers,
	* Connect the row that pin `1` (labelled as `1,2EN`) on the IC is plugged into (row 5 on our board) to channel `S0` on the PWM expansion.
	* Connect pin `2` (`1A`, or row 6 on our board) to channel `S1`
	* Lastly, pin `7` (`2A`, or row 11) to channel `S2`
	* Your board should now look something like ours (below), make sure the pins on the IC and the channels on the PWM match properly, otherwise the code we'll run won't work!
1. Now it's time to connect the motor, the motor should have two wires with male pin connectors, one red and one black.
	* Connect the red wire to the row pin `3` is plugged into (for us, it's row 7)
	* Connect the black wire to *pin*  `7` (row 10 on our board)
1. We'll ground the circuit by connectin the dangling end of the ground (black) jumper wire to the `GND` pin on the expansion header.
1. Last but not least, we'll set power to the Vcc rail by connecting the dangling end of the Vcc (red) jumper to the `5V` pin on the expansion's header.


#### Writing the Code

// Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * write the hBridge class (from the file above) that drives an h-bridge
//  * don't have to bother with a DigitalPin class like the file above, just set the two direction inputs using 0% or 100% duty cycle

// the program:
//  * two switches: control how fast the motor spins (binary 00 -> 11, make sure to include a truth table)
//  * one switch: controls the direction (on is left, and off is right, or whatever makes sense)
// duty cycle: 0 -> 30 -> 40 -> 50


#### What to Expect

When run, the script starts the PWM oscillator, and then sets the output to be enabled (channel 0 to 100% duty). Then the script will ask you for a set of 3 digits, the first one sets the direction of the motor, the next two digits set the speed. The program will repeated ask for input, and adjust the speed and direction accordingly.

| Position        | Code | Result                        |
|-----------------|------|-------------------------------|
| First digit     | 0    | Motor turns clockwise         |
|                 | 1    | Motor turns counter clockwise |
| Last two digits | 00   | off                           |
|                 | 01   | 30% speed                     |
|                 | 10   | 40% speed                     |
|                 | 11   | 50% speed                     |

As you've probably seen before, we use an infinite loop here, and you can break it by hitting `ctrl`+`c`.

>We recommend setting the motor to 000 before breaking the loop to avoid damaging the motor. If you forgot, you can simply call `pwm-exp -s` to stop the motor in the terminal or ssh.


### A Closer Look at the Code

<!-- // is there something interesting about the code? if so cover it in this section -->
In this tutorial, we put together knowledge from the previous tutorials to control the DC motor with python. On top of that we mixed in python Tuples to codify the output we wish the PWM controller to send, and in doing so baked in failsafes to protect hardware from erroneous signalling. Finally, we used a lookup table to track and translate the input from the user into the output sent to the controller.

#### Tuples

In python, there's only one way to create 'permanent variables' - or to give values names: through what is known as a 'tuple'. It's short for multiple, and it represents a set of values that are permanent. In the code, we used it to enforce a set of signals to be sent to the PWM, so that the motor would always operate within range. In this way, tuples or other forms of permanent variables (`final` in java, or `#define` in C) can restrict devices to safe operating limits when dealing with variable user input. Here, no matter what you enter, the signals sent to operate the motor would always fall into either off, or between 30 to 50% power in either direction. This way, the motor never sees signal too low to force its turning, and never signals too high that would wear it out or damage the board.

#### Lookup Tables

You may notice that the input given by the user in the main loop is always checked against the [// TODO: fill in variable name] variable - this variable stores a set of known values to be checked against. In our case, the table contains valid user input matched with its corresponding output - also known as a key-value pair - and the script sends out the output to the PWM controller if the input obtained from the user matches any value in the table.

### Limits of PWM Motor Control

DC motors rely on an applied voltage to run, and using PWM means the motor is actually being 'tapped' by a series of pulses. Sort of like pushing a box to make it move versus tapping it really quickly. There's a limit to how short each tap can be before the the motor won't have time to react to it - if you send out a duty cycle of less than about 15% at 50Hz, you'll see the motor would wiggle, but won't rotate at all. Another way to see this in action is to set the motor to about 30%, but set the frequency to 100Hz, the same thing should happen, since the actual pulses of 'high' voltage being sent to the motor is dropping below a certain timeframe.

Try out different outputs to the motor and see how it behaves. If you're testing a project with motors and want to slow it down to debug, keeping the limitations of PWM motor control in mind can save you a lot of time!
