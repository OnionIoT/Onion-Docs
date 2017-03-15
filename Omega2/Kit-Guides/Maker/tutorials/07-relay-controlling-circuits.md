---
title: Controlling Other Circuits
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 7
---
## Isolated Control with the Relay Expansion {#maker-kit-relay-controlling-circuits}

In this tutorial, we'll use a switch with the Omega Relay expansion to turn a buzzer on or off. Along the way, we'll be looking into why relays are useful, and go into more detail regarding pitfalls when interacting with hardware.

<!-- // TODO: can modify or replace this warning with the one from our store (should keep same friendly tone) -->
**Note:** this Expansion allows you to switch power sources of a **much higher voltage** than the board - and possibly your body - is able to handle. This experiment is designed to be very safe. However for future, we urge you to read up the specifications of the [Relay Expansion](#relay-expansion) in our hardware overview documentation to understand the capabilities and limits of the Relay Expansion.

**We at Onion cannot accept any responsibility for any damages caused by improper use of the Relay Expansion.**

### Circuit Isolation

<!-- // explain that the omega's relays are completely isolated from the circuit that is connected to the terminals, it merely acts as a switch

// this is useful since it allows the Omega to control other, larger, more powerful circuits
//  expand along those lines, maybe throw in the max specs of the relays, hint that you can control house-hold appliances -->

Omega boards and components are not designed to handle much more than 5V circuit and 12V supply. Attempting to directly control 120V appliances like lights, heaters, garage doors will almost certainly fry your Omega. So how can you turn on your lights?

Enter the **relay**! A relay is a mechanical switch that is triggered electronically. This physically separates the circuit that triggers the switch and the circuit that the switch actually switches. The relay expansion is designed to isolate the Omega and the dock from high power circuits while still allowing them to be controlled by the Omega.


### Building the Circuit

Our goal here is to connect a buzzer to the relay expansion and a power supply, and then connect a switch to the Omega's expansion headers. Once it's set up, we'll use the code to turn the buzzer on and off.

The switch used here is an SPDT switch - Single Pole, Dual Throw. Single pole means there's a single power source being switched, dual throw means the power is always connected to one output or the other. The middle pin is the power input, and the two pins on the side are the outputs. Here we'll just use a single output, leaving the other as open circuit.

>In this tutorial, we'll be using the power supplied by our Dock due to easy access. Feel free to try using different power supply methods, but take note you may need voltage dropping resistors for higher powered supplies to avoid burning out the buzzer.

#### What You'll Need

Grab the components listed from your kit, and let's get wiring!

* 1x Omega plugged into the Expansion Dock
* 1x Relay Expansion
* 1x Buzzer
* 1x SPDT (or three-way) switch
* 1x Breadboard
* 7x Jumper wires (M-M)

#### Hooking up the Components

The circuit for this

1. First we'll have to find a place on the breadboard to place the buzzer, we chose row 1 and mounted the buzzer across the middle channel.
	* Taking note where the cathode (+) and where the anode (-) is, we'll have to make sure the right wires go in the right terminal.
1. Connect the anode of the buzzer to the `GND` rail on your breadboard with a jumper. The cathode will be getting signal, so we'll deal with that later.
1. Next the SPDT switch needs to go into the breadboard, with each pin plugged into a different row. We chose row 5-7.
1. Connect row 5 to the `GND` rail, and leave the other rows for now.

The circuit should look something like this:

<!-- // TODO: IMAGE of breadboard with switch and buzzer in, grounded to exp dock -->


Now the circuit is ready, we need to set up the relay connections. We'll be using channel 0, with all switches on the relay set to `OFF`. We've included a diagram below to help out.

<!-- // TODO: IMAGE diagram of the relay switch numbering -->

1. To set up the relay, turn the screw on the `IN` terminal counterclockwise until the metal clamp inside is sitting a bit less than halfway in the bottom of the housing, not too much or the screw might pop out.
    * If you're unsure, close the terminal all the way by turning the screw clockwise until you can't anymore, then open it.
1. Grab a male-to-male jumper wire (we prefer red or orange, as this will be connected to power) and insert one end into the `IN` terminal
1. Turn the screw clockwise until the wire is tightly clamped.
1. Repeat for the `OUT` terminal.

Once the relay is set up, let's connect our circuit to it:

1. First, grab a jumper wire (preferably black) and connect one end to the `GND` pin on the Dock, and the other to the `GND` rail on the breadboard.
1. Connect the middle row of the SPDT switch (row 6) to GPIO0 on the dock using a M-M jumper.
1. Take the jumper connected to the `OUT` terminal and plug that into the row the cathode of your buzzer is plugged into. We have it plugged into row 1 column C.
1. Take the jumper connected to the `IN` terminal, and plug that into the `5V` pin on the Dock - this line will deliver power to the buzzer when the relay is turned on.
1. Grab a red or orange jumper and plug one end into the `3.3V` pin on the dock.
1. Plug the other end into remaining empty pin of the switch. We plugged it into row 7 - this will be the 'HIGH' position of the switch.

With that, we're all done!

Here's a picture of our completed circuit.

<!-- // TODO: IMAGE of completed circuit -->


### Writing the Code

The code we'll be using is a bit more complicated than you may think. We leverage the `relayExp` class from the `OmegaExpansion` Python Module to simplify the operation of the Relay Expansion. For this expriment, we don't just check the SPDT, and set the buzzer accordingly. Instead we read the relay switch first, make sure the state is different from the switch state, and then switch the Relay if needed. We'll cover why we do this below - but before we do, let's get to the action!

Create a file called `MAK07-relayCircuit.py` and paste the following code in it:


``` python
from onionGpio import OnionGpio
from OmegaExpansion import relayExp

SWITCH_PIN = 0
RELAY_ID = 7
RELAY_CHANNEL = 0
outputStrings = ['off', 'on']

def main():

    switch = OnionGpio(SWITCH_PIN)	# This works because we directly imported
									# the OnionGpio class from the module

	# Initializes switch GPIO, exits if the pin sends an error
    bSwitch = switch.setInputDirection()
    print ("Setting GPIO pin " + str(SWITCH_PIN) + " to input.")
    if (bSwitch is False):
        print ("GPIO set direction error.")
		return
	print ("Pin set.")

	# Initializes the relay, exits if the channel sends an error
    bRelay = relayExp.checkInit(RELAY_ID)
    print ("Checking Relay 0x2" + str(RELAY_ID) + " status.")
    if (bRelay is False):
        bInit = relayExp.driverInit(RELAY_ID)
        print ("Initializing Relay")
		if (bInit is False):
			print ("Relay initialization failure.")
			return
    print ("Relay initialized.")


    while (True):
        # getValue() returns a string with predictable formatting,
        # so we can convert it to int without trouble
        switchState = int(switch.getValue(), 10)
        relayState = relayExp.readChannel(RELAY_ID, RELAY_CHANNEL)

        if (switchState is not relayState):
            status = relayExp.setChannel(RELAY_ID, RELAY_CHANNEL, switchState)
            if (status is False):
                print ("Error switching relay, the script will now exit.")
                break
            else:
                print ("Switch flipped, turning relay " +
						outputStrings[switchState] + ".")

    relayExp.setChannel(RELAY_ID, RELAY_CHANNEL, 0)

if __name__ == "__main__":
    main()

```

### What to Expect

<!-- TODO: IMAGE or gif of project working -->

When the script is running, you'll see a ton of debug messages from the console. Now when you flick the switch to on or off, the buzzer should respond by turning on or off appropriately.

Infinite loop appears here as well, and as usual, exit the script with `Ctrl-C`.


### A Closer Look at the Code

From the PWM tutorials, we've touched on how to account for the limitations of hardware when writing software. In this tutorial we've put more of that into practice. One important thing introduced is the **Read - Modify - Write** cycle. One major part of the cycle is **checking status** of our components (the 'read' part of the cycle). Additionally, we **log** the status - this is a very good habit to get into for fast debugging.


#### Reading then Writing

Almost always, when we want to switch hardware states in software, the program has no innate knowledge of the state the hardware is in already. To make sure hardware functions properly, and that no false signals or badly timed signals are sent, the software should as a rule read the state of the hardware first before making changes.

This concept is known as Reading then Writing, and it actually applies to a lot of situations even in software. Multithreading, database updating, and filling and recieving forms all use this concept to try and ensure intended signals are sent, and no false signals get let through.


#### Checking Status

You'll notice that of all the code, only about 5 lines are directly dedicated to changing the state of the relay! The bulk of the code is actually all about checking the states and making decisions off of that information. The reason is simple: we want to make sure the commands we send to the hardware is absolutely correct, since hardware errors are difficult to recover from! Software can be written, started, and restarted fairly quickly; but if you burn out an LED, it's gone for good.

That's why we consider all the variables in this circuit by reading from the relay and the GPIO pins first and make sure to only change the state of the relay when it's safe, and it makes sense to do so. Of course when this circuit is properly wired, there's very little that can go wrong through bad signals, but it's always good practice to make sure.

#### Logging Errors and Successes

There's often a great deal of difference between what we *expect* our software to do versus what our software *actually* does. Logging is how we can sync up the expected behaviour with actual behaviour. Printing out values of variables, messages of success and failures, we bring what is normally hidden to light. This way, we can follow our code as it runs and make sure it's doing what we really want.


Next time, sky's the limit!
