## Using the ADC Expansion {#using-adc-expansion}

// intro to the ADC Expansion, something like:
The ADC (Analog-to-Digital Converter) Expansion allows the user to read and interpret analog voltage, effectively giving the Omega analog inputs. The Expansion has 4 input channels, each with a resolution of 16 bits and a maximum of 860 samples per second.

With the ADC Expansion, a whole world of analog sensors is now open to you and your Omega projects.

>You can learn more about the technical specifications of the ADC Expansion in our [ADC Expansion hardware overview](#adc-expansion)

### The Channels

// the ADC has 4 input channels, they're available on the header as well as the grove connectors.
// it's important to note that a channel should be connected to an input source either through the header or the grove connector, using both for a single input channel can cause damage to the ADC Expansion

#### Input Header

// input channels are available on the female header on the board, along with 5V power and ground headers, to power the sensors

// VISUAL: labelled diagram of the headers

// brief explanation of how a sensor can be connected

// VISUAL: soil moisture sensor connected to input header

#### Grove Connectors

// two analog grove connectors

// VISUAL: labelled diagram of the 2 analog grove connectors and their input channels

// reiterate that it's important to note that a channel should be connected to an input source either through the header or the grove connector, using both for a single input channel can cause damage to the ADC Expansion


### Digital Grove Connector

// also included is a digital I2C grove connector, allowing for additional Grove sensors to be connected

// VISUAL: labelled diagram of the digital grove connector


### The Address Switch

// CAN INCLUDE THE EXISTING ADDRESS SWITCH COMPONENT: Omega2/Documentation/Hardware-Overview/Expansions/ADC-Expansion-Component-address-switch.md

### Using the Command Line

// command line utility is available to read analog inputs from the Omega's Linux command line


#### Installing the Utility

// First need to install the `adc-exp` utility:

```
opkg update
opkg install adc-exp
```

#### Command Usage
For a print out of the command’s usage, run it with just a -h argument:

```
adc-exp -h
```

In general, the usage is as follows:

```
adc-exp [options] <channel>
```

#### Reading an Input Voltage

// reading a single channel, when the switch is at the default value (0x48)

```
adc-exp <channel>
```

// so for example if we want to read channel 0:

```
adc-exp 0
```

Will return something like

```
A0 Voltage: 2.12 V
```

#### The Switch Option

// reading a single channel and specifying the value of the switch:

```
adc-exp -s <switch value> <channel>
```

// so for example, reading channel 3 when the switch is set to 0x49:

```
adc-exp -s 0x49 3
```

Will return something like

```
A3 Voltage: 3.33 V
```

#### Reading All channels

// reading all channels at once:

```
adc-exp [-s <switch value>] all
```

// give an example, and show the output

#### JSON Output

// sometimes it's useful to have the output in JSON, so we've built in an option:

```
adc-exp -j [-s <switch value>] <channel>
```

// again, give an example, and show the output
