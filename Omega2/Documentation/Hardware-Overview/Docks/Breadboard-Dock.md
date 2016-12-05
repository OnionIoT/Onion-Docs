---
title: Breadboard Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---


# The Breadboard Dock

// The Breadboard Dock is the most no-frills dock, it provides power to the Omega and allows it to be plugged in to a breadboard. The pins on the breadboard are mapped 1-to-1 as on the Omega.


# The Hardware

// overview of the dock

## Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

## The Breadboard Dock at a Glance

https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example)

## The Breadboard Header

// explanation of the breadboard header, have photos of plugging it into a breadboard

### Detailed Pinout diagram

<!-- [//]: # (A detailed pinout diagram of the Breadboard Header, showing which pins are multiplexed - see Lazar for an example) -->

## The MicroUSB Port

<!-- [//]: # (explain that it provides power to the omega, mention that the Omega is powered by 3.3V and that the Dock has a regulator to take the 5V from the microUSB and step it down to 3.3V) -->

### No USB-to-Serial

<!-- [//]: # (explanation that there is no usb to serial chip on-board) -->

## Reset button

<!-- [//]: # (reset button is connected directly to the Omega's reset GPIO, can be used to just trigger a reboot or even a full factory restore) -->

### Reboot

Momentarily pressing the reset button and letting go will initiate a reboot of the Omega OS.

### Factory Restore

Pressing and holding the reset button for 10 seconds and releasing will trigger a factory restore.

Warning: This will reset your Omega to the default filesystem of the last firmware update, **this will delete ALL of your data!**
