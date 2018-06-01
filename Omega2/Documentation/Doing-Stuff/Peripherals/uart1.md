---
title: Communicating with Serial Devices
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

## Communicating with Serial Devices {#uart1}


A **universal asynchronous receiver/transmitter (UART)** is a device used for serial communication between two devices. The Omega comes with two UART devices: `UART0`, and `UART1`. `UART0` is largely used for outputting the Omega's command line, and `UART1` is free to communicate with other devices.

This article will cover:

* what the UART does
* where it is on the hardware
* using the UART on the Omega
    * via the command line
    * via the `screen` command
    * using Python

Only **two devices** can communicate with each other per UART connection. This is different from other communication protocols, such as I2C or SPI, where there may be 3, 10, or many more devices connected to the same data lines.

### What is a UART?

A UART is used for serial communication between devices. UART has no master-slave architecture and allows you to set the transmissions speeds of your data. The transmission speed is known as the **baud rate**, and it represents the time spent holding each bit high or low.

>If you've connected to the Omega via serial before you'll remember that we set the baud rate to 115200 bits-per-second, meaning that the time spent holding each bit high or low is 1/115200bps or 8.6µs per bit.

The UART on the Omega formats the data using the **8N1 configuration**, in which there are **8** data bits, **No** parity bit, and **one** stop bit.

![uart data frame](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-data-frame.png)

#### Connecting UART Devices {#connecting-uart-devices}

The UART uses the TX line to **transmit** data, and RX to **receive** data. When communicating with other devices, the TX on device A will send data to the RX on device B and vice versa.

![cross tx rx](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-tx-rx-cross.png)

To set up a serial line connection between two devices:

1. Connect device A's `TX` line to device B's `RX` line.
1. Connect device A's `RX` line to device B's `TX` line.
1. Connect the two devices' `GND` lines together.

<!-- // describe what a UART is and how devices can use it to communicate, no master-slave architecture, make sure to cross Tx->Rx and Rx->Tx
// introduce the following:
//  - baud rates
//  - what 8n1 means
//    - 8: number of data bits
//    - n: no stop bit (NO PARITY)
//    - 1: 1 parity (look this up --  it's actually 1 stop bit) -->

### The Omega & UART

UART interactions on the Omega2 are done using the virtual device files `/dev/ttyS0` and `/dev/ttyS1`. This is made possible with `sysfs`, a pseudo-file system that holds information about the Omega's hardware in files, and lets the user control the hardware by editing the files.

#### On the Hardware
<!-- highlight the UART1 pins on both the Omega and the Expansion Header -->

The UART pins are highlighted on the Omega2, Expansion Headers, and Breadboard Dock below.

![pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-pins-omega2.jpg)

Pins `12` and `13` are used for `UART0`. These are primarily used for the command line on the Omega.

The `UART1` uses pins `45` and `46`. These are labelled as `TX1` and `RX1` to signify that they are used for `UART1`.

##### Expansion Dock & Power Dock

On the Expansion Dock and Power Dock, only `UART1` is broken out, shown below:

![uart-exp-power-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-pins-exp-dock.jpg)

On the Expansion Dock, `UART0` is connected to the on-board USB-to-Serial chip, providing [direct access to the Omega's command prompt](#connecting-to-the-omega-terminal-serial) with a USB connection.

##### Mini Dock

There are no GPIO headers on the Mini Dock so neither of the UARTs are available on the Mini Dock. However, just on like the Expansion Dock, `UART0` is connected to the on-board USB-to-Serial chip, providing [direct access to the Omega's command prompt](#connecting-to-the-omega-terminal-serial) with a USB connection.

##### Arduino Dock2

Both `UART0` and `UART1` are available on the Arduino Dock 2:

![uart-arduino-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-pins-arduino-dock.jpg)

The Arduino Dock connects the on-board microcontroller's serial port with `UART1` on the Omega, allowing direct communication between the microcontroller and the Omega. This is useful since it offers users the freedom to fully define and design the communication between the two devices.

##### Breadboard Dock

Both `UART0` and `UART1` are available on the Breadboard Dock:

![uart-breadboard-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-pins-breadboard-dock.jpg)

**IMPORTANT: The TX+/- and RX+/- pins are used for the *Ethernet Expansion*. Be careful not to connect your serial lines to these pins!**


### Using the Command Line

<!-- // will be using the `/dev/ttyS1` interface and some command line tools to communicate

// for this section: need to research how echo and cat know the baud rate...

^ apparently cat (and probably echo too) don't know about the baud rate, there should be some underlying utility (such as stty, but not installed by default) that takes care of those details for it -->

We'll be using some command line tools to write to (send) and read from (receive) data from `/dev/ttyS1` just as if it were any other file.

#### Sending Data

To send data to `UART1`, simply `echo` to `/dev/ttyS1` like so:

```bash
echo "my message" > /dev/ttyS1
```

This command will not display any text on the screen when entered, as you are simply writing to a file.

#### Receiving Data

To read data from `UART1`, simply run `cat` on it like so:

```bash
cat /dev/ttyS1
                                # waits for input data
```

This command will wait for and print any data received by the Omega until you exit the program (`Ctrl-C`).

#### Send and Print Received Data

The above commands don't do anything useful if you don't have any serial devices connected. However, you can simulate real serial communication by having the Omega **talk to itself!**

Simply connect the Omegas's `RX` and `TX` pins together as shown below; the `GND` connection is shared between the pins already.

![connect-rx-tx](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-omega-jumpered.jpg)

Now open two separate command line sessions on your Omega. It's easiest to connect via SSH in **two separate terminals** from your computer.

* In one terminal, run `cat /dev/ttyS1` to start reading the serial port.
* In the other, run `echo "hello world!" > /dev/ttyS1` to write a message to the serial port.

![two-terminals](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-echo-cat.png)

You will see your message appear in the terminal running `cat`. And that's the basics of serial communication on the Omega!

### Using the `screen` Command

The above method is a great way to introduce using UART, but it's not all that practical. By using the `screen` command, we can actually send commands to other Omegas or connected devices.

#### Installing Screen

<!-- // will most likely need to install screen, give em the usual -->

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

```bash
screen /dev/ttyS1 <BAUD RATE>
```

The terminal will go blank, and the command works the following way:

* Any keys or letters you type are immediately sent to the UART (ie. to the device connected to it)
* The terminal will immediately display any data received from the UART (ie. from the device connected to it)

To test this out using just 1 Omega, login to 2 separate SSH sessions as with the previous section. In both sessions, run the following example command:

```bash
screen /dev/ttyS1 9600
```

Both terminals will now go blank, waiting for your input.

Now start typing `hello world!` in the first terminal, and the words will start to appear in the second!

This can be also done with 2 Omegas by connecting their `TX1`, `RX1`, and `GND` pins as described in [Connecting UART Devices](#connecting-uart-devices).

#### Working With `screen` Sessions

* To detach from the `screen` session and leave it running so you can come back to it later, type `Ctrl-a` then `d`.
    * For detailed information on how to work with attaching and reattaching, see the [Screen User's Manual](https://www.gnu.org/software/screen/manual/screen.html).
* To kill (end) a session, type `Ctrl-a` then `k`.

Detaching from a `screen` process does not end it, ie. it is still running. If you start and detach from several `screen` processes, these will begin to tie up your Omega's memory.

To kill all `screen` processes, copy and paste the following command:

```bash
for pid in $(ps  | grep "screen" | awk '{print $1}'); do kill -9 $pid; done
```

This big command essentially does the following:

1. Get the list of running processes using `ps`
1. Pipe (send) it to the `grep` command and search for process names containing the word `screen`
    * `grep` is a powerful utility to analyze text using regular expressions.
1. Pipe those processes' information to `awk`, which outputs their process IDs
    * `awk` is another powerful utility that can perform
1. `kill` each of the process IDs corresponding to `screen`

<!-- // the command is: `screen /dev/ttyS1 <BAUD RATE>`
// will show a new screen (ha-ha) that will print any incoming data, you can type and press enter to send commands -->

<!-- // give an example of one Omega's UART1 connected to another Omega's UART0, can login through to the other Omega's serial Terminal -->

### Using Python

<!-- // There's a python module for interacting with serial ports python-pyserial, read up on the Documentation -->

You can use Python in order to communicate serially via the UART. The module to accomplish this is `PySerial` which can be installed using `opkg`.


#### Installing the Module

<!-- // should be `opkg install pyton-pyserial` -->

You'll need to have Python or Python-light installed in order to continue. If you've installed the full version of Python you will already have PySerial.

>You can read our guide to [installing and using Python on the Omega](#installing-and-using-python) for more information.

First update `opkg`:

```
opkg update
```

And then install `python-pyserial`:

```
opkg install python-pyserial
```

You'll now be able to use PySerial!

#### Using PySerial

You can use PySerial by connecting a device to your Omega's UART1. For more on the usage of PySerial you can read the [PySerial documentation](https://pythonhosted.org/pyserial/shortintro.html).

<!-- // TODO: batch5: give a small example example script on how to use the UART
// potential example: Omega A's UART1 is connected to Omega B's UART0, can send commands from Omega A and find out stuff about Omega B, the hostname, mac addr, that sort of thing, iunno -->
