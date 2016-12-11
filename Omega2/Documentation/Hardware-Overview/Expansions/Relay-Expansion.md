---
title: Relay Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Relay Expansion

The Relay Expansion allows you to control two other independent, external circuits using the Omega. These circuits are safely isolated from the Omega and so it does not matter whether they are lower or higher voltage.

This Expansion communicates with the Omega using the I2C protocol. If you're curious, check out the [article on I2C](#communicating-with-i2c-devices).

The Relay Expansion is designed so you can stack multiple Relay Expansions onto the same Omega. Each board comes with a small switch used to give it a unique address, and up to 8 Relay Expansions can be controlled by a single Omega. This means you can control up to 16 external circuits and devices!

### The Hardware

#### Connecting to a Dock

<!-- // plugged into the expansion Header
// have photos of it plugged into the Exp dock, power dock, and arduino dock 2

// mention that other expansions can be safely stacked on top of it -->

<!-- TODO: requires photos -->

To connect the Relay Expansion to the Omega, plug it into the Expansion Header on the Expansion Dock.

#### At a Glance

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-expansion-illustration.jpg)

#### The Relays

Relays are simple switches that can open (disconnect) and close (connect) circuits. Take the following example circuit:

![example-circuit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-example-circuit.jpg)

In the above diagram, the function of the Switch can be performed by a single relay. Now here comes the good part: the Relay Expansion comes with *two* of them!

The Relay Expansion uses two TE Axicom IM03 relay modules. Some of the specifications are shown below:

| Parameter                 | Specification             |
|---------------------------|---------------------------|
| Maximum Switching Voltage | 220VDC, 250VAC            |
| Current Rating            | 2A                        |
| Switching Power           | 60W, 62.5VA               |
| Switching Time            | Typical: 1ms Maximum: 3ms |

For full specifications, please see the [TE Axicom datasheet](http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Specification+Or+Standard%7F108-98001%7FV%7Fpdf%7FEnglish%7FENG_SS_108-98001_V_IM_0614_v1.pdf%7F4-1462039-1).

The relays channels are labelled below:

![relay-labels](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-expansion-channels-labelled.png)

#### The Screw Terminals

<!-- // instructions on how to connect wires to the screw Terminals
// include photos -->

<!-- TODO: take photos -->

#### The Address Switch

The address switch allows you to change the I2C address of the board. This is needed to differentiate multiple Relay Expansions from each other when connected to the same Omega. It has 3 switches that can be turned either ON or OFF. See the following table for the address values:

| Switch 1 | Switch 2 | Switch 3 | Binary Value |
|----------|----------|----------|--------------|
| OFF      | OFF      | OFF      | *000*        |
| OFF      | OFF      | ON       | *001*        |
| OFF      | ON       | OFF      | *010*        |
| OFF      | ON       | ON       | *011*        |
| ON       | OFF      | OFF      | *100*        |
| ON       | OFF      | ON       | *101*        |
| ON       | ON       | OFF      | *110*        |
| ON       | ON       | ON       | *111*        |

The I2C addresses corresponding to the different switch positions are shown below:

| I2C Device Address | Switch Binary Setting |
|--------------------|-----------------------|
| 0x27               | 000                   |
| 0x26               | 100                   |
| 0x25               | 010                   |
| 0x24               | 110                   |
| 0x23               | 001                   |
| 0x22               | 101                   |
| 0x21               | 011                   |
| 0x20               | 111                   |

## Using the Relay Expansion



<!-- // give an example of how this can be used and when it would be useful (turning on a lamp or something, some cool IoT example)
// reiterate that relays allow you to use the Omega to switch external circuits

// point them to the article on using the relay Expansion
//  this article should include:
    * An Example circuit
    * Controlling the Relays from the command line
    * Info on how the address switch configuration affects the command line call
    * Link to article on controlling relays from C/C++, python
// refer to existing doc for reference - should follow it closely -->
