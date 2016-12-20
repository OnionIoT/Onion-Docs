---
title: Controlling an LCD Screen
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 10
---

# Controlling an LCD Screen {#starter-kit-controlling-an-lcd-screen}

// in this experiment, we will:
//  * be building on the previous experiment
//  * writing to an lcd screen
//    * using the i2c protocol


## LCD Screen
// should be in its own markdown file

// LCD screen:
//  * 16x2 meaning two rows that can fit 16 characters each
//  * led backlight to illuminate the display
//  * usually these LED screens are controlled by parallel (many) data lines - like 11 usually
//    * this one has additional circuitry that allows devices to use the i2c protocol to control the screen


## The I2C Bus
// should be in its own markdown file

// mention all of the key points:
//  * two lines: data and clock
//  * master slave architecture
//  * each device has it's own unique two byte address
// on the omega:
//  * accesses through the virtual device file /dev/i2c-0

// make sure to mention that it can be referred to as I2C, IIC, Two-wire interface (TWI)

// can totally rip off large chunks of the i2c article from the documentation
//  * should isolate that text from the i2c article into  markdown files that can be included here


## Building the Circuit

// start from the temperature sensor circuit
// straight-forward addition: I2C SCL+SDA, Vcc (3.3V), GND


### Hooking up the Components

// refer them back to the temp sensor article for that part

// some i2c devices will require pull-up resistors on one, or both of SCL and SDA
// [experiment with the i2c screen and see if it needs the resistors]


## Writing the Code

// have a script that:
//  * reads the temperature data
//  * writes the time and temperature to the display once a minute
//    * use the onion i2c module to write to the display

### What to Expect

// calling the script will update the lcd screen, but wouldn't it be nice if something could run the script for us every minute to actually update the lcd?

### A Closer Look at the Code

// intro to the onion i2c module

#### The Onion I2C Module

// introduce the onion i2c module, written by Onion to facilitate the easy use of the i2c bus
// give a brief overview of the functions that we used and point them to the documentation reference (need to include docs.onion.io link, not markdown tag)

#### Multiple Different objects

// small blurb about how the main program uses two objects of different classes to accomplish its purpose - make a note that this is an incredibly common programming method/technique

### Going Further: Automating the Script

// introduce cron
// show example of how to setup cron to run the script we wrote once every minute
