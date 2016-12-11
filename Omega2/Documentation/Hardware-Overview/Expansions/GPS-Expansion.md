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

### The Hardware

// Overview of the hardware
//  - the ublox Chip
//  - the antenna
//  - usb connection

#### Connecting to a Dock

// plugged into the USB Port
// have photos of it plugged into the Exp dock, power dock, minidock, and arduino dock 2

#### At a Glance

// illustration - make sure its GPS v2

#### The ublox Chip and Antenna

// mention the ublox chip model
// mention that the ublox chip translates the information received from the antenna into NMEA messages the omega can understand - maybe include a link to NMEA documentation

#### USB Port

// means of powering the Expansion and communicating with the Omega



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
