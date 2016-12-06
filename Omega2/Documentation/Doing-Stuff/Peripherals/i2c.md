---
title: Communicating with I2C Devices
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Communicating with I2C Devices

// brief description of I2C (sometimes called TWI - two wire interface):
//  - has a master-slave architecture (many slaves, one master)
//    - Omega is configured to be the bus master
//    - each slave is identified with an address: sending a command to 0x27 will only be read by the device who's address is 0x27, other devices on the bus will ignore it
//    - great for having a bunch of different devices connected to the Omega (sensors, controllers, etc)
//  - based on using two lanes: one for clock(SCL) and one for data(SDA)
//    - read up about this but I think it generally works like this: the master generates the clock and then sends data on the data lane, or the master generates the clock and then requests data on the data lane, the device responds by driving the data lane
//  - provide a link to an in-depth article

// list of Omega Expansions that use SPI

### On the Hardware
// highlight the Omega pins: SCL and SDA on both the Omega and the Expansion Dock


### Controlling I2C Devices from the Command line

// Using the i2cget, i2cset commands on the command line

<!-- #### Detecting I2C devices -->
<!-- // leave this out for now, there's a bug that makes this useless -->

#### Reading a Byte

// explain how to use i2cget to read an i2c register value
//  explain the components of the command :`i2cget -y 0 0x27 0x00`

#### Writing a Byte

// explain how to use i2cset to write to a register
//  explain the components of the command :`i2cset -y 0 0x27 0x00 0x33`

#### Going further

// look into the command line options for writing two bytes at a time

#### The Omega Expansions

// mention that the for the omega expansions, they each have their own tools written for the command line - link to the articles

### Moving Beyond the Command line

#### Controlling I2C Devices using Python

// introduce that onion has developed an I2C module for Python
// Show a small example: can be based on https://wiki.onion.io/Tutorials/Python-I2C-LCD-Display
// link to reference article on onion i2c python module

#### Controlling I2C Devices using C & C++

// introduce that onion has developed an I2C library for C and C++
// link to reference article on onion i2c c lib
