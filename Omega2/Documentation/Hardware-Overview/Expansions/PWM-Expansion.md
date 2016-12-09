---
title: PWM Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

## PWM Expansion

// intro to the pwm exp - allows you to generate 16 distinct PWM signals
// can be used to control anything that can be controlled by pwm: leds, servos, motors, etc

// mention this expansion is controlled with i2c

### The Hardware

// Overview of the Hardware
//  - the 16 channels
//  - the dc barrel jack

#### Connecting to a Dock

// plugged into the expansion Header
// have photos of it plugged into the Exp dock, power dock, and arduino dock 2

// mention that other expansions can be safely stacked on top of it - just be mindful of wires connected to the headers

// maybe a good place to mention that only 1 pwm expansion per omega will work

#### At a Glance

// illustration

#### The 16 Channels (maybe change this title?)

// explanation of channel ordering - which channel is 0, which is 1

// Explanation that each channel has male headers for Vcc, ground, and the pwm signal; the important part here is the signal header - thats the pwm signal

##### Connecting Servos

// mention that we made the headers this way so that servo connectors can be plugged right in - add photo of a servo expansion on a dock with a servo plugged in, maybe also a photo of the pwm expansion on the spider robot

#### The Barrel Jack adapter

// highlight that the omega can only provide enough power to move one or two servos under light load, in order to power projects with a bunch of servos, we've included a barrel jack adapter
// the DC voltage that comes in will be provided on the Vcc and GND pins on the channels, the PWM signal will also be stepped up to this voltage

// mention that they shouldn't go too nuts, say that we've tested up to 12V
// also mention that this does not provide power to the Omega, it will still need to be powered a different way

// see existing doc for reference

#### The Oscillator

// the chip that generates the pwm signals has an internal oscillator that controls the frequency of the generated pwm signals
// since there is one oscillator, all of the pwm signals will run on the same frequency. make sure to make the distinction that they just operate on the same frequency but their pwm duty cycles can be different
// mention the frequency range - see existing doc

### Using the PWM Expansion

// examples of use: robotics, making led light shows, anything involving pwm signals

// point them to the article on using the pwm Expansion
//  this article should include:
      * explanation of pwm signals
      * controlling the servos from the command line
      * link to articles on controlling relays from C/C++, python
// refer to existing doc for reference
