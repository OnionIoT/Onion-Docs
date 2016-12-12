---
title: GPS Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 5
---

## GPS Expansion

// intro to the gps expansion - has a ublox chip and an antenna that allows you to pickup information from GPS satellites
// communicates with the Omega serially through USB

The GPS Expansion for the is a USB-based expansion that allows your Omega to pinpoint its location using both GPS as well as China’s Beidou satellite positioning systems. It comes with an on-board GPS antenna as well as a built-in u.FL connector to attach your own antenna. It provides up to 1.8m accuracy, 66 search channels, 22 tracking channels, -165 dBM sensitivity and up to 10Hz update rate.

### The Hardware

// Overview of the hardware
//  - the ublox Chip
//  - the antenna
//  - usb connection


The GPS Expansion uses the u-blox GPS receiver which features the high performance u-blox 6 positioning engine. This chip sends the GPS data to the Omega via the USB connection. Simply plug in your GPS expansion into a Dock to get started.

You can even change the antenna by disconnected the current antenna, and connecting your antenna to the onboard u.FL connector.

#### Connecting to a Dock

// plugged into the USB Port
// have photos of it plugged into the Exp dock, power dock, minidock, and arduino dock 2

#### At a Glance

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/gps-expansion-illustration.jpg)

#### The ublox Chip and Antenna

// mention the ublox chip model
// mention that the ublox chip translates the information received from the antenna into NMEA messages the omega can understand - maybe include a link to NMEA documentation

The ublox chip used on the GPS expansion is the ublox NEO-6M. This chip translates the information received from the antenna into NMEA messages that the Omega can understand.

>NMEA is the National Marine Electronics Associtation protocol. If you're interested in marine electronics you can read the [wikipedia article on the latest NMEA protocol](https://en.wikipedia.org/wiki/NMEA_2000).

For more on the ublox chip you can read the [ublox chip datasheet](https://www.u-blox.com/sites/default/files/products/documents/NEO-6_DataSheet_(GPS.G6-HW-09005).pdf)

#### USB Connector

// means of powering the Expansion and communicating with the Omega

The USB connector serves two purposes. By plugging the Expansion into a Dock's USB port we power the GPS Expansion, and we can communicate with the Omega.

### Using the GPS Expansion

// give an example of how this can be used, and when it would be useful (tracking gps location on a roadtrip or something)

// point them to the article on using the GPS Expansion
// this article should include:
//  * explanation of ogps
//    * installation
//    * usage of ogps (which is a ubus function call)
//  * give example of reading the raw NMEA messages (and how using ogps is totally better)

// note: no longer need the 'Hardware Fix for Stability Issue' section, that as an Omega1 issue. Let's just mention that the Omega1 had issues with the GPS expansions and that the Omega2 is a-ok


// refer to the existing article for details: https://wiki.onion.io/Tutorials/Expansions/Using-the-GPS-Expansion
