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

// should create a temperature sensor class that does the above

// implementation:
// take a look at: https://wiki.onion.io/Tutorials/Reading-1Wire-Sensor-Data
//  the procedure for using 1w on the omega2 is likely similar

<!-- // from gabe: o2 firmware 0.1.6b136 has the following files in /etc/modules.d:
./55-sound-soc-core ## the existing wiki article says to use 55-w1-gpio-custom
./w1-master-gpio ## only contains "w1-gpio"
./w1-slave-therm ## only contains "w1_therm"
(no files with the word "custom")
I'm guessing it's one of these, will come back to this later. Not exactly sure how this works yet, I need the sensor to try it out
-->

// TODO: need a scan program to find the 1W device's address if it's not known!

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
