---
title: Blinking an LED
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---

## Blinking an LED {#starter-kit-blinking-led}

In our very first experiment, we're going to blink an LED on and off. This is the hardware development equivalent of the 'Hello World' program. This first experiment will start small but it will be a solid foundation for the rest of the experiments.

Remember, when inventing and building new things, try to break the work down into bite sized chunks, that way you'll see progress much sooner and it will motivate you to keep going!


<!-- ### GPIO Pins as Outputs -->
```{r child = '../../shared/gpio-output.md'}
```

<!-- LEDs -->
```{r child = '../../shared/led.md'}
```

### How to Build Circuits

Before we start building our experiment, let's first go over some of the building blocks when it comes to experimenting with electronics.


<!-- Jumper wires -->
```{r child = '../../shared/jumper-wires.md'}
```

<!-- Breadboard -->
```{r child = '../../shared/breadboard.md'}
```

### Building the Circuit {#starter-kit-blinking-led-building-the-circuit}

<!-- // DONE: fill this with something like 'Ok, now that we know the general tools we'll be using, let's build our very first circuit!' -->

Now that we've gotten familiar with the tools we'll be using, let's build our very first circuit!

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Expansion Dock
* Breadboard
* M-M Jumper Wires
* 1x 200Ω Resistor
* Any LED color of your choice!

#### Hooking up the Components {#starter-kit-blinking-led-hooking-up-the-components}

OK here we go, let's put together our circuit! We're going to be connecting an LED's anode to a GPIO on the Omega2, and cathode to Ground through a current limiting resistor.

<!-- // TODO: FRITZING: fritzing circuit diagram of the experiment -->

```{r child = '../../shared/wiring-led.md'}
```

Your circuit should now look like this:

<!-- // TODO: image of circuit -->

<!-- Breadboard -->
```{r child = '../../shared/wiring-precautions.md'}
```

> A note on components with and without **polarity**:
>
> You'll notice that we were careful to make sure which end of the LED we connected to incoming current and which we connected to ground. This is because LEDs are **polarized**, so they will only when current is flowing in the correct direction, that is, when they're plugged in the correct way.
>
> With the resistor, either way will work since resistors are symmetric components, meaning they don't care which way current flows through them, they'll work either way.


The circuit diagram for our first experiment looks like this:
<!-- // TODO: CIRCUIT DIAGRAM: circuit showing this experiment -->


### Writing the Code

Now we get to write the code that will make our circuit actually do something! That something will be blinking our LED!

We'll be writing code in the **Python** programming language. It is designed to be accessible to beginners while also being powerful enough to run major software programs, web services, research tools, and more.

Let's make a new file called `STK01-blink.py` to hold our code:

``` python
import onionGpio
import time

sleepTime = 0.5                   # sleep for half a second

gpio0 = onionGpio.OnionGpio(0)    # initialize a GPIO object
gpio0.setOutputDirection(0)       # set to output direction with zero being the default value

ledValue     = 1

while 1:
    gpio0.setValue(ledValue)      # set the GPIO's value
    
    # flip the value variable
    if ledValue == 1:
        ledValue = 0
    else:
        ledValue = 1

    time.sleep(sleepTime)         # sleep 
```

To run our Python program, enter the following in the Omega's command line:

```
python STK01-blink.py
```

We'll be running our programs in this way in the following experiments.

### What to Expect

Your LED should be blinking. It should turn on for half a second, and then turn off for half a second, repeating until you exit the program by pressing `Ctrl-C`.

<!-- // TODO: GIF: Showing this experiment with the LED blinking -->

> To exit a program like this one: press `Ctrl-C` (`Cmd-C` for Mac users)

### A Closer Look at the Code

This is a small program, but there are quite a few things going on. Let's take a closer look.

#### Importing a Module

The first line in the code imports a Python source code module. In this case, the module was made by the Onion team for controlling the Omega's GPIOs. The module contains a class that implements functions for everything you can do with a GPIO on an Omega.

#### Object Oriented Programming - Instantiating an Object

Before we continue, we'd like to mention that Python is an **Object Oriented** programming language. This means we can make use of classes and objects.

<!-- Classes and Objects -->
```{r child = '../../shared/classes-and-objects.md'}
```

We'll explain these concepts in better detail as we go along in the following experiments.

Now back to our program! After we import the `onionGpio` module, we instantiate an `OnionGpio` object in this line:

``` python
gpio0 = onionGpio.OnionGpio(0)
```

Here we passed the number `0` as an argument to the **constructor** of the `OnionGpio` class. The constructor is a function that runs when an object is instantiated and can be used to supply data to the object that it could need for configuration. In our case, the `OnionGpio` constructor tells the object which of the Omega's GPIOs the object will use, in this case `GPIO0`. We assign this instantiated object to a variable `gpio0` so that we can use it later in the program to interact with the GPIO pin.

#### The `time` Module

This module is used for anything involving measuring time, but also contains the very important `sleep()` function. This function, pauses execution of the Python script for the specified time in **seconds**; similar functions in other languages may interpret the number as milliseconds. It can accept decimal numbers too!

#### While Loop

Loops are structures used to control program flow by repeating certain sections of the code multiple times. They are a very common and important building block in programming.

Here we're using a **while** loop: the code inside the loop will run over and over *while* a given condition holds true. In this case, the loop condition is `1`, which is equivalent to `True` in these situations, so we have in effect made an **infinite loop**.

Before program enters the loop, we set the `ledValue` variable to `1`. Inside the while loop, we assign the value of `ledValue` (1) to our LED GPIO which turns it on. Then we reverse the value using the `if-else` statement which looks at the latest value of `ledValue`: if it is `1`, it will be changed to `0` and vice versa. The program will then pause the program execution for half a second, at the `time.sleep(sleepTime)` statement. The program then returns back to the beginning of the loop and assigns the new value of `ledValue` to the GPIO, and repeats the steps we described in this paragraph until you exit the program (`Ctrl-C`).

If you're wondering why we make the program sleep for half a second every loop cycle, it's because computers execute program code **really** fast. Try increasing, decreasing, or getting rid of the sleep instruction all-together and running the program again. See what happens with the LED.
