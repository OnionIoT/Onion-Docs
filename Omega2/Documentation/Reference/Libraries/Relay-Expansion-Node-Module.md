## Relay Expansion Node Module

The Onion Relay Node Module, node-relay-exp is a wrapper around the `libonionrelayexp` dynmic C library that provides functions to setup and control the relay expansion.

<!-- TODO: IMAGE reupload this to github -->

![Relay Expansion](http://i.imgur.com/iPswHOC.jpg)

The same library is available for use in C and Python programs.


### Programming Flow {#relay-node-programming-flow}


After each power-cycle, the chip that controls the Relay Expansion must be programmed with an initialization sequence. After the initialization, the relays can be turned on and off at will.


```{r child = '../Shared/I2C-Device-Address.md'}
```


### The Node Module {#relay-node-description}

The node-relay-exp module exposes a series of methods that perform all of the actions specified in the Programming Flow section.

#### Install the Module

Install the module on your Omega:

``` bash
opkg update
opkg install node-relay-exp
```

NodeJS will need to be installed for Node programs to actually run:

``` bash
opkg install nodejs
```

#### Importing the module into your Node Script

To use the module within your script you have to import it into your node program as you would a module:

``` javascript
var relayExp = require("/usr/bin/node-relay-exp");
```


#### Example Code

Example code that uses the `node-relay-exp` module can be [found here](https://github.com/OnionIoT/i2c-exp-node-addons/blob/master/Examples/relay_node_example.js) in the `i2c-exp-node-addons` Onion GitHub Repo.


#### Return Values

All of the functions will either return a 0 indicating success or 1 indicating failure.


#### Calling Methods

Methods are called in the following format.

``` javascript
relayExp.method();
```
Replace method with your funcion of interest.


### Available Methods {#relay-node-function-table}

Refer to the table below for a list and brief description of available relay methods.

| Methods                                      | Inputs      | Description                                                                                   |
|----------------------------------------------|-------------|-----------------------------------------------------------------------------------------------|
| [init(int addr)](#relay-node-init)                               | 0-7         | Initializes the selected relay expansion (0-7), relay states can be set after initialization. |
| [checkInit(int addr)](#relay-node-check-init)                          | 0-7         | Checks initialization state of selected relay expansion.                                      |
| [setChannel(int addr, int channel, int state)](#relay-node-set-channel) | 0-7,0-1,0-1 | Sets the selected channel on the selected relay to the specified states.                      |
| [setAllChannels(int addr, int state)](#relay-node-set-all-channels)          | 0-7,0-1     | Sets all channels on the selected relay expansion to the specified state.                     |

### Initialization Function {#relay-node-init}

This function programs the initialization sequence on the Relay Expansion, after this step is completed, the functions to set the relay states can be used with success:

``` javascript
relayExp.init(int addr);
```

#### Arguments

The `addr` argument is described above in the [I2C Device Address](#relay-node-i2c-device-address) section.

#### Examples

Initialize a Relay Expansion with all switches set to 0, meaning the I2C device address will be 0x27:

``` javascript
relayExp.init(7);
```

Initialize with switches set to on-off-on (device address: 0x22):

``` javascript
relayExp.init(2);
```

Initialize with switches set to on-on-off (device address: 0x24):

``` javascript
relayExp.init(4);
```

### Check for Initialization {#relay-node-check-init}

This function performs several reads to determine if the Relay Expansion requires the initialization sequence to be programmed before the relay states can be changed.

``` javascript
relayExp.checkInit(int addr);
```

#### Arguments

The `addr` argument is described above in the [I2C Device Address](#relay-node-i2c-device-address) section.

#### Examples

<!-- TODO: all switches set to on? '(with all switches set to On)' -->

Check if a Relay Expansion is initialized:

``` javascript
relayExp.checkInit(0);
```



### Set Relay State {#relay-node-set-channel}

Finally the fun stuff! Use this function to change the sate of the relay:

``` javascript
relayExp.setChannel(int addr, int  channel, int state);
```

#### Arguments

|  Argument  |  Input                |  Meaning                                |
|------------|:---------------------:|-----------------------------------------|
| addr       |  `0 - 7`            |  I2C Device Address                     |
| channel    |  `0`, `1`         |  Relay channel                          |
| state      |  `0`, `1`         |  Relay state (`0` - Off, `1` - On)  |

The `addr` argument is described above in the [I2C Device Address](#relay-node-i2c-device-address) section.



#### Examples

<!-- TODO: all switches off? -->

Let's turn Relay0 **on** and Relay1 **off**. <!-- (all switches Off) -->

``` javascript
relayExp.setChannel(7,0,1);
relayExp.setChannel(7,1,0);
```

### Set State for both Relays {#relay-node-set-all-channels}

In the event that both relays need to be turned on or off at the same time:

``` javascript
relayExp.setAllChannels(int addr, int state);
```

This is performed with a single register write so both relays should react at the same time.

#### Arguments

|  Argument  |  Input                |  Meaning                                |
|------------|:---------------------:|-----------------------------------------|
| addr       |  `0 - 7`            |  I2C Device Address                     |
| state      |  `0`, `1`         |  Relay state (`0` - Off, `1` - On)  |

The `addr` argument is described above in the [I2C Device Address](#relay-node-i2c-device-address) section.


#### Examples

All switches are in Off position, turn both relays on, then turn Relay 0 off, the send a command to turn both off:
``` javascript
relayExp.setAllChannels(7,1);
relayExp.setChannel(7,0,0);
relayExp.setAllChannels(7,0);
```
