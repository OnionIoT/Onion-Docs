---
title: Controlling Many LEDs
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---

## Controlling Many LEDs

"We've blinked one LED sure, but what about a second LED?"

In this experiment, we're going to use what we learned in the first experiment and wire up a bunch of LEDs. Then we're gonna make some visual effects.

### Building the Circuit

// same as the first experiment, just repeated a bunch of times

Similar to the previously experiment, we need our breadboard and jumper wires. However, now we will use 6 LEDS along with 6 current limiting resistors. We will makes the LEDs turn on one-by-one going left to right, and then turn them off one-by-one again going left to right.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 6x 200Ω Resistor
* 6x LED color of your choice!

#### Hooking up the Components

// look to the multiple leds article in the starter kit for ideas of what needs to be covered
// make sure the physical order of the LEDs is kept when increasing the gpio number

1. Plug in six LEDs onto the breadboard in parallel, each across the middle channel of the breadboard.
2. Connect the six anodes of LEDs (left to right) to six digital pins (9, 8, 7, 6, 5, 4) on the Arduino Dock (near the jack barrel connector).
3. Connect cathodes of the LEDs to ground (GND) each through a different 200Ω current limiting resistor.

### Writing the Code

// write an arduino sketch that makes the LEDs turn on one-by-one going left to right, and then turn off, again going left to right
// look to the multiple leds article in the starter kit for details

``` arduino
int timer = 100;           // time delay between each LED in ms
int ledPins[] = {9, 8, 7, 6, 5, 4};       // an array of GPIO numbers with LED attached
int pinCount = 6;           // number of GPIOs used

void setup() {      // codes to be ran once
  // loop for initializing the GPIOs
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
  }
}

void loop() {     // codes to be ran continously
  // loop for turn on GPIOs one-by-one going left to right
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);
  }

  // loop for turn off GPIOs one-by-one going left to right 
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], LOW);
    delay(timer);
  }
}
```

#### What to Expect

Your line-up of LEDs will be essentially chasing it's tail: the left-most LED will turn on, and then the next one, and the next and so on. When all of them turn on, the left-most one will turn off, and the rest will follow suit.

// TODO: GIF: Showing this experiment with the LEDs lighting up one after another and then turning off one after another

#### A Closer Look at the Code

// talk about the topics we introduced here

##### Arrays

// talk about arrays, how we use an array to hold the gpio numbers in order

##### For Loop

// talk about how we use the for loop to make sure we cycle through all of our leds
