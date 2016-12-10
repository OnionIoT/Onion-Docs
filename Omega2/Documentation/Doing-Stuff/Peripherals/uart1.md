---
title: Communicating with Serial Devices
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

## Communicating with Serial Devices

// Introduce the uart as a serial communication protocol, talk about that the Omega now has two UARTs, UART0 is largely for outputting the Omega's command line, and UART1 can be used to communicate with other devices

// mention that this article will be explaining the uart a little bit, showing you where it is on the hardware, how to use the uart from the command line, how to use the screen command with the uart, how to use the uart thru Python

### What is a UART?

// describe what a UART is and how devices can use it to communicate, no master-slave architecture, make sure to cross Tx->Rx and Rx->Tx
// introduce the following:
//  - baud rates
//  - what 8n1 means
//    - 8: number of data bits
//    - n: no stop bit
//    - 1: 1 parity (look this up)

### On the Hardware-Overview
highlight the UART1 pins on both the Omega and the Expansion Header


### Using the Command Line

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

// the above is all well and nice, but using the screen command, we can actually have back and forth communication

#### Installing Screen

// will most likely need to install screen, give em the usual


#### Running `screen`

// the command is: `screen /dev/ttyS1 <BAUD RATE>`
// will show a new screen (ha-ha) that will print any incoming data, you can type and press enter to send commands

// give an example of one Omega's UART1 connected to another Omega's UART0, can login through to the other Omega's serial Terminal

### Using Python

// There's a python module for interacting with serial ports python-pyserial, read up on the Documentation

#### Installing the module

// should be `opkg install pyton-pyserial`

#### Using PySerial

// give a small example example script on how to use the UART
// potential example: Omega A's UART1 is connected to Omega B's UART0, can send commands from Omega A and find out stuff about Omega B, the hostname, mac addr, that sort of thing, iunno
