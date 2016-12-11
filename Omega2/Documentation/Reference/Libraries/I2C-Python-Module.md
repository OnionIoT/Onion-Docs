# I2C Python Library

The Onion I2C Library, `libonioni2c` is a dynamic C library that provides functions to easily read from and write to devices communicating with the Omega via I2C. The library can be used in C and C++ programs.

Also available is a Python module that implements an I2C object using functions from the C library. The module is called `onionI2C` and is part of the `OmegaExpansion` package.


[[_TOC_]]

[//]: # (Linux and I2C)

# Linux and I2C

I2C devices are usually controlled by a kernel driver, however, it is also possible to access devices through an adapter in the Linux filesystem. The adapter can be found at `/dev/i2c-X`, where `X` is the adapter number which can range from 0 to 255. On the Omega, `/dev/i2c-0` is available by default. This allows users to interact with I2C slaves from the Linux environment.

The Onion I2C library uses the `/dev/i2c-0` adapter, and implements read and write functions I2C devices.

[//]: # (MAJOR HEADING)
[//]: # (The Python Module)

# The Python Module

The `onionI2C` Python module in the `OmegaExpansion` package provides a Python object that serves as a wrapper around the C library functions. The usage is slightly different since the Python module is object oriented and the C library is just a set of functions.


[//]: # (Source Code)

## Source Code

The source code can be found in the [Onion `i2c-exp-driver` GitHub Repo](https://github.com/OnionIoT/i2c-exp-driver).

[//]: # (Python: Programming Flow)

## Programming Flow

Once the I2C object is initialized, the read and write functions can be called freely using the object. 


[//]: # (Using the Python Module)

## Using the Python Module

**Installing the Module**

To install the Python module, run the following commands:
```
opkg update
opkg install python-light pyOnionI2C
```

This will install the module to `/usr/lib/python2.7/OmegaExpansion/`

*Note: this only has to be done once.*


**Using the Module**

To add the Onion I2C Module to your Python program, include the following in your code:
``` python
from OmegaExpansion import onionI2C
```

[//]: # (Example Code)

## Example

An example of how the `onionI2C` library is used can be found in the [`i2c-exp-driver` repo.](https://github.com/OnionIoT/i2c-exp-driver/blob/master/examples/onion-i2c.py)

The example code programs the Relay Expansion directly.


[//]: # (Functions)

## Functions

Each of the main functions implemented in this module are described below.


[//]: # (Initialization)

### Initialization

The object needs to be initialized before it can be used for reading and writing:
``` python
i2c 	= onionI2C.OnionI2C()
```

After this call, the object can be used for reading and writing.

**Arguments**

The constructor has an optional argument that defines the I2C device adapter number. This corresponds to the `X` in `/dev/i2c-X`.

If no argument is supplied, the adapter will be set to `/dev/i2c-0`. This is the only default adapter on the Omega and should suit most use cases.

If your use case requires a different adapter, add an integer argument to the constructor call.



[//]: # (Reading)

### Reading from an I2C Slave

#### Reading Bytes

This function reads a specified number of bytes from a specific device on the I2C bus, and returns them in a list:
``` python
valList = i2c.readBytes(devAddr, addr, size)
```

**Arguments**

The `devAddr` argument defines the I2C slave device address. 

The `addr` argument defines the address on the device from which to read.

The number of bytes to be read should be placed in the `size` argument.


**Examples**

Read 4 bytes from address `0x00` on a device with an address of `0x48`:
``` python
rdBytes   = i2c.readBytes(0x48, 0x00, 4)
```

Read a byte from address `0x24` on a device with an address of `0x27`:
``` python
byteList  = i2c.readBytes(0x27, 0x24, 1)
```
Note that even though only a single byte is being read, the variable `byteList` will be in the form of a list.


[//]: # (Writing)

### Writing to an I2C Slave

All writing functions share the same schema for return values:
* For a successful write, `0` will be returned
* An unsuccessful write will return `1`

[//]: # (Writing: Single Byte)

#### Write a Single Byte

This function will write a single byte to a specific device on the I2C bus:
``` python
status 	= i2c.writeByte(devAddr, addr, value)
```

**Arguments**

The `devAddr` argument defines the I2C slave device address. 

The `addr` argument defines the address on the device that will be written to.

The `value` argument is the single byte to be written.


**Examples**

Write `0xef` to address `0xf1` on a device with an address of `0x11`:
``` python
status  = i2c.writeByte(0x11, 0xf1, 0xef)
```

Write `0xbe` to address `0xaa` on a device with an address of` 0x33`:
``` python
status  = i2c.writeByte(0x33, 0xaa, 0xbe)
```


[//]: # (Writing: Multiple Bytes)

#### Write a List of Bytes

This function will write a list of bytes to an address on a specific device on the I2C bus:
``` python
status  = i2c.writeBytes(devAddr, addr, values)
```

**Arguments**

The `devAddr` argument defines the I2C slave device address. 

The `addr` argument defines the address on the device that will be written to.

The `values` argument is the list of bytes to be written.


**Examples**

Write `0xde, 0xad, 0xbe, 0xef` to address `0x1a` on a device with an address of `0x66`:
``` python
bytes   = [0xde, 0xad, 0xbe, 0xef]
status  = i2c.writeBytes(0x66, 0x1a, bytes)
```

Write `0xbe` to address `0xaa` on a device with an address of `0x33`:
``` python
status  = i2c.writeBytes(0x33, 0xaa, [0xbe])
```

Write `0x01, 0x03, 0x05` to address `0x55` on a device with an address of `0x24`:
``` python
status  = i2c.writeBytes(0x24, 0x55, [0x01, 0x03, 0x05])
```


[//]: # (Writing: Multiple Bytes w/ No Address)

#### Write a List of Bytes without Specifying an Address

This function will write a list of bytes to a specific device on the I2C bus:
``` python
status  = i2c.write(devAddr, values)
```

It can be used when no specific on address on the device needs to be specified.

**Arguments**

The `devAddr` argument defines the I2C slave device address. 

The `values` argument is the list of bytes to be written.


**Examples**

Write `0xde, 0xad, 0xbe, 0xef` to a device with an address of `0x67`:
``` python
bytes   = [0xde, 0xad, 0xbe, 0xef]
status  = i2c.write(0x67, bytes)
```

Write `0xaa, 0xbe` to a device with an address of `0x34`:
``` python
status  = i2c.write(0x34, [0xaa, 0xbe])
```

Write `0x01, 0x03, 0x05, 0x02, 0x04, 0x06, 0xaa` to a device with an address of `0x13`:
``` python
bytes   = [0x01, 0x03, 0x05, 0x02, 0x04, 0x06, 0xaa]
status  = i2c.write(0x13, bytes)
```

