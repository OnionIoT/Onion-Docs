---
title: Using an H-Bridge
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---

<!-- // DONE: always capitalize Onion products: PWM Expansion, Expansion Dock, on the Dock, etc -->

<!-- // DONE: Expansion Dock GPIOs should be referred to as Omega GPIOx, can include 'on the Expansion Header' to make it clear -->
<!-- // DONE: the 5V, 3.3V, and GND pins should be referred to as 5V, 3.3V, and GND pins on the Expansion Header -->

## Controlling a DC Motor using an H-Bridge {#maker-kit-servo-h-bridge}

<!-- // this expriment will show us how to control a dc motor using an h-bridge. we'll also continue using the class from the first example to create classes to help us accomplish our goals -->

<!-- // DONE: this is the rewritten intro -->
For this expriment, we'll be controlling a motor using the PWM Expansion. To do this, we'll be using an H-Bridge chip and sending it the appropriate control signals with the PWM Expansion, the H-Bridge will then take care of running the motor. Along the way, we'll learn exactly how H-Bridges work and create more classes that take advantage of the ones we've made previously. To expand on that, we'll hook up three switches and program the Omega to control the speed and direction of the motor based on their positions.

<!-- // this is the old intro: -->
<!-- For this expriment, we’ll be controlling a motor using the PWM Expansion. To do this, the PWM Expansion will send appropriate signals to an ‘H-bridge’ by changing duty cycles, and the H-bridge will transmit the signal to the motor. Using three switches, we can send signals to change the speed and direction of the motor -->
<!-- // note the changes, -->

<!-- // DONE: this should point back to the previous experiment, not a Docs article -->

>If you need a refresher on how PWM (or Pulse-Width Modulation) works, you can find an explaination in the [first dimming LED expriment](#maker-kit-servo-dimming-led).

<!-- dcmotor -->
```{r child = '../../shared/dcmotor.md'}
```

<!-- hbridge -->
```{r child = '../../shared/hbridge.md'}
```

<!--
// DONE: i like what this is trying to convey, but I think a more logical ordering would be to talk about:
//	* controlling a DC motor's speed using PWM
//	* how the H-bridge provides the capability of choosing the direction
//	* how we're going to be pulsing (applying a PWM signal to) an H-bridge input to control the speed of our motor
-->

The way a PWM signal operates a motor is by switching the power supply on and off really quickly. Normally this can be done sending the PWM signal to a transistor, and have the transistor switch ther power supply. By varying the pulsewidth of the PWM signal, the speed of the motor can be controlled. An H-bridge can replace the transistor and add functionality by allowing the direction of the current to be easily changed. We still send a pulsating signal to the H-bridge in order to control the speed, except now we can switch the direction of the current flow by changing which switches are open.

In our circuit, we'll be using an H-bridge Integrated Circuit (**IC**) chip so we don't need to wire the internals ourselves, and to prevent short circuits that could arise if we directly controlled those switches.
<!-- // DONE: NOTE: IC stands for Integrated Circuit! -->

If you want to start building right away, skip ahead to the [next section](#controlling-a-dc-motor-with-an-h-bridge-building-the-circuit). If you'd like to know how the signals from our code will control the motor, read on!

<!-- // DONE: move this section into it's own markdown file -->

```{r child='../../shared/hbridge-ic.md'}
```


### Building the Circuit {#controlling-a-dc-motor-with-an-h-bridge-building-the-circuit}

<!--
// DONE: this first sentence is a little convoluted
//	* should be Omega -> PWM Expansion -> H-Bridge -> DC motor
-->

This circuit will connect the Omega to a DC motor. The Omega will first be connected to the PWM Expansion, the PWM Expansion will be sending signals to an H-bridge, which will deliver power to the DC motor according to the signals. The PWM will signal how fast the motor should turn and the H-bridge acts as a switch - turning the supply voltage on or off according to the PWM signal.

<!-- // DONE: include a block diagram of the system -->
![How our circuit will work](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/03-block-diagram.png)

In the pictures, you'll see some shorter wires, these we used instead of jumpers to give you a better picture of what's going on. To more easily see the rotations of the motor, we wrapped some duct tape around the motor axle.
<!-- // DONE: let's not overcomplicate by telling them to use shorter wires since they don't have shorter wires. -->
<!-- // * just state that in our pictures we've used shorter wires to better illustrate the connections that need to be made. -->
<!-- // * Tell them that this is just for illustration purposes and using longer wires won't make a difference -->
<!-- // * also, take out the parts of how this build can get messy. just say that there's a lot of connections that need to be made -->


**Note**: As can be seen above, the chip is roughly mirrored. The top right and bottom left pins are the power supply for the outputs (`pin 8`) and the chip (`pin 16`) respectively. The difference between the two power pins is the voltage supplied to the outputs can be up to 36V, while the voltage supplied to the chip is recommended to be within 2~5V. If you want to power a large motor, you should power the motor with the external supply through `pin 8` and supply around 3V to `pin 16`.


<!-- // DONE: include a circuit diagram -->
Here's a diagram to refer back to if things get hectic:

![Circuit diagram for this experiment](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/diagrams/03-circuit-diagram.png)


#### What You'll Need

<!-- // DONE: don't mention that 'we need stuff that isn't in the Kit', that makes us look bad. instead recommend they grab a rubber band to hold the motor steady or something along those lines -->

You may need a couple of rubber bands and a block to hold down the DC Motor when it's running. Altogether, this is what you'll be using to make the circuit:

* 1x Omega2 plugged into Expansion Dock
* 1x PWM Expansion plugged into Expansion Dock above
* 1x DC Motor
* 1x H-bridge (has "SN754410" on top of the chip)
* 1x Breadboard
* 3x SPDT switches
* Jumper wires
	* 4x M-F
	* 18x M-M


#### Hooking up the Components

<!-- 
// omega -> h-bridge: three channels from pwm expansion to control the two input pins and the duty cycle pin, all requisite wiring for power
//  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)
// h-bridge -> dc motor: the h-bridge motor outputs to the motor... duh

// make sure to drive home the point that the H-bridge can be burnt if improperly wired
//  make sure the pwm expansion is not producing any signals (or they're all at 0%) while you're wiring it -->

<!-- // the # of SPDT switches in the kit will be increased to 10 as of 2017-01-01 -->

When working with ICs, setting up the breadboard's rails can be very helpful in reducing clutter. For this expriment, we'll do this first to reduce the wires needed.

1. Connect the negative (`-`) rails on either side of the board together on one end (usually the end away from most of the wiring) with a M-M jumper, we'll call this the `GND` rail.
1. Do the same with the positive (`+`) rails, we'll call these `Vcc` rails in this expriment.

<!-- // DONE: IMAGE of connected rails on a breadboard -->
![How the breadboard rails are connected together](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/03-rails-connected.jpg)

Now let's set up our Circuit:

1. Grab your H-bridge, pick a location on your breadboard and plug the H-bridge across the channel in the middle of your breadboard. It should be sitting across with one side in column E and the other in column F, with the **half-circle cutout** pointing toward the end of the breadboard. We picked rows 5 to 12 in our breadboard.

<!-- // DONE: IMAGE of H-bridge across channel with pins labelled -->
![The H-bridge sitting in the breadboard](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/03-h-bridge-wired.png)


<!-- // DONE: when talking about IC pins, I would rather refer to them by the NAME of the pin, so 'wire 3A to GND' as opposed to 'pin 5 to GND' -->
<!-- //	the goal is to teach them what's going on, rather then have them follow wiring instructions -->

1. Take note of which number each pin is from the diagram above - if you're lost, always look for the little half circle cutout on the chip denoting the 'top' of the H-bridge to orient it correctly.
	* **This is important, you can damage the H-bridge if it's not wired correctly!**
1. Let's connect first connect all the ground connections - pins `4`, `5`, `12`, and `13` on the H-bridge are are all grounding pins, so let's connect those to the `GND` rail on their respective sides using four M-M jumpers. We used short wires here to make sure you can see what's going on.

<!-- // DONE: mention that we used short wires here to better illustrate the connections -->

1. Now it's time to connect the motor to the H-bridge, the motor should have two wires with male pin connectors, one red and one black. They'll be connected to the pins on the H-bridge through the breadboard.
    * Connect the white wire to `1Y` of the H-bridge (row 7 on our breadboard).
    * Connect the black wire to `2Y` of the H-bridge (row 10 on our board).

<!-- // DONE: won't we be using the switches as digital inputs to our program, which will then decide what to send to the PWM Expansion, which then controls the H-Bridge, and finally causes the motor to turn -->

1. Next, we'll set up the switches - we'll use them to control what digital signals are sent to the PWM Expansion, and in turn the motor through the H-bridge:
	* Pick three sets of three rows (we used row 14 to 24)
	* Plug your switches into the rows, three rows per switch - each switch needs a half-row of clearance between the next switch if you want to put them side-by-side.
1. With 6 M-M jumpers, connect the leftmost row of each switch to `GND` rail, and the rightmost row of each switch to `Vcc` rail.

<!-- DONE: IMAGE of fully wired H-bridge, short wires, pins labelled -->
![The motor, H-bridge, and switches wired](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/03-motor-h-bridge-switches.jpg)


<!-- // DONE: this sentence should be more like 'The H-Bridge circuit is done! Now let's connect it to the PWM Expansion so it can be controlled by the Omega' -->

Now that the H-bridge circuit is done, let's connect the whole thing to your Omega so it can control the motor:

1. We'll ground the circuit by connecting the `GND` rail to the `GND` pin on channel `S0` on the PWM Expansion with one M-F jumper.
1. Using 3 M-M jumpers, connect the center row of each switch to Omega GPIO0, GPIO1, and GPIO2 on the Expansion Headers. Make sure you remember which is which, since these will control your motor later!
1. Take one M-M jumper and connect `1,2EN` on the IC (row 5 on our board) to the `Vcc` rail.
1. Using two M-F jumpers,
	* Connect `1A`, or row 6 on our board, to channel `S0`.
	* Connect `2A`, or row 11, to channel `S1`.
1. Last but not least, we'll set power to the Vcc rail by connecting the dangling end of the Vcc (red) jumper to the `Vcc` pin of channel `S0` of the PWM Expansion.

Here's what it looks like when it's all wired up:

<!-- DONE: IMAGE assembled circuit -->
![All done!](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/03-assembled-circuit.jpg)


<!-- wiring precautions -->
```{r child = '../../shared/wiring-precautions.md'}
```

>There is a reason we use the `GND` and `Vcc` pins on the **PWM Expansion** instead on the header pins from the Dock. If it's connected to the header pins, the motor will feedback voltage to the Expansion Dock. This can cause a boot-loop or other unpredictable behaviour with the omega. The PWM Expansion's `Vcc`/`GND` pins have circuit breaking diodes in place to prevent this.



### Writing the Code

<!-- // Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * write the hBridge class (from the file above) that drives an h-bridge
//  * don't have to bother with a DigitalPin class like the file above, just set the two direction inputs using 0% or 100% duty cycle

// the program:
//  * two switches: control how fast the motor spins (binary 00 -> 11, make sure to include a truth table)
//  * one switch: controls the direction (on is left, and off is right, or whatever makes sense)
// duty cycle: 0 -> 30 -> 40 -> 50
-->

<!-- // DONE: its a class definition, not a blueprint, beginner users might get the idea that 'blueprint' is the legit terminology -->

Let's add a class definition for a DC motor controlled by an H-bridge to the `motors.py` file we made in the previous expriment. This class definition will specifically drive a DC motor hooked up to an H-bridge. It builds on the abstractions in the `OmegaPwm` class and takes care of the details in operating the motor.

Open up `motors.py` from the [Dimming LEDs experiment](#maker-kit-servo-dimming-led) and add the following:

``` python
H_BRIDGE_MOTOR_FORWARD = 0
H_BRIDGE_MOTOR_REVERSE = 1

class hBridgeMotor:
    """Class that two digital signals and a pwm signal to control an H-Bridge"""

    def __init__(self, pwmChannel, fwdChannel, revChannel):
        # note the channels
        self.pwmChannel = pwmChannel
        self.fwdChannel = fwdChannel
        self.revChannel = revChannel

        # setup the objects
        self.pwmDriver = OmegaPwm(self.pwmChannel)
        self.pwmDriver.setDutyCycle(0)
        self.fwdDriver = OmegaPwm(self.fwdChannel)
        self.fwdDriver.setDutyCycle(0)
        self.revDriver = OmegaPwm(self.revChannel)
        self.revDriver.setDutyCycle(0)

        # set the constraints
        self.minDuty = 0
        self.maxDuty = 100

    def setupMinDuty(self, duty):
        """Set the minimum allowed duty cycle for pwm"""
        self.minDuty = duty

    def setupMaxDuty(self, duty):
        """Set the maximum allowed duty cycle for pwm"""
        self.maxDuty = duty

    def reset(self):
        """Set the PWM to 0%, disable both H-Bridge controls"""
        ret =  self.pwmDriver.setDutyCycle(0)
        ret |= self.fwdDriver.setDutyCycle(0)
        ret |= self.revDriver.setDutyCycle(0)

        return ret

    def spin(self, direction, duty):
        """Set the PWM to the specified duty, and in the specified direction"""
        ret = 0

        # 0 - forward, 1 - reverse
        if (direction == H_BRIDGE_MOTOR_FORWARD):
            self.revDriver.setDutyCycle(0)
            self.fwdDriver.setDutyCycle(100)
        elif (direction == H_BRIDGE_MOTOR_REVERSE):
            self.fwdDriver.setDutyCycle(0)
            self.revDriver.setDutyCycle(100)
        else:
            ret = -1

        if (ret == 0):
            # check against the minimum and maximium pwm
            if duty < self.minDuty:
                duty     = self.minDuty
            elif duty > self.maxDuty:
                duty     = self.maxDuty

            # program the duty cycle
            ret = self.pwmDriver.setDutyCycle(duty)
        return ret

    def spinForward(self, duty):
        ret = self.spin(H_BRIDGE_MOTOR_FORWARD, duty)
        return ret

    def spinReverse(self, duty):
        ret = self.spin(H_BRIDGE_MOTOR_REVERSE, duty)
        return ret
```

Next, let's write the code for the experiment. This code will get the motor to actually do stuff using the hBridgeMotor class we've made above. The script will ask you to enter some numbers, and drives the motor based on your input!

Create a file called `MAK03-hBridgeExperiment.py` and paste the following code in it:

<!--
// DONE: this code is overkill for what we're doing... no need for the lambda stuff
// let's explore a simpler solution:
//	* have a lookup table for the speed control:
//		00 -> 25%
//		01 -> 50%
//		10 -> 75%
//		11 -> 100%
//		- ideally, have a function that takes the switch values as input and returns the duty cycle
//	* read the direction switch into a variable to get 0 or 1 for direction
// 	* just have a single `hBridge(direction, dutyCycle)` call to control the motor
-->

<!-- // DONE: another oversight, it's useful to be able to disable our motor completely. We might not use it in this example, but still useful -->
<!-- //	* see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py#L152 for an example, should use a PWM Expansion channel to control the H-Bridge 1,2EN -->

``` python
from motors import hBridgeMotor
import onionGpio
import time

# setup PWM Expansion Channels connected to H-Bridge IC
H_BRIDGE_1A_CHANNEL = 0
H_BRIDGE_2A_CHANNEL = 1
H_BRIDGE_12EN_CHANNEL = 2

# instantiate gpio objects for our switch inputs
directionGPIO = onionGpio.OnionGpio(0)
speed1GPIO = onionGpio.OnionGpio(1)
speed2GPIO = onionGpio.OnionGpio(2)

# create a dictionary of functions against which to check user input
# this is basically a dispatch table to map function calls to different names
motorCommands = {
    '000': (lambda motor: motor.reset()),
    '001': (lambda motor: motor.spinForward(50)),
    '010': (lambda motor: motor.spinForward(60)),
    '011': (lambda motor: motor.spinForward(70)),
    '100': (lambda motor: motor.reset()),
    '101': (lambda motor: motor.spinReverse(50)),
    '110': (lambda motor: motor.spinReverse(60)),
    '111': (lambda motor: motor.spinReverse(70)),
}

def main():
    # instantiate the motor object
    motor = hBridgeMotor(H_BRIDGE_12EN_CHANNEL, H_BRIDGE_1A_CHANNEL, H_BRIDGE_2A_CHANNEL)
    command = '000';

    # loop forever
    while(True):
        # sleeps for a bit to accomodate switches
        time.sleep(0.5)

        # gets the signals going through the switches
        commandNew = directionGPIO.getValue()[0]
        commandNew = commandNew + speed1GPIO.getValue()[0]
        commandNew = commandNew + speed2GPIO.getValue()[0]

        # parses the command into motorCommands format
        commandNew.replace('\n', '')

        # check user input against dictionary, run the corresponding function
		#   but only if the command has changed, no need to keep calling the same command
        if (command != commandNew):
            command = commandNew
            motorCommands[command](motor)


if __name__ == '__main__':
    main()
```

<!--
// DONE: everything from here on out needs to be updated to reflect that we're using switches and new code.
// * When the new code is done, reconfigure this to fit the circuit and code
-->

### What to Expect

When run, the script starts the PWM oscillator, and then sets the output to be enabled (channel 0 to 100% duty). Then the script will ask you for a set of 3 digits, the first one sets the direction of the motor, the next two digits set the speed. The program will repeated ask for input, and adjust the speed and direction accordingly.

| Position        | Code | Result                        |
|-----------------|------|-------------------------------|
| First digit     | 0    | Motor turns clockwise         |
|                 | 1    | Motor turns counter clockwise |
| Last two digits | 00   | off                           |
|                 | 01   | 50% speed                  |
|                 | 10   | 60% speed                  |
|                 | 11   | 70% speed                     |

<!-- // DONE: the above speed digits need to be updatd -->

Here it is in action:

<!-- DONE: IMAGE or gif of project working -->
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zC9l3LXt4fs" frameborder="0" allowfullscreen></iframe>


As you've probably seen before, we use an infinite loop here, and you can break it by hitting `Ctrl-C`.

**Note**: We recommend setting the motor to `000` before breaking the loop to avoid damaging the motor. As a reminder, you can simply call `pwm-exp -s` to stop the motor in the terminal or ssh.

### A Closer Look at the Code

In this expriment, we put together knowledge from the previous expriments to control a DC motor with Python. We're now **receiving user input** interactively, allowing us to change the output in real-time. On top of that we we used a **lookup table** to track and translate the input from the user into the output sent to the controller.

#### Receiving User Input

<!-- DONE: see embeded todo -->

Here we started to interactively obtain input in a very controlled way. Each switch has two states - 1/ON/HIGH and 0/OFF/LOW. So for three switches there's `2^3 = 8` differt states of the switch system. This means that we really only have to account for 8 separate input cases. 

Unfortunately it's not always this easy, and it's good practice to assume all kinds of different inputs can be recieved. Here a good deal error checking happens right at the start of the interaction by limiting the number of input states that are available - we only have three switches. If we allowed users to enter arbitrary commands, we would have to do a lot more validation.

#### Lookup Tables

You may notice that the input given by the user in the main loop is always checked against the motorCommands variable - this variable stores a set of known values to be checked against. In our case, the table contains valid switch input matched with its corresponding output - also known as a key-value pair - and the script sends out the output to the PWM controller if the input obtained from the user matches any value in the table.

By checking input against a lookup table before sending commands, we can guarantee that no erroneous commands are sent. Couple this with proper calibration and we can greatly reduce the risk of operating hardware remotely.

### Limits of PWM Motor Control

DC motors rely on an applied voltage to run, and using PWM means the motor is actually being 'tapped' by a series of pulses. Sort of like pushing a box to make it move versus tapping it really quickly. Just like there's a minimum amount of force needed for a tap to get a box moving, there's a limit to how short each tap can be before the the motor won't to react to it. 

That is to say, if the pulsewidth is below a certain threshold, the motor won't start. In testing, the pulsewidth needed to start the motor is somewhere around 10ms - about 50% duty at 50Hz.

<!-- // DONE: rewrite the above so the main concept your're talking about is the pulse width in ms, then make comments on the duty cycle and frequency as a corollary -->

Try out different motor settings and see how it behaves. If you're testing a project with motors and want to slow it down to debug, keeping the limitations of PWM motor control in mind can save you a lot of time!

Next time, we [write text to a screen](#maker-kit-oled-writing-text).
