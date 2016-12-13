## Flashing the Microcontroller

// intro: whole point of the arduino dock is having the ATmega328P microcontroller and Omega interact, an OS with connectivity and a microcontroller can be very powerful when used together effectively

> Programming and flashing a microcontroller mean the same thing, you are taking compiled code and uploading it to a microcontroller. The terms are often used interchangeably.

### Prerequisites

#### Accessing the Omega
// 1) your computer must be able to connect to the Omega by it's `Omega-ABCD` name
// can recycle content from: https://wiki.onion.io/Tutorials/Arduino-Dock/Initial-Setup#computer-setup_accessing-the-omega-s-url

#### Arduino IDE

// arduino ide must be installed on your computer
// can reference https://wiki.onion.io/Tutorials/Arduino-Dock/Initial-Setup#computer-setup_arduino-ide

#### Modification of `boards.txt`

// need to modify arduino's boards.txt file to allow ssh sketch uploads
// recycle content from https://wiki.onion.io/Tutorials/Arduino-Dock/Initial-Setup#computer-setup_arduino-ide_modification-of-boards-txt

// TODO: LAZAR to update this messy solution



### Doing the Actual Flashing

// two methods to flash the mcu
//  1. using the arduino IDE
//  2. copying the compiled file to the omega and flashing manually from the command line

// make sure to mention that the Arduino Dock 2 comes ready to flash the microcontroller out of the bux

### Wireless Flashing with the Arduino IDE

// can borrow heavily from https://wiki.onion.io/Tutorials/Arduino-Dock/Using-the-Arduino-Dock#using-the-arduino-dock_flashing-sketches
// just get rid of the stuff about the onion library and onion object, the new arduino dock doesn't need that!
// take new screenshots please

### Manually Flashing on the Command line

// mention that this should be the back-up way in case the above method doesn't work
// can borrow heavily from  https://wiki.onion.io/Tutorials/Arduino-Dock/Using-the-Arduino-Dock#using-the-arduino-dock_flashing-sketches_using-the-omega
// for the part where we copy over the file, link to the transferring files article
