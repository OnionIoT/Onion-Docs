---
title: Controlling Other Circuits
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 7
---
## Isolated Control with the Relay Expansion {#isolated-control-with-the-relay-expansion}

In this tutorial, we'll use a switch with the Omega Relay expansion to turn a buzzer on or off. Along the way, we'll be looking into why relays are useful, and go into more detail regarding pitfalls when interacting with hardware.

>**Note**: this expansion allows you to switch power sources of a *much* higher voltage than the board - and possibly your body - is able to handle. We urge you to read up the specifications of the [Relay Expansion](#relay-expansion) in our hardware overview documentation to understand the capabilities and limits of the Relay Expansion. We cannot accept responsibility for damages you may incur, and we recommend you use this expansion only if you are comfortable with whatever you may be switching.


### Circuit Isolation

<!-- // explain that the omega's relays are completely isolated from the circuit that is connected to the terminals, it merely acts as a switch

// this is useful since it allows the Omega to control other, larger, more powerful circuits
//  expand along those lines, maybe throw in the max specs of the relays, hint that you can control house-hold appliances -->

Omega boards and components are not designed to handle much more than 5V circuit and 12V supply. Attempting to directly control 120V appliances like lights, heaters, garage doors will almost certainly fry your Omega. So how can you turn on your lights?

Enter the **relay**! A relay is a mechanical switch that is triggered electronically. This physically separates the circuit that triggers the switch and the circuit that the switch actually switches. The relay expansion is designed to isolate the Omega and the dock from high power circuits while allowing it to be controlled by the Omega.


### Building the Circuit

Our goal here is to connect a buzzer to the relay expansion and a power supply, and then connect a switch to the Omega's expansion headers. Once it's set up, we'll use the code to turn the buzzer on and off.

The switch used here is an SPDT switch - Single Pole, Dual Throw. Single pole means there's a single power source being switched, dual throw means the power is always connected to one output or the other. The middle pin is the power input, and the two pins on the side are the outputs. Here we'll just use a single output, leaving the other as open circuit.

>In this tutorial, we'll be using the power supplied by our Dock due to easy access. Feel free to try using different power supply methods, but take note you may need voltage dropping resistors for higher powered supplies to avoid burning out the buzzer.

#### What You'll Need

* 1x Relay Expansion
* 1x Expansion/Power/Arduino Dock
* 1x Buzzer
* 1x SPDT (or three-way) switch
* 1x Breadboard
* Jumper wires
	* 5x M-M


#### Hooking up the Components

<!-- // detailed explanation of connecting wires to the screw terminals

// wiring up the buzzer so that the connection is interrupted by the relay -->

1. First we'll have to find a place on the breadboard to place the buzzer, we chose row 1 and mounted the buzzer across the middle channel
	* Taking note where the cathode (+) and where the anode (-) is, we'll have to make sure the right wires go in the right terminal later
1. Next the switch needs to go into the breadboard, with each pin plugged into a different row. We chose row 5-8.
// TODO: IMAGE of breadboard with switch and buzzer in
1. Now to set up the relay connections. We'll be using channel 0, with all switches on the relay set to `OFF`. We've included a diagram below to help out.
	* Turn the screw on the `IN` terminal counterclockwise until the metal clamp inside is sitting a bit less than halfway in the bottom of the housing, not too much or the screw might pop out.
	* If you're unsure, close the terminal all the way by turning the screw clockwise until you can't anymore, then open it.
	* Grab a male-to-male jumper wire (we prefer red or orange, as this will be connected to power) and insert it into the terminal
	* Turn the screw clockwise until the wire is tightly clamped.
	* Repeat for the `OUT` terminal.
1. Take the jumper connected to the `IN` terminal, and plug that into the `5V` pin on the Dock.
	* Or if you have a power supply, the positive terminal of it.
1. Take the jumper connected to the `OUT` terminal and plug that into the row the positive terminal of your buzzer is plugged into. We used the socket in row 1 column C.
1. Grab a jumper wire (preferably black) and connect one end to the `GND` pin on the Dock, and the other to the same row as the negative terminal of your buzzer. Row 1, column H for us.
// TODO: IMAGE diagram of the buzzer+relay configuration
1. Now the buzzer can be turned off and on via commands to the Relay Expansion. Next we'll connect the switch, the final result should look something like this:
// TODO: IMAGE diagram of the switch configuration
1. Grab a red or orange jumper and plug one end into the `3.3V` pin on the dock.
1. Plug the other end into the same row as the middle pin of the switch. We plugged it into row 6
1. Next connect one of the two free pins on the switch to pin `0` on the dock using the last jumper wire.

We're all done!

Here's a picture of our completed circuit.
// TODO: IMAGE of completed circuit


#### Writing the Code

As usual, before running the code, make sure you have all the appropriate libraries installed. Commands as follows:

```
opkg update
opkg install python-light
opkg install pyRelayExp pyOnionGpio
```

//TODO: remove all opkg commands

The code we'll be running:

```
from onionGpio import OnionGpio
from OmegaExpansion import relayExp

SWITCH_PIN = 0
RELAY_ID = 7
RELAY_CHANNEL = 0
outputStrings = ['off', 'on']

def main():

    switch = OnionGpio(SWITCH_PIN)	# This works because we directly imported the
									# OnionGpio class from the module

    status = switch.setInputDirection()
    if (status is False):
        print ("GPIO set direction error.")

    relayStatus = relayExp.checkInit(RELAY_ID)
    print ("Checking Relay 0x2" + str(RELAY_ID) + " status.")

    if (relayStatus is False):
        relayExp.driverInit(RELAY_ID)
        print ("Initializing Relay")

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
                print ("Switch flipped, turning relay " + outputStrings[switchState] + ".")

    relayExp.setChannel(RELAY_ID, RELAY_CHANNEL, 0)

if __name__ == "__main__":
    main()

```

#### What to Expect

When the script is running, you'll see a ton of debug messages from the console. Now when you flick the switch to on or off, the buzzer should respond by turning on or off appropriately.

Infinite loop appears here as well, and as usual, exit the script with `ctrl`+`c`.


### A Closer Look at the Code

From the PWM tutorials, we've touched on how to account for the limitations of hardware when writing software. In this tutorial we've put more of that into practice.

Main topics covered:
* Read - Modify - Write
* Checking Status

#### Reading then Writing

Almost always, when we want to switch hardware states in software, the program has no innate knowledge of the state the hardware is in already. To make sure hardware functions properly, and that no false signals or badly timed signals are sent, the software should as a rule read the state of the hardware first before making changes.

This concept is known as Reading then Writing, and it actually applies to a lot of situations even in software. Multithreading, database updating, and filling and recieving forms all use this concept to try and ensure intended signals are sent, and no false signals get let through.


#### Checking Status

You'll notice that of all the code, only about 5 lines are directly dedicated to changing the state of the relay! The bulk of the code is actually all about checking the states and making decisions off of that information. The reason is simple: we want to make sure the commands we send to the hardware is absolutely correct, since hardware errors are difficult to recover from! Software can be written, started, and restarted fairly quickly; but if you burn out an LED, it's gone for good.

That's why we consider all the variables in this circuit by reading from the relay and the GPIO pins first and make sure to only change the state of the relay when it's safe, and it makes sense to do so. Of course when this circuit is properly wired, there's very little that can go wrong through bad signals, but it's always good practice to make sure.
