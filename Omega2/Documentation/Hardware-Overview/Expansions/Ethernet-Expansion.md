---
title: Ethernet Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---

## Ethernet Expansion

<!-- // intro on the ethernet expansion - allows the omega to be wired as well as wireless -->

The Ethernet Expansion adds an Ethernet port to the Omega. With this expansion you can add reliable, wired network access to your Omega, without affecting its wireless capabilities. It also has the added bonus of being able to reflash an Omega whose software is corrupted ("bricked").



### The Hardware

#### Connecting to a Dock

<!-- // plugged into the expansion Header -->
<!-- // TODO: have photos of it plugged into the Exp dock, power dock, and arduino dock 2 -->

The Ethernet Expansion is to be plugged into an Expansion Header. These headers can be found on the Expansion Dock, Power Dock, and the Arduino Dock 2. In addition to that, the Ethernet Expansion can also be plugged into most other Expansions.

>*NOTE: The Ethernet Expansion does not plug in ALL THE WAY like the Omega does. The pin will be exposed at the top (refer to image above)*

<!-- // mention that other expansions can be safely stacked on top of it -->

This Expansion features an Expansion Header, so other expansions can be safely stacked on top of it.

#### At a Glance

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/ethernet-expansion-illustration.jpg)

#### Connecting an Ethernet Cable

<!-- // instructions and photos of connecting and disconnecting an ethernet Cable -->

Your Omega will automatically discover when an Ethernet cord is connected to your Ethernet Expansion. If you've got a terminal open with a serial connection to the Omega you'll see the following output when you plug in an Ethernet cord:

```
root@Omega-2757:/# [  473.834234] rt3050-esw 10110000.esw: link changed 0x01
```

and when you unlpug the ethernet cord you'll see this:

```
[  491.625850] rt3050-esw 10110000.esw: link changed 0x00
```

To connect an Ethernet cord to your Ethernet Expansion, properly align the Ethernet plug with the jack, and insert. It will click in place.

In order to disconnect the Ethernet cable you'll need to press down on the cord in order to release the lock mechanism (the click sound was this mechanism).


## Using the Ethernet Expansion

<!-- TODO: This article already exists under Documentation/connectivity/ethernet-expansion.md, where is the preferred location for these articles? -->

<!-- // providing wired, ethernet connectivity to the omega extends its networking capabilities -->

The Ethernet Expansion is a great tool to extend the networking capabilities of your Omega by providing another method of connecting to the internet.

To learn more about using the Ethernet Expansion check out our guide to [using the Ethernet Expansion](#using-ethernet-expansion)

<!-- // introdocue and link to articles on -->
<!-- //  - connecting to a wired networking -->
<!-- //  - using the omega as a router -->
<!-- //  - using the omega as an ethernet bridge -->
