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


<!-- operating system -->
```{r child = '../shared/Hardware-Overview-Component-90-Omega-operating-system.md'}
```

### The Omega LED {#omega2p-hw-omega-led}

<!-- omega led content -->
```{r child = '../shared/Hardware-Overview-Component-91-Omega-omega-led-content.md'}
```


<!-- reset gpio -->
```{r child = '../shared/Hardware-Overview-Component-92-Omega-reset-gpio.md'}
```

### MicroSD Card Slot

The MircoSD card slot can be used to expand the Omega2+'s storage capacity to ridiculous levels. If 32MiB was a problem for you, you can now hit it with a tactical warhead. To help you get started, there's a guide on [using a MicroSD card](#using-a-microsd-card).

The slot can be found at the bottom of the Omega2+. To physically mount a MicroSD card, slide it into the slot, push it down until it clicks. If it pops all the way back up, just do it again, and it should stay.

![MicroSD Card Slot Location](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2p-microsd-slot.jpg)



<!-- batch2: ## Antenna and U.FL Connector -->

<!--  Description of SMT antenna used on the Omega, mention that it's directional, have a diagram of the directionality -->
<!--  Describe that U.FL connector can be used to connect other, bigger antennas -->

<!--  leave this out for now -->
### Mechanical drawing

We've made available a detailed [diagram](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-O2.PDF) of the dimensions and geometry of the Omega2+.
