---
title: Communicating with SPI Devices
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Communicating with SPI Devices {#communicating-with-spi-devices}

<!-- // The Omega2 has a built-in hardware SPI controller that can be used to communicate with SPI-enabled peripherals -->

The Omega has a built-in hardware SPI controller allowing it to communicate with an SPI-enabled peripherals. To implement SPI communication, the Omega has a C library, a Python module, and a command-line tool. This article will focus on the command line program, `spi-tool`.

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

The Omega2's hardware SPI bus has one Slave Select line available (`CS1`). The bus is registered to the operating system via the virtual device file `/dev/spidev32766.1`. This is made possible with `sysfs`, a pseudo-file system that holds information about the Omega's hardware in files, and lets the user control the hardware by editing the files.

Here's what the numbers mean:

* `32766` is the Omega2's **bus number**.
* `1` indicates the **device ID**. This corresponds to the slave connected to the Omega2's `CS1` pin.

When using this bus, you will need to specify these particular numbers. Keep these handy for the sections below!

<!-- // mention that device 0 is the flash memory used by the omega -->
On a side note, device `0` (`CS0`) is connected to the flash memory used by the Omega.

#### On the Hardware

The SPI pins on the Omega2 and Expansion Dock are shown below.

![spi-pins-omega2](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/spi-pins-omega2.jpg)

![spi-pins-exp-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/spi-pins-exp-dock.jpg)

### The Command Line tool

<!-- // jack from the existing article -->


The `spi-tool` command line utility allows the user to read and write single bytes from the Omega2's SPI bus. For the examples below, use the SPI device `bus number` and `device ID` listed in [the above section](#omega-and-spi).

This utility is not included by default in the Omega's firmware. To install it:
```
opkg update
opkg install spi-tool
```

Try running `spi-tool -h` for a print-out of the tool's usage.

#### Read a Byte {#spi-read-a-byte}

<!-- // jack from the existing article -->

To read a single byte from an SPI device, specify the memory address on the device:
```bash
spi-tool -b <BUS NUMBER> -d <DEVICE ID> [options] read <ADDRESS>
```

This command will print the byte read from the specified address on the SPI device.


**Arguments and Options**

The following arguments are required:

* `<BUS NUMBER>`, `<DEVICE ID>` - specified in [this section](#omega-and-spi).
* `address` - indicates the address from which to read on the SPI device.

Some useful options you can use are:

* `--frequency <Hz>` - Set max SPI frequency
* `--delay <us>` - Set delay after the last bit transfered before optionally deselecting the device before the next transfer, in microseconds.
* `--bpw <number>` - Set number of bits per word
* `--cs <gpio>` - Set GPIO for SPI CS signal
* `--3wire` - Slave In/Slave Out  signals shared
* `--no-cs` - No chip select signal
* `--cs-high` - Set chip select to active HIGH
* `--lsb` - Transmit Least Significant Bit first

**Examples**

Read a byte on bus `32766`, from device `1`, from address `0x11`:
```
root@Omega-ABCD:~# spi-tool -b 32766 -d 1 read 0x11
> SPI Read from addr 0x11: 0x81
```

Read a byte on bus `32766`, from device `1`; chip select is *active HIGH*; from address `0x00`:
```
root@Omega-ABCD:~# spi-tool -b 32766 -d 1 --cs-high read 0x00
> SPI Read from addr 0x00: 0xf8
```

Read a byte on bus `32766`, from device `1`; shared `Slave In/Slave Out` signals; from address `0xaf`:
```
root@Omega-ABCD:~# spi-tool -b 32766 -d 1 --3wire read 0xaf
> SPI Read from addr 0xaf: 0xbe
```


#### Write a Byte

<!-- // jack from the existing article -->
Along with reading, you can also use `spi-tool` to write to a memory address on an SPI device:

```bash
spi-tool -b <BUS NUMBER> -d <DEVICE ID> [options] write <ADDRESS> <VALUE>
```

**Arguments and Options**

* `<BUS NUMBER>`, `<DEVICE ID>` - specified in [this section](#omega-and-spi).
* `<ADDRESS>` - indicates the address from which to read on the SPI device.
* `<VALUE>` - the value to write.

The options are the same as in [Read a Byte](#spi-read-a-byte).

**Examples**

On bus `32766`, device `1`, `write` to address `0x12` a value of `0x42`:
```
root@Omega-ABCD:~# spi-tool -b 32766 -d 1 write 0x12 0x42
> SPI Write to addr 0x12: 0x42
```

On bus `32766`, device `1`;  set chip select to *active HIGH*; `write` to address `0x09` a value of `0xfa`:
```
root@Omega-ABCD:~# spi-tool -b 32766 -d 1 --cs-high write 0x09 0xfa
> SPI Write to addr 0x09: 0xfa
```

On bus `32766`, device `1`; shared `Slave In/Slave Out` signals; `write` to address `0xbf` a value of `0x01`:
```
root@Omega-ABCD:~# spi-tool -b 32766 -d 1 --3wire write 0xbf 0x01
> SPI Write to addr 0xbf: 0x01
```

### Moving Beyond the Command Line

<!-- // jack from the existing article -->
<!-- // make sure to include links -->


The `spi-tool` utility allows for some basic interaction with SPI devices using the command line. With interesting projects and use-cases, you will require additional interaction with the SPI device that might not be suited to the command line.

 Well, you're in luck! There is an Onion developed [C library](#spi-c-library) and [Python module](#spi-python-module) that gives you the flexibility to use SPI devices however you want!
