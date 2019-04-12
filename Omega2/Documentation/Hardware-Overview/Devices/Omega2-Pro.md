## Onion Omega2 Pro {#omega2-pro}

The Omega2 Pro is the next generation of our Omega2 and the most powerful IoT computer we’ve made yet. It is a standalone device – the processor, memory, gigabytes of storage, and Wi-Fi are all built-in, and it’s smaller than a breadboard.

![Omega2 Pro](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2-pro-iso-1.jpg)

### Getting Started with the Omega2 Pro

See our guide on getting started with the Omega2 Pro for all of the details on getting your device up and running: https://onion.io/omega2-pro-get-started

It also includes an [FAQ](https://onion.io/omega2-pro-get-started/#faq) that will answer any questions that may come up.

### The Omega2 Pro at a Glance

| Omega2 Pro Specs  | |
| :-------------: | :-------------:  |
| Processor | 580MHz MIPS CPU  |
| Memory | **128MB** RAM and **384MB** Swap File  |
| Storage | **8 GB** eMMC Storage  |
| Connectivity | 2.4 GHz b/g/n Wi-Fi  |
| Operating System | OpenWrt 18.06 Linux  |
| Storage | **8 GB** eMMC Storage  |
| Battery Support | LiPo battery management & JST-PH battery connector  |
| Antenna | 2 dBi directional chip antenna & U.FL connector for external antenna  |
| Dimensions | 73 mm x 44 mm  |
| | |
| USB | USB 2.0  |
| GPIOs | 18  |
| PWM | 2  |
| UART | 2  |
| I2C | 1  |
| SPI |  1   |
| I2S | 1  |


![Omega2 Pro ](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2-pro-features.png)

|                                   |                       |
|-----------------------------------|-----------------------|
| **A.** 30-pin expansion header    | **G.** USB host       |
| **B.** Battery connector          | **H.** USB-to-serial  | 
| **C.** 8 GB eMMC                  | **I.** Full-color LED |
| **D.** Programmable button        | **J.** Omega2 core    |
| **E.** Power management           | **K.** Chip antenna   |
| **F.** Micro USB (power & serial) |                       |

The Omega2 Pro is based around the [Omega2S+ module](#omega2s), it is the centerpiece of the Omega2 Pro, providing the CPU, 128MB RAM memory & WiFi radio.

### The Expansion Header

The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each section.

> Take a look at the [Using the GPIOs](https://docs.onion.io/omega2-docs/using-gpios.html#important-special-gpios) article to learn more about the Omega's GPIOs, multiplexing GPIO functionality, and the behaviour and requirements of the Omega's special GPIOs.

<!-- expansion header pinout intro -->
```{r child = '../shared/Hardware-Overview-Component-01-expansion-header-pinout-intro.md'}
```

![expansion header pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/expansion-dock-expansion-header-pinout.png)

<!-- expansion header pinout explanation -->
```{r child = '../shared/Hardware-Overview-Component-02-expansion-header-pinout-explanation.md'}
```

### LiPo Battery Support

An on-board battery management chip makes the Omega2 Pro compatible with LiPo batteries: they can be used as the main power source, and will be charged when the Omega is connected to USB power. Use a battery to make your project portable, or to act as a back-up power supply.

Learn more about the Omega2 Pro and batteries: https://onion.io/omega2-pro-get-started/#lipobatterysupport

### Full-color Notification LED

Along with the system status and Wi-Fi status LEDs, there is a full-color LED (WS2812) driven by a hardware pulse width modulation (PWM) controller. 

Learn more about controlling the full-color LED: https://onion.io/omega2-pro-get-started/#fullcolorled

### Node-Red

Node-RED is a flow-based, visual programming tool that runs in the browser. It comes packaged as an OnionOS App on the Omega2 Pro and can be easily accessed through OnionOS in any browser.


Learn more about installing and using Node-Red on the Omega2 Pro by following [this guide](#node-red-article).

<!-- operating system -->
```{r child = '../shared/Hardware-Overview-Component-90-Omega-operating-system.md'}
```

### The Omega LED {#omega2pro-hw-omega-led}

<!-- omega led content -->
```{r child = '../shared/Hardware-Overview-Component-91-Omega-omega-led-content.md'}
```


<!-- Micro USB Port -->
```{r child = '../shared/Hardware-Overview-Component-1-Micro-USB-Port.md'}
```

<!-- USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-2-USB-to-Serial.md'}
```

<!-- USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-4-Power-Switch.md'}
```

<!-- Reset Button -->
```{r child = '../shared/Hardware-Overview-Component-0-Reset-Button.md'}
```

<!-- USB Port -->
```{r child = '../shared/Hardware-Overview-Component-5-Omega-USB-Port.md'}
```

<!-- wifi antenna -->
```{r child = '../shared/Hardware-Overview-Component-92-Omega-smt-antenna.md'}
```

<!-- u.fl connector -->
```{r child = '../shared/Hardware-Overview-Component-93-Omega-ufl-connector.md'}
```
