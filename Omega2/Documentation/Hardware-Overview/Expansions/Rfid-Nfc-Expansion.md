## NFC & RFID Expansion {#nfc-rfid-expansion}

The NFC & RFID Expansion brings contact-less RFID and NFC communication to the Omega ecosystem. It supports reading and writing with several NDC and RFID protocols at 13.56 MHz. The Expansion is based on the popular `PN532` NFC Chip and communicates with the Omega via `UART1`


### The Hardware

The RFID & NFC Expansion features a 13.56 MHz stripline antenna and features an Expansion Header, so other expansions are stackable on top

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/rfid-nfc-expansion.png)

### Connecting to a Dock

To use the RFID & NFC Expansion, plug it into a Dock that has Expansion header pins (Expansion Dock, Power Dock 2, Arduino Dock R2).

You can safely stack other Expansion on top of it, **However, be mindful of wires that are connected to the header pins underneath.**

>Note: You may only have one RFID & NFC Expansion stacked onto an Omega at a time.

During the boot process, the Expansion draws a lot of current. For safety reasons, do not plug the Expansion onto the dock while the Omega is powered ON.

//TODO: Pictures of the expansion on different docs

### The Antenna

The RFID & NFC Expansion has onboard PCB antenna with 0cm~6cm communication distance above and below the antenna, and RFID reader/writer modes

* Mifare 1k, 4k, Ultralight and DesFire cards 
* ISO/IEC 14443-4 cards such as CD97BX, CD light, DesFire, P5CN072 (SMX)
* Innovision Jewel cards such as IRT5001 card
* FeliCa cards such as RCS_860 and RCS_854
	
### Using the RFID & NFC Expansion

The RFID & NFC Expansion can be used to read from and write to supported 13.56MHz cards and tags. It can also be used for bi-directional communication with NFC devices.
 
Read our [guide to using the RFID & NFC Expansion]() to learn how to control it using software