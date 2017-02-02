---
title: Reading an I2C Sensor
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 9
---

# Reading a One-Wire Temperature Sensor

<!-- // in this experiment we will:
//  * introduce the one-wire bus protocol
//  * read the ambient temperature using a sensor
//  * learn how to read and write files -->

Let's now learn about and use the One Wire bus protocol to read the ambient temperature using a temperature sensor. We'll also learn how to read and write files.

## One Wire Protocol

<!-- one wire -->
```{r child = '../../shared/one-wire.md'}
```

## Building the Circuit

// very straight-forward circuit: signal wire to a gpio, Vcc (3.3V), GND

### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Expansion Dock
* Breadboard
* Jumper wires
* Resistors
    * 1x 5kΩ
* One Wire temperature sensor
    * Should read "Dallas 18B20" on the part
    * Don't mix this up with the analog temperature sensor! (says "TMP 36" on it)

### Hooking up the Components

// most 1-wire devices need a pull-up resistor on the data line
// [experiment with the 1-wire temperature sensor to confirm]


## Writing the Code


// the script: should read and write from files on the filesystem
//  * check if the device exists/is registered
//    * if not, register it with the system (have this in its own function)
//  * perform a a reading (have this in its own function)
//  * display the reading on the command line

/// NEW NEW NEW!
// overall implementation:
// 1. checking for the 1-wire master device in Linux
//   - if `/sys/devices/w1_bus_master1` does not exist
//      - need to run `insmod w1-gpio-custom bus0=0,19,0` where 19 is the gpio number where we connect the 1w data line
//      - add a wait and then check to make sure the dir above exists
//   - if it exists, all good, keep going

// 2. find the ID of the 1-wire slave device
//  - first check that there are any slaves by reading `/sys/devices/w1_bus_master1/w1_master_slave_count`,
//  - if the number of slaves is > 0 then:
//    - find the id of the slave by reading `/sys/devices/w1_bus_master1/w1_
master_slaves`
//  - if there are no slaves, that means the temp sensor has not been detected by the kernel module! need to exit in this case

// 3. find the temperature reading from the sensor by reading: `/sys/devices/w1
_bus_master1/<1-wire slave ID>/w1_slave` where <1-wire slave ID> is what we read in step 2
//  it will output something like:
        b1 01 4b 46 7f ff 0c 10 d8 : crc=d8 YES
        b1 01 4b 46 7f ff 0c 10 d8 t=27062

// the t=27062 part means that the temperature is 27.062 degrees celsius. the contents of this file will have to be parsed to isolate just the temperature
// make sure the following cases are handled correctly:
//  - negative temperature will be shown as: t=-1234 this means -1.234
//  - when 0 < temp < 1 the temperature will be shown as t=543 meaning 0.543 degrees
//  - when -1 < temp < 0 the temp will be shown as t=-876 meaning -0.876 degrees


First, we'll create a Python **class** for the temperature sensor. Create a file called `temperatureSensor.py` and paste the following code into it:

``` python
class OneWire:
    def __init__(self, uniqueId):
        self.uniqueId = uniqueId
        self.__prepare()

    def __prepare(self): # internal use only
        # check if the system file exists
            # if so, check if it's registered
                # if not, call the register function

    // TODO: the existing wiki article says you need to reboot the Omega to set up a new 1W sensor

    def __register(self):
        # register the device    

    def readValue(self): # call this to read data from the sensor
        # read from the system file
        return sensorValue

# You can extend this file to include other types of sensors, such as an analog-based sensor, I2C-based, etc!
```

Let's create a file called `oneWireTempSensor.py` to hold our code:

``` python

import time

# define constants, classes, functions

sensorAddress = 0x12 # replace with sensor address from scan script
pollingInterval = 1

# One Wire temperature sensor

# main routine
tempSensor = temperatureSensor.OneWire(sensorAddress)

# periodically check and print the temperature
while 1:
    value = tempSensor.readValue()
    print value
    time.sleep(pollingInterval)

```

Let's run the code:
```
python oneWireTempSensor.py
```

### What to Expect

<!-- // run the program, get a print-out on the command line of the current temperature -->
You should see the Omega printing the ambient temperature in degrees Celsius measured by the sensor once every second.

### A Closer Look at the Code

// reading from and writing to the filesystem

#### Writing to the Filesystem

// explanations of opening files, writing/reading the contents, closing the file
// mention that all programs that interact with the filesystem work like this
