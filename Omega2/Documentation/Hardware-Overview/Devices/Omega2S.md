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
* Does not have built-in pull-up resistors on I2C bus - requires external pull-up resistors

### Development Kit

The Omega2S Development Kit includes everything you need to fully evaluate the functionality of the Omega2S Module and begin the development of your IoT product.

* Easy insertion socket for the Omega2S Module
* USB, Micro-USB, Ethernet Connectors
* Connectors Pins for all Input/Output Signals
* Dual Reset Functions

![o2s dev kit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2s-dev-kit-emmc-0.jpg)

Two versions are available:

| OM2S-DK-SD<br>SD Card Slot Version       | OM2S-DK-EM<br>eMMC Storage Version |
|------------------------------------------|------------------------------------|
| Micro SD Card Slot<br>8 GB Micro SD Card | Built-in 8GB eMMC                  |
| Two (2) Omega2S modules                  | Two (2) Omega2S modules            |
| Two (2) Omega2S+ modules                 | Two (2) Omega2S+ modules           |
| 2 dBi uFL Tape Antenna                   | 2 dBi uFL Tape Antenna             |
| Micro USB Cable                          | Micro USB Cable                    |
| Ethernet Cable                           | Ethernet Cable                     |

### Ordering Information

To get information on ordering or evaluating the Omega2S, visit: https://onion.io/omega2s/

### Datasheet

The datasheet for the MT7688 SoC used on the Omega2S can be found here: [Mediatek MT7688 Datasheet](https://github.com/OnionIoT/Onion-Docs/raw/master/Omega2/MT7688_Datasheet_v1_4.pdf)

The Omega2S datasheet can be found here: [Omega2S Datasheet](https://github.com/OnionIoT/Omega2/raw/master/Documents/Omega2S%20Datasheet.pdf)

The full Omega2S technical document package can be downloaded as well: [Omega2S Technical Document Package](https://github.com/OnionIoT/Omega2/archive/master.zip)
