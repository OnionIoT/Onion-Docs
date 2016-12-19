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

<!-- one wire -->
```{r child = '../../shared/one-wire.md'}
```

## Building the Circuit

// very straight-forward circuit: signal wire to a gpio, Vcc (3.3V), GND

### Hooking up the Components

// most 1-wire devices need a pull-up resistor on the data line
// [experiment with the 1-wire temperature sensor to confirm]


## Writing the Code


// the script: should read and write from files on the filesystem
//  * check if the device exists/is registered
//    * if not, register it with the system (have this in its own function)
//  * perform a a reading (have this in its own function)
//  * display the reading on the command line

// should create a temperature sensor class that does the above

// implementation:
// take a look at: https://wiki.onion.io/Tutorials/Reading-1Wire-Sensor-Data
//  the procedure for using 1w on the omega2 is likely similar


### What to Expect

// run the program, get a print-out on the command line of the current temperature


### A Closer Look at the Code

// reading from and writing to the filesystem

#### Writing to the Filesystem

// explanations of opening files, writing/reading the contents, closing the file
// mention that all programs that interact with the filesystem work like this
