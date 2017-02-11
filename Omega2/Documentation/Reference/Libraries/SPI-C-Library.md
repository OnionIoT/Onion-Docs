## SPI C Library {#spi-c-library}

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

#### Linux and SPI

Linux systems usually control SPI devices through kernel drivers. However, it is also possible to generate the SPI protocol by bit-banging on connecte GPIOs. Bit-banging SPI is done through an adapter usually found at `/dev/spidevX.Y` where `X` is the device number and `Y` is the bus number.

The Omega does not have an SPI bit-banging adapter setup by default, but this can be done by using the `insmod` command to insert a module into the kernel. The `libonionspi` library takes care of this for you so you don't have to deal with the intricacies.



<!-- MAJOR HEADING -->
<!-- The C Library -->

### The C Library

The `libonionspi` C library is a series of functions that implement SPI communication through the Linux device interface.


<!-- Source Code -->

#### Source Code

The source code can be found in the [Onion `spi-gpio-driver` GitHub Repo](https://github.com/OnionIoT/spi-gpio-driver).


<!-- Programming Flow -->

#### Programming Flow

Any program using the `libonionspi` library must first initialize the `spiParams` structure since it is used by all of the other library functions. Then, the `spiParams` structure members should be modified to suit the requirements of the use case. For example, the desired bus number and device ID should be programmed.

Transactions will not work if the SPI adapter is not registered with the system, there are functions to check if an adapter is registered, and if not, to register the adapter. There is also a setup function to set  additional parameters on the adapter.

After the above is complete, the functions to transfer data using the SPI protocol can be used freely



#### Header File

To add the Onion SPI Library to your C/C++ program, include the header file in your C code:
``` c
#include <onion-spi.h>
```

#### Library for Linker

In your project's makefile, you will need to add the following dynamic libraries to the linker command:
``` c
-loniondebug -lonionspi
```

The dynamic libraries are stored in `/usr/lib` on the Omega.



<!-- Example Code -->

#### Example

An example of how the `libonionspi` library is used can be found in the C implementation of the [command line SPI tool.](https://github.com/OnionIoT/spi-gpio-driver/blob/master/src/main-spi-tool.c)

Additional example code can be found in the sections below.



<!-- Return Values -->

#### Return Values

All functions follow the same pattern with return values:

If the function operation is successful, the return value will be `EXIT_SUCCESS` which is a macro defined as `0` in `cstdlib.h.`

If the function operation is not successful, the function will return `EXIT_FAILURE` which is defined as `1`.

Any deviations from this rule will be specified below.



<!-- Parameter Structure -->

#### Parameter Structure

The `spiParams` structure is the central location that stores all of the data required by the library functions:
``` c
struct spiParams {
	// bus number and device id
	int 	busNum;
	int 	deviceId;

	int		speedInHz;		// system clock frequency
	int 	delayInUs;		// delay after last bit transferred before optionall deselecting the device before the next transfer
	int 	bitsPerWord;	// how many bits are in a transfered word

	int 	mode;			// SPI mode: can be 0 to 3 (0 is the most common)
	int 	modeBits;		// additional SPI setup

	// Omega GPIO definitions
	int 	sckGpio;
	int 	mosiGpio;
	int 	misoGpio;
	int 	csGpio;
};
```

##### SPI Mode Bits

Additional SPI options can be setup on the interface by adding specific bits to the `modeBits` member of the structure. Macros exist to define which bits need to be set.

The following macros are available:
* `SPI_3WIRE`
  * Use three-wire implementation of SPI where the MOSI and MISO lines are shared on a single GPIO.
* `SPI_NO_CS`
  * Modify the protocol to not generate a Chip-Select line.
* `SPI_CS_HIGH`
  * Modify the protocol for an active-high Chip-Select line.
* `SPI_LSB_FIRST`
  * Modify the protocol to transmit bytes LSB to MSB.
* `SPI_LOOP`
  * Enable loopback mode where the slave is configured to transmit the received bytes. This can be achieved with a single master by wiring the MISO and MOSI lines together.

To enable any one of the options, perform a bitwise `or` operation with the `modeBits` structure member:
``` c
params.modeBits |= SPI_CS_HIGH;
params.modeBits |= SPI_LSB_FIRST;
```

Then run the `spiSetupDevice()` function to set the options in the adapter device. More information on this function in the sections below.



<!-- SUB-HEADING -->
<!-- Setup Functions -->

#### Setup Functions

The following functions serve to initialize the `spiParams` structure and do any SPI adapter setup required to actually perform transfers.

<!-- Initialize the Parameter Structure -->

### Initialize the Parameter Structure: `spiParamInit()`

There is a function to initialize the `spiParams` structure with acceptable default values:
``` c
void spiParamInit (struct spiParams *params);
```

The default settings:

| SPI Setting | Programmed Default                  |
|-------------|-------------------------------------|
| speedInHz   | 100000 Hz (100 kHz)                 |
| delayInUs   | 0                                   |
| bitsPerWord | 0 (Corresponds to 8 bits per  word) |
| mode        | SPI Mode 0                          |


Sets the SPI lines to the following GPIOs:

| SPI Signal | Omega Gpio |
|------------|------------|
| SCK        | 6          |
| MOSI       | 18         |
| MISO       | 1          |
| CS/SS      | 7          |


**Arguments**

The `params` argument should be the structure you want to initialize passed by reference.


<!-- Check if SPI Device is Mapped -->

### Check if SPI Device is Mapped: `spiCheckDevice()`

Performs a check to see if an SPI device with the specified bus number and device ID is mapped:

``` c
int spiCheckDevice (int busNum, int devId, int printSeverity);
```

**Return Value**

If the SPI device adapter is found, the function returns `EXIT_SUCCESS`, a macro mapped to `0`

If the SPI device adapter is **not found**, the function returns `EXIT_SUCCESS`

**Arguments**

The `busNum` and `devId` specify the bus number and device ID of the adapter, respectively.

The print severity refers to the Onion Debug Library verbosity level. For now set to `ONION_SEVERITY_DEBUG_EXTRA` for no additional messages printed.
**More info on this to come.**


**Examples**

To check if a device on bus 1 with device ID 2 is registered, and print out a message based on the result:
``` c
int status;

status 	= spiCheckDevice(1, 2, ONION_SEVERITY_DEBUG_EXTRA);
if (status == EXIT_SUCCESS) {
	printf("SPI Device is mapped.\n");
}
else {
	printf("WARNING: SPI Device NOT mapped!\n");
}
```


<!-- Register SPI Device -->

### Register SPI Device: `spiRegisterDevice()`

This function will register an SPI device with the bus number, device ID, and other SPI parameters as specified in the parameter structure:

``` c
int spiRegisterDevice (struct spiParams *params);
```

It will first check if a device with the specified bus number and device ID is already registered. If it is, it will just return `EXIT_SUCCESS`.

If not, it will attempt to register the SPI device adapter by inserting an SPI-gpio module into the kernel. If this operation is successful, the function will return `EXIT_SUCCESS`, if not, `EXIT_FAILURE` is returned.


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
``` c
int 	status;
struct  spiParams	params;

// initialize the SPI parameters
spiParamInit(&params);

// set the desired bus number and device id
params.busNum 	= 0;
params.devId 	= 1;

// change the CS line to use GPIO23
params.csGpio 	= 23;

// register the device
status 	= spiRegisterDevice(&params);

```


<!-- Setup SPI Device -->

### Setup SPI Device: `spiSetupDevice()`

This function will setup additional SPI parameters on the device adapter
``` c
int spiSetupDevice (struct spiParams *params);
```

It will setup the following SPI parameters:
* The maximum speed of the link
* The number of bits per word
* Additional mode information, see [section on additional mode information above](#the-c-library_parameter-structure_spi-mode-bits)



<!-- SUB-HEADING -->
<!-- Communication Functions -->

#### Communication Functions

Once a device adapter is registered, the functions below can be used to read from and write data to the device via SPI.


<!-- Transfer Data Function -->

### Transferring Data: `spiTransfer()`

This is the function that implements all data transfers using the SPI protocol:
``` c
int spiTransfer	(struct spiParams *params, uint8_t *txBuffer, uint8_t *rxBuffer, int bytes);
```

**Arguments**

The `params` spiParams structure holds all of the relevant SPI information.

The `txBuffer` argument will hold the data to be transferred via SPI.

The `rxBuffer` argument will be populated by data received during the SPI transfer.

And finally, the `bytes` argument indicates the number of bytes being transferred. Note that the txBuffer and rxBuffer need to be allocated to at least this size.


<!-- Transfer Data Function: Example Code: Reading -->

###### Example Code: Reading a Byte

The following example code uses the SPI protocol to read a byte of data from a specific address on an SPI device:

``` c
void SpiReadValue(int addr)
{
	int 		status, size;
	uint8_t 	*txBuffer;
	uint8_t 	*rxBuffer;

	struct spiParams	params;

	// initialize the SPI parameters and set the bus number and device ID
	spiParamInit(&params);
	params.busNum		= 0;
	params.deviceId 	= 1;

	// set the transmission size and allocate memory for the buffers
	size 		= 1;
	txBuffer	= (uint8_t*)malloc(sizeof(uint8_t) * size);
	rxBuffer	= (uint8_t*)malloc(sizeof(uint8_t) * size);

	// assign the register address to the transmission buffer
	*txBuffer 	= (uint8_t)addr;

	// invoke the SPI transfer
	status 	= spiTransfer(&params, txBuffer, rxBuffer, size);

	// rxBuffer now contains the data read through the SPI interface
	printf("> SPI Read from addr 0x%02x: 0x%02x\n", addr, *rxBuffer);

	// clean-up
	free(txBuffer);
	free(rxBuffer);
}
```

During the SPI transfer, the SPI Master (the Omega) will send the contents of the transmission buffer, in this case, the address from which to read. The slave device will respond with a value that corresponds to the register address, this value will be populated into the receive buffer.

In this case, the `size` variable refers to the number of bytes to be read from the SPI device.

Before this function will work, the SPI device adapter needs to be registered, check out [the section above](#the-c-library_setup-functions_register-spi-device-spiregisterdevice).

Some devices require specific bit-wise operations on the address to indicate a read operation. Most common are:
* A bitwise shift to the left
* Setting a specific bit to 1 to indicate a read

Refer to the datasheet of your device for specifics.


<!-- Transfer Data Function: Example Code: Writing -->

###### Example Code: Writing a Value

This example uses the SPI protocol to write a byte of data to a specific address on an SPI device:

``` c
void SpiWriteValue(int addr, int value)
{
	int 		status, size;
	uint8_t 	*txBuffer;
	uint8_t 	*rxBuffer;

	struct spiParams	params;

	// initialize the SPI parameters and set the bus number and device ID
	spiParamInit(&params);
	params.busNum		= 0;
	params.deviceId 	= 1;

	// set the transmission size and allocate memory for the buffers
	size 		= 2;
	txBuffer	= (uint8_t*)malloc(sizeof(uint8_t) * size);
	rxBuffer 	= (uint8_t*)malloc(sizeof(uint8_t) * size);

	// assign the register address and data to be written to the transmission buffer
	txBuffer[0] = (uint8_t)addr;
	txBuffer[1] = (uint8_t)value;

	// invoke the SPI transfer
	status 	= spiTransfer(&params, txBuffer, rxBuffer, size);

	// data has been written
	// any response is now in rxBuffer (usually don't get a response from a write operation so it should be empty)
	printf("> SPI Write to addr 0x%02x: 0x%02x\n", txBuffer[0], txBuffer[1] );

	// clean-up
	free(txBuffer);
	free(rxBuffer);
}
```

In this case, the SPI Master will first send the register address where the write is to be performed, and then the value to be written. Usually the SPI Slave will not send a response, however, the `spiTransfer()` function still requires a buffer to be passed in order to work properly.

<!-- Transfer Data Function: Example Code: Writing Stream of Data -->

###### Example Code: Writing Several Values

Some devices allow/require the user to write a stream of data with no address, this can be accomplished using the `spiTransfer()` function as well:

``` c
void SpiWriteValues(int addr, int* data, int size)
{
	int 		status;
	uint8_t 	*txBuffer;
	uint8_t 	*rxBuffer;

	struct spiParams	params;

	// initialize the SPI parameters and set the bus number and device ID
	spiParamInit(&params);
	params.busNum		= 0;
	params.deviceId 	= 1;

	// allocate memory for the buffers based on input data size
	txBuffer	= (uint8_t*)malloc(sizeof(uint8_t) * size);
	rxBuffer 	= (uint8_t*)malloc(sizeof(uint8_t) * size);

	// fill the transmission buffer with the data
	for (i = 0; i < size; i++) {
		txBuffer[i] = (uint8_t)data[i];
	}

	// invoke the SPI transfer
	status 	= spiTransfer(&params, txBuffer, rxBuffer, size);

	// data has been written
	// any response is now in rxBuffer (usually don't get a response from a write operation so it should be empty)
	printf("> SPI: wrote a %d bytes of data to device\n", size );

	// clean-up
	free(txBuffer);
	free(rxBuffer);
}
```


<!-- Additional Functions -->

##### Additional Functions

The `spiTransfer()` is all that's required to perform reads and writes using SPI. However, two additional functions are provided to perform reads and writes. Internally, they both use the `spiTransfer()` function, but they provide a slightly simpler interface.


<!-- Additional Functions: spiRead -->

### Reading Data: `spiRead()`

This function can be used to perform a register read:

``` c
int spiRead(struct spiParams *params, int addr, uint8_t *rdBuffer, int bytes);
```

It can read a specified number of bytes from a specified address. The limitation is that the address can only be a single byte. Use `spiTransfer()` if your use-case requires more than 8-bits for the address.

**Arguments**

The `params` spiParams structure holds all of the relevant SPI information.

The `addr` argument is the 8-bit address from which to read.

The `rdBuffer` argument will be populated by data received during the SPI transfer.

And finally, the `bytes` argument indicates the number of bytes being read. Note that the `rdBuffer` needs to be allocated to at least this size.


###### Example Code

The following function will read two bytes from the specified address, the data will be stored in `rdBuffer`:

``` c
void SpiReadValue2(int addr)
{
	int 		status, size;
	uint8_t 	*rdBuffer;

	struct spiParams	params;

	// initialize the SPI parameters and set the bus number and device ID
	spiParamInit(&params);
	params.busNum		= 0;
	params.deviceId 	= 1;

	// set the transmission size and allocate memory for the buffers
	size 		= 2;
	rdBuffer	= (uint8_t*)malloc(sizeof(uint8_t) * size);

	// invoke the SPI read
	status 		= spiRead(&params, addr, rdBuffer, size);

	// rdBuffer now contains the data read through the SPI interface
	printf("> SPI Read from addr 0x%02x: 0x%02x, 0x%02x\n", addr, rdBuffer[0], rdBuffer[1]);

	// clean-up
	free(rdBuffer);
}
```

In essence, this simplifies the use of the `spiTransfer()` for read scenarios.
*Note that this function has not been tested as thoroughly as the `spiTransfer()` function.*



<!-- Additional Functions: spiWrite -->

### Reading Data: `spiWrite()`

This function can be used to perform a register write:
``` c
int spiWrite(struct spiParams *params, int addr, uint8_t *wrBuffer, int bytes);
```

It will write a specified number of bytes to a specified address. The limitation is that the address can only be a single byte. Use `spiTransfer()` if your use-case requires more than 8-bits for the address.

**Arguments**

The `params` spiParams structure holds all of the relevant SPI information.

The `addr` argument is the 8-bit address on which to perform the write

The `wrBuffer` argument holds the data to be transmitted during the SPI transfer.

And finally, the `bytes` argument indicates the number of bytes being written. Note that the `wdBuffer` needs to be allocated to at least this size.


###### Example Code

The following code will write a byte to the specified address, the data will be stored in `rdBuffer`:

``` c
void SpiWriteValue2(int addr, int value)
{
	int 		status, size;
	uint8_t 	*wrBuffer;

	struct spiParams	params;

	// initialize the SPI parameters and set the bus number and device ID
	spiParamInit(&params);
	params.busNum		= 0;
	params.deviceId 	= 1;

	// set the transmission size and allocate memory for the buffers
	size 		= 1;
	wrBuffer	= (uint8_t*)malloc(sizeof(uint8_t) * size);

	// put the value to be written in the wrBuffer
	*wrBuffer 	= (uint8_t)value;

	// invoke the SPI read
	status 		= spiWrite(&params, addr, wrBuffer, size);

	// data in wrBuffer has been written to the SPI device
	printf("> SPI Write to addr 0x%02x: 0x%02x\n", addr, *wrBuffer );

	// clean-up
	free(wrBuffer);
}
```

This function simplifies the use of `spiTransfer()` for scenarios where SPI is used to write to a register.
*Note that this function has not been tested as thoroughly as the `spiTransfer()` function.*
