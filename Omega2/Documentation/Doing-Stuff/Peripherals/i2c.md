---
title: Communicating with I2C Devices
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Communicating with I2C Devices {#communicating-with-i2c-devices}

<!-- // brief description of I2C (sometimes called TWI - two wire interface):
//  - has a master-slave architecture (many slaves, one master)
//    - Omega is configured to be the bus master
//    - each slave is identified with an address: sending a command to 0x27 will only be read by the device who's address is 0x27, other devices on the bus will ignore it
//    - great for having a bunch of different devices connected to the Omega (sensors, controllers, etc)
//  - based on using two lanes: one for clock(SCL) and one for data(SDA)
//    - read up about this but I think it generally works like this: the master generates the clock and then sends data on the data lane, or the master generates the clock and then requests data on the data lane, the device responds by driving the data lane -->

**I2C** (Inter-Integrated Circuit), sometimes called Two-Wire Interface, is a serial interface used to quickly and easily connect multiple devices to controllers and processors such as the Omega2. Examples of I2C devices include:

* Sensors, such as temperature, humidity, current
* Actuators, such as buzzers, lights
* Controllers, such as motors, relays

Communication is performed over 2 data lanes, each given their own pin on the Omega2:

* Clock (SCL) - Signals when data is being transferred
* Data (SDA) - Carries the data to be transferred

The I2C bus uses a **master-slave** architecture, which means the following:

* Bus **masters** are devices that are in control of when and to whom they send and receive data.
    * Masters send commands which include the address of the slave who should receive it.
    * When using I2C with the Omega2, the Omega2 is configured to be the only bus master.
* Bus **slaves** are devices that respond to masters when they receive a command addressed to them.
    * Each slave is identified with a hexadecimal address (eg. `0x27`).
    * Slaves will safely ignore commands not addressed to them.
* Masters and slaves operate in either of two modes:
    * **transmit** - sending data
    * **receive** - receiving data

If you're interested in the full details, see the [Wikipedia article on I2C](https://en.wikipedia.org/wiki/I%C2%B2C) for more.

### The Omega & I2C

// all i2c interactions on the omega are done using the sysfs /dev/i2c-0 file, everything mentioned in this article uses this sysfs file to communicate with the hardware I2C controller (useful background knowledge)

#### On the Hardware

The I2C pins (SCL and SDA) on the Omega2 and Expansion Dock are highlighted below.

![i2c-pins-omega2](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/i2c-pins-omega2.jpg)

![i2c-pins-exp-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/i2c-pins-exp-dock.jpg)

**Note: On some older Expansion Dock units, `SCL` is labelled as pin `20`, and `SDA` is labelled as pin `21`.**

### Controlling I2C Devices from the Command line

<!-- // TODO: add a little intro the the two command line utilities that we'll be using. note that i2c communication with these tools is register based. Have a sentence or two explaining what resisters are and how we use them -->

We'll be using two command line utilities, `i2cget` and `i2cset`, to work with I2C devices. These tools work by accessing data stored in **registers** on the device. A register is a location in a device's memory. When reading from/writing to an I2C device, you need to specify the register on the device that you want to access.

<!-- #### Detecting I2C devices -->
<!-- // leave this out for now, there's a bug that makes this useless -->

#### Reading a Byte

`i2cget` is used to read a value of a specific register on an I2C device. A typical command reads as follows:

```bash
i2cget -y 0 <DEVICE ADDRESS> <REGISTER>
```

The options are explained below:

* `-y` - skip the prompt for confirmation from the `i2cget` command
* `0` - the I2C bus to use. The Omega2 has one I2C bus, denoted as bus `0`.
* `<DEVICE ADDRESS>` - the address of the slave device, eg. `0x40`
* `<REGISTER>` - the register on the slave to read from, eg. `0x00`

For example, let's say we have an I2C temperature sensor at address `0x40` acting as a slave with the following registers:

* `0x00` - stores temperature in degrees Fahrenheit
* `0x01` - stores temperature in degrees Celsius

Let's say we're interested in reading the temperature in degrees Fahrenheit. We do this using the following command:

```bash
i2cget -y 0 0x40 0x00
```

And it returns `0x48`, which is 72 in decimal (22 degrees Celsius). That's some nice weather outside!

#### Writing a Byte

`i2cset` is used to set the value of a register on a target I2C device. A typical command looks like this:

```bash
i2cset -y 0 <DEVICE ADDRESS> <REGISTER> <VALUE>
```

The options are explained below:

* `-y` - skip the prompt for confirmation from the `i2cget` command
* `0` - the I2C bus to use. The Omega2 has one I2C bus, denoted as bus `0`.
* `<DEVICE ADDRESS>` - the address of the slave device, eg. `0x27`
* `<REGISTER>` - the register on the slave to write to, eg. `0x00`
* `<VALUE>` - the value to write, eg. `0x33`

Let's say we have an I2C room light controller at address `0x27` acting as a slave with the following registers:

* `0x00` - living room, `0` for OFF, `1` for ON
* `0x01` - dining room
* `0x02` - bedroom

For example, to turn the living room lights ON and the dining room lights OFF, we would run these commands:

```bash
i2cset -y 0 0x27 0x00 0x01          # living room lights ON
i2cset -y 0 0x27 0x01 0x00          # dining room lights OFF
```

<!-- #### Going further
// TODO: look into the command line options for writing two bytes at a time -->

#### The Omega Expansions

Some of our Expansions use I2C to communicate with the Omega. To learn more about how to work with them, take a look at the guides below:

* [Relay Expansion](#using-relay-expansion)
* [PWM Expansion](#using-pwm-expansion)
* [OLED Expansion](#using-oled-expansion)

### Moving Beyond the Command line

#### I2C using Python

We've developed an I2C Python module that you can import into your apps. For all the details, see the [I2C Python Module](#i2c-python-module).

##### Example - Controlling an I2C LCD Display

This tutorial is brought to you by [Matthew Ogborne](https://github.com/moggiex) and [David Stein](https://github.com/Fires04). Thanks guys!

First find or buy an I2C LCD display. They can be found online on Amazon or Ebay.

Install the following packages on your Omega2:

```bash
opkg update
opkg install git git-http python-light pyOnionI2C
```

Next, download David's library for the LCD display:

```bash
cd /root
git clone https://bitbucket.org/fires/fireonion_i2c_lcd
```

Wire up your LCD display as shown below:

| Omega Pin | LCD Display Pin |
|-|-|
| 5V | 5V |
| GND | GND |
| 20 | SCL |
| 21 | SDA |

Navigate to the `src` directory:

```bash
cd fireonion_i2c_lcd/src
```

Run the command:

```bash
python lcd.py
```

Now you should see sample text on your LCD. You can edit `lcd.py` to change the displayed text. You can also import the whole library into your own Python project!

![i2c-lcd](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/i2c-python-lcd-output.jpg)

For more details, see [David's blog post](http://davidstein.cz/2016/03/13/onion-io-i2c-lcd-16x220x4-backpack-library/).

#### I2C using C & C++

We have also developed an I2C library for C and C++. For all the details, see the [I2C C Library](#i2c-c-library)

<!-- // introduce that onion has developed an I2C library for C and C++
// link to reference article on onion i2c c lib -->
