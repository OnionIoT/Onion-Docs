### One Wire Protocol

The One Wire protocol is a bus-based protocol that uses, as the name implies, one data wire to transmit data between devices. It's similar to [the I2C protocol](#starter-kit-controlling-an-lcd-screen), but it has a longer range and a lower data rate.

It follows a master-slave architecture with each bus allowing for one master, in this case the Omega, and many slave devices. Every device type has its own unique single-byte (8 bit) identifier, eg. `0x8f`. Each device in turn has its own unique 8-byte (64-bit) serial number that includes a byte to describe the device type, known as the **family code**, as the Least Significant Byte. An example of a serial number is shown below:

![one-wire-serial-number](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/one-wire-serial-number.jpg)

>There's a lot of ways to spell out the protocol - One-Wire, 1-Wire, 1W. For consistency, we'll be using 1-Wire in this and other guides. In code, we'll probably use oneWire or variants due to variable naming limits.
