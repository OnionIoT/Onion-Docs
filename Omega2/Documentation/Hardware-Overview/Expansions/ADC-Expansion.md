## ADC Expansion {#adc-expansion}

The ADC Expansion allows you to read analog signals up to 5V with your Omega2. Now you have an opportunity to convert analog signal such as sound, temperature, humidity and others into a digital signal. It has 4 analog input channels, 16 BIts of precision and up to 860 samples per second. The expansion also communicates with the Omega over I2C.

### The Hardware

The ADC Expansion features the following:

* 4 analog input channels and provides 5V and GND female headers for each of the 4 inputs
* provides 5V and GND female headers for each of the 4 inputs
* An address switch
* 3x Grove connectors

![ADC-Expansion-illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-expansion.png)

The ADC Expansion is based on the TI ADS1115 analog-to-digital converter chip.

### Connecting to a Dock

To use the ADC Expansion, plug it into a Dock that has Expansion header pins (Expansion Dock, Power Dock 2, Arduino Dock R2).

You can safely stack other Expansion on top of it, **However, be mindful of wires that are connected to the header pins underneath.**

>Note: You may have **no more** than one ADC Expansion stacked onto an Omega at a time. [TO BE CONFIRMED]

![ADC-Expansion-expansion-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-on-expansion-dock.jpg)

![ADC-Expansion-power-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-on-power-dock.jpg)

![ADC-Expansion-arduino-dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-on-arduino-dock.jpg)

### Analog Input Headers

A female header provides access to all 4 analog input channels, making analog input plug and play.

![ADC-Expansion-analog](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-soil-connection-1.jpg

5V and GND female headers are also provided for each of the 4 inputs, to make powering the analog sensor easier.

![ADC-Expansion-analog2](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-soil-connection-2.jpg

### Grove Connectors

The ADC expansion includes 3 grove connectors, 2x analog, 1x digital (I2C) allowing you to easily connect any Grove sensors and peripherals.

![ADC-Expansion-illustration-labeled](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/adc-expansion-labeled.png)

The digital Grove connector is connected to the Omega's I2C bus. Since I2C is a bus, it's acceptable, and in fact, intended, that many I2C devices are connected to the bus. So it's alright to have an I2C Grove peripheral connected as well as other I2C devices.

>IMPORTANT NOTE: Only a single input is allowed for each channel. If a Grove peripheral is connected and occupying an analog input channel, you CANNOT "re-use" the input channel by connecting a different input signal to the female header. This can lead to damage of the ADC Expansion, the connected Omega, or both.

### The Address Switch

```{r child='./ADC-Expansion-Component-address-switch.md'}
```

### Using the ADC Expansion

Read our [guide to using the ADC Expansion](#using-adc-expansion) to learn how to control it using software.