## SPI Python Module {#spi-python-module}

The Onion SPI Library, `libonionspi` is a dynamic C library that provides functions to easily read from and write to devices communicating with the Omega over the GPIOs via the SPI protocol. The library can be used in C and C++ programs.

Also available is a Python module, called `onionSpi`, that implements an SPI object using functions from the C Library.





<!-- The SPI Protocol -->

### The SPI Protocol

The Serial Peripheral Interface (SPI) is a four-wire synchronous communication protocol, largely used to connect microprocessors or microcontrollers to sensors, memory, and other peripherals.

The four signals are:

| SPI Signal | Meaning                                                       |
|------------|---------------------------------------------------------------|
| SCK        | System Clock                                                  |
| MOSI       | Master Out, Slave In - Data sent from the Master to the Slave |
| MISO       | Master In, Slave Out - Data sent from the Slave to the Master |
| CS/SS      | Chip Select/Slave Select                                      |

The fact that it is a *synchronous* data bus means that one of the lines is a clock, used to synchronize the bits being sent on the data lines.

The protocol is based on the Master-Slave architecture, so the Master will generate the System Clock and the Slave Select signals. In systems with multiple slaves, there will be multiple Slave Select signals.

For more details on SPI, check out the [Wikipedia article](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus).


<!-- The SPI Protocol: Linux and SPI -->

### Linux and SPI

Linux systems usually control SPI devices through kernel drivers. However, it is also possible to generate the SPI protocol by bit-banging on connecte GPIOs. Bit-banging SPI is done through an adapter usually found at `/dev/spidevX.Y` where `X` is the device number and `Y` is the bus number.

The Omega does not have an SPI bit-banging adapter setup by default, but this can be done by using the `insmod` command to insert a module into the kernel. The `libonionspi` library takes care of this for you so you don't have to deal with the intricacies.

<!-- MAJOR HEADING -->
<!-- The Python Module -->

### The Python Module

The `onionSpi` Python module provides a Python object, `OnionSpi`, that serves as a wrapper around the C library functions. The usage is slightly different since the Python module is object oriented and the C library is just a set of functions.


<!-- Source Code -->

### Source Code

The source code can be found in the [Onion `spi-gpio-driver` GitHub Repo](https://github.com/OnionIoT/spi-gpio-driver).


<!-- Python: Programming Flow -->

### Programming Flow

The Python module revolves around the `OnionSpi` object; once it is initialized with the bus number and device ID that the desired SPI adapter uses, the rest of the class functions can be used to register the adapater, setup the adapter's SPI options, and most importantly, make data transfers!

Once the object is initialized, the recommended flow is as follows:
* Check that the device adapter is registered
* If not, register the device adapter with the system
* Set any additional SPI parameters and setup the adapter with them
* Perform any SPI transfers as required.

The details of the specific functions to perform these actions are outlined below.



#### Installing the Module

To install the Python module, run the following commands:
```
opkg update
opkg install python-light pyOnionSpi
```

This will install the module to `/usr/lib/python2.7/OmegaExpansion/`

>This only needs to be done once.

To add the Onion SPI Module to your Python program, include the following in your code:
``` python
import onionSpi
```

<!-- Python: Example Code -->

#### Example

An example of how the `OnionSpi` object is used can be found in the [`spi-gpio-driver` repo.](https://github.com/OnionIoT/spi-gpio-driver/blob/master/examples/testSpi.py)



<!-- Python: Initialization -->

### Initialization of the Object

The object needs to be initialized before it can be used for reading and writing:

``` python
spi  = onionSpi.OnionSpi(busNumber, deviceId)
```

**Arguments**

The constructor requires the bus number and device ID of the SPI device adapter that is to be used. These numbers correspond to the device adapter itself: `/dev/spidevX.Y` where `X` is the device number and `Y` is the bus number.


<!-- Python: Object Member Variables -->

#### Object Member Variables

The `OnionSpi` object has several member variables that are used to define specific SPI parameters and settings. The can be accessed and modified directly using the object.

The member variables are as follows:

| Object Member | Meaning                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------|
| `bus`         | The device adapter bus number                                                                           |
| `device`      | The device adapter device ID                                                                            |
| `speed`       | Maximum transmission clock speed in Hz                                                                  |
| `delay`       | Delay in us after last bit transferred before optionall deselecting the device before the next transfer |
| `bitsPerWord` | Number of bits in a transmitted word                                                                    |
| `mode`        | SPI mode: can be 0 to 3 (Mode 0 is the most common)                                                     |
| `modeBits`    | Additional SPI operating parameters                                                                     |
| `sck`         | GPIO for SPI SCK signal                                                                                 |
| `mosi`        | GPIO for SPI MOSI signal                                                                                |
| `miso`        | GPIO for SPI MISO signal                                                                                |
| `cs`          | GPIO for SPI CS signal                                                                                  |

The `modeBits` parameter may be a little difficult to work with so the following member variables were added:

| Object Member | Meaning                                                         |
|---------------|-----------------------------------------------------------------|
| `threewire`   | Three-wire SPI: MOSI and MISO lines are shared on a single GPIO |
| `lsbfirst`    | Modify the protocol to transmit bytes LSB to MSB                |
| `loop`        | Enable loopback mode                                            |
| `noCs`        | Modify the protocol to not generate a Chip-Select line          |
| `csHigh`      | Modify the protocol for an active-high Chip-Select line         |

Changing any of these parameters will modify the `modeBits` member as well.


<!-- Python: Object Member Variables: Defaults -->

##### Default Values

When the object is first initialized, all of the member variables are initialized to legitimate values:

| SPI Setting   | Programmed Default                  |
|---------------|-------------------------------------|
| `speed`       | 100000 Hz (100 kHz)                 |
| `delay`       | 0                                   |
| `bitsPerWord` | 0 (Corresponds to 8 bits per  word) |
| `mode`        | SPI Mode 0                          |


Sets the SPI lines to the following GPIOs:

| SPI Signal | Omega Gpio |
|------------|------------|
| SCK        | 6          |
| MOSI       | 18         |
| MISO       | 1          |
| CS/SS      | 7          |


<!-- Python: Object Member Variables: Examples -->

##### Examples

Creating an SPI object, modifying some of the parameters, and then printing parameters:

``` python
spi 	= onionSpi.OnionSpi(0, 1)

spi.cs 		= 20
spi.sck		= 19
spi.csHigh 	= 1
spi.speed 	= 400000

print 'SPI CS GPIO:   %d'%(spi.cs)
print 'SPI SCK GPIO:  %d'%(spi.sck)
print 'SPI MISO GPIO: %d'%(spi.miso)
print 'SPI MOSI GPIO: %d'%(spi.mosi)

print 'SPI Speed: %d Hz (%d kHz)'%(spi.speed, spi.speed/1000)
print 'Mode Bits: 0x%x, CS-High: %d'%(spi.modeBits, spi.csHigh)
```



<!-- SUB-HEADING -->
<!-- Python: Setup Functions -->

#### Setup Functions

The following functions are used to register the SPI device adapter and setup any SPI protocol options as required.


<!-- Python: Check if Device is Registered -->

### Check if Device is Registered

To check if a device adapter with the bus number and device ID that were specified in the object constructor is already registered with the system:

``` python
return = spi.checkDevice()
```

**Return Values**

The function will return `0` if the device adapter is already mapped.

The return value will be `1` if the device adapter is NOT mapped/


<!-- Python: Register Device -->

### Register Device

This function will register an SPI device with the bus number, device ID, and other SPI parameters as specified in the object variable members:

``` python
return = spi.registerDevice()
```

It will first check if a device with the specified bus number and device ID is already registered. If it is, it will just return `0`.

If not, it will attempt to register the SPI device adapter by inserting an SPI-gpio module into the kernel. If this operation is successful, the function will return `0`, if not, `1` is returned.

The function uses the following information to register the device:
* The bus number
* The device ID
* SPI mode
* The SPI speed
* The GPIO for the SCK line
* The GPIO for the MOSI line
* The GPIO for the MISO line
* The GPIO for the CS line


**Example**

A short example showing how to register an SPI device adapter:
``` python
spi 	= onionSpi.OnionSpi(0, 1)

### modify any SPI settings as required
spi.cs 		= 20
spi.speed 	= 400000

### register the device
spi.registerDevice()
```


<!-- Python: Setup SPI Device -->

### Setup SPI Device

This function will setup additional SPI parameters on the device adapter
``` python
return  = spi.setupDevice()
```

It will setup the following SPI parameters:
* The maximum speed of the link
* The number of bits per word
* Additional mode information, see [section on additional mode information above](#the-python-module_object-member-variables)


<!-- Python: Setup SPI Device -->

##### Conclusion

Once a device is registered, data can be read from and written to the device via SPI.


<!-- Python: Reading Functions -->

### Reading Function

This function reads a specified number of bytes from a specified address on an SPI device:
``` python
values 	= spi.readBytes(addr, size)
```

The read bytes are returned in the form of a list, even if there is only one byte.


**Arguments**

The `addr` argument specifies from which address on the SPI device to read.

The `size` argument specifies the number of bytes to read.


**Examples**

Read a byte from address 0x33:
``` python
rdVal = spi.readBytes(0x33, 1)
### rdVal[0] now contains the byte that was read
```


Read three byres from address 0x00:
``` python
rdVal = spi.readBytes(0x00, 3)
### the rdVal list now contains the three bytes that were read
```



<!-- SUB-HEADING -->
<!-- Python: Writing Functions -->

#### Writing Functions

The `OnionSpi` class has two functions that can be used to write data via SPI:
* One that requires an address and a list of bytes to write
* One that just sends a list of bytes to write


<!-- Python: Write Bytes -->

### Write Bytes

This function will write a list of bytes to a specified address on an SPI device
``` python
return 	= spi.writeBytes(addr, values)
```

**Arguments**

The `addr` argument specifies to which address on the SPI device to write.

The `values` argument is a list of values to be written. Even if there is only a single byte, it should be in list form.

**Examples**

Write 0x23 to address 0x91:
``` python
ret 	= spi.writeBytes(0x91, [0x23])
```

Write 0x23, 0x33, 0x07 to address 0x96:
``` python
vals 	= [0x23, 0x33, 0x07]
ret 	= spi.writeBytes(0x96, vals)
```


<!-- Python: Write Bytes without an Address -->

### Write Bytes without an Address

This function will just write a list of bytes to an SPI device (without specifying an address):
``` python
return 	= spi.write(values)
```


**Arguments**

The `values` argument is a list of values to be written. Even if there is only a single byte, it should be in list form.


**Examples**

Write 0x08, 0x34, 0x02, 0x07:
``` python
ret 	= spi.write([0x08, 0x34, 0x02, 0x07])
```

Write 0x00, 0x1C, 0x07, 0x12, 0x37, 0x32, 0x29, 0x2D:
``` python
vals 	= [0x00, 0x1C, 0x07, 0x12, 0x37, 0x32, 0x29, 0x2D]
ret 	= spi.write(vals)
```

Write 0x11:
``` python
ret 	= spi.write([0x11])
```
