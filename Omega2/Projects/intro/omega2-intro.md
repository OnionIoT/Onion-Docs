## Introduction to the Omega2 {#omega2-intro}

Wondering what exactly the Omega2 is all about? You've come to the right place!

#### What is an IoT Computer?


- what is IoT
- what is a connected hardware application
- what is an IoT computer used for

An IoT computer is a Linux computer designed specifically for use in building connected hardware applications.

What makes the Omega an IoT computer:

- small form factor
- power efficiency
- processing and networking capabilities
- flexibility that comes from running Linux  


- somewhere in-between an arduino and a raspi

#### History

Back in 2015, Onion launched the [original Omega](https://www.kickstarter.com/projects/onion/onion-omega-invention-platform-for-the-internet-of) on Kickstarter. The response was great! About 4,400 makers, coders, and tinkerers backed the campaign.

After listening to feedback from the community and taking a hard look at the state of IoT, Onion decided to launch the Omega2 in 2016. The Omega2 would have two models with different specs, be even lower cost than the original, and be fully FCC certified! The [Omega2 Kickstarter](https://www.kickstarter.com/projects/onion/omega2-5-iot-computer-with-wi-fi-powered-by-linux) was successful beyond belief, with over 16 thousand backers pledging to the campaign!

### Hardware

The Omega2 IoT Computer:

![omega2](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2-illustration.png)

The Specs:

|   | Omega2 | Omega2+ |
| :-------------: | :-------------:  | :-------------:  |
| Processor | 580MHz MIPS CPU  | 580MHz MIPS CPU  |
| Memory | 64MB Memory  | **128MB Memory**  |
| Storage | 16MB Storage  | **32MB Storage**  |
| USB | USB 2.0  | USB 2.0  |
| MicroSD Slot | No  | **Yes**  |
| WiFi adapter | b/g/n Wi-Fi  | b/g/n Wi-Fi  |
| Operating Voltage | **3.3V**  | **3.3V**  |

#### SoC

The Omega2 uses the Mediatek MT7688AN System-on-a-Chip (SoC). The processor is MIPS 24KEc, little-endian, 32-bit RISC core that operates at 580 MHz. For the truly curious, it has a 64 KB I-Cache and 32 KB D-Cache.

While this family of SoCs has traditionally been used in routers, this is very much a real CPU (and not a microcontroller) like you would find in a smartphone or laptop. It's just a different architecture (MIPS as opposed to ARM in smartphones or x86 in laptops & desktops) and operates at a lower frequency: about a quarter of the speed of a modern laptop CPU.

The lower clock speed and the MIPS architecture of the SoC lend to the Omega's low power consumption and low heat generation. This makes it ideal for use in the space and energy constrained use cases common for IoT applications.

| SoC | |
| :-------------: | :-------------:  |
| SoC | MediaTek MT7688AN |
| Architecture | MIPS 24KEc (RISC, 32-bit) |
| Endianness | Little |
| Clock Speed | 580 MHz |
| I-Cache | 64 KB |
| D-Cache | 32 KB |


#### Memory

The Omega2 comes with **128 MB** of memory and the Omega2+ with **256 MB**. Both models use DDR2 DRAM (Dynamic Random Access Memory).


#### Storage

While technically still memory, we refer to the Omega's onboard SPI flash memory as storage since it provides persistent, non-volatile memory that will not be destroyed when the Omega is powered off. The flash storage is where the Operating System (OS), programs, and all other files are stored. This flash storage is to the Omega what a hard-drive is to a laptop computer.

The Omega2 comes with **16 MB** flash storage while the Omega2+ has **32 MB**.


##### Micro-SD Card Slot

The Omega2+ additionally has a Micro-SD card slot on the underside that can be used to extend the storage available to the system. It is also possible to boot the Omega from the SD card.


#### Networking

The Omega2 has support for both wireless and wired networking.

##### WiFi

The Omega supports 2.4 GHz IEEE 802.11 b/g/n WiFi with a 150 Mbps PHY data rate. The antenna is 1T1R, meaning that it is used for both transmitting and receiving by virtue of time-multiplexing. By default, the Omega uses the on-board ceramic chip antenna. However, there is also a u.FL connector onboard for those who wish to use external antennas.

The Omega's WiFi interface supports hosting its own WiFi Access Point, connecting to existing WiFi networks, or both simultaneously.

##### Ethernet

The Omega supports 10M/100M wired ethernet network connectivity as well when used with a Dock and an Ethernet Expansion.


#### GPIOs

The Omega2 has twelve General Purpose Input/Output (GPIO) pins that can be controlled by the user.

##### GPIO Mapping

On the Omega, the GPIOs are laid out in two banks:

<!-- image of omega2 pinout -->
![pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/Omega-2-Pinout-Diagram.png)

##### Electrical Characteristics

// electrical characteristics

###### Digital Signal Voltage Level

```{r child = '../../Documentation/Doing-Stuff/GPIO-electrical-characteristics.md'}
```

###### Current Limits

// lookup from mt7688 datasheet


##### Serial Protocols

###### I2C

###### UART

###### SPI


### Software

// Operating system

// supported programming languages

// limitations

// mention web-based


### Docks

// explanation of Docks, why we need them, what they provide

#### Expansion Dock

- value proposition of expansion dock:
	- Expansion Header for using Expansions
	- Power the Omega using any Micro-USB
	- Serial terminal
	- usb broken out
- link to Docs Exp Dock article


#### Arduino Dock

- value proposition of expansion dock:
	- Expansion Header for using Expansions
	- On-board ATmega328P (from Arduino Uno) that can be programmed by the Omega
	- Form-factor allows for reuse of existing Arduino Shields
	- Power the Omega using any Micro-USB
	- usb broken out
- link to Docs Arduino Dock article


#### Power Dock

- value proposition of expansion dock:
	- Expansion Header for using Expansions
	- Power the Omega using any 3.7V LiPo battery
	- Charge the battery
	- Power the Omega using any Micro-USB
	- usb broken out
- link to Docs Power Dock article

#### Mini Dock

- value proposition of expansion dock:
	- Power the Omega using any Micro-USB
	- usb broken out
	- small footprint
- link to Docs Mini Dock article


### Expansions

- key to the Omega's modularity

#### Supported Docks

- expansion header required
- list the exp, pwr, and ard docks

#### Available Expansions

- listing of available expansions and their value propositions
