---
title: Arduino Dock R2
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---


## Arduino Dock 2 {#arduino-dock}

<!-- [//]: # (The Arduino Dock 2 contains an ATmega328P micro-controller, the same one found on the Arduino Uno R3.) -->
<!-- [//]: # (The Omega can program the microcontroller and then communicate with it) -->

<!-- The Arduino Dock 2 is the lovechild of the Arduino Uno R3 and the Omega. Is good? -->

The Arduino Dock 2 is our supercharged version of an Arduino Uno R3 board. These two boards share the same microcontroller, the ATmel ATmega328P microcontroller (MCU), and have identical pin layouts. This allows you to use any Arduino shields that you've used with the Arduino Uno R3 with the Arduino Dock and the Omega.

The Omega can program the microcontroller while connected to the board. This means you can wirelessly connect to the Omega, and then program the MCU for a wireless Arduino experience!

### The Hardware

<!-- [//]: # (small overview of the things the headings below cover) -->

![arduino dock alone](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-alone.jpg)


The Arduino Dock includes an In-Circuit Serial Programming (ICSP) header to break out the SPI pins which can be used to program the Arduino's microcontroller. Additionally, there is a USB-host port that is connected to the Omega which can be used for any sort of USB type application.

You can power the dock using a microUSB connection, or using the DC Barrel jack.

### Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

To connect an Omega to the Arduino Dock, line up the Omega's edges with the purple lines on the Arduino Dock's as demonstrated below:

![arduino dock plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-top-plugged-in.jpg)

Make sure your Omega is pushed all the way down as demonstrated in the picture below:


![arduino dock side view](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-side-view.jpg)

You may need to line up the pins with the holes before pressing the Omega into the Dock.


### The Arduino Dock at a Glance

<!-- [//]: # (illustration with all of the key parts labelled - see https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example) -->
![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-illustration.jpg)


### The Expansion Header

<!-- [//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions) -->
The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each section.


<!-- #### Detailed Pinout -->

<!-- [//]: # (A detailed pinout diagram of the Expansion Header, showing which pins are multiplexed - see Lazar for an example) -->
<!-- TODO: add photo -->

### The ATmega Headers

<!-- [//]: # (breakout of the ATmega's pins, same as the Arduino Uno R3) -->
<!-- [//]: # (include an image) -->

The ATmega headers are a breakout of the ATmega's pins. They are arranged in the exact same way as an Arduino Uno R3, so all your shields are cross compatible. The pins are also labelled for your convenience.

![arduino dock atmega headers](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-atmega-header.jpg)



### The MicroUSB Port

<!-- [//]: # (explain that it provides power to the omega, mention that the Omega is powered by 3.3V and that the Dock has a regulator to take the 5V from the microUSB and step it down to 3.3V) -->

<!-- [//]: # (mention there's no usb to serial chip) -->

The MicroUSB Port is used to supply power to the Arduino Dock, which in turn supplies power to the Omega and the ATmega328P chip.

The MicroUSB Port takes in 5V, and the Arduino Dock comes equipped with a voltage regulator to step the voltage down to the required 3.3V for the Omega.


#### No USB-to-Serial

There is no USB-to-Serial Chip on the Breadboard Dock. This means that you will **not** be able to connect to the Omega serially over the Micro-USB port.


### DC Barrel Jack

<!-- [//]: # (provide power to the Omega using a DC power adapter) -->
<!-- [//]: # (REALLY highlight the fact that 5V is the maximum input and that any more than 5V will damage the dock and omega) -->

The DC barrel jack may also be used to provide power to the Omega using a DC power adapter.

**Note that the Arduino Dock's DC barrel jack should only be used with 5V DC power supplies. If a higher voltage is used, your Omega and Arduino Dock have a high chance of being damaged!**


### Reset Button

<!-- [//]: # (reset button is connected directly to the Omega's reset GPIO, can be used to just trigger a reboot or even a full factory restore) -->

The Omega Reset Button on the Arduino Dock is connected directly to the Omega's Reset GPIO. Pressing this button do one of two things: reboot, or factory restore.


#### Reboot

Momentarily pressing the reset button and letting go will initiate a reboot of the Omega OS.

#### Factory Restore

Pressing and holding the reset button for 10 seconds and releasing will trigger a factory restore.

**Warning**: This will reset your Omega to the default filesystem of the last firmware update. **This will delete ALL of your data!**

### Micro-Controller Reset Button

<!-- [//]: # (issues a reset to the ATmega chip, give background on what that means in the Arduino Context) -->

In addition to the Omega's reset button, the Arduino Dock 2 comes with a microcontroller reset button. This button can be used to reset the ATmega chip whenever you'd like in order to prepare the chip for uploading a new sketch. This will **NOT** reset the Omega.

### Omega USB Port

<!-- [//]: # (USB port connected to the Omega - interface USB devices with the Omega, mention that it's a type A connector) -->

The Omega's USB Port can be used to connect to all sorts of devices, namely a USB storage device to extend the storage space of your Omega. The USB port supports USB 2.0, and is a type A connector.


### Omega to ATmega MCU Connections

<!-- [//]: # (The Omega and ATmega are connected via the following:) -->
<!-- [//]: # (- Omega UART1 to Arduino's serial pins) -->
<!-- [//]: # (- I2C pins) -->
<!-- [//]: # (- Omega's GPIOs 15, 16, 17 to ATmega's SPI SCK, SPI MOSI, and SPI MISO pins respectively) -->
<!-- [//]: # (- Omega's GPIO 19 to reset ATmega (will pull the RESET high)) -->

<!-- [//]: # (mention that there's a 3.3V to 5V Logic Level shifter for the connections) -->

The Arduino Dock is outfitted with a 3.3V to 5V Logic Level converter in order for the Omega to successfully communicate with the ATmega chip.

The table below shows the connections between the Omega's pins and the ATmega's pins:

| Omega Pin  | ATmega Pin |
| :-------------: | :-------------:  |
| UART1 | Serial Pins  |
| I2C | I2C  |
| GPIO 15 | SPI SCK  |
| GPIO 16 | SPI MOSI  |
| GPIO 17 | SPI MISO  |
| GPIO 19 | Reset  |

The purposes of these connections are covered in the subsections below.


#### UART Connection

<!-- [//]: # (functionality: provide easy to use two-way communication between the Omega and MCU) -->

The UART connection is used to provide two-way communication between the Omega and the ATmega MCU.

#### I2C

<!-- [//]: # (funcionality: provide I2C connectivity between the Omega and ATmega, the Omega is setup to be the master in most cases) -->
<!-- [//]: # (this is also useful when using 5V I2C devices, plug them into the ATmega I2C pins, and the Omega will be able to read it) -->

The I2C connection provides I2C connectivity between the Omega and the ATmega. In most cases, the Omega is set up as the master, and the ATmega as the slave.

This is useful when using 5V I2C devices. Plug them into the ATmega's I2C pins and the Omega will be able to read them.

#### SPI and Reset Connection

<!-- [//]: # (these four pins are used by the Omega to reset and program the ATmega with sketches) -->

The four SPI connections are used to upload the ATmega with sketches using your Omega.

The reset connection is used to reset the ATmega chip. This can be done using the reset button, or using the Omega's GPIO 19.


<!-- TODO: ### Mechanical Drawings -->

<!-- [//]: # (insert gabe's dope mechanical drawings) -->


### Using the Dock

<!-- [//]: # (little overview of the special features of this dock) -->

The Arduino Dock 2 is loaded with features that allow you to use your Omega with the ATmega chip with ease. You can program or reset the micro-controller using the Omega's GPIOs, and even connect to the ATmega's serial port using the Omega's UART.


<!-- TODO:  These articles are to be part of the Arduino Kit guides, and we will link to them when the guides are ready. -->
<!-- ### Programming the Micro-Controller -->

<!-- [//]: # (create a separate article for this under Doing Stuff - should be included in the RESETTING article mentioned above (part of batch3)) -->
<!-- [//]: # (two methods:) -->
<!-- [//]: # (- using the arduino ide) -->
<!-- [//]: # (- flashing sketches stored on the Omega's memory) -->

<!-- ### Connecting with UART1 -->

<!-- [//]: # (create a separate article for Omega <-> ATmega communication via serial, in this article link to the UART1 peripheral article and have an example scenario with an example sketch for the arduino and sample code for the Omega) -->

<!-- ### Resetting the Micro-Controller -->

<!-- [//]: # (create a separate article for this under Doing Stuff (part of batch3)) -->
<!-- [//]: # (link to Arduino Dock article on resetting the microcontroller) -->
<!-- [//]: # (two methods:) -->
<!-- [//]: # (- pressing the physical button) -->
<!-- [//]: # (- using GPIO19) -->
