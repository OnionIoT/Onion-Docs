### I2C

<!-- // mention all of the key points:
//  * two lines: data and clock
//  * master slave architecture
//  * each device has it's own unique two byte address
// on the omega:
//  * accesses through the virtual device file /dev/i2c-0

// make sure to mention that it can be referred to as I2C, IIC, Two-wire interface (TWI)

// can totally rip off large chunks of the i2c article from the documentation
//  * should isolate that text from the i2c article into  markdown files that can be included here -->

**I2C** (Inter-Integrated Circuit), sometimes called IIC or Two-Wire Interface, is a serial interface used to quickly and easily connect multiple devices to controllers and processors such as the Omega2. Examples of I2C devices include:

* Sensors, such as temperature, humidity, current
* Actuators, such as buzzers, lights
* Controllers, such as motors, relays

Communication is performed over 2 data lanes, each given their own pin on the Omega2:

* Clock (SCL) - Signals when data is being transferred
* Data (SDA) - Carries the data to be transferred

The I2C bus uses a **master-slave** architecture, which means the following:

* Bus **masters** are devices that are in control of when and to whom they send and receive data.
    * Masters send commands which include the address of the slave who should receive it.
    * When using I2C with the Omega2, the Omega2 is configured to be the only bus master.
* Bus **slaves** are devices that respond to masters when they receive a command addressed to them.
    * Each slave is identified with a hexadecimal address (eg. `0x27`).
    * Slaves will safely ignore commands not addressed to them.
* Masters and slaves operate in either of two modes:
    * **transmit** - sending data
    * **receive** - receiving data

If you're interested in the full details, see the [Wikipedia article on I2C](https://en.wikipedia.org/wiki/I%C2%B2C) for more.

#### The Omega & I2C

<!-- // all i2c interactions on the omega are done using the sysfs /dev/i2c-0 file, everything mentioned in this article uses this sysfs file to communicate with the hardware I2C controller (useful background knowledge) -->

All I2C interactions on the Omega2 are done using the virtual device file `/dev/i2c-0`. This is made possible with `sysfs`, a pseudo-file system that holds information about the Omega's hardware in files, and lets the user control the hardware by editing the files.

#### I2C using Python

We've developed an I2C Python module that you can import into your apps. For all the details, see the [I2C Python Module](#i2c-python-module).