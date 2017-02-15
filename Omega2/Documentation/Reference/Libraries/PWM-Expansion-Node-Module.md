## PWM Expansion Node Module

The Onion PWM Node Module, node-pwm-exp is a wrapper around the `libonionpwmexp` dynamic C library that provides functions to setup the servo Expansion and generate PWM signals.


<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/aNoYCZc.png)


### Programming Flow

After each power-cycle, the chip that controls the PWM Expansion must be programmed with an initialization sequence to enable the on-board oscillator so that PWM signals can be generated.

After the initialization, the other functions can be used to generate PWM signals on specific channels or to change the PWM signal frequency.

Additionally, it is possible to disable to the oscillator, disabling the generation of all PWM signals at once. 

Before generating new PWM signals, the initialization sequence must be run again.

### PWM Refresher

The PWM Expansion has 16 channels that can generate distinct PWM signals. Note that they will all be running on the **same frequency**

Pulse Width Modulated signals can be described with duty cycle percentages and frequencies/periods:


<!-- TODO: IMAGE reupload this to github -->

![imgur](http://www.bristolwatch.com/picaxe/images/io43.gif)

The **duty cycle** indicates what percentage of time a signal is on or high voltage.

The **frequency** determines the overall period of the pulse.

For a more detailed explanation, see the guide on using the [PWM Expansion](https://docs.onion.io/omega2-docs/using-pwm-expansion.html).

### The Node Module

The node-pwm-exp exposes a series of methods that perform all of the actions specified in the Programming Flow section.

#### Install the Module

Install the module on your Omega:

``` bash
opkg update
opkg install node-pwm-exp
```

NodeJS will need to be installed to run any Node programs:
``` bash
opkg install nodejs
```

#### Importing the Module

To use the module within your script you have to import it into your node program as you would a module:

``` javascript
var oledModule = require("/usr/bin/node-pwm-exp");
```




#### Example Code

Example code that uses the `node-pwm-exp` module can be [found here](https://github.com/OnionIoT/i2c-exp-node-addons/blob/master/Examples/pwm_node_example.js) in the `i2c-exp-node-addons` Onion GitHub Repo.



#### Return Values

All of the functions will either return a 0 indicating success or 1 indicating failure.

#### Calling Methods

Methods are called in the following format.

``` javascript
pwmExp.method();
```

Replace method with your funcion of interest.


#### Available Methods

Refer to the table below for a list and brief description of available PWM methods.

|  Method |   Inputs|  Description |
|---|---|---|
|driverInit()|none| Initialize the PWM expansion for use|
|setupDriver(int driverNum, float duty, float delay )| 0-15 or -1, 0-100, 0-100 |Generates the specified PWM signal on the specified channel|
|setFrequency(float freq)| 24-1526| Sets the frequency for the oscillator chip|
|disableChip()|none|Disables the oscillator chip and stops all PWM signals|



### Initialization Function

This function programs the initialization sequence on the PWM Expansion, after this step is completed, the functions to generate PWM signals or change the signal frequency can be used with success:
``` javascript
pwmExp.driverInit();
```

### Check for Initialization

This function performs several reads to determine if the PWM Expansion has been initialized and the oscillator is running.
```javascript
pwmExp.checkInit()
```

#### Examples

Let's check if the oscillator is initialized.
```javascript
if (pwmExp.checkInit()) {
  console.log('Oscillator sucessfull initialized');
} else {
  console.error('Error with oscillator initializing');
}
```

### Generate a PWM Signal
Here we go! Use this function to generate a PWM signal on a specified channel:
``` javascript
pwmExp.setupDriver(int driverNum, float duty, float delay);
```

#### Arguments

The `driverNum` argument is detemines on which channel to generate the PWM signal. The accepted values are:

| Value | Meaning                                   |
|-------|-------------------------------------------|
| 0-15  | Matches the label on the PWM Expansion  |
| -1    | Generates the same signal on all channels |

The `duty` argument specifies duty cycle percentage for the PWM signal. Accepted values are 0 to 100. Decimal values are allowed.

The `delay` argument specifies the percentage delay before the PWM signal goes high. Accepted values are 0 to 100 with decimal values being allowed. In normal use with servos this should be set to 0.

#### Examples

Set channel 0 to a PWM signal with a 50% duty cycle:
``` javascript
pwmExp.setupDriver(0,50,0);
```

Generate a 3.55% duty cycle PWM signal with a 45% delay on channel 7:
``` javascript
pwmExp.setupDriver(7, 3.55f, 45);
```

Set channel 0 to a PWM signal with a 50% duty cycle:
``` javascript
pwmExp.setupDriver(15, 100, 0);
```

Set channel 8 to always off:
``` javascript
pwmExp.setupDriver(8, 0, 0);
```

Set all channels to a 15.65% duty cycle PWM signal:
``` javascript
pwmExp.setupDriver(-1, 15.65f, 0.0f);
```

### Set PWM Signal Frequency

The oscillator can be reprogrammed to generate a variety of different frequencies:
``` javascript
pwmExp.setFrequency(float freq);
```
The default frequency is 50 Hz.

This method changes the frequency of the PWM signals generated on all of the channels. The oscillator can generate frequencies between 24 Hz and 1526 Hz.

#### Arguments

The `freq` argument is a floating point number that specifies the frequency. The function will accept any input but the programmed frequency will be clamped between 24 Hz and 1526 Hz.

#### Examples

Change the frequency to 60 Hz and generate a 40% duty cycle signal on channel 14:

``` javascript
pwmExp.setFrequency(60);
pwmExp.setupDriver(14,40,0);
```

Generate a signal on channel 13, change the chip frequency to 105.45 Hz, and generate a new signal on channel 13:
``` javascript
pwmExp.setupDriver(13,99,0);
pwmExp.setFrequency(105.45);
pwmExp.setupDriver(13,82,0);
```

### Disabling the Oscillator

The oscillator can also be disabled, automatically stopping all PWM signal generation:

``` javascript
pwmExp.disableChip();
```

This might be useful for disabling PWM signal-driven devices while not powering off the Omega. **The initialization function will have to be run before new PWM signals can be generated**
