## Onion Omega2+

The Omega2+ is the upgraded version of the Omega2. It comes packed with built-in Wi-Fi, a MicroSD slot, and a powerful processor among other things.

### The Omega2 at a Glance

![omega2Plus](../img/omega-2p-pic.png)

| Omega2+ Specs  | |
| :-------------: | :-------------:  |
| Processor | 580MHz MIPS CPU  |
| 128MB Memory | 128MB Memory  |
|  32MB Storage | 32MB Storage  |
| USB | USB 2.0  |
| MicroSD Slot | Yes  |
| WiFi adapter | b/g/n Wi-Fi  |
| GPIOs | 15  |
| PWM | 2  |
| UART | 2  |
| I2C | 1  |
| SPI |  1   |
| I2S | 1  |

### The Pins

![pinout](../img/omega-2-pinout-diagram.png)

<!-- LATER: include section on the 50pin connector -->


### The Operating system

The Omega2+ runs the Linux Embedded Development Environment (LEDE) operating system, a distribution based on OpenWRT. This distribution gives the Omega2+ access to the OPKG functionality, allowing you to download packages to enhance your experience.

### The Omega LED

The Omega LED is a great tool for communicating information with a user. It notifies you when your Omega is off, booting, and on.

The Omega LED uses GPIO44, and can be programmed to do a number of cool things. You can learn more about the LED in [the article on how to use the Omega's LED](../../Doing-Stuff/The-Omega-LED)

### Reset GPIO

The Omega's can be reset using GPIO38. When plugged into a Dock (e.g. Expansion Dock), this GPIO gives various functionality to the reset button found on docks. For example, a quick button press triggers the reboot command, whereas holding the button for longer than 7 seconds will trigger a factory reset command.

<!--  leave this out for now -->
<!--  ## MicroSD Card Slot -->

<!--  little explanation of the MicroSD Slot -->
<!--  images & explanation of proper sd card insertion and removal -->

<!-- batch2: ## Antenna and U.FL Connector -->

<!--  Description of SMT antenna used on the Omega, mention that it's directional, have a diagram of the directionality -->
<!--  Describe that U.FL connector can be used to connect other, bigger antennas -->

<!--  leave this out for now -->
<!-- ## Mechanical Drawing -->

<!--  insert mechanical drawing image, link to repo -->
