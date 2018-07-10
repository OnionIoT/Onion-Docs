The address switch changes the I2C device address of the ADC Expansion, allowing users to use two ADC Expansions with a single Omega, providing EIGHT analog input channels

![ADC-Expansion-switch](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-on-expansion-circle.jpg)

The switch changes the I2C address of the ADC chip on the ADC Expansion. That way, two ADC Expansions can be included on the Omega's I2C bus


| Switch Position                      | I2C Device Address |
|:------------------------------------:|:------------------:|
| 0x48 (Farther from Expansion Header) | 0x48               |
| 0x49 (Closer to Expansion Header)    | 0x49               |