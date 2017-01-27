---
title: Reading a Switch
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---

## Reading a Switch

<!-- // intro to this experiment:
//  * so far, we've been using a program to control GPIOs, lets have some physical, user input controlling our software
//  * will be using a slide switch as input for our program, it will control whether an LED is on or off -->

So far, we've been using a program to control GPIOs. Let's try using physical user input to control our software!

We'll be using a **slide switch** as an input to control whether an LED should be turned on or off.


### GPIO Pins as Input

<!-- gpio input -->
```{r child = '../../shared/gpio-input.md'}
```


### Switches

<!-- switches -->
```{r child = '../../shared/switches.md'}
```


### Slide Switches

<!-- slide switches -->
```{r child = '../../shared/switches-slide-switch.md'}
```

### Building an Example Circuit

<!-- // diagram, general description of what the circuit does/the purpose
// circuit 1: switch controls turning an LED on and off to illustrate how the slide switch works
// spdt switch (one side is pull-up, other side is pull-down) connected to an led -->

We'll be building the following circuit.

// TODO: circuit diagram, see paper notes

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Expansion Dock
* Breadboard
* Jumper wires
* SPDT switch
* 1x 200Ω Resistor <!-- LED resistor -->
* Any LED color of your choice!

#### Hooking up the Components

<!-- // step by step guide of how to hook up the components
//  * how to connect one side of the switch to gnd and one to vcc
//  * connect the switchable part to the led -->
Before putting the circuit together, make sure the Omega2 is powered OFF for safety. 

1. Connect the Expansion Dock's 3.3V pin to one of the "+" columns on the breadboard.
    * We'll call this column **Vcc**.
1. Connect the Expansion Dock's GND pin to one of the "-" columns.
    * We'll call this column **ground**.
1. Connect the slide switch to the breadboard along any of the columns.
1. Connect the switch's top pin to Vcc.
    * We'll call this pin the **pull-up fork**.
1. Connect the switch's bottom pin to ground.
    * We'll call this pin the **pull-down fork**.
1. Connect the LED's anode to ground, and the cathode to one end of a (// TODO: resistor value) resistor.
1. Connect the other end of that resistor to the middle of the slide switch.

Your circuit should look like this.

<!-- // TODO: photo -->

If your circuit matches, go ahead and turn the Omega2 on!

#### What to Expect

<!-- // the switch controls if there is power flowing to the LED:
//  when the switch is set to the pull-up fork, the LED will be on
//  when the switch is set to the pull-down fork, the LED will be off

// this is a simple circuit but we wanted to illustrate how the switch works, let's move on to including our Omega in this circuit -->

The slide switch physically controls if electricity flows or does not flow to the LED. 

* When the switch is set to the pull-up fork, the LED receives power and lights up. 
* When the switch is set to the pull-down fork, the LED does not receive power and turns off.

This is a very simple circuit, but we wanted to illustrate how this switch works. Let's move on to including our Omega in this setup!

### Building the Experiment Circuit

<!-- // circuit 2: switch connected to GPIO, controls LED with software
// spdt switch (with pull-up and pull-down sides) connected to gpio input
// regular led circuit connected to gpio setup as output -->

In the next circuit, the Omega2 connects to the slide switch and LED. We'll write a program that turns the LED on or off depending on how you set the switch.

<!-- // TODO: photo -->

#### What You'll Need

* Use the same components as in the first circuit above.
* You may need a few more jumper wires handy.

#### Hooking up the Components

<!-- // step by step guide of how to hook up the components
//  jack the switch setup from the above section - adjust so taht it leads to a gpio
//  jack the LED setup from the previous articles -->
Turn the Omega off before changing your circuit. Then, do the following:

1. Remove the LED and its resistor from the breadboard.
1. Connect GPIO 0 on the Expansion Dock to the button pin using a jumper wire from the Expansion Dock to the breadboard.
1. Place the LED back on the breadboard by doing the following:
    1. Connect the cathode to GPIO 1 using a jumper wire from the breadboard to the Expansion Dock.
    1. Connect the anode to one end of the (// TODO: resistor value) resistor.    
1. Connect the other end of that resistor to ground.

Your circuit should look like this:

<!-- // TODO: photo -->

If your circuit matches, power your Omega back on!

### Writing the Code

Let's make a new file called `readSwitch.py` to hold our code:

<!-- // code should poll a gpio, based on the input value, set a different gpio to output the read value
// implementation:
//  * while loop for polling
//  * if it makes sense, write functions to read the gpio, and then set the other gpio (want to teach them good practices right off the bat)
//  * make the delay at the end of the loop pretty long 2-5 seconds -->

``` python
import onionGpio
import time

# initialize GPIOs
switchPin     = onionGpio.OnionGpio(0)      # use GPIO0
ledPin        = onionGpio.OnionGpio(1)      # use GPIO1

# set the GPIO directions
switchPin.setInputDirection()               # switch pin is an input
ledPin.setOutputDirection(0)                # led pin is an output

# periodically check the switch and turn the LED on or off
while 1:
	switchValue = switchPin.getValue()     # read the switch's value
    ledPin.setValue(switchValue)           # turn the LED on/off depending on the switch

	time.sleep(2)                          # sleep for 2 seconds
```

Let's run the code:
```
python readSwitch.py
```

Now try flipping the switch on and off. What happens?

#### What to Expect

<!-- // the switch controls whether the LED is on or off. yes the same thing was achieved with the far simpler circuit, but is meant to illustrate how a physical input can control something virtual -->

This circuit does pretty much the same thing as the first circuit, albeit with a slower reaction to the switch input. This is meant as a simple example of a physical input affecting something virtual (eg. a program), which can in turn affect the physical world or interact with other virtual entities.

#### A Closer Look at the Code

<!-- // small overview of anything new we did -->
##### Polling

<!-- // explain polling is the process of repeatedly checking an input
//  * a delay was added since we don't want to burn up the cpu constantly checking the same thing - remember the CPU runs incredibly fast

// talk about how sometimes it takes a while for the led to react:
//  * this is due to the long delay, have them try shortening the delay
//  * introduce some of the issues related to having polling:
//    * can't do anything else in the program
//    * can potentially have a long delay between the physical action and the software reacting
//    * if only there was a better way! -->

Polling is the process of repeatedly checking an input.

When flipping the switch, you may have noticed a delay of 2 seconds before the LED reacted. This delay was added so that the CPU has some time to rest between every check on the LED. We don't want to burn up the CPU by constantly checking the same thing - remember that it runs incredibly fast!

The delay length is set by the `time.sleep(2)` line. Try changing the number to something shorter, like 0.5 or 0.1, and seeing what happens.

Some of the issues during polling are as follows:

* You can't do anything else in the program.
* You need to find a polling speed that balances the time delay and stress on the CPU.

If only there were a better way of doing this!