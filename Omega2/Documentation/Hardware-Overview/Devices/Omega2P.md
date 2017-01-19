## Onion Omega2+ {#omega2p}

The Omega2+ is the upgraded version of the Omega2. It comes packed with built-in Wi-Fi, a MicroSD slot, and a powerful processor among other things.

### The Omega2 at a Glance

![omega2Plus](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2p-illustration.png)

| Omega2+ Specs  | |
| :-------------: | :-------------:  |
| Processor | 580MHz MIPS CPU  |
| Memory | 128MB Memory  |
| Storage | 32MB Storage  |
| USB | USB 2.0  |
| MicroSD Slot | Yes  |
| WiFi adapter | b/g/n Wi-Fi  |
| GPIOs | 15  |
| PWM | 2  |
| UART | 2  |
| I2C | 1  |
| SPI |  1   |
| I2S | 1  |

### Processor Datasheet

The datasheet for the Omega2 Plus' processor can be found here: [Mediatek MT7688 Datasheet](https://labs.mediatek.com/fileMedia/download/9ef51e98-49b1-489a-b27e-391bac9f7bf3)

### The Pins

![pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/Omega-2-Pinout-Diagram.png)

<!-- TODO: include section on the 50pin connector -->


### The Operating system

The Omega2+ runs the Linux Embedded Development Environment (LEDE) operating system, a distribution based on OpenWRT. This distribution gives the Omega2+ access to the OPKG functionality, allowing you to download packages to enhance your experience.



The Omega LED is a great tool for communicating information with a user. It notifies you when your Omega is off, booting, and on.

The Omega LED uses GPIO44, and can be programmed to do a number of cool things. You can learn more about the LED in [the article on how to use the Omega's LED](#the-omega-led)

<!-- TODO: fix this link -->

### Reset GPIO

The Omega's can be reset using GPIO38. When plugged into a Dock (e.g. Expansion Dock), this GPIO gives various functionality to the reset button found on docks. For example, a quick button press triggers the reboot command, whereas holding the button for longer than 7 seconds will trigger a factory reset command.

### MicroSD Card Slot

<!--  little explanation of the MicroSD Slot -->
<!-- - explanation that the microsd card slot is on the underside of the omega2+ -->
<!-- - link to 'Using a MicroSD card' article, mention that it provides info on how to correctly use the slot and how to access data from the sd card -->

The MircoSD card slot can be used to expande the Omega2+'s storage capacity to ridiculous levels. If 32MiB was a problem for you, you can now hit it with a tactical warhead. A detailed guide on how to get it working can be found in the [Using a MicroSD Card](#using-a-microsd-card) article.

The slot can be found at the bottom of the Omega2+. To physically mount a MicroSD card, slide it into the slot, push it down until it clicks. If it pops all the way back up, just do it again, and it should stay.

![MicroSD Card Slot Location](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2p-sd-slot.jpg)



<!-- batch2: ## Antenna and U.FL Connector -->

<!--  Description of SMT antenna used on the Omega, mention that it's directional, have a diagram of the directionality -->
<!--  Describe that U.FL connector can be used to connect other, bigger antennas -->

<!--  leave this out for now -->
<!-- ## Mechanical Drawing -->
### Technical Drawing

We have provided a [PDF](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-O2.PDF) here.
<!--  insert mechanical drawing image, link to repo -->
