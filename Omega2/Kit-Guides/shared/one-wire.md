### 1-Wire Communication Protocol

The 1-Wire protocol is a bus-based protocol that uses, as the name implies, one data wire to transmit data between devices. It's similar to [the I2C protocol](#starter-kit-controlling-an-lcd-screen), but it has a longer range and a lower data rate.

It follows a master-slave architecture with each bus allowing for one master, in this case the Omega, and many slave devices. Every device type has its own unique single-byte (8 bit) identifier, eg. `0x8f`. Each device in turn has its own unique 8-byte (64-bit) serial number that includes a byte to describe the device type, known as the **family code**, as the Least Significant Byte. An example of a serial number is shown below:

![one-wire-serial-number](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/one-wire-serial-number.jpg)

The protocol may also be found written as One Wire, One-Wire, or sometimes 1W. For consistency, we'll be using 1-Wire in this and other guides. In code, we'll use oneWire or OneWire because **variable names cannot start with numbers** in Python (and several other programming languages as well).