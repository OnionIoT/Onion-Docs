---
title: Reading a Push Button
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 5
---

# Reading a Push Button

<!-- // intro to push button
// building on what we did with the slide switch, but let's use the button as a trigger for an action - as opposed to constantly reading the state of the switch

// we will be building an led controlled by a push button, when the button is pressed, the led will turn on, and remain on for 10 seconds, then turn off -->

For this experiment, we'll build on what we did with the slide switch. This time, let's use the button as the trigger instead of constantly polling the switch! 

We'll be making a circuit with an LED controlled by a **push button**. When the button is pressed, the LED will turn on for 10 seconds, then turn off.

## Push Buttons

<!-- // put in its own markdown file -->

<!-- // explanation of push buttons: how they are momentary switches and only close the circuit while the button is depressed
// explanation of the pins, and what connection happens when the button is pressed -->
```{r child = '../../shared/switches-push-button.md'}
```

### Debouncing Switches

<!-- debouncing switches -->
```{r child = '../../shared/switches-debouncing.md'}
```

## Building an Example Circuit

// circuit 1: button with debouncing circuit controls an LED directly

### Hooking up the Components

// explain how to connect a push-button switch to an led

### What to Expect

// push and hold the button, the led is on
// release it and the led turns off

// the drawback of this circuit is that the switch just controls if there is current flowing to the LED or not
// adding


## Building the Real Circuit

// circuit 2: button with debouncing circuit connected to GPIO,  LED connected to GPIO


## Writing the Code

Let's go about writing our code, but first let's cover an important topic first.

### Edge Detection

<!-- edge detection -->
```{r child = '../../shared/gpio-edge-detection.md'}
```

// edge detection is when the system waits for an "edge" in the signal to perform an action. an edge being a place where the signal goes from high to low (falling edge), or low to high (rising edge) (have an illustration)

// in terms of the action, we'll be defining a function to be executed when the trigger, in this case the edge in the signal is detected
// relate this back to interrupts and interrupt service routines


### The Code Itself

// * write a program that uses edge detection to turn an led on, sleep for 10 seconds and then turn it off
note: the mechanism for edge detection hasn't been ironed out yet


### What to Expect

// hit the button, the light turns on, stays on for 10 seconds, turns off

### A Closer Look at the Code

// explanation of the edge detection code
