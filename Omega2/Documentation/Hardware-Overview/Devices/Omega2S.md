## Onion Omega2S & Omega2S+ {#omega2s}

The Omega2S is a smaller, surface-mount packaged version of the through-hole Omega2, designed for IoT applications that require drop-in connectivity and computing. 

The 34mm x 20mm x 2.8mm package is based on the MT7688 SoC and features a CPU, memory, flash storage, and a WiFi radio. It supports a wide variety of I/O protocols, with 42-pins available to the developer. The module is self-contained and only requires a power supply and an external WiFi antenna to operate. The pre-loaded Linux Operating System reduces development time by allowing the use of existing software package and high-level programming languages. This module is precertified for FCC and CE, further reducing time to market in the fast-moving world of IoT.

![omega2s](https://onion.io/wp-content/uploads/2018/09/Omega2S_W_BG.png)

### Variants

The Omega2S comes in two variants: the Omega2S and Omega2S+

|  | Omega2S | Omega2S+ | 
| ------------- | -------------  | -------------  |
| Processor | 580MHz MIPS CPU  | 580MHz MIPS CPU  |
| Memory | 64MB Memory  | **128MB** Memory  |
| Storage | 16MB Storage  | **32MB** Storage  |
| WiFi adapter | b/g/n Wi-Fi  | b/g/n Wi-Fi  |
| USB 2.0 | 1  | 1  | 
| SD/eMMC | 1  | 1  | 
| Ethernet | 1  | 1  |
| GPIOs | **37**  | **37**  |
| PWM | **4**  | **4**  |
| UART | **3**  |  **3**  |
| I2C | 1  | 1  |
| SPI | 1  | 1  |
| I2S | 1  | 1  |

### The Pins

Take a look at the [Using the GPIOs](https://docs.onion.io/omega2-docs/using-gpios.html#important-special-gpios) article to learn more about the Omega's GPIOs, multiplexing GPIO functionality, and the behaviour and requirements of the Omega's special GPIOs.

![omega2s pinout](https://github.com/OnionIoT/Onion-Media/raw/master/Pinouts/Omega2S.png)

### Datasheet & Other Resources

Find the Omega2S datasheet and all of the available documents for download here: https://onion.io/omega2s/#documents

### Differences from Omega2
The Onion Omega2S is the surface-mount packaged version of the Omega2, designed specifically for high volume production due to its low profile, extended feature-set, and production friendly design.

The specific differences from the Omega2 are as follows:

* Surface-mount module form-factor
* Low profile, measuring 34x20x2.8 mm
* 63 total pins compared to 32 pins on Omega2
* Pins for SD/eMMC are available on the pinout - no MicroSD slot
* Features 3 UARTs, compared to 2 on the Omega2
* Features 4 PWM channels, compared to 2 on the Omega2
* Exposes SPI Chip-Select 0 (CS0) pin
* No on-board antenna - features Antenna signal pin and U.FL connector
* No on-board system status LED - features system status pin for connection to external LED


### SoC Datasheet

The datasheet for the Omega2S SoC can be found here: [Mediatek MT7688 Datasheet](https://labs.mediatek.com/fileMedia/download/9ef51e98-49b1-489a-b27e-391bac9f7bf3)
