# Onion GPIO Python Module

The `onionGpio` Python module provides a Python object, `OnionGpio` that allows programs to control the Omega's GPIOs. The module uses the sysfs GPIO interface that is part of the Linux operating system.


[[_TOC_]]


[//]: # (Python: Programming Flow)

# Programming Flow

Once the `OnionGpio` object is initialized, the class methods can be used to:
* Set the GPIO to the input or output direction
* Read the value of the GPIO (for both the input and output directions)
* Set the value of the GPIO (only in the output direction)



[//]: # (Using the Python Module)

# Using the Python Module

**Installing the Module**

To install the Python module, run the following commands:
```
opkg update
opkg install python-light pyOnionGpio
```

This will install the module to `/usr/lib/python2.7/`

*Note: this only has to be done once.*


**Using the Module**

To add the Onion GPIO Module to your Python program, include the following in your code:
``` python
import onionGpio
```


[//]: # (Example Code)

# Example Code

Several examples of how the `OnionGpio` object is used can be found in the [examples in the `onion-gpio-sysfs` repo.](https://github.com/OnionIoT/onion-gpio-sysfs/tree/master/python/examples) This directory contains all of the code seen below as well as some additional examples.

The main example is the [`gpio-test.py` script](https://github.com/OnionIoT/onion-gpio-sysfs/blob/master/python/examples/gpio-test.py), it sets GPIO14 to be an input and reads the value, it then changes the GPIO direction to output, reads the current value, sets the value to 1, and reads the value again.


[//]: # (Functions)

# Functions

Each of the main functions implemented in this module are described below.


[//]: # (Functions: Constructor)

## Constructor

The object needs to be initialized before it can be used, hence, the constructor:
``` python
gpioObject 	= onionGpio.OnionGpio(gpioNumber)
```

After this call, the object can be used freely.

**Arguments**

The `gpioNumber` argument is an integer that indicates the GPIO that is to be controlled by this object.


**Example**

To initialize an OnionGpio object to control GPIO14:
``` python
gpio14 		= onionGpio.OnionGpio(14)
```


[//]: # (Functions: GPIO Direction)

## GPIO Direction

The GPIOs on the Omega can be set to the input or output direction. When in the input direction, external signals can be connected to the GPIO and the digital value can be read. When in the output direction, the digital value the GPIO is driving can be programmed.

[//]: # (Functions: GPIO Direction: Read the Direction)

### Reading the Current Direction

In some instances, it will be useful to find out the current direction of the GPIO:
``` python
direction 	= gpioObject.getDirection()
```

**Return Value**

The function will return the following:
* `in` if the Input direction is selected
* `out` if the Output direction is selected


[//]: # (Functions: GPIO Direction: Set the Direction)

### Setting the Direction

The direction of the GPIO can be set to **input**:
``` python
status 	= gpioObject.setInputDirection()
```

Or **output**:
``` python
status 	= gpioObject.setOutputDirection(defaultValue)
```

**Return Value**

The function will return the following:
* `0` if the operation is successful
* `-1` if the operation is NOT successful


**Arguments**

The `setOutputDirection()` function has an **optional** integer argument that, when defined, will set the initial value of the GPIO to ensure glitch-free operation. 

If the optional argument is not set, the GPIO will just be set to output and the initial value will most likely be LOW. However, glitch-free operation cannot be guaranteed.


**Examples**

Set your GPIO to input:
``` python
status = gpio14.setInputDirection()
```

Set the GPIO to output:
``` python
status = gpio14.setOutputDirection()
```

Set the GPIO to output with LOW (0) as the initial value:
``` python
status = gpio14.setOutputDirection(0)
```

Set the GPIO to output with HIGH (1) as the initial value:
``` python
status = gpio14.setOutputDirection(1)
```



[//]: # (Functions: GPIO Value)

## GPIO Value

The good part, finally! Now we will be reading and setting a GPIO's value.

[//]: # (Functions: GPIO Value: Reading)

### Reading the Value

Reading the current value of the GPIO:
``` python
value 	= gpioObject.getValue()
```

Note that the value of the GPIO can be read in both **Input** and **Output** mode. 

The difference is that in input mode, the GPIO can be driven high or low based on external signals, and that is the value that will be read. In output mode, the value that will be read is what the GPIO is currently outputting.


**Return Value**

The function will return the current value of the GPIO: either `0` or `1`


**Examples**

Set the GPIO to input and then read and print the value every second:
``` python
import time
import onionGpio

gpioNum = 7
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to input 
status 	= gpioObj.setInputDirection()

# read and print the value once a second
loop = 1
while loop == 1:
	value = gpioObj.getValue()
	print 'GPIO%d input value: %d'%(gpioNum, int(value))
	
	time.sleep(1)
```	

*This code can be found in the [`onion-gpio-sysfs` repo example directory](https://github.com/OnionIoT/onion-gpio-sysfs/tree/master/python/examples), it's named [`read-input-loop.py`](https://github.com/OnionIoT/onion-gpio-sysfs/blob/master/python/examples/read-input-loop.py)*


Set the GPIO to output, read the initial value:
``` python
import onionGpio

gpioNum = 6
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to input 
status 	= gpioObj.setOutputDirection()
print 'GPIO%d set to output,'%(gpioNum),

# read the value
value 	= gpioObj.getValue()
print ' initial value: %d'%(int(value))
```

*This code can be found in the [`onion-gpio-sysfs` repo example directory](https://github.com/OnionIoT/onion-gpio-sysfs/tree/master/python/examples), it's called [`read-output.py`](https://github.com/OnionIoT/onion-gpio-sysfs/blob/master/python/examples/read-output.py)*


[//]: # (Functions: GPIO Value: Setting)

### Setting the Value

And what we've all been waiting for, setting the value of a GPIO:
``` python
status 	= gpioObject.setValue(value)
```

Note that this will only work the the GPIO is programmed to the **Output** direction!


**Arguments**

The `value` argument is the value to set the GPIO. Set it to `0` to make the GPIO output a digital 0 (LOW), or set to `1` to output a digital 1 (HIGH).


**Return Value**

The function will return the following:
* `0` if the operation is successful
* `-1` if the operation is NOT successful


**Example**

Set a GPIO to output, and alternate the output between LOW and HIGH every 5 seconds:
``` python
import time
import onionGpio

gpioNum = 1
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to output 
status 	= gpioObj.setOutputDirection(0)

# alternate the value
loop 	= 1
value 	= 0
while loop == 1:
	# reverse the value
	if value == 0:
		value = 1
	else:
		value = 0
	
	# set the new value
	status 	= gpioObj.setValue(value)
	print 'GPIO%d set to: %d'%(gpioNum, value)
	
	time.sleep(5)
```	

*This code can be found in the [`onion-gpio-sysfs` repo example directory](https://github.com/OnionIoT/onion-gpio-sysfs/tree/master/python/examples), it's called [`set-high-low-loop.py`](https://github.com/OnionIoT/onion-gpio-sysfs/blob/master/python/examples/set-high-low-loop.py)*





