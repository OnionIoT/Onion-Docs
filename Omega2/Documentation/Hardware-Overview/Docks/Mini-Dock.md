---
title: Mini Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

// TODO: bring over changes from exp dock article


## The Mini Dock

<!-- [//]: # (Brief overview on the expansion dock and what it's used for (usb connection, power omega). Highlight it's size and how it's useful) -->
<!-- [//]: # (for Omega-only projects or USB-based projects.) -->

The Mini Dock functions very similarly to the Expansion Dock. It supplies your Omega with power and allows you to communicate serially via a Micro-USB port. It also has a USB type A connector for you to use. All of this with a fraction of the size of an Expansion Dock.

The Mini Dock is approximately the exact same size as the Omega. It does not have the Expansion Header of some of the other Docks, but this makes it perfect for Omega-only or USB-based projects.

### The Hardware

<!-- [//]: # (Picture of mini dock with important bits highlighted like usb port, how to plug in the Omega, power switch (which direction is ON?).) -->
<!-- [//]: # (Maybe in depth discussion of various pieces, like USB to serial chip. People like that.) -->
<!-- [//]: # (Refer to current Power Dock Expansion doc for more info) -->

<!-- //NOTE: CAN LARGELY COPY FROM THE EXPANSION DOCK ARTICLE! -->

The Mini Dock is tiny. It is approximately 4.3cm (1.7in) long, and 2.7cm (1.07in) wide.

The Mini Dock is powered by the Micro-USB port that supplies 5V to the Dock. This voltage is stepped down to the required 3.3V required to power the Omega, and also provides 5V to the USB Host port

The Mini Dock allows for easy communication via the USB-to-Serial chip located in the center of the board.

The reset button, located next to the USB Connector, can be used to quickly reboot your Omega, or you can hold it down for a factory reset if your Omega is ever in a bad state.

#### Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

To connect an Omega to the Mini Dock, line up the Omega's edges with that of the Mini Dock's as demonstrated below:

<!-- Insert "mini-dock-line-up" pic here -->

Make sure your Omega is pushed all the way down as demonstrated in the picture below:


<!-- Insert "expansion-dock-plugged-in" here -->

You may need to line up the pins with the holes before pressing the Omega into the Dock.


#### The Mini Dock at a Glance

<!-- [//]: # (illustration with all of the key parts labelled - see https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example) -->

#### The MicroUSB Port

<!-- [//]: # (explain that it provides power to the omega, mention that the Omega is powered by 3.3V and that the Dock has a regulator to take the 5V from the microUSB and step it down to 3.3V) -->

The Micro-USB Port is used to supply power to the Mini Dock, which in turn supplies power to the Omega. It can also be used to communicate with the Omega serially.
// TODO:bring in changes from expansion dock article

The Micro-USB Port takes in 5V, and the Mini Dock comes equipped with a voltage regulator to step the voltage down to the required 3.3V for the Omega.


##### USB-to-Serial

<!-- [//]: # (explanation that there is a usb to serial chip on-board that allows for a serial connection between the Omega and a computer) -->
<!-- [//]: # (LATER: add link to the connecting to the omega with serial article) -->
The USB-to-Serial chip allows for a serial connection between the Omega and a computer using the Micro-USB port. You can connect a Micro-USB to USB cord from the Omega to your computer, open a terminal, and connect to the Omega via a COM port as opposed to SSH.


<!-- To learn more about the various ways you can connect to the Omega you can read our [guide to connecting to the Omega](#connecting-to-the-omega) -->


#### Power Switch

<!-- [//]: # (inform them of what the power switch will do: cut power to the Omega but keep the USB to serial chip running) -->
<!-- [//]: # (have illustrations showing the ON and OFF positions) -->

The Power Switch is located next to the Micro-USB port on the Mini Dock. This switch will cut power to the Omega, but not the serial chip. This means your computer will still detect a USB serial device, but will not be able to communicate with the Omega.


#### Reset button

<!-- [//]: # (reset button is connected directly to the Omega's reset GPIO, can be used to just trigger a reboot or even a full factory restore) -->
The Reset Button on the Mini Dock is connected directly to the Omega's Reset GPIO. Pressing this button do one of two things: reboot, or factory restore.

##### Reboot

Momentarily pressing the reset button and letting go will initiate a reboot of the Omega OS.

##### Factory Restore

Pressing and holding the reset button for 10 seconds and releasing will trigger a factory restore.

Warning: This will reset your Omega to the default filesystem of the last firmware update, **this will delete ALL of your data!**

#### Omega USB Port

<!-- [//]: # (USB port connected to the Omega - interface USB devices with the Omega, mention that it's a type A connector) -->
The Omega's USB Port can be used to connect to all sorts of devices, namely a USB storage device to extend the storage space of your Omega. The USB port supports USB 2.0, and is a type A connector.

#### Mechanical Drawings

<!-- [//]: # (insert gabe's dope mechanical drawings) -->



<!-- [//]: # (LATER: Add using the dock:) -->
<!-- [//]: # ( - usb storage ) -->
<!-- [//]: # ( - controlling a usb serial device) -->
