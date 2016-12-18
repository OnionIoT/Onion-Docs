---
title: Breadboard Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 5
---


## Breadboard Dock {#breadboard-dock}

<!-- // The Breadboard Dock is the most no-frills dock, it provides power to the Omega and allows it to be plugged in to a breadboard. The pins on the breadboard are mapped 1-to-1 as on the Omega. -->

The Breadboard Dock is the perfect solution for building breadboard circuits with the Omega. This Dock can be plugged into a breadboard, and the pins of the dock are mapped 1-to-1 as on the Omega.


### The Hardware

<!-- // overview of the dock -->

The Breadboard Dock provides power to the Omega via a Micro-USB port that takes in 5V. This voltage is stepped down to the 3.3V required to power the Omega.

All of the Omega's pins are broken out via a breadboard header. You can use this Dock with your own circuits, custom embedded applications, or just for hacking!

#### Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

Connect your Omega to the Breadboard Dock by lining up the two rows of header pins so that the sticker with the Omega's MAC address is on the **left** side of the Dock. Basically, make sure that the lines of the Omega and Breadboard Dock are aligned, RESET button is visible, and all of the pins are seated.

![connect-omega](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/breadboard-dock-omega-connected.jpg)

#### The Breadboard Dock at a Glance

<!-- https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example) -->

![breadboard-dock-illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/breadboard-dock-illustration.png)

#### The Breadboard Header

<!-- // explanation of the breadboard header, have photos of plugging it into a breadboard -->

The breadboard header is the part that connects the Dock to your breadboard.

Breadboards have a slot in the middle that divides them in left and right halves. Position the Dock's pins along the length of the slot and line up the pins so that they land on each side of the breadboard.

**IMPORTANT: Make sure the pins are separated by the slot before connecting to power, or they will be short-circuited! Otherwise this WILL damage your Omega and Breadboard Dock!**

Fully insert the Dock so that all of the breadboard header's pins fit into the breadboard as shown below.

![connect-to-breadboard-1](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/breadboard-dock-mounted-1.jpg)

![connect-to-breadboard-2](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/breadboard-dock-mounted-2.jpg)



<!-- TODO: ##### Detailed Pinout diagram -->

<!-- [//]: # (A detailed pinout diagram of the Breadboard Header, showing which pins are multiplexed - see Lazar for an example) -->

<!-- Micro USB Port -->
```{r child = '../shared/Hardware-Overview-Component-1-Micro-USB-Port.md'}
```

<!-- No-USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-3-No-USB-to-Serial.md'}
```

<!-- Reset Button -->
```{r child = '../shared/Hardware-Overview-Component-0-Reset-Button.md'}
```
