## Onion Omega2+ {#omega2p}

The Omega2+ is the upgraded version of the Omega2. It comes packed with built-in Wi-Fi, a MicroSD slot, a Linux Operating System, and a powerful processor, among other things.

### The Omega2 at a Glance

![omega2Plus](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2p-illustration.png)

| Omega2+ Specs  | |
| :-------------: | :-------------:  |
| Processor | 580MHz MIPS CPU  |
| Memory | **128MB** Memory  |
| Storage | **32MB** Storage  |
| USB | USB 2.0  |
| MicroSD Slot | **Yes**  |
| WiFi adapter | b/g/n Wi-Fi  |
| GPIOs | 18  |
| PWM | 2  |
| UART | 2  |
| I2C | 1  |
| SPI |  1   |
| I2S | 1  |

### Processor Datasheet

The datasheet for the Omega2+ processor can be found here: [Mediatek MT7688 Datasheet](https://github.com/OnionIoT/Onion-Docs/raw/master/Omega2/MT7688_Datasheet_v1_4.pdf)

### The Pins

Take a look at the [Using the GPIOs](https://docs.onion.io/omega2-docs/using-gpios.html#important-special-gpios) article to learn more about the Omega's GPIOs, multiplexing GPIO functionality, and the behaviour and requirements of the Omega's special GPIOs.

![pinout](https://github.com/OnionIoT/Onion-Media/raw/master/Pinouts/Omega2.png)

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

The MircoSD card slot can be used to expand the Omega2+'s storage capacity to ridiculous levels. If 32MB is a problem for you, you can now hit it with a tactical warhead. To help you get started, there's a guide on [using a MicroSD card](#using-a-microsd-card).

The slot can be found at the bottom of the Omega2+. To physically mount a MicroSD card, slide it into the slot, push it down until it clicks. If it pops all the way back up, just do it again, and it should stay.

![MicroSD Card Slot Location](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2p-microsd-slot.jpg)


<!-- wifi antenna -->
```{r child = '../shared/Hardware-Overview-Component-92-Omega-smt-antenna.md'}
```

<!-- u.fl connector -->
```{r child = '../shared/Hardware-Overview-Component-93-Omega-ufl-connector.md'}
```


<!--  leave this out for now -->
### Mechanical drawing

We've made available a detailed [diagram](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-O2.PDF) of the dimensions and geometry of the Omega2+.
