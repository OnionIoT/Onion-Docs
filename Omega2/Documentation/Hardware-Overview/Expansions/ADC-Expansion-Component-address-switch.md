// the address switch changes the I2C device address of the ADC Expansion, allowing users to use two ADC Expansions with a single omega, providing EIGHT analog input channels

// VISUAL: ADC Exp with circle around address switch (see https://docs.onion.io/omega2-docs/relay-expansion.html#the-address-switch)

// the switch changes the I2C address of the ADC chip on the ADC Expansion. That way, two ADC Expansions can be included on the Omega's I2C bus
// need to display the switch setting and the i2c in a table similar to https://docs.onion.io/omega2-docs/relay-expansion.html#the-address-switch

// values:
// Switch 																I2C Device Address
//	0x48 (farther from expansion header)	0x48
//	0x49 (closer to expansion header)			0x49
