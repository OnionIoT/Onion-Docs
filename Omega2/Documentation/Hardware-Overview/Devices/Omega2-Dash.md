## Onion Omega2 Dash {#omega2-dash}

The Omega2 Dash is a Wi-Fi-enabled Linux computer with a built-in touchscreen. It is a stand-alone, all-in-one solution that provides a touch-based visual UI that can be internet-connected, connected to other devices, or both. 

It can display the commandline, run programs that create a touch-based UI, and display images (png, jpeg).

![Omega2 Dash](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/OM-O2DASH-00-cover-image.png)

### Getting Started with the Omega2 Dash

See our guide on getting started with the Omega2 Pro for all of the details on getting your device up and running: https://onion.io/omega2-dash-guide/

It includes instructions on how to create an interactive UI using the LVGL graphics library and C, as well as LVGL in Micropython.

### The Omega2 Dash at a Glance

![Omega2 Pro back labelled](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2dash-labelled-back.png)

|     |     |
|-----|-----|
| **A.** 30-pin Expansion Header  | **E.** Chip antenna |
| **B.** MicroSD card slot | **F.** On/off switch |
| **C.** Reset button | **G.** Micro USB port |
| **D.** Omega2S+ IoT module  | **H.** USB 2.0 host port  |

![Omega2 Pro front labelled](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2dash-labelled-front-edit.png)

|     |     |
|-----|-----|
| **I.** 3.2" TFT touchscreen  | **K.** Amber System Status LED  |
| **J.** Holes for easy mounting | **L.** Blue Wi-Fi Status LED |

### Features and Specifications

> The Omega2 Dash is powered by the [Omega2S+ module](#omega2s), which provides the CPU, memory, storage, & WiFi radio.

* 3.2" TFT **touchscreen display**  
    * 320x240 resolution  
    * 16-bit (RGB565) color support  
    * 12-bit resistive touch input  
    * Rated at minimum MTBF value of 50,000 hours with normal operation  
* Based on the **[Omega2S+](https://onion.io/omega2s/) IoT computer module**  
    * **Processor:** 580 MHz MIPS CPU  
    * **Memory:** 128 MB RAM  
    * **Storage:** 32 MB  
    * **Connectivity:** 2.4 GHz b/g/n Wi-Fi (access point & client)  
    * **Operating System:** OpenWrt 18.06 Linux  
* **I/O**  
    * Expansion Header  
         * I²C, UART, PWM, Ethernet, GPIOs
         * Compatible with existing ecosystem of Omega2 Expansions
    * USB 2.0 host  
    * MicroSD card slot  
* **Antenna**
    * 2 dBi directional chip antenna
    * U.FL connector for external antenna
* **USB-to-serial interface** on Micro USB port  
    * Provides reliable, always-on access to the Omega's commandline
* **Status LEDS**
    * Amber: boot status
    * Blue: Wi-Fi status
* **Weight:** 60 g
* **Dimensions:** 82 mm x 70 mm

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

<!-- operating system -->
```{r child = '../shared/Hardware-Overview-Component-90-Omega-operating-system.md'}
```

### The Status LEDs

![Omega2 Dash status LED label](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2dash-status-leds.png)

| Status LED            | LED Activity |
|------------------|--------------|
| **Amber** System status LED    | Whether Linux OS has booted          |
| **Blue** Wi-Fi status LED       | Connection to a Wi-Fi network is active
     |

The behaviour of the LEDs indicates:

* System status LED
    * **Off** – Device not powered on
    * **Blinking** – Booting/updating
    * **On** – Up and running
* WiFi status LED
    * **Off** – Not connected to WiFi network
    * **Blinking** – Connecting
    * **On** – Connected

<!-- Micro USB Port -->
```{r child = '../shared/Hardware-Overview-Component-1-Micro-USB-Port.md'}
```

<!-- USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-2-USB-to-Serial.md'}
```

<!-- Power Switch -->
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
