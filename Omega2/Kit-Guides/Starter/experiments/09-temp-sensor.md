---
title: Reading an I2C Sensor
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 9
---

# Reading an One-Wire Temperature Sensor

// in this experiment we will:
//  * introduce the one-wire bus protocol
//  * read the ambient temperature using a sensor
//  * learn how to read and write files

## One Wire Protocol

// should be its own markdown file

The One Wire protocol is a bus-based protocol that uses, as the name implied, one wire for data transmission. It's similar to I2C (link to lcd screen article) but it has a longer range and a lower data rate. It follows a master-slave architecture with each bus allowing for one master, the Omega in this case, and many slave devices. Every device type has it's own unique single-byte (eight bit) identifier, and each device has it's own unique 64-bit serial number that includes the device type byte as the Least Significant Byte.
// throw in an example of a single-byte in hex
// bonus points: throw in an image showing 64 bits (separated into bytes), and highlighting the lsb (can make this easily in excel)

// make sure to mention that it can be referred to as 1W, 1-Wire, etc.

## Building the Circuit

// very straight-forward circuit: signal wire to a gpio, Vcc (3.3V), GND

### Hooking up the Components

// most 1-wire devices need a pull-up resistor on the data line
// [experiment with the 1-wire temperature sensor to confirm]


## Writing the Code

// take a look at: https://wiki.onion.io/Tutorials/Reading-1Wire-Sensor-Data
//  the procedure for using 1w on the omega2 is likely similar
// the script: should read and write from files on the filesystem
//  * check if the device exists/is registered
//    * if not, register it with the system (have this in its own function)
//  * perform a a reading (have this in its own function)
//  * display the reading on the command line

// might be a good idea to create a temperature sensor class that does the above


### What to Expect

// run the program, get a print-out on the command line of the current temperature


### A Closer Look at the Code

// reading from and writing to the filesystem

#### Writing to the Filesystem

// explanations of opening files, writing/reading the contents, closing the file
// mention that all programs that interact with the filesystem work like this
