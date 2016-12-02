---
title: Omega2
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

# Onion Omega2

[//]: # (intro of the Omega2 IoT computer)
The Omega2 is the latest in development boards from Onion. It comes packed with built-in Wi-Fi

## The Omega2 at a Glance

[//]: # (TODO: have an illustration with labels)
![omega2](../img/omega-2-pic.png)

| Omega2 Specs  |
| :-------------: |
| 580MHz CPU |
| 64MB Memory |
|  16MB Storage |
| USB 2.0 |
| b/g/n Wi-Fi |
| 15 GPIO |
| 2 PWM |
| 2 UART |
| 1 I2C |
| 1 SPI |
| 1 I2S |

## The Pins

[//]: # (image of omega2 pinout)
![pinout](../img/omega-2-pinout-diagram.png)

[//]: # (LATER: include section on the 50pin connector)


## The Operating system

[//]: # (Linux operating system: LEDE blah blah)
The Omega2 runs the Linux Embedded Development Environment (LEDE) operating system, a distribution based on OpenWRT. This distribution gives the Omega2 access to the OPKG functionality, allowing you to download packages to enhance your experience.

## The Omega LED

[//]: # (Info on the Omega LED, state that it uses GPIO44, link to Omega LED article)

## Reset GPIO

[//]: # (mention the reset gpio (GPIO38) and the reboot and factory restore functionality when connected to a dock,)
GPIO38 is the reset gpio. When plugged into a dock (e.g. expansion dock), this gpio gives various functionality to the reset button found on docks. For example, a quick button press triggers the reboot command, whereas holding the button for longer than 7 seconds will trigger a factory reset command.

## Antenna and U.FL Connector

[//]: # (Description of SMT antenna used on the Omega, mention that it's directional, have a diagram of the directionality)
[//]: # (Describe that U.FL connector can be used to connect other, bigger antennas)

[//]: # (TO DO: ## Mechanical Drawing)

[//]: # (insert mechanical drawing image, link to repo)
