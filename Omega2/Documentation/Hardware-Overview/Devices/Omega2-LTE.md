## Onion Omega2 LTE {#omega2-lte}

The Omega2 LTE is a Linux IoT computer with built-in high-speed 4G LTE cellular data connectivity and GNSS global positioning. This is in addition to WiFi and ethernet network capabilities.

It features an LTE Cat 4 modem that delivers 150 Mbps downlink and 50 Mbps uplink data rates, and supports GNSS.

![Omega2 LTE](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/O2LTE-cover.png)

There are two variants of the Omega2 LTE:

|              Model              | Part Number |
|:-------------------------------:|-------------|:---------------:|
| Omega2 LTE North American Model | OM-O2LTE-NA | 
| Omega2 LTE Global Model         | OM-O2LTE-G  |

### Getting Started with the Omega2 LTE

See our guide on getting started with the Omega2 LTE for all of the details on getting your device up and running: https://onion.io/omega2-lte-guide/

In addition to getting started for the first time, the guide outlines how to control and share the cellular data connection, how to use the GNSS positioning data, and more.

### Hardware Designs, Measurements, Images, and More

Visit the OnionIoT/Omega2-LTE GitHub repo: https://github.com/OnionIoT/Omega2-LTE

### The Omega2 LTE at a Glance

![Omega2 LTE labelled front](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/onion-omega2-lte-front-labelled.jpg)

|     |     |
|-----|-----|
| **A.** 30-pin Expansion Header  | **G.** Power switch |
| **B.** LTE modem + GPS receiver | **H.** USB-C (power & serial) |
| **C.** LTE status LEDs | **I.** Programmable button |
| **D.** LTE & GNSS U.FL antenna connectors  | **J.** Omega2S+ module  |
| **E.** JST-PH battery connector | **K.** Wi-Fi chip antenna  | 
| **F.** Power management | **L.** Omega status LEDs  |

![Omega2 LTE back labelled](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/onion-omega2-lte-back01-labelled.jpg)

|     |     |
|-----|-----|
| **A.** Nano-SIM slot  | **B.** MicroSD slot  |

### Features & Specifications

* Based on the **[Omega2S+](https://onion.io/omega2s/) IoT computer module**  
    * **Processor:** 580 MHz MIPS CPU  
    * **Memory:** 128 MB RAM  
    * **Storage:** 32 MB  
        * Expandable up to 2 TB with MicroSD card
    * **Connectivity:** 2.4 GHz b/g/n Wi-Fi (access point & client)  
    * **Operating System:** OpenWrt 18.06 Linux  
* **Antenna:**
    *  **Wi-Fi:** On-board 2 dBi direction chip antenna & U.FL connector for external antenna
    * **4G LTE:** U.FL connectors for main and diversity antennas
    * **GNSS:** U.FL connector for GNSS antenna
* **SIM Support:** Nano-SIM slot for cellular data
* **Battery Support:** LiPo battery management and JST-PH battery connector
* **Dimensions:** 80 x 50 mm

### LTE Modem & Variants

There are two variants of the Omega2 LTE, each using a Quectel modem for cellular and GNSS connectivity but with different capabilities:

|              Model              | Part Number |      Modem      |
|:-------------------------------:|-------------|:---------------:|
| Omega2 LTE North American Model | OM-O2LTE-NA | Quectel EC25-AF |
| Omega2 LTE Global Model         | OM-O2LTE-G  | Quectel EG25-G  |

The OM-O2LTE-NA model is compatible with cellular networks in North America, while the OM-O2LTE-G is a Global model that supports network bands around the world: 

| Cellular Technology | Omega2 LTE (OM-O2LTE-NA) | Omega2 LTE Global Model (OM-O2LTE-G) |
| -- | -- | -- |
| 4G LTE (FDD) | B2, B4, B5, B12, B13, B14, B66, B71 | B1, B2, B3, B4, B5, B7, B8, B12, B13, B18, B19, B20, B25, B26, B28 |
| 4G LTE (TDD) | - | B38, B39, B40, B41 |
| 3G UMTS WCDMA | B2, B4, B5 | B1, B2, B4, B5, B6, B8, B19 |
| *Modem* | *Quectel EC-25AF* | *Quectel EG-25G* | 



### The Expansion Header

The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each section.

> Take a look at the [Using the GPIOs](https://docs.onion.io/omega2-docs/using-gpios.html#important-special-gpios) article to learn more about the Omega's GPIOs, multiplexing GPIO functionality, and the behaviour and requirements of the Omega's special GPIOs.

<!-- expansion header pinout intro -->
```{r child = '../shared/Hardware-Overview-Component-01-expansion-header-pinout-intro.md'}
```

![Omega2 LTE header pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2-lte-expansion-header-pinout-1.png)

<!-- operating system -->
```{r child = '../shared/Hardware-Overview-Component-90-Omega-operating-system.md'}
```

### The Status LEDs

The Omega2 LTE uses a series of LEDs to provide visual feedback on the current status of the device:

| Status LED                          | Indicates                                |
|-------------------------------------|------------------------------------------|
| A. **Green** Power LED                 | Running on battery                       |
| B. **Amber** System status LED         | Whether Linux OS has booted              |
| C. **Blue** Wi-Fi status LED           | Connection to a Wi-Fi network is active  |
| D. **Green** Cellular network status   | Connection to cellular network is active |
| E. **Amber** Cellular network activity | Transmitting and receiving cellular data |

![Omega2 LTE status LED label](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/onion-omega2-lte-led-labelled.jpg)


<!-- USB-C Port -->
```{r child = '../shared/Hardware-Overview-Component-1A-USB-C-Port.md'}
```

<!-- USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-2A-USB-C-to-Serial.md'}
```

### LiPo Battery Support

An on-board battery management chip makes the Omega2 Pro compatible with LiPo batteries: they can be used as the main power source, and will be charged when the Omega is connected to USB power. Use a battery to make your project portable, or to act as a back-up power supply.

Learn more about the Omega2 Pro and batteries: https://onion.io/omega2-lte-guide/#battery

<!-- Power Switch -->
```{r child = '../shared/Hardware-Overview-Component-4-Power-Switch.md'}
```

<!-- Reset Button -->
```{r child = '../shared/Hardware-Overview-Component-0-Reset-Button.md'}
```

<!-- wifi antenna -->
```{r child = '../shared/Hardware-Overview-Component-92-Omega-smt-antenna.md'}
```

<!-- u.fl connector -->
```{r child = '../shared/Hardware-Overview-Component-93-Omega-ufl-connector.md'}
```

### Software 

See the [`omega2-lte` package in the OnionIoT/openwrt-packages GitHub repo](https://github.com/OnionIoT/OpenWRT-Packages/tree/openwrt-18.06/omega2-lte#omega2-lte-base-package) for more details on the software package that's specific to the Omega2 LTE.
