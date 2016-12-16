---
title: Reading a Switch
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---

## Reading a Switch

// intro to this experiment:
//  * so far, we've been using a program to control GPIOs, lets have some physical, user input controlling our software
//  * will be using a slide switch as input for our program, it will control whether an LED is on or off


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

// circuit 1: switch controls turning an LED on and off to illustrate how the slide switch works
// spdt switch (one side is pull-up, other side is pull-down) connected to an led

#### Hooking up the Components

// step by step guide of how to hook up the components
//  * how to connect one side of the switch to gnd and one to vcc
//  * connect the switchable part to the led

#### What to Expect

// the switch controls if there is power flowing to the LED:
//  when the switch is set to the pull-up fork, the LED will be on
//  when the switch is set to the pull-down fork, the LED will be off

// this is a simple circuit but we wanted to illustrate how the switch works, let's move on to including our Omega in this circuit

### Building the Experiment Circuit

// circuit 2: switch connected to GPIO, controls LED with software
// spdt switch (with pull-up and pull-down sides) connected to gpio input
// regular led circuit connected to gpio setup as output

#### Hooking up the Components

// step by step guide of how to hook up the components
//  jack the switch setup from the above section - adjust so taht it leads to a gpio
//  jack the LED setup from the previous articles

### Writing the Code

// code should poll a gpio, based on the input value, set a different gpio to output the read value
// implementation:
//  * while loop for polling
//  * if it makes sense, write functions to read the gpio, and then set the other gpio (want to teach them good practices right off the bat)
//  * make the delay at the end of the loop pretty long 2-5 seconds

#### What to Expect

// the switch controls whether the LED is on or off. yes the same thing was achieved with the far simpler circuit, but is meant to illustrate how a physical input can control something virtual


#### A Closer Look at the Code

// small overview of anything new we did

##### Polling

// explain polling is the process of repeatedly checking an input
//  * a delay was added since we don't want to burn up the cpu constantly checking the same thing - remember the CPU runs incredibly fast

// talk about how sometimes it takes a while for the led to react:
//  * this is due to the long delay, have them try shortening the delay
//  * introduce some of the issues related to having polling:
//    * can't do anything else in the program
//    * can potentially have a long delay between the physical action and the software reacting
//    * if only there was a better way!
