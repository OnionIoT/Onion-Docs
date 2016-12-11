## PWM Expansion Python Module {#pwm-expansion-pytho-module}

The Onion PWM Expansion Python module, `pwmExp` is based on the [C PWM Expansion Library](./PWM-Expansion-C-Library). Using this module, you will be able to control the PWM Expansion from within your Python program.

![PWM Expansion Photo](http://i.imgur.com/aNoYCZc.png)


[[_TOC_]]



[//]: # (Programming Flow)

### Programming Flow

After each power-cycle, the chip that controls the PWM Expansion must be programmed with an initialization sequence to enable the on-board oscillator so that PWM signals can be generated.

After the initialization, the other functions can be used to generate PWM signals on specific channels or to change the PWM signal frequency.

Additionally, it is possible to disable to the oscillator, disabling the generation of all PWM signals at once. Before generating new PWM signals, the initialization sequence must be run again.


#### Channels

The PWM Expansion has 16 channels that can generate distinct PWM signals. Note that they will all be running on the same frequency.



[//]: # (PWM Signal Refresher)

### PWM Signal Refresher

Pulse Width Modulated signals can be described with duty cycle percentages and frequencies/periods:

![Duty Cycle Graph](http://www.bristolwatch.com/picaxe/images/io43.gif)

The **duty cycle** indicates what percentage of time a signal is on or high voltage.

The **frequency** determines the overall period of the pulse.

For a more detailed explanation, see the guide on [using the Servo Expansion.](../../Tutorials/Expansions/Using-the-Servo-Expansion#pwm-signals)
[//]: # (MAJOR HEADING)
[//]: # (The Python Module)

### The Python Module

The `pwmExp` Python module in the `OmegaExpansion` package provides a wrapper around the C library functions. The functions are largely the same as their C counterparts, including the arguments and return values. Any differences from the C library will be explicitly mentioned below.


[//]: # (Source Code)

#### Source Code

The source code can be found in the [Onion `i2c-exp-driver` GitHub Repo](https://github.com/OnionIoT/i2c-exp-driver).


[//]: # (Using the Python Module)

#### Using the Python Module

**Installing the Module**

To install the Python module, run the following commands:
```
opkg update
opkg install python-light pyPwmExp
```

This will install the module to `/usr/lib/python2.7/OmegaExpansion/`

*Note: this only has to be done once.*


**Using the Module**

To add the Onion PWM Expansion Module to your Python program, include the following in your code:
``` python
from OmegaExpansion import pwmExp
```


[//]: # (Python: Example Code)

#### Example Code

Example code that uses the `pwmExp` module can be [found here](https://github.com/OnionIoT/i2c-exp-driver/blob/master/examples/pwm-exp.py), in the `i2c-exp-driver` Onion GitHub Repo.



[//]: # (Python: Return Values)

#### Return Values

All functions follow the same pattern with return values:

If the function operation is successful, the return value will be `0`.

If the function operation is not successful, the function will return `1`.


[//]: # (Python Functions)

#### Functions

Each of the main functions implemented in this module are described below.

[//]: # (Python: Init Function)

##### Initialization Function

This function programs the initialization sequence on the Servo Expansion, after this step is completed, the functions to generate PWM signals or change the signal frequency can be used with success:
``` python
pwmExp.driverInit()
```

**Examples**

Initialize the PWM Expansion:
``` c
status 	= pwmExp.driverInit();
```


[//]: # (Python: Check Init Function)

##### Check for Initialization

This function performs several reads to determine if the Servo Expansion has been initialized and the oscillator is running:

``` python
pwmExp.checkInit()
```

The **return value** of the function indicates the Initialization Status:

| Return Value | Initialization Status |
|--------------|-----------------------|
| 0            | Not Initialized       |
| 1            | Initialized           |

**Example**

Check if the PWM Expansion is initialized:
``` python
bInit 	= pwmExp.checkInit()

if (bInit == 0):
	print 'The Servo Expansion needs to be initialized\n'
else:
	print 'The Servo Expansion is up and running!'
}
```


[//]: # (Python: Generate PWM Signal Function)

##### Generate a PWM Signal

This function is used to generate a PWM singal on a specified channel:
``` python
pwmExp.setupDriver(channel, duty, delay)
```

**Arguments**

The `channel` argument determines on which channel to generate the PWM signal.
* 0 to 15 will select a specific channel
* -1 will generate the same signal on all channels

The `duty` argument specifies duty cycle percentage for the PWM signal. Accepted values are **0 to 100**. Decimal values are allowed.


The `delay` argument specifies the percentage delay before the PWM signal goes high. Accepted values are **0 to 100** with decimal values being allowed. *In normal use with servos this should be set to 0.*


**Example**

Set channel 7 to 6.55% duty cycle:
``` python
status = pwmExp.setupDriver(7, 6.55, 0)
```

Set channel 14 to always on:
``` python
status = pwmExp.setupDriver(14, 100, 0)
```

Set all channels to 66.66% duty with a 9% delay:
``` python
status = pwmExp.setupDriver(-1, 66.66, 9)
```


[//]: # (Python: Set Signal Frequency)

##### Set PWM Signal Frequency

The oscillator can be reprogrammed to generate a variety of different frequencies:
``` python
pwmExp.setFrequency(frequency)
```

This will change the frequency of the PWM signals generated on all of the channels.
The oscillator can generate frequencies between **24 Hz and 1526 Hz,** the default value is **50 Hz.**


**Arguments**

The `freq` argument is a floating point number that specifies the frequency. The function will accept any input but the programmed frequency will be clamped between 24 Hz and 1526 Hz.


**Example**

Change the frequency to 60 Hz:
``` python
status = pwmExp.setFrequency(60)
```

Change the frequency to 92.23 Hz:
``` python
status = pwmExp.setFrequency(92.23)
```


[//]: # (Python: Disable Oscillator)

##### Disabling the Oscillator

The oscillator can also be disabled, automatically stopping all PWM signal generation:
``` python
pwmExp.disableChip()
```

This might be useful for disabling PWM signal-driven devices while not powering off the Omega.
**The initialization function will have to be run before new PWM signals can be generated.**


**Example**

Disable the oscillator:
``` python
status 	= pwmExp.disableChip()
```
