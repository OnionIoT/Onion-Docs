---
title: Blinking an LED
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---

## Blinking an LED

In our very first experiment, we're going to blink an LED on and off. This is the hardware development equivalent of the 'Hello World' program. This first experiment will start small but it will be a solid foundation for the rest of the experiments.

Remember, when inventing and building new things, try to break the work down into bite sized chunks, that way you'll see progress much sooner and it will motivate you to keep going!


<!-- ### GPIO Pins as Outputs -->
```{r child = '../../shared/gpio-output.md'}
```

<!-- LEDs -->
```{r child = '../../shared/led.md'}
```

### Building the Circuit

Before we start building our experiment, let's first go over some of the building blocks when it comes to experimenting with electronics.


<!-- Jumper wires -->
```{r child = '../../shared/jumper-wires.md'}
```

<!-- Breadboard -->
```{r child = '../../shared/breadboard.md'}
```

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Expansion Dock
* Breadboard
* Jumper wires
* Resistors
    * 1x (// TODO: LED resistor)Ω <!-- LED resistor -->
* Any LED color of your choice!

#### Hooking up the Components

OK here we go, let's put together our circuit! We're going to be connecting an LED's anode to a GPIO on the Omega2, and cathode to Ground through a current limiting resistor.

// TODO: FRITZING: fritzing circuit diagram of the experiment

1. Plug in the LED into the breadboard, make sure you plug the anode and cathode into different rows and that you know which is plugged where.
2. Let's choose `GPIO0` on the Omega2 to drive our LED, so let's run a jumper wire to the row of the LED's anode.
3. Now connect one end of a (// TODO: figure out resistance)kΩ resistor to the the cathode row, and the other end to an empty row.
4. The final step is connecting a jumper wire to a Ground pin on the Omega2.

> A note on components with and without **polarity**:

> You'll notice that we were careful to make sure which end of the LED we connected to incoming current and which we connected to ground. This is because LEDs are polarized, so they will only when current is flowing in the correct direction, that is, when they're plugged in the correct way.

> With the resistor, either way will work since resistors are symmetric components, meaning they don't care which way current flows through them, they'll work either way.


The circuit diagram for our first experiment looks like this:
// TODO: CIRCUIT DIAGRAM: circuit showing this experiment


### Writing the Code

Now we get to write the code that will make our circuit actually do something! That something will be blinking our LED!

// TODO: rework this when

Let's make a new file `blink.py` to hold our code:
``` python
import onionGpio
import time

gpio0 	= onionGpio.OnionGpio(0)	# initialize a GPIO object
gpio0.setOutputDirection(0)		# set to output direction with zero being the default value

ledValue 	= 1

while 1:
	gpio0.setValue(ledValue)	# program the GPIO

	# flip the value variable
	if ledValue == 1:
		ledValue = 0
	else:
		ledValue = 1

	time.sleep(0.5)		# sleep for half a second
```

Let's run the code:
```
python blink.py
```

#### What to Expect

Your LED should be blinking; it should turn on for half a second, and then turn off for half a second, repeating until you exit the program.

// TODO: GIF: Showing this experiment with the LED blinking

> To exit a program like this one: press `Ctrl+C` (`Cmd+C` for Mac users)

#### A Closer Look at the Code

While this is a small program, there are quite a few things going on, let's take a closer look.

##### Importing a Module

The very first line in the code imports a Python source code module. In this case, the module was made by the Onion team for controlling the Omega's GPIOs. The module contains a class that implements functions for everything you can do with a GPIO on an Omega.

// TODO: add a note about the time module

##### Object Oriented Programming - Instantiating an Object

Then, the very next thing we do is **instatiate** an object of the `OnionGpio` class from the `onionGpio` module we just included above. Make sure to note that we passed an argument to the **constructor** of the `OnionGpio` class, this argument defines which of the Omega's GPIOs we are going to be using, `GPIO0` in this case.

We also take care to assign the instantiated object to a variable so that we can access it to actually interact with the GPIO pin.


##### While Loop

Loops are incredibly common in literally every type and form of programming. The type of loop we're using here is called a *while* loop, since it will execute the code contained within it's body **while** the loop condition holds true. In this case, the loop condition is `1` which will always evaluate to true, so we have in effect made an **infinite loop**.

While we're talking about the loop, let's go over what is going on in the loop body code. We had previously set the `ledValue` variable to `1` so the first time through the loop, the GPIO will be set to a Logical High, turning our LED on. In the following `if-else` statement, since the current value of the `ledValue` variable is `1`, the code in the body of the `if` statement will be executed, and it will be changed to `0`. The program will then sleep for half a second, meaning it will stay at that line and nothing will be executed until the specified time is over.

So remember, we've changed the `ledValue` variable to be `0` now, so in the next iteration of the loop, the GPIO will be set to a Logical Low, turning the LED off. Since the value of `ledValue` is `0`, the code in the body of the `else` statement will be executed and the variable will be set to `1`. After this the program will sleep for another half second.

If you're wondering why we make the program sleep for half a second during each loop iteration, it's because computers execute program code **really** fast. Try increasing, decreasing, or getting rid of the sleep instruction all-together and rerunning the program. See what happens with our LED.
