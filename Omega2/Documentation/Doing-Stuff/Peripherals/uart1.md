---
title: Communicating with Serial Devices
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

## Communicating with Serial Devices {#uart1}

// Introduce the uart as a serial communication protocol, talk about that the Omega now has two UARTs, UART0 is largely for outputting the Omega's command line, and UART1 can be used to communicate with other devices

A universal asynchronous receiver/transmitter (UART) is a device used for serial communication. The Omega comes with two UART devices: UART0, and UART1. UART0 is largely used for outputting the Omega's command line, and UART1 is free to communicate with other devices.

This article will cover what the UART does, where it is on the hardware, and using the UART on the Omega.

// mention that this article will be explaining the uart a little bit, showing you where it is on the hardware, how to use the uart from the command line, how to use the screen command with the uart, how to use the uart thru Python

### What is a UART?

A UART is used for serial communication between devices. UART has no master-slave architecture and allows you to set the transmissions speeds of your data. The transmission speed is known as the baud rate, and it represents the time spent holding each bit high or low. F

>If you've connected to the Omega via serial before you'll remember that we set the baud rate to 115200 bits-per-second, meaning that the time spent holding each bit high or low is 1/115200bps or 8.6µs per bit.

The UART on the Omega formats the data using the 8n1 configuration, in which there are 8 data bits, no parity bit, and one stop bit.

![uart data frame](../img/uart-data-frame.png)

The UART uses TX to transmit data, and RX to receive data. When communicating with other devices the TX on device A will send data to the RX on device B, creating a cross effect.

![cross tx rx](../img/uart-tx-rx-cross.png)

When setting up a serial connection always make sure to cross the RX and TX lines.

// describe what a UART is and how devices can use it to communicate, no master-slave architecture, make sure to cross Tx->Rx and Rx->Tx
// introduce the following:
//  - baud rates
//  - what 8n1 means
//    - 8: number of data bits
//    - n: no stop bit (NO PARITY)
//    - 1: 1 parity (look this up --  it's actually 1 stop bit)

### On the Hardware-Overview
<!-- highlight the UART1 pins on both the Omega and the Expansion Header -->

![pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/Omega-2-Pinout-Diagram.png)

Pins 12 and 13 are used for UART0. These are primarily used for the command line on the Omega. The UART1 uses pins 45 and 46. These are labelled as TX1 and RX1 to signify that they are used for UART1.


### Using the Command Line
<!-- TODO: Couldn't get sending and receiving data to /dev/ttyS1 to work, could i get some help?` -->
// will be using the `/dev/ttyS1` interface and some command line tools to communicate

// for this section: need to research how echo and cat know the baud rate...

#### Sending Data

// simple as piping things to `/dev/ttyS1`:
//  echo "my message" > /dev/ttyS1

#### Receiving Data

// reading from the uart device
//  cat /dev/ttyS1
// and it will print the received data


### Using the Screen Command

The above method is a great way to introduce using UART, but it's not all that practical. By introducing `screen` we can begin to communicate back and forth between our Omega and connected devices.

#### Installing Screen

// will most likely need to install screen, give em the usual

You'll need to start by installing `screen` using the Omega's package manager `opkg`. We'll start by updating our list of packages:

```
opkg update
```

Now we'll install screen:

```
opkg install screen
```

And now you're ready to use screen with the UART!


#### Running `screen`

To use the UART with `screen` enter the following command:

```
screen /dev/ttyS1 <BAUD RATE>
```

This will show a new screen that will print any incoming data, and you can type and press enter to send commands.

// the command is: `screen /dev/ttyS1 <BAUD RATE>`
// will show a new screen (ha-ha) that will print any incoming data, you can type and press enter to send commands

// give an example of one Omega's UART1 connected to another Omega's UART0, can login through to the other Omega's serial Terminal

### Using Python

// There's a python module for interacting with serial ports python-pyserial, read up on the Documentation

You can use Python in order to communicate serially via the UART. The module to accomplish this is `PySerial` which can be installed using `opkg`.




#### Installing the module

// should be `opkg install pyton-pyserial`

You'll need to have Python or Python-light installed in order to continue. If you've installed the full version of Python you will already have PySerial.

>You can read our guide to [installing and using Python on the Omega](#using-python) for more information.

First update `opkg`:

```
opkg update
```

And then install `python-pyserial`:

```
opkg python-pyserial
```

You'll now be able to use PySerial

#### Using PySerial

You can use PySerial by connecting a device to your Omega's USB type-A port. For more on the usage of PySerial you can read the [PySerial documentation](https://pythonhosted.org/pyserial/shortintro.html).

// give a small example example script on how to use the UART
// potential example: Omega A's UART1 is connected to Omega B's UART0, can send commands from Omega A and find out stuff about Omega B, the hostname, mac addr, that sort of thing, iunno
