---
title: Using an H-Bridge
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---

// Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example, this (or something similar) is what the final result will be

# Driving a DC Motor using the Servo Expansion and an H-Bridge

// this tutorial will show us how to control a dc motor using an h-bridge. we'll also continue using the class from the first example to create classes to help us accomplish our goals

## DC Motor

<!-- dcmotor -->
```{r child = '../../shared/dcmotor.md'}
```

## H-Bridge

<!-- hbridge -->
```{r child = '../../shared/hbridge.md'}
```


## Building the Circuit

// omega -> h-bridge -> dc motor
// three switches as gpio inputs to the omega

### Hooking up the Components

// omega -> h-bridge: three channels from pwm expansion to control the two input pins and the duty cycle pin, all requisite wiring for power
//  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)
// h-bridge -> dc motor: the h-bridge motor outputs to the motor... duh

// make sure to drive home the point that the H-Bridge can be burnt if improperly wired
//  make sure the pwm expansion is not producing any signals (or they're all at 0%) while you're wiring it


## Writing the Code

// Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * write the hBridge class (from the file above) that drives an h-bridge
//  * don't have to bother with a DigitalPin class like the file above, just set the two direction inputs using 0% or 100% duty cycle

// the program:
//  * two switches: control how fast the motor spins (binary 00 -> 11, make sure to include a truth table)
//  * one switch: controls the direction (on is left, and off is right, or whatever makes sense)

### What to Expect

// explanation of how to use the two switches to set the speed of the motor and the remaining switch to change direction of the spin

// mention ctrl+c to quit the infinite loop

### A Closer Look at the Code

// is there something interesting about the code? if so cover it in this section
