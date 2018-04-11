## NFC & RFID Expansion {#nfc-rfid-expansion}

The NFC & RFID Expansion brings contact-less RFID and NFC communication to the Omega ecosystem. It supports reading and writing with several NFC and RFID protocols at 13.56 MHz. The Expansion is based on the popular `PN532` NFC Chip and communicates with the Omega serially via `UART1`.


### The Hardware

The RFID & NFC Expansion features a 13.56 MHz stripline antenna and an Expansion Header, so other expansions are stackable on top:

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/rfid-nfc-expansion.png)

### Connecting to a Dock

To use the RFID & NFC Expansion, plug it into a Dock that has Expansion header pins (Expansion Dock, Power Dock 2, Arduino Dock R2).

You can safely stack other Expansion on top of it, **However, be mindful of wires that are connected to the header pins underneath.**

>Note: You may only have one RFID & NFC Expansion stacked onto an Omega at a time.

During the boot process, the Expansion draws a lot of current. We recommend connecting it to a Dock while the Omega is powered off. If the Omega is powered on, the large current draw may cause the Omega to reboot.

![expansion-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/rfid-expansion-dock.jpg)

![power-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/rfid-power-dock.jpg)

![arduino-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/rfid-arduino-dock.jpg)

### The Antenna

The RFID & NFC Expansion has an onboard PCB antenna with 0cm~6cm communication distance above and below the antenna. The following RFID protocols and standards are supported:

* Mifare 1k, 4k, Ultralight and DesFire cards
* ISO/IEC 14443-4 cards such as CD97BX, CD light, DesFire, P5CN072 (SMX)
* Innovision Jewel cards such as IRT5001 card
* FeliCa cards such as RCS_860 and RCS_854

### Using the RFID & NFC Expansion

The RFID & NFC Expansion can be used to read from and write to supported 13.56MHz cards and tags. It can also be used for bi-directional communication with NFC devices.

Read our [guide to using the RFID & NFC Expansion](#using-rfid-nfc-expansion) to learn how to control your RFID & NFC Expansion.
