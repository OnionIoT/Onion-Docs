---
title: Expansion Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---


## The Expansion Dock {#expansion-dock}

<!-- [//]: # (Brief overview on the expansion dock and what it's used for (usb connection, power omega, attach expansions).) -->

The Expansion dock is a powerful piece of hardware that simplifies the usage of your Omega. It allows you to power the Omega and communicate with it via serial through the Micro-USB port, and makes it incredibly easy to use the GPIOs and Onion Expansions.


### The Hardware

<!-- [//]: # (small overview of the things the headings below cover) -->

Your Expansion Dock has a 30 pin Expansion Header, allowing you to use all of your Onion Expansions. The Expansion Dock is powered by the Micro-USB port that supplies 5V to the Dock. This voltage is stepped down to the required 3.3V required to power the Omega, and also provides 5V to the Expansions and USB Host port.

The Expansion Dock allows for easy communication via the USB-to-Serial chip located in the center of the board. You've also got a great RGB LED that you can control through the command-line interface.

The reset button, located between the power switch and the Micro USB port, can be used to quickly reboot your Omega, or you can hold it down for a factory reset if your Omega is ever in a bad state.

#### Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->
To connect an Omega to the Expansion Dock, line up the Omega's edges with that of the Expansion Dock's as demonstrated below:

<!-- Insert "expansion-dock-line-up" here -->

Make sure your Omega is pushed all the way down as demonstrated in the picture below:

<!-- Insert "expansion-dock-plugged-in" here -->


You may need to line up the pins with the holes before pressing the Omega into the Dock.

#### The Expansion Dock at a Glance

<!-- [//]: # (illustration with all of the key parts labelled - see https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example) -->

#### The Expansion Header

<!-- [//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions) -->

The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each section.


##### Detailed Pinout

<!-- [//]: # (A detailed pinout diagram of the Expansion Header, showing which pins are multiplexed - see Lazar for an example) -->

#### The Micro-USB Port

<!-- [//]: # (explain that it provides power to the omega, mention that the Omega is powered by 3.3V and that the Dock has a regulator to take the 5V from the microUSB and step it down to 3.3V) -->

The Micro-USB Port is used to supply power to the Expansion Dock, which in turn supplies power to the Omega and the Onion Expansions. It can also be used to connect to the Omega's serial terminal.

The Micro-USB Port takes in 5V, and the Expansion Dock comes equipped with a voltage regulator to step the voltage down to the required 3.3V for the Omega.


##### USB-to-Serial

<!-- [//]: # (explanation that there is a usb to serial chip on-board that allows for a serial connection between the Omega and a computer) -->
<!-- [//]: # (LATER: add link to the connecting to the omega with serial article) -->

The USB-to-Serial chip allows for a serial connection between the Omega and a computer using the Micro-USB port. You can connect a Micro-USB to USB cord from the Omega to your computer, open a terminal, and connect to the Omega via a COM port as opposed to SSH.

<!-- To learn more about the various ways you can connect to the Omega you can read our [guide to connecting to the Omega](#connecting-to-the-omega) -->

#### Power Switch

<!-- [//]: # (inform them of what the power switch will do: cut power to the Omega but keep the USB to serial chip running) -->
<!-- [//]: # (have illustrations showing the ON and OFF positions) -->

The Power Switch is located on the far side of the Expansion Dock, away from the Omega. This switch will cut power to the Omega, but not the serial chip. This means your computer will still detect a USB serial device, but will not be able to communicate with the Omega.

#### Reset button

<!-- [//]: # (reset button is connected directly to the Omega's reset GPIO, can be used to just trigger a reboot or even a full factory restore) -->

The Reset Button on the Expansion Dock is connected directly to the Omega's Reset GPIO. Pressing this button do one of two things: reboot, or factory restore.


##### Reboot

Momentarily pressing the reset button and letting go will initiate a reboot of the Omega's Operating System.

##### Factory Restore

Pressing and holding the reset button for 10 seconds before releasing will trigger a factory restore.

**Warning:** This will reset your Omega to the default filesystem of the last firmware update, **this will delete ALL of your data!**

#### Omega USB Port

<!-- [//]: # (USB port connected to the Omega - interface USB devices with the Omega, mention that it's a type A connector) -->

The Omega's USB Port can be used to connect to all sorts of devices, namely a USB storage device to extend the storage space of your Omega. The USB port supports USB 2.0, and is a type A connector.

#### RGB LED

<!-- [//]: # (explanation of the RGB LEDs, description of which Omega GPIOs control which colour, mention that the LED is active-low) -->
The RGB LED on the Expansion Dock consists of three LEDs that give you the ability to create RGB colors on the Expansion Dock.

GPIO 17 controls the red LED.
GPIO 16 controls the green LED.
GPIO 15 controls the blue LED.

The RGB LED is active-low, meaning that setting the GPIO to 0 will turn on the designated LED.


#### Mechanical Drawings

<!-- [//]: # (insert gabe's dope mechanical drawings) -->


### Using the Dock

<!-- [//]: # (little overview of the special features of this dock) -->

The Expansion Dock makes it incredibly easy to use your Omega. It let's you easily power your Omega, and use Onion Expansions without any external circuitry required. It also makes sure that you don't accidentally burn out your Omega by supplying too much power.

#### Controlling the GPIOs

<!-- [//]: # (mention how the GPIOs can be controlled and provide link to the gpio article) -->
The GPIOs on the dock can be controlled using a number of tools we've included in the Omega firmware. You find more on how you can control the Omega's GPIOs in the article on [using the Omega's GPIOS](#using-gpios)

#### Controlling the RGB LED

<!-- [//]: # (copy the existing RGB LED article) -->

You can use the `expled` tool to specify the color of the RGB LED. It will use software PWM to drive the three LEDs.

Usage:

```
expled <6 digit hex value>
```

Where the first two digits represent the Red value, the next two represent the Green value, and the last two represent the blue value.

Example:

```
expled 0xf21133
```

This will set the Red to `0xf2`, the Green to `0x11`, and the Blue to `0x33`.

The LED should now be pink-ish.
