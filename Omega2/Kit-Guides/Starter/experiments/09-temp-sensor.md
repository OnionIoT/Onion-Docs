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
//    - find the id of the slave by reading `/sys/devices/w1_bus_master1/w1_master_slaves`
//  - if there are no slaves, that means the temp sensor has not been detected by the kernel module! need to exit in this case

// 3. find the temperature reading from the sensor by reading: `/sys/devices/w1_bus_master1/<1-wire slave ID>/w1_slave` where <1-wire slave ID> is what we read in step 2
//  it will output something like:
        b1 01 4b 46 7f ff 0c 10 d8 : crc=d8 YES
        b1 01 4b 46 7f ff 0c 10 d8 t=27062

// the t=27062 part means that the temperature is 27.062 degrees celsius. the contents of this file will have to be parsed to isolate just the temperature
// make sure the following cases are handled correctly:
//  - negative temperature will be shown as: t=-1234 this means -1.234
//  - when 0 < temp < 1 the temperature will be shown as t=543 meaning 0.543 degrees
//  - when -1 < temp < 0 the temp will be shown as t=-876 meaning -0.876 degrees


First, let's create a base class for any generic One-Wire device. Create a file called `oneWire.py` and paste the following code in it:

``` python
import os
from subprocess import call
from time import sleep

setupDelay = 3
oneWireDir = "/sys/devices/w1_bus_master1"
paths = {
    "slaveCount": oneWireDir + "/w1_master_slave_count",
    "slaves": oneWireDir + "/w1_master_slaves"        
}

# scan addresses of all connected 1-w devices
def scanAddresses():
    with open(paths["slaves"]) as slaveListFile:
        slaveList = slaveListFile.read().split("\n")
        # last element is an empty string due to the split
        del slaveList[-1]
    return slaveList

# use to get the address of a single connected device
def scanOneAddress():
    addresses = scanAddresses()
    return addresses[0]

class OneWire:
    def __init__(self, address, gpio=19):      # use gpio 19 by default if not specified
        self.gpio = str(gpio)
        self.address = str(address)
        self.slaveFilePath = oneWireDir + "/" + self.address + "/" + "w1_slave"
        
        self.ready = self.__prepare()
        
    def __insertKernelModule(self):
        argBus = "bus0=0," + self.gpio + ",0"
        call(["insmod", "w1-gpio-custom", argBus])
    
    # prepare the object
    def __prepare(self):
        # check if the system file exists
        # if not, set it up, then check one more time
        for i in range (2):
            if os.path.isdir(oneWireDir):    
                break
            self.__insertKernelModule()
            
            # wait for a bit, then check again
            sleep(setupDelay)                   
        else:
            # could not set up 1wire on the gpio
            return False                        
        
        # check that the kernel is detecting slaves
        with open(paths["slaveCount"]) as slaveCountFile:
            slaveCount = slaveCountFile.read().split("\n")[0]
            
        if slaveCount == "0":
            # slaves not detected by kernel               
            return False
        
        # check if this instance's device is properly registered
        slaveList = scanAddresses()
        registered = False
        for line in slaveList:
            if self.address in line:
                registered = True
        
        if not registered:
            # device is not recognized by the kernel  
            return False                        
        
        # the device has been properly set up
        return True
        
    def readDevice(self): # call this to read data from the sensor
        # read from the system file
        with open(self.slaveFilePath) as slave:
            message = slave.read().split("\n")
        # return an array of each line printed to the terminal
        return message
```

Let's create a file called `temperatureSensor.py` to hold our code:

``` python
from oneWire import OneWire

# main class definition
class TemperatureSensor:
    def __init__(self, interface, args):
        self.supportedInterfaces = ["oneWire"]
        self.interface = interface
        
        # if specified interface not supported
        if self.interface not in self.supportedInterfaces:
            print "Unsupported interface."
            self.listInterfaces()
            return
            
        # set up a driver based on the interface type 
        # you can extend this class by adding more! (eg. 1-Wire, serial, I2C, etc)
        if self.interface == "oneWire":
            self.driver = OneWire(args.get("address"), args.get("gpio", None))
            # match the return value to 
            self.readValue = self.__readOneWire;
    
    def listInterfaces(self):
        print "The supported interfaces are:"
        for interface in self.supportedInterfaces:
            print interface

    # read one-wire devices
    def __readOneWire(self):
        # device typically prints 2 lines, the 2nd line has the temperature sensor at the end
        # eg. a6 01 4b 46 7f ff 0c 10 5c t=26375
        rawValue = self.driver.readDevice()
        value = rawValue[1].split()[-1].split("=")[1]
        
        # convert value from string to number
        value = int(value)
        
        # DS18B20 outputs in 1/1000ths of a degree C, so convert to standard units
        value /= 1000.0
        return value
    # add more __read() functions for different interface types later!
```

Now let's write the script for the main routine. Create a file called `STK09-temp-sensor.py` and paste the following in it.

``` python
# main routine

from temperatureSensor import TemperatureSensor
import oneWire
import time

# get the address of the temperature sensor when it's the only device connected
sensorAddress = oneWire.scanOneAddress()
# set the GPIO that we've connected the sensor to
oneWireGpio = 18

pollingInterval = 1                             # seconds

sensor = TemperatureSensor("oneWire", { "address": sensorAddress, "gpio": oneWireGpio })

# periodically check and print the temperature
while 1:
    value = sensor.readValue()
    print value
    time.sleep(pollingInterval)
```

### What to Expect

<!-- // run the program, get a print-out on the command line of the current temperature -->
You should see the Omega printing the ambient temperature in degrees Celsius measured by the sensor once every second.

### A Closer Look at the Code

// reading from and writing to the filesystem

#### Writing to the Filesystem

// explanations of opening files, writing/reading the contents, closing the file
// mention that all programs that interact with the filesystem work like this
