## Resetting the Microcontroller {#arduino-dock-reset}

// explain what happens in a microcontroller reset: it fully resets the current program and starts again, in the context of an arduino sketch, it will reset any global variables, run the setup function again, and then start the loop function (do some research into what exactly goes on during a mcu reset)

// give a few examples of why you would want to do this

There are two ways of resetting the ATmega, either by the button labelled MCU_RESET on the Arduino Dock or using a software command. Pressing the reset button is similar to turn off the MCU and turn it back on again. This will only stops the program on the ATmega and restarts it from the beginning. It will not erase the program. In the context of an arduino sketch, it will reset any global variables, run the setup function again, and then start the loop function.

There are several cases where resetting the MCU is useful. For example, if the program isn't looped or stopped and we want to run the program again. Instead of reflashing the program we can simply press the reset button. Resetting the ATmega is very useful when testing a code and restarting the program for debugging purposes.

### Physically with a Button

// point out the MCU_RESET button on the arduino dock

The microcontroller can be reset physically pressing the MCU_RESET button on the Arduino Dock.

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/arduino-dock-illustration.png)

When the MCU_RESET button is pressed and released, the blue LED should quickly blink a few times, indicating that its in the bootloader before it start running the program on the ATmega. If the LED fails to blink, then the ATmega is not properly resetted.

// TODO: bootloader? this came out of left field

<!-- ### Virtually with Software

// TODO: write this when actually implemented in software

// using the `arduino-dock reset` Command

// explanation: the Omega's GPIO19 can control the microcontroller reset circuit, and that is precisely what the command does
// include a link back to the arduino dock 2 hardware article
// TODO: LAZAR to provide more info -->
