---
title: Arduino Dock R2
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---


# The Arduino Dock 2

<!-- [//]: # (The Arduino Dock 2 contains an ATmega328P micro-controller, the same one found on the Arduino Uno R3.) -->
<!-- [//]: # (The Omega can program the microcontroller and then communicate with it) -->


# The Hardware

<!-- [//]: # (small overview of the things the headings below cover) -->

## Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

## The Arduino Dock at a Glance

<!-- [//]: # (illustration with all of the key parts labelled - see https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example) -->

## The Expansion Header

<!-- [//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions) -->

### Detailed Pinout

<!-- [//]: # (A detailed pinout diagram of the Expansion Header, showing which pins are multiplexed - see Lazar for an example) -->

## The ATmega Headers

<!-- [//]: # (breakout of the ATmega's pins, same as the Arduino Uno R3) -->
<!-- [//]: # (include an) -->

## The MicroUSB Port

<!-- [//]: # (explain that it provides power to the omega, mention that the Omega is powered by 3.3V and that the Dock has a regulator to take the 5V from the microUSB and step it down to 3.3V) -->

<!-- [//]: # (mention there's no usb to serial chip) -->

## DC Barrel Jack

<!-- [//]: # (provide power to the Omega using a DC power adapter) -->
<!-- [//]: # (REALLY highlight the fact that 5V is the maximum input and that any more than 5V will damage the dock and omega) -->

## Reset Button

<!-- [//]: # (reset button is connected directly to the Omega's reset GPIO, can be used to just trigger a reboot or even a full factory restore) -->

### Reboot

Momentarily pressing the reset button and letting go will initiate a reboot of the Omega OS.

### Factory Restore

Pressing and holding the reset button for 10 seconds and releasing will trigger a factory restore.

Warning: This will reset your Omega to the default filesystem of the last firmware update, **this will delete ALL of your data!**

## Micro-Controller Reset Button

<!-- [//]: # (issues a reset to the ATmega chip, give background on what that means in the Arduino Context) -->

## Omega USB Port

<!-- [//]: # (USB port connected to the Omega - interface USB devices with the Omega, mention that it's a type A connector) -->

## Omega to ATmega MCU Connections

<!-- [//]: # (The Omega and ATmega are connected via the following:) -->
<!-- [//]: # (- Omega UART1 to Arduino's serial pins) -->
<!-- [//]: # (- I2C pins) -->
<!-- [//]: # (- Omega's GPIOs 15, 16, 17 to ATmega's SPI SCK, SPI MOSI, and SPI MISO pins respectively) -->
<!-- [//]: # (- Omega's GPIO 19 to reset ATmega (will pull the RESET high)) -->

<!-- [//]: # (mention that there's a 3.3V to 5V Logic Level shifter for the connections) -->

### UART Connection

<!-- [//]: # (functionality: provide easy to use two-way communication between the Omega and MCU) -->

### I2C

<!-- [//]: # (funcionality: provide I2C connectivity between the Omega and ATmega, the Omega is setup to be the master in most cases) -->
<!-- [//]: # (this is also useful when using 5V I2C devices, plug them into the ATmega I2C pins, and the Omega will be able to read it) -->

### SPI and Reset Connection

<!-- [//]: # (these four pins are used by the Omega to reset and program the ATmega with sketches) -->


## Mechanical Drawings

<!-- [//]: # (insert gabe's dope mechanical drawings) -->


# Using the Dock

<!-- [//]: # (little overview of the special features of this dock) -->

## Resetting the Micro-Controller

<!-- [//]: # (create a separate article for this under Doing Stuff (part of batch3)) -->
<!-- [//]: # (link to Arduino Dock article on resetting the microcontroller) -->
<!-- [//]: # (two methods:) -->
<!-- [//]: # (- pressing the physical button) -->
<!-- [//]: # (- using GPIO19) -->

## Programming the Micro-Controller

<!-- [//]: # (create a separate article for this under Doing Stuff - should be included in the RESETTING article mentioned above (part of batch3)) -->
<!-- [//]: # (two methods:) -->
<!-- [//]: # (- using the arduino ide) -->
<!-- [//]: # (- flashing sketches stored on the Omega's memory) -->

## Connecting with UART1

<!-- [//]: # (create a separate article for Omega <-> ATmega communication via serial, in this article link to the UART1 peripheral article and have an example scenario with an example sketch for the arduino and sample code for the Omega) -->
