## Relay Expansion C Library {#relay-expansion-c-library}

The Onion Relay Expansion library, `libonionrelayexp` is a dynamic C library that provides functions to setup, read, and change the state of the relays on the Relay Expansion.

![Relay Expansion](http://i.imgur.com/iPswHOC.jpg)

The library can be used in C and C++ programs.

This library is also available as a [module for use in Python](./Relay-Expansion-Python-Module). The module is called `relayExp` and is part of the `OmegaExpansion` package.






<!-- Programming Flow -->

### Programming Flow

After each power-cycle, the chip that controls the Relay Expansion must be programmed with an initialization sequence. After the initialization, the relays can be turned on and off at will.



<!-- I2C Device Address -->

### I2C Device Address

The Relay Expansion is the only expansion that has a configurable I2C device address. This was done so that up to eight Relay Expansions can be stacked on a single Omega, giving the user the ability to control 16 relay modules independently.

The base device address is `0x20`, the dip switches control the offset added to the base address:
* The 'Off' position for each switch is when the toggle is close to the numbers on the switch, or away from the relay modules.
* The 'On' position is when the toggle is away from the numbers on the switch, or closer to the relay modules.

The table below defines the relationship:

| Switch 1 | Switch 2 | Switch 3 | I2C Device Address |
|----------|----------|----------|--------------------|
| Off      | Off      | Off      | *0x27*             |
| Off      | Off      | On       | *0x26*             |
| Off      | On       | Off      | *0x25*             |
| Off      | On       | On       | *0x24*             |
| On       | Off      | Off      | *0x23*             |
| On       | Off      | On       | *0x22*             |
| On       | On       | Off      | *0x21*             |
| On       | On       | On       | *0x20*             |


**All of the functions in this library will require an address argument that specifies the offset to add to the base address of `0x20`**



<!-- MAJOR HEADING -->
<!-- The C Library -->

### The C Library

The `libonionrelayexp` C library is a series of functions that perform all of the actions specified in the [Programming Flow section](#Programming-Flow).


<!-- Source Code -->

#### Source Code

The source code can be found in the [Onion `i2c-exp-driver` GitHub Repo](https://github.com/OnionIoT/i2c-exp-driver).


<!-- Using the C Library -->

#### Using the C Library

**Header File**

To add the Onion Relay Expansion Library to your program, include the header file in your code:
``` c
###include <relay-exp.h>
```

**Library for Linker**

In your project's makefile, you will need to add the following dynamic libraries to the linker command:
``` c
-loniondebug -lonioni2c -lonionmcp23008 -lonionrelayexp
```

The dynamic libraries are stored in `/usr/lib` on the Omega.


<!-- Using the C Library: Example Code -->

#### Example Code

The Onion Relay Expansion C library is used in the implementation of [the `relay-exp` command line tool.](../../Tutorials/Expansions/Using-the-Relay-Expansion#using-the-command-line).

The source code can be found [here](https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/main-relay-exp.c), on the `i2c-exp-driver` Onion GitHub Repo.


<!-- Return Values -->

#### Return Values

All functions follow the same pattern with return values:

If the function operation is successful, the return value will be `EXIT_SUCCESS` which is a macro defined as `0` in `cstdlib.h.`

If the function operation is not successful, the function will return `EXIT_FAILURE` which is defined as `1`.

A few reasons why the function might not be successful:
* The specified device address cannot be found on the I2C bus (the Expansion is not plugged in)
* The system I2C interface is currently in use elsewhere

An error message will be printed that will give more information on the reason behind the failure.


<!-- Types -->

#### Types

This library has only one enumerated type defined and it is meant to easily define which relay module on the device is to be used.

The enumerated type is defined as follows:
``` c
typedef enum e_RelayDriverChannels {
	RELAY_EXP_CHANNEL0 		= 0,
	RELAY_EXP_CHANNEL1,
	RELAY_EXP_NUM_CHANNELS,
} ePwmDriverAddr;
```

![Relay Channel Identification](https://i.imgur.com/Wk6Z9lW.png)



<!-- Functions -->

#### Functions

Each of the main functions implemented in this library are described below.


<!-- Init Function -->

##### Initialization Function

This function programs the initialization sequence on the Relay Expansion, after this step is completed, the functions to set the relay states can be used with success:
``` c
int relayDriverInit (int addr);
```

**Arguments**

The `addr` argument is described above in the [I2C Device Address section](#i2c-device-address).


**Examples**

Initialize a Relay Expansion with all switches set to 0, meaning the I2C device address will be 0x27:
``` c
int status 	= relayDriverInit(7);
```

Initialize with switches set to on-off-on (device address: 0x22):
``` c
int status 	= relayDriverInit(2);
```

Initialize with switches set to on-on-off (device address: 0x24):
``` c
int status 	= relayDriverInit(4);
```




<!-- Check Init Function -->

##### Check for Initialization

This function performs several reads to determine if the Relay Expansion requires the initialization sequence to be programmed before the relay states can be changed.

``` c
int relayCheckInit (int addr, int *bInitialized);
```

**Arguments**

The `addr` argument is described above in the [I2C Device Address section](#i2c-device-address).

The `bInitialized` argument is to be passed by reference and once the function executes, it will contain a value that corresponds whether or not the Expansion is currently in the initialized state.
The value follows the table below:

| Initialization Status | bInitialized |
|-----------------------|--------------|
| Not Initialized       | 0            |
| Initialized           | 1            |


**Example**

Check if a Relay Expansion (with all switches set to On) is initialized:
```c
int status, bInit;
status 	= relayCheckInit(0, &bInit);

if (bInit == 0) {
	printf("The Relay Expansion needs to be initialized\n");
}
else {
	printf("The Relay Expansion is good to go!\n");
}
```


<!-- Set Relay State Function -->

##### Set Relay State

Finally the fun stuff! Use this function to change the state of the relay:

``` c
int relaySetChannel	(int addr, int channel, int state);
```

**Arguments**

The `addr` argument is described above in the [I2C Device Address section](#i2c-device-address).

The `channel` argument selects the relay in question. See the [diagram above](#the-c-library_types) for info on which channel corresponds to which relay.

The `state` argument allows the user to select if the relay will be turned on or off:
* 0 turn the relay OFF
* 1 turn the relay ON

**Example**

Turn Relay0 **on** and Relay1 **off** (all switches are Off)
``` c
status 	=  relaySetChannel (7, 0, 1);
status 	|= relaySetChannel (7, 1, 0);
```


<!-- Set State for Both Relays Function -->

##### Set State for both Relays

In the event that both relays need to be turned on or off at the same time:

``` c
int relaySetAllChannels	(int addr, int state);
```

This is performed with a single register write so both relays should react at the same time.


**Arguments**

The `addr` argument is described above in the [I2C Device Address section](#i2c-device-address).

The `state` argument allows the user to select if the relays will be turned on or off:
* 0 turn the relays OFF
* 1 turn the relays ON

**Example**

All switches are in Off position, turn both relays on, then turn Relay0 off, then send a command to turn both off:
``` c
status 	=  relaySetAllChannels (7, 1);
status 	|= relaySetChannel (7, 0, 0);
status 	|= relaySetAllChannels (7, 0);
```

<!-- Read Relay State -->

##### Read Relay State

Use this function to read the state of a specific relay:

``` c
int relayReadChannel (int addr, int channel, int *state);
```

**Arguments**

The `addr` argument is described above in the [I2C Device Address section](#i2c-device-address).

The `channel` argument selects the relay in question. See the [diagram above](#the-c-library_types) for info on which channel corresponds to which relay.

The `bInitialized` argument is to be passed by reference and once the function executes, it will contain a value that corresponds whether or not the Expansion is currently in the initialized state.
The value follows the table below:

The `state` argument is to be passed by reference and once the function executes, it will containt the state of the relay in question:
* `0` indicating the relay is OFF
* `1` indicating the relay is ON

**Example**

Read the state of Relay 0 with all switches in Off position:
``` c
int state, status;
int channel = 0;

status	= relayReadChannel(7, channel, &state);

if (status == EXIT_SUCCESS) {
	if (state == 0) {
		printf("Relay%d is OFF!", channel);
	}
	else {
		printf("Relay%d is ON!", channel);
	}
}
```
