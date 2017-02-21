---
title: Reading a Switch
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---

## Reading a Switch {#starter-kit-04-reading-switch}

<!-- // intro to this experiment:
//  * so far, we've been using a program to control GPIOs, lets have some physical, user input controlling our software
//  * will be using a slide switch as input for our program, it will control whether an LED is on or off -->

So far, we've been using a program to control GPIOs. Let's try using physical user input to control our software!

We'll be using a **slide switch** as an input to control whether an LED should be turned on or off.

First, we'll make a simple circuit to figure out how the switch works, then we'll use the switch to control the LED through the Omega!

// TODO: append a sentence along the lines of: First we'll make a simple circuit to illustrate how the switch works, and then we'll move on to building a circuit where the switch is connected to your Omega.


<!-- gpio input -->
```{r child = '../../shared/gpio-input.md'}
```


<!-- switches -->
```{r child = '../../shared/switches.md'}
```

<!-- slide switches -->
```{r child = '../../shared/switches-slide-switch.md'}
```

### Building an Example Circuit

<!-- // diagram, general description of what the circuit does/the purpose
// circuit 1: switch controls turning an LED on and off to illustrate how the slide switch works
// spdt switch (one side is pull-up, other side is pull-down) connected to an led -->

// TODO: this is an awful intro. mention that this is an example circuit that we're making to show off how switches work. briefly describe what we'll be building

The first circuit we build will have the LED directly controlled by the switch to demonstrate how the switch works. The Omega will be used as a source of voltage only, and won't really do anything to affect the operation of the circuit.

<!-- // TODO: circuit diagram, see paper notes -->

#### What You'll Need

Prepare the following components from your kit:

* 1x Omega plugged into Expansion Dock
* 1x Breadboard
* 1x SPDT switch
* 1x 200Ω Resistor
* 4x Jumper wires (Male-to-Male)
* 1x Any LED color of your choice!

#### Hooking up the Components

<!-- // step by step guide of how to hook up the components
//  * how to connect one side of the switch to gnd and one to vcc
//  * connect the switchable part to the led -->

1. Connect the switch's top pin to one of the "+" columns on the breadboard.
    * We'll call this column **`Vcc` rail**.
    * We'll call this pin the **pull-up fork**.
1. Connect the switch's bottom pin to one of the "-" columns.
    * We'll call this column **`GND` rail**.
    * We'll call this pin the **pull-down fork**.
1. Connect the slide switch to the breadboard along any of the columns.
1. Connect the LED's anode to `GND`
1. Connect the LED's cathode to one end of a 200Ω resistor through the breadboard.
1. Connect the other end of the resistor to the middle of the slide switch.
1. Connect the Expansion Dock's `GND` pin to the `GND` rail.
1. Connect the Expansion Dock's '3.3V' pin to the `Vcc` rail.

Your circuit should look like something like this:

<!-- // TODO: photo -->

```{r child ='../../shared/wiring-precautions.md'}
```


### What to Expect

<!-- // the switch controls if there is power flowing to the LED:
//  when the switch is set to the pull-up fork, the LED will be on
//  when the switch is set to the pull-down fork, the LED will be off

// this is a simple circuit but we wanted to illustrate how the switch works, let's move on to including our Omega in this circuit -->

The slide switch physically controls the electricity flowing to the LED.

* When the switch is set to the pull-up fork, the LED receives power and lights up.
* When the switch is set to the pull-down fork, the LED does not receive power and turns off.

This is circuit is quite direct - it demonstrates that this switch works and how it does so. In fact, the only reason we have the Omega connected is to supply power to the LED. Let's move on to including our Omega and get some logic in this setup!


### Building the Experiment Circuit

<!-- // circuit 2: switch connected to GPIO, controls LED with software
// spdt switch (with pull-up and pull-down sides) connected to gpio input
// regular led circuit connected to gpio setup as output -->

Now let's try letting the Omega reading the signal the switch sends and use that to turn on the LED. We'll rewire the circuit to have the Omega connecting the switch and the LED. Once we finished wiring the circuit, we'll write a program that turns the LED on or off through reading the switch position.

<!-- // TODO: photo -->

#### What You'll Need

* Use the same components as in the first circuit above.
* You may need a few more jumper wires

#### Hooking up the Components

<!-- // step by step guide of how to hook up the components
//  jack the switch setup from the above section - adjust so taht it leads to a gpio
//  jack the LED setup from the previous articles -->
If you had the

1. Remove the LED and its resistor from the breadboard.
1. Connect GPIO 0 on the Expansion Dock to the button pin using a jumper wire from the Expansion Dock to the breadboard.
1. Place the LED back on the breadboard by doing the following:
    1. Connect the cathode to GPIO 1 using a jumper wire from the breadboard to the Expansion Dock.
    1. Connect the anode to one end of the (// TODO: resistor value) resistor.    
1. Connect the other end of that resistor to ground.

Your circuit should look like this:

<!-- // TODO: IMAGE photo -->


### Writing the Code

Let's make a new file called `STK04-readSwitch.py` to hold our code:

<!-- // code should poll a gpio, based on the input value, set a different gpio to output the read value
// implementation:
//  * while loop for polling
//  * if it makes sense, write functions to read the gpio, and then set the other gpio (want to teach them good practices right off the bat)
//  * make the delay at the end of the loop pretty long 2-5 seconds -->

``` python
import onionGpio
import time

# TODO: Lazar: point out this addition
# set which GPIOs will be used
switchPin     = 0      # use GPIO0
ledPin        = 1      # use GPIO1


# instantiate GPIO objects
switch        = onionGpio.OnionGpio(switchPin)
led           = onionGpio.OnionGpio(ledPin)

# set the GPIO directions
switch.setInputDirection()               # switch pin is an input
led.setOutputDirection(0)                # led pin is an output

# periodically check the switch and turn the LED on or off
while 1:
	switchValue = switch.getValue()     # read the switch's value
	led.setValue(switchValue)           # turn the LED on/off depending on the switch

	time.sleep(2)                          # sleep for 2 seconds
```

Let's run the code:
```
python SKT04-readSwitch.py
```

Now try flipping the switch on and off. What happens?

### What to Expect

<!-- // the switch controls whether the LED is on or off. yes the same thing was achieved with the far simpler circuit, but is meant to illustrate how a physical input can control something virtual -->

This circuit does pretty much the same thing as the first circuit, albeit with a much slower reaction to the switch input. This demostrates a physical input affecting something virtual (like our script); the virtual entity can interpret the signal then proceed to act on the physical world or interact with other virtual entities.

### A Closer Look at the Code

In this experiment, we continuously read a sensor (our switch) to update the LED as soon as we detect the corresponding change from the sensor. This is the most classic way of digitally controlling a device - most commonly known as **polling**.

<!-- // small overview of anything new we did -->
#### Polling

<!-- // explain polling is the process of repeatedly checking an input
//  * a delay was added since we don't want to burn up the cpu constantly checking the same thing - remember the CPU runs incredibly fast

// talk about how sometimes it takes a while for the led to react:
//  * this is due to the long delay, have them try shortening the delay
//  * introduce some of the issues related to having polling:
//    * can't do anything else in the program
//    * can potentially have a long delay between the physical action and the software reacting
//    * if only there was a better way! -->

Polling is the process of repeatedly checking an input.

When flipping the switch, you may have noticed a delay of 2 seconds before the LED reacted. This delay was added so that the CPU has some time to rest between every check on the LED. We will needlessly tax the CPU by constantly checking the same thing - remember that it runs really fast!

The delay length is set by the `time.sleep(2)` line. Try changing the number to something shorter, like 0.5 or 0.1, and seeing what happens.

Polling is not without its issues:

* You can't do anything else in the program.
* You need to find a polling speed that balances the time delay and stress on the CPU.

If only there were a better way of doing this!

<!-- TODO: lead-in for 05 -->
