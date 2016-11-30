---
title: Expansion Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---


# The Expansion Dock

[//]: # (Brief overview on the expansion dock and what it's used for (usb connection, power omega, attach expansions).)


# The Hardware

[//]: # (small overview of the things the headings below cover)

## Connecting an Omega

[//]: # (picture guide on how to properly plug in an Omega)

## The Expansion Dock at a Glance

[//]: # (illustration with all of the key parts labelled - see https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example)

## The Expansion Header

[//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions)

### Detailed Pinout

[//]: # (A detailed pinout diagram of the Expansion Header, showing which pins are multiplexed - see Lazar for an example)

## The MicroUSB Port

[//]: # (explain that it provides power to the omega, mention that the Omega is powered by 3.3V and that the Dock has a regulator to take the 5V from the microUSB and step it down to 3.3V)

### USB-to-Serial

[//]: # (explanation that there is a usb to serial chip on-board that allows for a serial connection between the Omega and a computer)
[//]: # (LATER: add link to the connecting to the omega with serial article)

## Power Switch

[//]: # (inform them of what the power switch will do: cut power to the Omega but keep the USB to serial chip running)
[//]: # (have illustrations showing the ON and OFF positions)

## Reset button

[//]: # (reset button is connected directly to the Omega's reset GPIO, can be used to just trigger a reboot or even a full factory restore)

### Reboot

Momentarily pressing the reset button and letting go will initiate a reboot of the Omega OS.

### Factory Restore

Pressing and holding the reset button for 10 seconds and releasing will trigger a factory restore.

Warning: This will reset your Omega to the default filesystem of the last firmware update, **this will delete ALL of your data!**

## Omega USB Port

[//]: # (USB port connected to the Omega - interface USB devices with the Omega, mention that it's a type A connector)

## RGB LED

[//]: # (explanation of the RGB LEDs, description of which Omega GPIOs control which colour, mention that the LED is active-low)

## Mechanical Drawings

[//]: # (insert gabe's dope mechanical drawings)


# Using the Dock

[//]: # (little overview of the special features of this dock)

## Controlling the GPIOs

[//]: # (mention how the GPIOs can be controlled and provide link to the gpio article)

## Controlling the RGB LED

[//]: # (copy the existing RGB LED article)
