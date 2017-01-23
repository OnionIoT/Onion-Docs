---
title: Arduino Dock R2
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---


## Arduino Dock 2 {#arduino-dock-2}

<!-- [//]: # (The Arduino Dock 2 contains an ATmega328P micro-controller, the same one found on the Arduino Uno R3.) -->
<!-- [//]: # (The Omega can program the microcontroller and then communicate with it) -->

<!-- The Arduino Dock 2 is the lovechild of the Arduino Uno R3 and the Omega. Is good? -->

The Arduino Dock 2 is our supercharged version of an Arduino Uno R3 board. These two boards share the same microcontroller, the ATmel ATmega328P microcontroller (MCU), and have identical pin layouts. This allows you to use any Arduino shields that you've used with the Arduino Uno R3 with the Arduino Dock and the Omega.

![arduino dock alone](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-alone.jpg)

The Omega can program the microcontroller while connected to the board. This means you can wirelessly connect to the Omega, and then program the MCU for a wireless Arduino experience!

### The Hardware

<!-- [//]: # (small overview of the things the headings below cover) -->

The Arduino Dock includes an In-Circuit Serial Programming (ICSP) header to break out the SPI pins which can be used to program the Arduino Dock's microcontroller with an external programmer. Additionally, there is a USB-host port that is connected to the Omega which can be used for any sort of USB type application.

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-illustration.png)

You can power the dock using a microUSB connection, or using the DC Barrel jack.

### Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

To connect an Omega to the Arduino Dock, line up the Omega's edges with the purple lines on the Arduino Dock's as demonstrated below:

![arduino dock plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-top-plugged-in.jpg)

Make sure your Omega is pushed all the way down as demonstrated in the picture below:


![arduino dock side view](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-side-view.jpg)

You may need to line up the pins with the holes before pressing the Omega into the Dock.


### The Expansion Header

<!-- [//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions) -->
The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each header.

It follows the same layout as the Expansion Header found on the Expansion Dock and Power Dock.

>**Note**:If you own an Omega2 or Omega2+ and intend to use the PWM expansion with a DC power supply, please take note there is likely to be a short circuit between the barrel jack and the metal case of the Omega itself. We recommend inserting a thin plastic sheet between the expansion and the omega to break this short. For more information, see the [PWM Expansion](#pwm-expansion) article.

<!-- expansion header pinout intro -->
```{r child = '../shared/Hardware-Overview-Component-01-expansion-header-pinout-intro.md'}
```

![expansion header pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-expansion-header-pinout.png)

<!-- expansion header pinout explanation -->
```{r child = '../shared/Hardware-Overview-Component-02-expansion-header-pinout-explanation.md'}
```


### The ATmega Headers

<!-- [//]: # (breakout of the ATmega's pins, same as the Arduino Uno R3) -->

The ATmega headers are a breakout of the ATmega's pins. They are arranged and spaced in the exact same way as an Arduino Uno R3, so all your Arduino Shields are compatible. These pins are also labelled for your convenience.

>Note: Remember that the ATmega runs on 5V, and therefore it reads 5V as logical high.

<!-- Note that the ATmega runs on 5V and therefore its pins' logical high voltage levels is 5V. -->

<!-- DONE: fix the above sentence -->

![arduino dock atmega headers](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-atmega-header.jpg)

### The MicroUSB Port

The MicroUSB Port is used to supply power to the Arduino Dock, which in turn supplies power to the Omega and the ATmega328P chip.

The MicroUSB Port receives 5V power and uses it directly to power the ATmega328P chip. The Dock comes equipped with a voltage regulator to step the voltage down to the required 3.3V for the Omega.


<!-- No-USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-3-No-USB-to-Serial.md'}
```


### DC Barrel Jack

The DC barrel jack may also be used to provide power to the Omega using a DC power adapter.

**Note that the Arduino Dock's DC barrel jack should only be used with 5V DC power supplies. If a higher voltage is used, your Omega and Arduino Dock have a high chance of being damaged!**


<!-- Reset Button -->
```{r child = '../shared/Hardware-Overview-Component-0-Reset-Button.md'}
```

### Micro-Controller Reset Button

<!-- [//]: # (issues a reset to the ATmega chip, give background on what that means in the Arduino Context) -->

In addition to the Omega's reset button, the Arduino Dock 2 comes with a microcontroller reset button. This button can be used to reset the ATmega chip whenever you'd like. This will **NOT** reset the Omega.

<!-- USB Port -->
```{r child = '../shared/Hardware-Overview-Component-5-Omega-USB-Port.md'}
```


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

### Mechanical Drawings

We've made available a detailed [diagram](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-D-ARD.PDF) of the dimensions and geometry of the Arduino Dock 2.

### Using the Dock

<!-- [//]: # (little overview of the special features of this dock) -->

The Arduino Dock 2 is loaded with features that allow you to use your Omega with the ATmega chip with ease. You can program or reset the micro-controller using the Omega's GPIOs, and even connect to the ATmega's serial port using the Omega's UART.

***More articles coming soon!***


<!-- TODO:  These articles are to be part of the Arduino Kit guides, and we will link to them when the guides are ready. -->
### Programming the Arduino Micro-Controller

Follow the steps in our [Flashing the Microcontroller](#flash-arduino-dock-wirelessly) to learn how to upload sketches (programs) to the Arduino micro-controller onboard the Arduino Dock.

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
