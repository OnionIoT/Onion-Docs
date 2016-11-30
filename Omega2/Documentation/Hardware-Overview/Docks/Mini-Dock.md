---
title: Mini Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---


# The Mini Dock

[//]: # (Brief overview on the expansion dock and what it's used for (usb connection, power omega). Highlight it's size and how it's useful)
[//]: # (for Omega-only projects or USB-based projects.)


# The Hardware

[//]: # (Picture of mini dock with important bits highlighted like usb port, how to plug in the Omega, power switch (which direction is ON?).)
[//]: # (Maybe in depth discussion of various pieces, like USB to serial chip. People like that.)
[//]: # (Refer to current Power Dock Expansion doc for more info)

//NOTE: CAN LARGELY COPY FROM THE EXPANSION DOCK ARTICLE!

## Connecting an Omega

[//]: # (picture guide on how to properly plug in an Omega)

## The Mini Dock at a Glance

[//]: # (illustration with all of the key parts labelled - see https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example)

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

## Mechanical Drawings

[//]: # (insert gabe's dope mechanical drawings)



[//]: # (LATER: Add using the dock:)
[//]: # ( - usb storage )
[//]: # ( - controlling a usb serial device)
