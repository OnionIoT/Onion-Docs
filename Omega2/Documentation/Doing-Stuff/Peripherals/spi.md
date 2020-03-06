---
title: Communicating with SPI Devices
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Communicating with SPI Devices {#communicating-with-spi-devices}

<!-- // The Omega2 has a built-in hardware SPI controller that can be used to communicate with SPI-enabled peripherals -->

The Omega has a built-in hardware SPI controller allowing it to communicate with an SPI-enabled peripherals. The Omega only supports half-duplex SPI transmissions. To implement SPI communication, we recommend using the `python-spidev` module.

### What is SPI?

The Serial Peripheral Interface (SPI) is a four-wire synchronous communication protocol, largely used to connect microprocessors or microcontrollers to sensors, memory, and other peripherals.

The four signals are:

| SPI Signal | Meaning                                                       |
|------------|---------------------------------------------------------------|
| SCK        | System Clock                                                  |
| MOSI       | Master Out, Slave In - Data sent from the Master to the Slave |
| MISO       | Master In, Slave Out - Data sent from the Slave to the Master |
| CS/SS      | Chip Select/Slave Select                                      |

SPI is a **synchronous** data bus, meaning that one of the lines is a clock, used to synchronize the bits being sent on the data lines.

The protocol is based on the **Master-Slave architecture**. The Master will generate the System Clock and the Slave Select signals. Each Slave requires its own Slave Select connection to the Master.

For more details on SPI, check out the [Wikipedia article](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus).


### The Omega & SPI {#omega-and-spi}

The Omega2's hardware SPI bus has one Slave Select line available, `CS1` (the Omega's flash storage occupies the `CS0`). The bus is registered to the operating system via the virtual device file `/dev/spidev0.1`. This is made possible with `sysfs`, a pseudo-file system that holds information about the Omega's hardware in files, and lets the user control the hardware by editing the files.

Here's what the numbers mean:

* `0` is the Omega2's **SPI bus number**.
* `1` indicates the **device ID**. This corresponds to the slave connected to the Omega2's `CS1` pin.

When using this bus, you will need to specify these particular numbers. Keep these handy for the sections below!

<!-- // mention that device 0 is the flash memory used by the omega -->
On a side note, device `0` (`CS0`) is connected to the flash memory used by the Omega.

#### On the Hardware

The SPI pins on the Omega2 and Expansion Dock are shown below.

![spi-pins-omega2](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/spi-pins-omega2.jpg)

![spi-pins-exp-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/spi-pins-exp-dock.jpg)

### Using Python

To interact with SPI devices, we recommend using Python and the `spidev` module. The `spidev` module provides series of functions that implement SPI communication through the Linux device interface. It also provides an Omega2-specific `xfer3` function that implements a half-duplex write-then-read SPI transmission. 

For more information on installing and using the `spidev` module, please see the instructions in our [`python-spidev` GitHub repo](https://github.com/OnionIoT/python-spidev). See the [Installing and Using Python article](#installing-and-using-python) for more details on using Python with the Omega2.

> Under the hood, the Python `spidev` module uses the spidev linux kernel driver in C

### Using C Programs

It's also possible to write C programs that make use of the spidev linux kernel driver to implement SPI communication. 

Useful resources:

* Our documentation article about [Cross-compiling C programs](#cross-compiling)
* General information about the [spidev linux kernel driver](https://www.kernel.org/doc/Documentation/spi/spidev)
* A good example of the [spidev driver can be used in a C program](http://linux-sunxi.org/SPIdev#In_the_user_space)
* For an idea on implementing a half-duplex write-then-read, see how [our `xfer3()` function from the Python spidev module was written](https://github.com/OnionIoT/python-spidev/blob/master/src/spidev_module.c#L575)
