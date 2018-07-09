
## ADC Expansion {#adc-expansion}

The ADC Expansion allows you to read analog signals up to 5V with your Omega2. Now you have an opportunity to convert analog signal such as sound, temperature, humidity and others into a digital signal. It has 4 analog input channels, 16 BIts of precision and up to 860 samples per second. The expansion also communicates with the Omega over I2C.

// intro to ADC Expansion
//	- allows you to read analog signals up to 5V with your Omega2
//	- 4 analog input channels, 16bits of precision, up to 860 samples per second
// 	- communicates with the omega over I2C

### The Hardware

The ADC Expansion features the following:
* 4 analog input channels and provides 5V and GND female headers for each of the 4 inputs
* provides 5V and GND female headers for each of the 4 inputs
* An address switch
* 3x Grove connectors

![ADC-Expansion-illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-expansion.png)

// VISUAL: ADC Expansion illustration

### Connecting to a Dock

To use the ADC Expansion, plug it into a Dock that has Expansion header pins (Expansion Dock, Power Dock 2, Arduino Dock R2).

You can safely stack other Expansion on top of it, **However, be mindful of wires that are connected to the header pins underneath.**

>Note: You may have **no more** than one ADC Expansion stacked onto an Omega at a time. [TO BE CONFIRMED]

// VISUAL: ADC on Expansion Dock

// VISUAL: ADC on Power Dock

// VISUAL: ADC on Arduino Dock

### Analog Input Headers

A female header provides access to all 4 analog input channels, making analog input plug and play.

// VISUAL: labelled diagram of the headers

5V and GND female headers are also provided for each of the 4 inputs, to make powering the analog sensor easier.

// VISUAL: soil moisture sensor connected to input header

### Grove Connectors

The ADC expansion includes 3 grove connectors, 2x analog, 1x digital (I2C) allowing you to easily connect any Grove sensors and peripherals.

// VISUAL: labelled diagram of the 2 analog and 1 digital grove connector

The digital Grove connector is connected to the Omega's I2C bus. Since I2C is a bus, it's acceptable, and in fact, intended, that many I2C devices are connected to the bus. So it's alright to have an I2C Grove peripheral connected as well as other I2C devices.

// VISUAL: ADC with 3x Grove peripherals attached, the digital sensor should be labelled

>IMPORTANT NOTE: Only a single input is allowed for each channel. If a Grove peripheral is connected and occupying an analog input channel, you CANNOT "re-use" the input channel by connecting a different input signal to the female header. This can lead to damage of the ADC Expansion, the connected Omega, or both.

### The Address Switch

The address switch allows users to use two ADC Expasions with a single Omega, providing EIGHT analog input channels!

// VISUAL: ADC Exp with circle around address switch (see https://docs.onion.io/omega2-docs/relay-expansion.html#the-address-switch)
//Label Switch 1 and 2 corresponded to its I2C address

The switch changes the I2C address of the ADC chip on the ADC Expansion. That way, two ADC Expansions can be included on the Omega's I2C bus. Switches can be turned either ON or OFF. See the following table for the address values:

|   0x48   |   0x49   | Binary Value |
|:--------:|:--------:|:------------:|
|    OFF   |    OFF   |     *00*     |
|    OFF   |    ON    |     *01*     |
|    ON    |    OFF   |     *10*     |
|    ON    |    ON    |     *11*     |

The I2C addresses corresponding to the different switch positions are shown below:

// values:
// Switch 																I2C Device Address
//	0x48 (farther from expansion header)	0x48
//	0x49 (closer to expansion header)			0x49
