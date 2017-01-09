## Resetting the Microcontroller

// explain what happens in a microcontroller reset: it fully resets the current program and starts again, in the context of an arduino sketch, it will reset any global variables, run the setup function again, and then start the loop function (do some research into what exactly goes on during a mcu reset)

// give a few examples of why you would want to do this

### Physically with a Button

// point out the MCU_RESET button on the arduino dock
// have the labelled illustration included here

### Virtually with Software

// using the `arduino-dock reset` Command
// TODO: LAZAR implement this!

// explanation: the Omega's GPIO19 can control the microcontroller reset circuit, and that is precisely what the command does
// include a link back to the arduino dock 2 hardware article
// TODO: LAZAR to provide more info
