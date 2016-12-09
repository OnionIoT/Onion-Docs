---
title: Breadboard Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---


## Breadboard Dock {#breadboard-dock}

<!-- // The Breadboard Dock is the most no-frills dock, it provides power to the Omega and allows it to be plugged in to a breadboard. The pins on the breadboard are mapped 1-to-1 as on the Omega. -->

The Breadboard Dock is the perfect solution for building circuits with the Omega. This Dock can be plugged into a breadboard, and the pins of the dock are mapped 1-to-1 as on the Omega.

The Breadboard Dock provides power to the Omega via a Micro-USB port that takes in 5V. This voltage is stepped down to the 3.3V required to power the Omega.


### The Hardware

<!-- // overview of the dock -->

#### Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

#### The Breadboard Dock at a Glance

<!-- https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example) -->

#### The Breadboard Header

<!-- // explanation of the breadboard header, have photos of plugging it into a breadboard -->

##### Detailed Pinout diagram

<!-- [//]: # (A detailed pinout diagram of the Breadboard Header, showing which pins are multiplexed - see Lazar for an example) -->

#### The MicroUSB Port

<!-- [//]: # (explain that it provides power to the omega, mention that the Omega is powered by 3.3V and that the Dock has a regulator to take the 5V from the microUSB and step it down to 3.3V) -->

The Micro-USB Port is used to supply power to the Breadboard Dock, which in turn supplies power to the Omega.

The Micro-USB Port takes in 5V, and the Breadboard Dock comes equipped with a voltage regulator to step the voltage down to the required 3.3V for the Omega.


##### No USB-to-Serial

There is no USB-to-Serial Chip on the Breadboard Dock. This means that you will **not** be able to connect to the Omega serially over the Micro-USB port.


<!-- [//]: # (explanation that there is no usb to serial chip on-board) -->

<!-- You can still connect to your Omega's terminal with SSH. You can learn how to do that in this [guide to connecting to the Omega](#connecting-to-the-omega) -->


#### Reset button

<!-- [//]: # (reset button is connected directly to the Omega's reset GPIO, can be used to just trigger a reboot or even a full factory restore) -->
The Reset Button on the Expansion Dock is connected directly to the Omega's Reset GPIO. Pressing this button do one of two things: reboot, or factory restore.

##### Reboot

Momentarily pressing the reset button and letting go will initiate a reboot of the Omega OS.

##### Factory Restore

Pressing and holding the reset button for 10 seconds and releasing will trigger a factory restore.

Warning: This will reset your Omega to the default filesystem of the last firmware update, **this will delete ALL of your data!**
