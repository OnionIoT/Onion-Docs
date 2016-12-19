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

#### Hooking up the Components

// look to the multiple leds article in the starter kit for ideas of what needs to be covered
// make sure the physical order of the LEDs is kept when increasing the gpio number

### Writing the Code

// write an arduino sketch that makes the LEDs turn on one-by-one going left to right, and then turn off, again going left to right
// look to the multiple leds article in the starter kit for details

#### What to Expect

Your line-up of LEDs will be essentially chasing it's tail: the left-most LED will turn on, and then the next one, and the next and so on. When all of them turn on, the left-most one will turn off, and the rest will follow suit.

// TO DO: GIF: Showing this experiment with the LEDs lighting up one after another and then turning off one after another

#### A Closer Look at the Code

// talk about the topics we introduced here

##### Arrays

// talk about arrays, how we use an array to hold the gpio numbers in order

##### For Loop

// talk about how we use the for loop to make sure we cycle through all of our leds
