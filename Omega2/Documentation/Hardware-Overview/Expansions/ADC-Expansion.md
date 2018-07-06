
## ADC Expansion {#adc-expansion}

// intro to ADC Expansion
//	- allows you to read analog signals up to 5V with your Omega2
//	- 4 analog input channels, 16bits of precision, up to 860 samples per second
// 	- communicates with the omega over I2C

### The Hardware

// The ADC Expansion has:
//	- 4 analog input channels
//	- provides 5V and GND female headers for each of the 4 inputs
//	- an address switch
//	- 3x Grove connectors

// VISUAL: ADC Expansion illustration

### Connecting to a Dock

// intro to this section

// VISUAL: ADC on Expansion Dock

// VISUAL: ADC on Power Dock

// VISUAL: ADC on Arduino Dock

### Analog Input Headers

// A female header provides access to all 4 analog input channels, making analog input plug and play.

// VISUAL: labelled diagram of the headers

// 5V and GND female headers are also provided for each of the 4 inputs, to make powering the analog sensor easier

// VISUAL: soil moisture sensor connected to input header

### Grove Connectors

// the expansion includes 3x grove connectors, 2x analog, 1x digital (I2C)
//	can use these to easily connect any Grove sensors and peripherals

// VISUAL: labelled diagram of the 2 analog and 1 digital grove connector

// The digital Grove connector is connected to the Omega's I2C bus. Since I2C is a bus, it's acceptable, and in fact, intended, that many I2C devices are connected to the bus. So it's alright to have an I2C Grove peripheral connected as well as other I2C devices.

// VISUAL: ADC with 3x Grove peripherals attached, the digital sensor should be labelled

// IMPORTANT NOTE: Only a single input is allowed for each channel. If a Grove peripheral is connected and occupying an analog input channel, you CANNOT "re-use" the input channel by connecting a different input signal to the female header. This can lead to damage of the ADC Expansion, the connected Omega, or both.


### The Address Switch

// the address switch allows users to use two ADC Expasions with a single Omega, providing EIGHT analog input channels!

// VISUAL: ADC Exp with circle around address switch (see https://docs.onion.io/omega2-docs/relay-expansion.html#the-address-switch)

// the switch changes the I2C address of the ADC chip on the ADC Expansion. That way, two ADC Expansions can be included on the Omega's I2C bus
// need to display the switch setting and the i2c in a table similar to https://docs.onion.io/omega2-docs/relay-expansion.html#the-address-switch

// values:
// Switch 																I2C Device Address
//	0x48 (farther from expansion header)	0x48
//	0x49 (closer to expansion header)			0x49
