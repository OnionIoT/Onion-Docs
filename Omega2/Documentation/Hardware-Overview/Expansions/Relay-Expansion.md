---
title: Relay Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Relay Expansion {#relay-expansion}

The Relay Expansion allows you to control two other independent, external circuits using the Omega. These circuits are safely isolated from the Omega and can be either lower or higher voltage; see the maximum ratings in the table in the article below for more details.

>Never exceed the maximum electrical ratings of the relays or you risk damaging the Relay Expansion, Omega, or even starting a fire.

This Expansion communicates with the Omega using the I2C protocol. If you're curious, check out the [article on I2C](#communicating-with-i2c-devices).

The Relay Expansion is designed so you can stack multiple Relay Expansions onto the same Omega. Each board comes with a small switch used to give it a unique address, and up to 8 Relay Expansions can be controlled by a single Omega. This means you can control up to 16 external circuits and devices!

<!-- TODO: The above sentence needs to also mention that you can stack any expansion on top. Or that needs to be specified in the connecting to a dock section. -->

### The Hardware

<!-- TODO: Add a spiel about the fact that there are two relays or whatever. -->

The Relay Expansion comes with 2 electromagnetic relays with screw terminals.

#### Connecting to a Dock

<!-- // plugged into the expansion Header
// have photos of it plugged into the Exp dock, power dock, and arduino dock 2

// mention that other expansions can be safely stacked on top of it -->

You can use the Relay Expansion with the Expansion Dock, Power Dock, or Arduino Dock R2. You can also safely stack other Expansions on top of it.

![expansion-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-expansion-dock.jpg)

![power-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-power-dock.jpg)

![arduino-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-arduino-dock.jpg)

To connect the Relay Expansion to the Omega, plug it into the Expansion Header on the Expansion Dock.

#### At a Glance

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-expansion-illustration.jpg)

#### The Relays

Relays are simple switches that can open (disconnect) and close (connect) circuits. Take the following example circuit:

![example-circuit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-example-circuit.jpg)

In the above diagram, the function of the Switch can be performed by a single relay.

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

The green block on the board is called the *terminal block*. It houses 4 terminals, 2 for each relay, into which you plug your circuit wires. To secure the wires inside the terminal block, screw them down with a small flathead screwdriver.

![screw-terminals](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-screw-terminals.jpg)

#### The Address Switch

The address switch allows you to change the I2C address of the board. This is needed to differentiate multiple Relay Expansions from each other when connected to the same Omega. 

![address-switch](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-address-switch.jpg)

It has 3 switches that can be turned either ON or OFF. See the following table for the address values:

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

### Using the Relay Expansion

Consider this LED circuit:

![LED Circuit Diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/relay-example-circuit.png)

We can build this circuit without the switch:

![LED Circuit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/relay-circuit-1.jpg)

Next, we will add the Omega and Relay Expansion to act as the switch:

![Omega + Relay Exp + LED circuit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/relay-circuit-2.jpg)

The positive lead of the battery pack is connected to the port labelled `IN` on the Expansion. A jumper wire is connected from the `OUT` port back to the circuit. Since the Relay is `OFF`, the switch is off and no current is passing through the LED:

![Relay Exp connection close-up](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/relay-circuit-3.jpg)

When we turn the relay on, it acts as a closed switch, allowing current to flow through the LED:

![Omega + Relay Exp + LED circuit on](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/relay-circuit-4.jpg)

The Relay Expansion can be used to control almost any type of external circuit, such as a lamp, coffee maker, or even your garage door!

Read our [guide to using the Relay Expansion](#using-relay-expansion) to learn how to control it using software.
