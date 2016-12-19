---
title: Dimming LEDs with the Servo
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---

// Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example, this (or something similar) is what the final result will be


# Dimming LEDs with the PWM Expansion

// in this tutorial, we will be learning how to use the PWM Expansion and animating 16 LEDs along the way. To do this we will create a class, and instantiate many objects of that class to control 16 individual LEDs



## What is Pulse Width Modulation?
// should be its own markdown file

// rip off the pwm description from the 'using the pwm expansion' article
//  * should isolate that text into it's own markdown file(s) and then include them here



## Building the Circuit

// 16 LEDs connected to the Servo Expansion

### Hooking up the Components

// 16 example of the most basic LED circuit
// - use M-F jumper wires to connect from the servo expansion
// - make sure to use 5V from the pwm expansion channel header


## Writing the Code

// Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * write the omegaPwm class (from the file above) that programs a single channel
//  * no need to include the frequency functions
// * create 16 objects, one for each of the LEDs
// * make the leds do something interesting, maybe like a wave or something, the key is to show that each object can be controlled completely independently
//    * perhaps find a way to work a button or switch into the mix


### What to Expect

// explanation of the something interesting that you decide to do, add a gif



### A Closer Look at the Code

// making a new class - this should be familiar if you've gone through all of the starter kit experiments

#### Using the Onion PWM Expansion Python Module

// introduce the pwm module, written by Onion to facilitate easy usage of the pwm expansion
// give a brief overview of the functions that we used and point them to the documentation reference (need to include docs.onion.io link, not markdown tag)


#### Creating a class

// refresher on object oriented Programming
//  - emphasis on each object being it's own separate entity

// [note] copy from or link back to the shift register article where we first introduced classes - probably makes more sense to link back since maker kit people will have all starter kit content as well

#### Initializing the PWM Expansion

// bring attention to the check for initialization and then performing the init
//  * talk about how we have to initialize the pwm expansion to start the oscillator in order to generate the pwm signals
