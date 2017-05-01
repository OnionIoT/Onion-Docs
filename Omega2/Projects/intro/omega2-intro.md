## Introduction to the Omega2 {#omega2-intro}

#### What is an IoT Computer?

- what is IoT
- what is a connected hardware application
- what is an IoT computer used for

An IoT computer is a Linux computer designed specifically for use in building connected hardware applications.

- small form factor
- power efficiency
- processing and networking capabilities
- flexibility that comes from running Linux  

- somewhere in-between an arduino and a raspi

#### History

// 2015: original Omega
// 2016: Omega2 at just $5, FCC certified

### Hardware

- operates at 3.3V

// TODO: labelled image of the Omega2

#### SoC

The Omega2 uses the Mediatek MT7688AN System-on-a-Chip (SoC). The processor is MIPS 24KEc, little-endian, 32-bit RISC core that operates at 580 MHz. For the truly <>, it has a 64 KB I-Cache and 32 KB D-Cache.

- this family of SoCs has traditionally been used in routers
- A real CPU - just a different architecture, runs much slower than a laptop computer

// table with the data


#### Memory

- DDR2 DRAM

The Omega2 comes with 128 MB of memory and the Omega2+ with 256 MB

// table comparing O2 and O2+


#### Storage

While technically still memory, we refer to the Omega's onboard SPI flash memory as storage since it provides persistent, non-volatile memory that will not be destroyed when the Omega is powered off. The flash storage is where the Operating System (OS), programs, and all other files are stored. This flash storage is to the Omega what a hard-drive is to a laptop computer.

The Omega2 comes with 16 MB flash storage while the Omega2+ has 32 MB.

// table comparing O2 and O2+

##### Micro-SD Card Slot

The Omega2+ additionally has a Micro-SD card slot on the underside that can be used to extend the storage available to the system. It is also possible to boot the Omega from the SD card.


#### Networking

- The Omega2 supports wireless and wired networking

##### WiFi

- 2.4 GHz
- 1T1R - same antenna is used for transmitting and receiving with time-multiplexing
- IEEE 802.11 b/g/n
- 150 Mbps PHY data rate
- AP mode, STA mode, simultaneous AP+STA

##### Ethernet

- available when used with a Dock and Ethernet Expansion
- 10M/100M

#### GPIOs

// list how many gpios are exposed on the omega

##### GPIO Mapping

// omega2 pinout

##### Electrical Characteristics

###### Digital Signal Voltage Level

// make a shared article with the docs using-gpios GPIO electrical ratings section

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
