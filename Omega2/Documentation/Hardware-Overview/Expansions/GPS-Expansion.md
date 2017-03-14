---
title: GPS Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 5
---

## GPS Expansion {#gps-expansion}

<!-- // intro to the gps expansion - has a ublox chip and an antenna that allows you to pickup information from GPS satellites
// communicates with the Omega serially through USB -->

The GPS Expansion for the is a USB-based expansion that allows your Omega to pinpoint its location using both GPS as well as China’s Beidou satellite positioning systems. It comes with an on-board GPS antenna as well as a built-in u.FL connector to attach your own antenna. It features:

* 1.8m accuracy
* 66 search channels
* 22 tracking channels
* -165 dBM sensitivity
* up to 10Hz update rate.

### The Hardware

<!-- // Overview of the hardware
//  - the ublox Chip
//  - the antenna
//  - usb connection -->


The GPS Expansion uses a u-blox GPS receiver which features a high performance u-blox 6 positioning engine. This chip sends the GPS data to the Omega via the USB connection. Simply plug in your GPS expansion into a Dock to get started.

You can even change the antenna by disconnecting the included antenna and connecting your own to the onboard u.FL connector.

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/gps-expansion-illustration.png)

### Connecting to a Dock

<!-- // plugged into the USB Port -->
<!-- // have photos of it plugged into the Exp dock, power dock, minidock, and arduino dock 2 -->

The GPS Expansion plugs into a Dock with a USB port. You can also connect a USB hub to a Dock's USB port and connect the GPS Expansion into the hub.


![gps expansion dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/gps-top-expansion-dock.jpg)

![gps power dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/gps-top-power-dock.jpg)

![gps arduino dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/gps-top-arduino-dock.jpg)

![gps mini dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/gps-top-mini-dock.jpg)


This is one of the few Expansions that doesn't require Expansion headers, so you can even use it with the Mini Dock if you'd like!

### The ublox Chip and Antenna

<!-- // mention the ublox chip model -->
<!-- // mention that the ublox chip translates the information received from the antenna into NMEA messages the omega can understand - maybe include a link to NMEA documentation -->

The ublox chip used on the GPS expansion is the **ublox NEO-6M**. This chip translates the information received from the antenna into NMEA messages that the Omega can understand.

>NMEA is the National Marine Electronics Association protocol. If you're interested in marine electronics you can read the [Wikipedia article on the latest NMEA protocol](https://en.wikipedia.org/wiki/NMEA_2000).

For more on the ublox chip, see the [ublox chip datasheet][1].

<!-- ### u.FL Connector -->
<!-- TODO: write this section: the u.fl connector allows you to use an alternative GPS antenna. Simply unplug the existing antenna and plug in the new one. -->

### USB Connector

<!-- // means of powering the Expansion and communicating with the Omega -->

The USB connector serves two purposes. By plugging the Expansion into a Dock's USB port we power the GPS Expansion, and we provide a means of communication between the Omega and the Expansion.

<!--- TODO: LINK update gps exp mech drawing link when finished
### Mechanical Drawings

We've made available a detailed [diagram](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-E-GPS.PDF) of the dimensions and geometry of the GPS Expansion.
-->

### Using the GPS Expansion

<!-- // give an example of how this can be used, and when it would be useful (tracking gps location on a roadtrip or something) -->

You can use the GPS Expansion to create some cool geo-data projects with your Omega! For example, you can try your hand at creating a navigation system using the GPS Expansion with the OLED Expansion. Or for a simpler project, you can create a treasure hunt game that alerts the user when they're in the vicinity of an item for a children's party.

You can learn more about this Expansion by reading our article on [how to use the GPS Expansion](#using-gps-expansion)

<!-- // point them to the article on using the GPS Expansion -->
<!-- // this article should include: -->
<!-- //  * explanation of ogps -->
<!-- //    * installation -->
<!-- //    * usage of ogps (which is a ubus function call) -->
<!-- //  * give example of reading the raw NMEA messages (and how using ogps is totally better) -->

<!-- // note: no longer need the 'Hardware Fix for Stability Issue' section, that as an Omega1 issue. Let's just mention that the Omega1 had issues with the GPS expansions and that the Omega2 is a-ok -->

<!-- // refer to the existing article for details: https://wiki.onion.io/Tutorials/Expansions/Using-the-GPS-Expansion -->

[1]: https://www.u-blox.com/sites/default/files/products/documents/NEO-6_DataSheet_(GPS.G6-HW-09005).pdf

<!--
### Technical Drawing

We have provided a [PDF](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/NAME.PDF) here.
-->
