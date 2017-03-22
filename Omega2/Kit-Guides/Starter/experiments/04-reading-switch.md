---
title: Reading a Switch
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---

## Reading a Switch {#starter-kit-reading-switch}

<!-- // intro to this experiment:
//  * so far, we've been using a program to control GPIOs, lets have some physical, user input controlling our software
//  * will be using a slide switch as input for our program, it will control whether an LED is on or off -->

So far, we've been using a program to control GPIOs. Let's try using physical user input to control our software!

We'll be using a **slide switch** as an input to control whether an LED should be turned on or off.

First, we'll make a simple circuit to figure out how the switch works. Then we'll connect the switch to your Omega, and control the LED using the Omega as the brain!

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

The first circuit we build will have the LED directly controlled by the switch to demonstrate how the switch works. The Omega will be used only as a power source and will not control the operation of the circuit.

<!-- // TODO: circuit diagram, see paper notes -->

#### What You'll Need

Prepare the following components from your kit:

* 1x Omega plugged into Expansion Dock
* 1x Breadboard
* 1x SPDT switch
* 1x 200Ω Resistor
* 4x Jumper wires (M-M)
* 1x Any LED color of your choice!

#### Hooking up the Components

<!-- // step by step guide of how to hook up the components
//  * how to connect one side of the switch to gnd and one to vcc
//  * connect the switchable part to the led -->

1. Plug in the switch vertically across three rows.
1. Connect the LED's anode to the switch's middle pin, and the cathode to an empty row.
1. Connect one end of a 200Ω resistor to the LED's cathode, and the other end into one of the "-" rails.
    * We'll call this the **ground** rail.
1. Connect the Expansion Dock's `GND` pin to the ground rail.
1. Connect the Expansion Dock's '3.3V' pin to the switch's top pin.

Your circuit should look like something like this:

<!-- // TODO: photo of example circuit -->

```{r child ='../../shared/wiring-precautions.md'}
```


### What to Expect


The slide switch physically controls the electricity flowing to the LED.

* When the switch is set to the pull-up fork, the LED receives power and lights up.
* When the switch is set to the pull-down fork, the LED does not receive power and turns off.

This is circuit is quite direct - it demonstrates that this switch works and how it does so. In fact, the only reason we have the Omega connected is to supply power to the LED. Let's move on to including our Omega and get some logic in this setup!


### Building the Experiment Circuit

Now let's try letting the Omega reading the signal the switch sends and use that to turn on the LED. We'll rewire the circuit to have the Omega connecting the switch and the LED. Once we finished wiring the circuit, we'll write a program that turns the LED on or off through reading the switch position.

<!-- // TODO: IMAGE CIRCUIT DIAGRAM of experiment -->

#### What You'll Need

* Use the same components as in the first circuit above.
* Throw in a few more jumper wires

#### Hooking up the Components

This circuit will keep the switch, but route the output of the switch to the Omega instead, and have it control the LED through a GPIO.

1. Remove the LED and resistor from the breadboard. Keep the switch and other wires in place.
1. Connect `GPIO0` on the Expansion Dock to the switch's middle pin.
1. Connect the switch's bottom pin to the ground rail.
1. Place the LED back on the breadboard across two empty rows, then do the following:
    1. Connect the anode to `GPIO1` using a jumper wire from the breadboard to the Expansion Dock.
    1. Connect the cathode to one end of the 200Ω resistor.
1. Connect the other end of that resistor to ground.

Your circuit should look like this:

<!-- // TODO: photo of experiment circuit-->


### Writing the Code

Let's make a new file called `STK04-readSwitch.py` to hold our code. This program will read in whatever state the switch is at, and then change the LED to match after some delay.

``` python
import onionGpio
import time

# specify sleep duration to be used in the program
sleepTime = 2

# set which GPIOs will be used
switchPin     = 0      # use GPIO0
ledPin        = 1      # use GPIO1


# instantiate GPIO objects
switch        = onionGpio.OnionGpio(switchPin)
led           = onionGpio.OnionGpio(ledPin)

# set the GPIO directions
switch.setInputDirection()               # switch pin is an input
led.setOutputDirection(0)                # led pin is an output

# infinite loop - runs main program code continuously
# 	periodically check the switch and turn the LED on or off
while 1:
	# read the switch value
    switchValue = switch.getValue()
	# turn the LED on/off depending on the switch
    led.setValue(switchValue)

	# make the program pause
    time.sleep(sleepTime)
```

Let's run the code:
```
python SKT04-readSwitch.py
```

Now try flipping the switch on and off. What happens?

### What to Expect

This circuit works the same way as the first circuit, albeit with a much slower reaction to the switch input. This demonstrates a physical input affecting something virtual (like our script); the virtual entity can interpret the signal then proceed to act on the physical world or interact with other virtual entities.


### A Closer Look at the Code

In this experiment, we continuously and repeatedly check the value of a sensor (our switch) then update the signal sent to the LED. This repeated checking is a classic way of reading a device and is called **polling**.

#### Polling

Polling is the process of repeatedly checking an input.

When flipping the switch, you may have noticed a delay of 2 seconds before the LED reacted. This delay was added so that the CPU has some time to rest between every check on the LED. Every time the program checks the switch, it puts a small load on the CPU - remember that it runs really fast, and doing many checks very often will waste CPU power that could be used for other system processes!

The delay length is set by the `time.sleep(sleepTime)` line. Try changing the `sleepTime` variable at the top to something shorter, like 0.5 or 0.1, and seeing what happens.

Polling is not without its issues:

* You can't do anything else in the program.
* You need to find a polling speed that balances the time delay and stress on the CPU.

If only there were a better way of doing this!

<!-- TODO: FUTURE: link to reading push button; edge detection is not ready yet -->
Next we'll learn how to [use a shift register](#starter-kit-using-shift-register).
