---
title: Relay Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Relay Expansion

// intro to the relay exp - allows you to control two other, independent, external circuits using the omega - these circuits can be lower voltage, higher voltage, don't matter
// mention this expansion is controlled with i2c

// due to the address selection switch, can use up to eight Relay Expansions with a single omega, allowing you to control up to 16 external circuits/devices

### The Hardware

// Overview of the hardware:
//  - the relays
//  - the screw terminals (this might not be the official name for this)
//  - the address switch

#### Connecting to a Dock

// plugged into the expansion Header
// have photos of it plugged into the Exp dock, power dock, and arduino dock 2

// mention that other expansions can be safely stacked on top of it

#### At a Glance

// illustration - use the one from the existing docs that numbers the servos

#### The Relays

// short explanation of what relays are
// stats of the relays - can find this on the datasheet of the relays or the existing relay articles
// REALLY IMPORTANT - people care a lot about this
// link to the relay datasheet

#### The Screw Terminals (confirm this name is legit)

// instructions on how to connect wires to the screw Terminals
// include photos

#### The Address switch

// explanation of the address switch and how it changes the I2C device address of the Relay Expansion
// include the table of switch positions and corresponding i2c device address
// see existing docs




## Using the Relay Expansion

// give an example of how this can be used and when it would be useful (turning on a lamp or something, some cool IoT example)
// reiterate that relays allow you to use the Omega to switch external circuits

// point them to the article on using the relay Expansion
//  this article should include:
    * An Example circuit
    * Controlling the Relays from the command line
    * Info on how the address switch configuration affects the command line call
    * Link to article on controlling relays from C/C++, python
// refer to existing doc for reference - should follow it closely
