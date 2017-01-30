---
title: Reading a Push Button
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 5
---

## Reading a Push Button

<!-- // intro to push button
// building on what we did with the slide switch, but let's use the button as a trigger for an action - as opposed to constantly reading the state of the switch

// we will be building an led controlled by a push button, when the button is pressed, the led will turn on, and remain on for 10 seconds, then turn off -->

For this experiment, we'll build on what we did with the slide switch. This time, let's use the button as the trigger instead of constantly polling the switch! 

We'll be making a circuit with an LED controlled by a **push button**. When the button is pressed, the LED will turn on for 10 seconds, then turn off.

### Push Buttons

<!-- // put in its own markdown file -->

<!-- // explanation of push buttons: how they are momentary switches and only close the circuit while the button is depressed
// explanation of the pins, and what connection happens when the button is pressed -->
```{r child = '../../shared/switches-push-button.md'}
```

<!-- debouncing switches -->
```{r child = '../../shared/switches-debouncing.md'}
```

### Building an Example Circuit

<!-- // circuit 1: button without debouncing circuit controls an LED directly -->

First we'll build a circuit with a button to control an LED directly. See the diagram below:

<!-- // TODO: diagram -->

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Expansion Dock
* Breadboard
* Jumper wires
* Tactile button
* Resistors
    * 1x 200Ω <!-- LED resistor -->
* Any LED color of your choice!

#### Hooking up the Components

<!-- // explain how to connect a push-button switch to an led -->

Before putting the circuit together, make sure the Omega2 is powered OFF for safety. 

1. Connect the Expansion Dock's 3.3V pin to one of the "+" columns on the breadboard.
    * We'll call this column **Vcc**.
1. Connect the Expansion Dock's GND pin to one of the "-" columns.
    * We'll call this column **ground**.
1. Connect the push button to the breadboard as shown below:
    * ![push-button-breadboard](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/push-button-breadboard.jpg)
    <!-- // TODO: photo showing how the legs are oriented across the breadboard-->
1. Connect one side of the switch to Vcc.
1. Connect the LED's cathode to the other side of the button, and the anode to one end of the 200Ω resistor.
1. Connect the other end of that resistor to ground.

Your circuit should look like this.

![debouncer-circuit-setup-01](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/debouncer-circuit-setup-01.jpg)

<!-- // TODO: photo -->

If your circuit matches, go ahead and turn the Omega2 on!

#### What to Expect

When you push and hold the button, the LED should turn off. When you release the button, the LED should turn on.

<!-- // push and hold the button, the led is on
// release it and the led turns off
// the drawback of this circuit is that the switch just controls if there is current flowing to the LED or not
// adding -->
<!-- * // ^ all logic swapped for inverting debouncer -->
<!-- * // TODO: regardless of whether the debouncer is inverting or not, there is so much resistance on the way to the LED that it will barely light up (microamps) -->

### Building the Real Circuit

<!-- // circuit 2: button with debouncing circuit connected to GPIO,  LED connected to GPIO -->

Now we'll build a circuit with a button and inverting debouncer circuit connected to a GPIO, and an LED connected to another GPIO that is driven by software.

#### What You'll Need

You'll need to pull a few more components from your Kit. Prepare the following:

* Resistors
    * 1x 50kΩ
    * 1x 5kΩ <!-- debounce resistors -->
* 1x 100nF capacitor

* Use the same components as in the first circuit above.
* You may need a few more jumper wires handy.

#### Hooking Up the Components

Turn the Omega off before changing your circuit. Then, do the following:

1. Connect one end of the switch to the 50kΩ resistor, and the other end of that resistor to Vcc.
1. Connect the switch's bottom pin to ground.
1. Connect one end of the 5kΩ resistor to the same point where the switch and 50kΩ resistor are connected, and the other end to an empty row on the breadboard.
    * We'll call this the **button pin**.
1. Connect one end of the capacitor to ground, and the other to the button pin.
1. Connect `GPIO0` on the Expansion Dock to the button pin using a jumper wire from the Expansion Dock to the breadboard.
1. Place the LED back on the breadboard by doing the following:
    1. Connect the cathode to GPIO 1 using a jumper wire from the breadboard to the Expansion Dock.
    1. Connect the anode to one end of the 200Ω resistor.    
1. Connect the other end of that resistor to ground.

Your circuit should look like this:

![debouncer-circuit-setup-02](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/debouncer-circuit-setup-02.jpg)

<!-- // TODO: photo -->

If your circuit matches, power your Omega back on!

### Writing the Code

Let's go about writing our code, but first let's cover an important topic first.

#### Edge Detection

<!-- edge detection -->
```{r child = '../../shared/gpio-edge-detection.md'}
```

<!-- // edge detection is when the system waits for an "edge" in the signal to perform an action. an edge being a place where the signal goes from high to low (falling edge), or low to high (rising edge) (have an illustration)

// in terms of the action, we'll be defining a function to be executed when the trigger, in this case the edge in the signal is detected
// relate this back to interrupts and interrupt service routines
 -->

#### The Code Itself

<!-- // write a program that uses edge detection to turn an led on, sleep for 10 seconds and then turn it off
note: the mechanism for edge detection hasn't been ironed out yet -->

Let's create a file called `debounceSwitch.py` to hold our code:

<!-- LAZAR: work in progress -->

``` python
import onionGpio
import time

## define constants
ledOnDuration = 10
pollingInterval = 0.1

## define GPIO functions
## edge detection
def edgeDetection(gpio):
    // TODO: still being worked on
    return pinValue

## reading a button (using edge detection here)
def readButton(gpio):
    pinValue = edgeDetection(gpio)          # using edge detection, but can use other methods if desired
    pinValue = not pinValue                 # inverting debouncer, so ON is LOW and OFF is HIGH
    return pinvalue

## initialize GPIOs
switchPin     = onionGpio.OnionGpio(0)      # use GPIO0
ledPin        = onionGpio.OnionGpio(1)      # use GPIO1

## set the GPIO directions
switchPin.setInputDirection()               # switch pin is an input
ledPin.setOutputDirection(0)                # led pin is an output

## trigger the switch via edge detection
// TODO: may not be in a while loop
while 1:
	if edgeDetection:
        ledPin.setValue(1)                     # turn the LED on
        time.sleep(ledOnDuration)              # sleep
        ledPin.setValue(0)                     # turn the LED off
    else:
        time.sleep(pollingInterval)            # sleep until we poll again
```

#### What to Expect

<!-- // hit the button, the light turns on, stays on for 10 seconds, turns off 
// ^ swapped for inverting debouncer -->

Let's run the code:
```
python debounceSwitch.py
```

Now try pushing the button on and off. What happens?

#### A Closer Look at the Code

<!-- // explanation of the edge detection code -->
