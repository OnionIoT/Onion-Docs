---
title: Using an H-Bridge
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---
<!-- // Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example, this (or something similar) is what the final result will be -->

## Controlling a DC Motor with an H-Bridge {#maker-kit-servo-h-bridge}

<!-- // this tutorial will show us how to control a dc motor using an h-bridge. we'll also continue using the class from the first example to create classes to help us accomplish our goals -->
For this tutorial, we'll be controlling a motor using the PWM expansion. To do this, the PWM expansion will send appropriate signals to an 'H-bridge' by changing duty cycles, and the H-bridge will transmit the signal to the motor. Using three switches, we can send signals to change the speed and direction of the motor

>If you need a refresher on how PWM (or Pulse-Width Modulation) works, you can find an explaination in the [Using PWM Expansion](#using-pwm-expansion) article.

<!-- dcmotor -->
```{r child = '../../shared/dcmotor.md'}
```

<!-- hbridge -->
```{r child = '../../shared/hbridge.md'}
```

The way a PWM signal operates a motor is by switching the power supply on and off really quickly. Normally this can be done sending the PWM signal to a transistor, and have the transistor switch ther power supply, but an H-bridge adds functionality to this control by allowing the direction of the current to be easily changed. In the H-bridge diagram above, the PWM expansion will be sending signals to open and close the four switches on the H-bridge. In our circuit, we'll be using an H-bridge integrated chip (IC) so we don't need to wire the internals ourselves, and to prevent short circuits that could arise if we directly controlled those switches.

If you want to start building right away, skip ahead to the [next section](#controlling-a-dc-motor-with-an-h-bridge-building-the-circuit). If you'd like to know how the signals from our code will control the motor, read on!

#### The SN754410 Integrated H-Bridge Chip

The [SN754410 chip](http://www.ti.com/lit/ds/symlink/sn754410.pdf) contains two H-bridges, allowing control of four outputs. The chip conveniently handles short circuit situations and simplifies the operation of an H-bridge to two switches from four. So instead of S1/S2/S3/S4 (as seen above), we'll be switching `1A` and `2A` (as seen in the datasheet). For this tutorial, we'll be using one of the two H-bridges to control power sent to the two inputs of your DC motor. Specifically, the pair of inputs and outputs (`1A`, `2A` and `1Y`, `2Y`) on the left side of the chip.

<!-- // TODO: IMAGE diagram of the SN754410 -->

On the chip, `1A` controls the polarity of `1Y`, same goes for `2A` and `2Y`. At a very high level, this H-bridge chip changes the output voltage (to the pins labelled `Y`) according to the input voltage sent to the pins labelled `A`. For example, sending a 'high' to `1A` will send the same to `1Y`. The difference is the signal sent out to `Y` pins use the voltage supplied to pin `8` regardless of what the input voltage is.

Voltage acts kind of like a waterfall - it always sends the current flowing from the voltage **source** (top) to the **ground** (bottom). You can think of the source as `HIGH` and ground as `LOW`. So if you connect a motor to `1Y` and `2Y`, it'll only move if they're sending out **different** signals.

The `1,2EN` pin simply turns the H-bridge on or off. If `1,2EN` sees a 'high', then everything we've covered above happens as normal, if it's off, then there won't be anything sent to the outputs no matter what `1A` and `2A` are set to.


### Building the Circuit {#controlling-a-dc-motor-with-an-h-bridge-building-the-circuit}
This circuit will connect the Omega to a DC motor through the PWM expansion, and then through an H-bridge. The PWM will signal how fast the motor should turn. The H-bridge acts as a switch - turning the supply voltage on or off according to the PWM signal.
This build can get a bit messy, if you want to make sure your board cleans up nicely, we recommend using short wires (Male-to-Male) for connecting `GND` and `Vcc` points from the components to the rails. If you're not sure how that would work, just swap 12 male-to-male jumpers for 12 shorter wires when gathering components, we'll let you know in the instructions whenever you can use shorter wires.

For better viewing, we taped a piece of paper to the motor axle to see the rotations clearly.

**Note**: As can be seen above, the chip is roughly mirrored. The top right and bottom left pins are the power supply for the outputs (`pin 8`) and the chip (`pin 16`) respectively. The difference between the two power pins is the voltage supplied to the outputs can be up to 36V, while the voltage supplied to the chip is recommended to be within 2~5V. If you want to power a large motor, you should power the motor with the external supply through `pin 8` and supply around 3V to `pin 16`.


#### What You'll Need

You may need some stuff that isn't in the kit for this build. Altogether, this is what you'll be using to make the circuit:

* 1x Omega2 plugged into Expansion Dock
* 1x PWM Expansion plugged into Expansion Dock above
* 1x DC Motor
* 1x H-bridge (has "SN754410" on top of the chip)
* 1x Breadboard
* 1x Something solid to mount the motor on \*
* 1x Method of strapping the motor down \*
* 3x SPDT switches
* Jumper wires
	* 4x M-F
	* 18x M-M

\* - These are optional because they don't come with the kit. Nonetheless we recommend tying the motor down as it does not like to stay put when it's running.

#### Hooking up the Components

<!-- // omega -> h-bridge: three channels from pwm expansion to control the two input pins and the duty cycle pin, all requisite wiring for power
//  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)
// h-bridge -> dc motor: the h-bridge motor outputs to the motor... duh

// make sure to drive home the point that the H-bridge can be burnt if improperly wired
//  make sure the pwm expansion is not producing any signals (or they're all at 0%) while you're wiring it -->

<!-- // the # of SPDT switches in the kit will be increased to 10 as of 2017-01-01 -->

When working with ICs, setting up the breadboard's rails can be very helpful in reducing clutter. For this tutorial, we'll do this first to reduce the wires needed.

1. Connect the negative (`-`) rails on either side of the board together on one end (usually the end away from most of the wiring) with a M-M jumper, we'll call this the `GND` rail.
1. Do the same with the positive (`+`) rails, we'll call these `Vcc` rails in this tutorial.

<!-- // TODO: IMAGE of connected rails on a breadboard -->

3. Grab your H-bridge, pick a location on your breadboard and plug the H-bridge across the channel in the middle of your breadboard. It should be sitting across with one side in column E and the other in column F, with the **half-circle cutout** pointing toward the closer edge of the breadboard. We picked rows 5 to 12 in our breadboard.

<!-- // TODO: IMAGE of H-bridge across channel with pins labelled -->

4. Take note of which number each pin is from the diagram above - if you're lost, always look for the little half circle cutout on the chip denoting the 'top' of the H-bridge to orient it correctly.
	* **This is important, you can damage the H-bridge if it's not wired correctly!**
1. Wire pins `4`, `5`, `12`, and `13` to the `GND` rail on their respective sides using four M-M jumpers. Use short wires here if you have them handy.

1. Now it's time to connect the motor to the H-bridge, the motor should have two wires with male pin connectors, one red and one black. They'll be connected to the pins on the H-bridge through the breadboard.
    * Connect the red wire to pin `3` of the H-bridge (row 7 on our breadboard).
    * Connect the black wire to pin  `7` of the H-bridge (row 10 on our board).

1. Next, we'll set up the switches - we'll use them to send digital signals to control the PWM, and in turn the motor.
	* Pick three sets of three rows (we used row 25 to 33)
	* Plug your switches into the rows, three rows per switch
1. Using 3 M-M jumpers, connect the center row of each switch to GPIO6, GPIO7, and GPIO8. Make sure you remember which is which, since these will control your motor later!
1. With 6 M-M jumpers, connect the leftmost row of each switch to `GND` rail, and the rightmost row of each switch to `Vcc` rail. If you have short wires ready, you should use them here.
1. Take one M-M jumper and connect `pin 1` on the IC (row 5 on our board) to `pin 1` on the expansion headers.
1. Using two M-F jumpers,
	* Connect pin `2` (`1A`, or row 6 on our board) to channel `S0`.
	* Connect pin `7` (`2A`, or row 11) to channel `S1`.
	* Your board should now look something like ours (below), make sure the pins on the IC and the channels on the PWM match properly, otherwise the code we'll run won't work!

<!-- TODO: IMAGE of fully wired H-bridge, short wires, pins labelled -->

1. We'll ground the circuit by connecting the `GND` rail to the `GND` pin on channel `S0` on the PWM expansion with one M-F jumper.
1. Last but not least, we'll set power to the Vcc rail by connecting the dangling end of the Vcc (red) jumper to the `VCC` pin of channel `S0` of the PWM expansion.

There is a reason we use the `GND` and `Vcc` pins on the **PWM expansion** instead on the header pins from the dock. If it's connected to the header pins, the motor will feedback voltage to the expansion dock. This can cause a boot-loop or other unpredictable behaviour with the omega. The PWM expansion's `Vcc`/`GND` pins have circuit breaking diodes in place to prevent this.

>Power is usually wired in last to keep your chips and components safe from accidental shorts when you're wiring.

### Writing the Code

<!-- // Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * write the hBridge class (from the file above) that drives an h-bridge
//  * don't have to bother with a DigitalPin class like the file above, just set the two direction inputs using 0% or 100% duty cycle

// the program:
//  * two switches: control how fast the motor spins (binary 00 -> 11, make sure to include a truth table)
//  * one switch: controls the direction (on is left, and off is right, or whatever makes sense)
// duty cycle: 0 -> 30 -> 40 -> 50
-->

Let's add a class blueprint for a DC motor controlled by an H-bridge to our motors file we made in the previous tutorial. Open the `motors.py` file and add this:


``` python
class hBridgeMotor:
	"""Class that two digital signals and a pwm signal to control an h-bridge"""

	def __init__(self, fwdChannel, revChannel):
		# note the channels
		self.fwdChannel		= fwdChannel
		self.revChannel 	= revChannel

		# setup the objects
		self.fwdDriver 		= OmegaPwm(self.fwdChannel)
		self.fwdDriver.setDutyCycle(0)
		self.revDriver 		= OmegaPwm(self.revChannel)
		self.revDriver.setDutyCycle(0)

		# setup the limitations
		self.minDuty 		= 0
		self.maxDuty		= 100

	def setupMinDuty(self, duty):
		"""Set the minimum allowed duty cycle for pwm"""
		self.minDuty 		= duty

	def setupMaxDuty(self, duty):
		"""Set the maximum allowed duty cycle for pwm"""
		self.maxDuty 		= duty

	def reset(self):
		"""Set the PWM to 0%, disable both h-bridge controls"""
		ret 	|= self.fwdDriver.setDutyCycle(0)
		ret 	|= self.revDriver.setDutyCycle(0)

		return ret

	def drive(self, direction, duty):
		"""Set the PWM to the specified duty, and in the specified direction"""
		ret 	= 0
		if duty < self.minDuty:
				duty 	= self.minDuty
    elif duty > self.maxDuty:
        duty 	= self.maxDuty


		# 0 - forward, 1 - reverse
		if (direction == H_BRIDGE_MOTOR_FORWARD):
			self.revDriver.setDutyCycle(0)
			self.fwdDriver.setDutyCycle(duty)
		elif (direction == H_BRIDGE_MOTOR_REVERSE):
			self.fwdDriver.setDutyCycle(0)
			self.revDriver.setDutyCycle(duty)
		else:
			ret 	= -1

		return ret

	def spinForward(self, duty):
		ret 	= self.drive(H_BRIDGE_MOTOR_FORWARD, duty)
		return ret

	def spinReverse(self, duty):
		ret 	= self.drive(H_BRIDGE_MOTOR_REVERSE, duty)
		return ret
```

Next, let's write the code for the experiment. Create a file called `MAK03-hBridgeExperiment.py` and paste the following code in it:

``` python
from omegaMotors import hBridgeMotor
import onionGpio
import time

# set up hbridge pins on the Omega
dircSignalPin = onionGpio.OnionGpio(6)
spd1SignalPin = onionGpio.OnionGpio(7)
spd2SignalPin = onionGpio.OnionGpio(8)
motor1A = 0
motor2A = 1

# create a dictionary of functions against which to check user input
# this is basically a dispatch table to map function calls to different names
motorCommands = {
    '000': (lambda motor: motor.reset()),
    '001': (lambda motor: motor.spinForward(30)),
    '010': (lambda motor: motor.spinForward(40)),
    '011': (lambda motor: motor.spinForward(50)),
    '100': (lambda motor: motor.reset()),
    '101': (lambda motor: motor.spinReverse(30)),
    '110': (lambda motor: motor.spinReverse(40)),
    '111': (lambda motor: motor.spinReverse(50)),
}

def main():
    # instantiate the motor object
    motor = hBridgeMotor(motor1A, motor2A)
    command = '000';

    # loop forever
    while(True):
				# sleeps for a bit to accomodate slow switches
				time.sleep(0.5)

				# gets the signals going through the switches
        commandNew = dircSignalPin.getValue()[0]
        commandNew = commandNew + spd1SignalPin.getValue()[0]
        commandNew = commandNew + spd2SignalPin.getValue()[0]

				# parses the command into motorCommands format
        commandNew.replace('\n', '')

        # check user input against dictionary, run the corresponding function
        if (command != commandNew):
            command = commandNew
            motorCommands[command](motor)

if __name__ == '__main__':
    main()
```

### What to Expect
<!-- TODO: IMAGE or gif of project working -->
When run, the script starts the PWM oscillator, and then sets the output to be enabled (channel 0 to 100% duty). Then the script will ask you for a set of 3 digits, the first one sets the direction of the motor, the next two digits set the speed. The program will repeated ask for input, and adjust the speed and direction accordingly.

| Position        | Code | Result                        |
|-----------------|------|-------------------------------|
| First digit     | 0    | Motor turns clockwise         |
|                 | 1    | Motor turns counter clockwise |
| Last two digits | 00   | off                           |
|                 | 01   | 30% speed                     |
|                 | 10   | 40% speed                     |
|                 | 11   | 50% speed                     |

As you've probably seen before, we use an infinite loop here, and you can break it by hitting `Ctrl-C`.

**Note**: We recommend setting the motor to `000` before breaking the loop to avoid damaging the motor. As a reminder, you can simply call `pwm-exp -s` to stop the motor in the terminal or ssh.

### A Closer Look at the Code

// TODO: remove and replace with whatever you introduce above - tuples probably won't work in this situation

In this tutorial, we put together knowledge from the previous tutorials to control a DC motor with Python. We're now **receiving user input** interactively, allowing us to change the output in real-time. On top of that we we used a **lookup table** to track and translate the input from the user into the output sent to the controller.

#### Receiving User Input

Here we started to interactively obtain input in a very controlled way. With some quick math, there's only 8 ways a set of 3 switches can be flipped. This means that we really only have to account for 8 separate input cases. However when requesting and processing user input, always keep in mind that all kinds of different inputs can be recieved. Here, our error checking happens right at the start of the interaction by limiting the number of inputs that the user has access to in the first place. If we allowed users to enter arbitrary commands, we would have to do a lot more validation.

#### Lookup Tables

You may notice that the input given by the user in the main loop is always checked against the motorCommands variable - this variable stores a set of known values to be checked against. In our case, the table contains valid switch input matched with its corresponding output - also known as a key-value pair - and the script sends out the output to the PWM controller if the input obtained from the user matches any value in the table.

By checking input against a lookup table before sending commands, we can guarantee that no erroneous commands are sent. Couple this with proper calibration and we can greatly reduce the risk of operating hardware remotely.

### Limits of PWM Motor Control

DC motors rely on an applied voltage to run, and using PWM means the motor is actually being 'tapped' by a series of pulses. Sort of like pushing a box to make it move versus tapping it really quickly. There's a limit to how short each tap can be before the the motor won't have time to react to it - if you send out a duty cycle of less than about 15% at 50Hz, you'll see the motor would wiggle, but won't rotate at all. Another way to see this in action is to set the motor to about 30%, but set the frequency to 100Hz, the same thing should happen, since the actual pulses of 'high' voltage being sent to the motor is dropping below a certain timeframe.

Try out different outputs to the motor and see how it behaves. If you're testing a project with motors and want to slow it down to debug, keeping the limitations of PWM motor control in mind can save you a lot of time!

Next time, we [write text to a screen](#maker-kit-oled-writing-text).
