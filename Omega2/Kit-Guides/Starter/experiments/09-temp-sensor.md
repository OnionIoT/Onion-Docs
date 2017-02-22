---
title: Reading an I2C Sensor
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 9
---

## Reading a One-Wire Temperature Sensor {#starter-kit-08-reading-a-one-wire-temp-sensor}

// TODO: choose a way to write One-Wire and stick to it through the whole article, it helps to mention that One-Wire is often referred to as: (list all of the variations 1-Wire, 1W, W1, etc)

<!-- // in this experiment we will:
//  * introduce the one-wire bus protocol
//  * read the ambient temperature using a sensor
//  * learn how to read and write files -->

Let's now learn about and use the **1-Wire bus protocol** to read the ambient temperature using a temperature sensor. We'll also learn how to **read from and write to files**.

// TODO: add intro to the script: how we'll first register a 1W bus master, and then read from the sensor, etc

<!-- one wire -->
```{r child = '../../shared/one-wire.md'}
```

// TODO: need a section on 1W & the Omega, describing how the Omega needs to register a 1w bus master in order to be able to communicate with the 1w sensor,
//  see the docs https://docs.onion.io/omega2-docs/communicating-with-1w-devices.html#the-omega-one-wire for an example but do not just copy the text, adapt it to this article and the beginner audience, also avoid all mentions of I2C, SPI, UART, etc

### Building the Circuit

We'll be building a very simple circuit to connect the 1-Wire temperature sensor to the Omega. As the name implies, only one data line is needed for communication between any and all devices on the bus!

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Expansion Dock
* Breadboard
* Jumper wires
    * 3x M-M
* Resistors
    * 1x 5.1kΩ (yellow-purple-red)
* 1-Wire temperature sensor
    * Should read "Dallas 18B20" on the part

#### Hooking up the Components

// TODO: add a graphic showing the legs of the temparature sensor (just lift it from the datasheet), describe each of the legs

1. Find the flat side of the temperature sensor. This is the **front** side.
1. With the front of the sensor facing to the left side of the breadboard, insert the three pins into column `e` in 3 consecutive rows, eg. 13, 14, and 15.
1. Turn the breadboard so that the front of the sensor is facing you.
1. Insert jumpers for the following connections into column `a` in the row corresponding to the pins below:
    * Left - `GND`. Connect this to the Omega's `GND` pin.
    * Middle - `DATA`. Connect this to the Omega's `GPIO19`.
    * Right - `Vcc`. Connect this to the Omega's `3.3V`.
1. Connect the 5.1kΩ resistor across the `DATA` and `Vcc` pins.

> TODO: add a note about pull-up resistors

Your circuit should look like this:

<!-- TODO: photo -->

### Writing the Code

First, let's create a base class for any generic 1-Wire device.
// TODO: a sentence or two describing what the 1W class will implement

Create a file called `oneWire.py` and paste the following code in it:

// TODO: was this code tested?

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

# insert the kernel module
def insertKernelModule(gpio):
    argBus = "bus0=0," + gpio + ",0"
    call(["insmod", "w1-gpio-custom", argBus])

def checkFilesystem():
    return os.path.isdir(oneWireDir)

# TODO: add a comment describing the operation of this function, doesn't look like it's right to me
def setupOneWire(gpio):
    for i in range (2):
        if checkFilesystem():
            return True
        insertKernelModule(gpio)
        # wait for a bit, then check again
        sleep(setupDelay)
    else:
        # could not set up 1wire on the gpio
        return False

def checkSlaves():
    # check that the kernel is detecting slaves
    with open(paths["slaveCount"]) as slaveCountFile:
        slaveCount = slaveCountFile.read().split("\n")[0]

    if slaveCount == "0":
        # slaves not detected by kernel               
        return False
    return True

def checkRegistered(address):
    slaveList = scanAddresses()
    registered = False
    for line in slaveList:
        if address in line:
            registered = True
    return registered

# scan addresses of all connected 1-w devices
def scanAddresses():
    if not checkFilesystem():
        return False

    with open(paths["slaves"]) as slaveListFile:
        slaveList = slaveListFile.read().split("\n")
        # last element is an empty string due to the split
        del slaveList[-1]
    return slaveList

# use to get the address of a single connected device
def scanOneAddress():
    addresses = scanAddresses()
    return addresses[0]

# main class definition
class OneWire:
    def __init__(self, address, gpio=19):      # use gpio 19 by default if not specified
        self.gpio = str(gpio)
        self.address = str(address)
        self.slaveFilePath = oneWireDir + "/" + self.address + "/" + "w1_slave"
        self.setupComplete = self.__prepare()

    # prepare the object
    def __prepare(self):
        # check if the system file exists
        # if not, set it up, then check one more time
        if not setupOneWire(self.gpio):
            print "Could not set up 1-Wire on GPIO " + self.gpio
            return False

        # check if the kernel is recognizing slaves
        if not checkSlaves():
            print "Kernel is not recognizing slaves."
            return False

        # check if this instance's device is properly registered
        if not checkRegistered(self.address):
            # device is not recognized by the kernel
            print "Device is not registered on the bus."
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

// TODO: describe what we hope to accomplish with this code
Let's create a file called `temperatureSensor.py` to hold our code:

``` python
from oneWire import OneWire

# main class definition
class TemperatureSensor:
    def __init__(self, interface, args):
        self.supportedInterfaces = ["oneWire"]
        self.interface = interface
        self.ready = False

        # if specified interface not supported
        if self.interface not in self.supportedInterfaces:
            print "Unsupported interface."
            self.listInterfaces()
            return

        # set up a driver based on the interface type
        # you can extend this class by adding more! (eg. 1-Wire, serial, I2C, etc)
        if self.interface == "oneWire":
            self.driver = OneWire(args.get("address"), args.get("gpio", None))
            # signal ready status
            self.ready = self.driver.setupComplete
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

Now let's write the script for the main routine. Create a file called `STK08-temp-sensor.py` and paste the following in it.
// TODO: short description of

``` python
# import modules and classes
from temperatureSensor import TemperatureSensor
import oneWire

# setup onewire and polling interval
oneWireGpio = 19 # set the GPIO that we've connected the sensor to
pollingInterval = 1 # seconds

def __main__():
    # check if 1-Wire is setup in the kernel
    if not oneWire.setupOneWire(str(oneWireGpio)):
        print "Kernel module could not be inserted. Please reboot and try again."
        return -1

    # get the address of the temperature sensor
    # it should be the only device connected in this experiment    
    sensorAddress = oneWire.scanOneAddress()

    sensor = TemperatureSensor("oneWire", { "address": sensorAddress, "gpio": oneWireGpio })
    if not sensor.ready:
        print "Sensor was not set up correctly. Please make sure that your sensor is firmly connected to the GPIO specified above and try again."
        return -1

    # check and print the temperature
    value = sensor.readValue()
    print "T = " + str(value) + " C"

if __name__ == '__main__':
    __main__()
```

Run the `STK08-temp-sensor.py` script and watch the terminal for output.

#### What to Expect

<!-- // run the program, get a print-out on the command line of the current temperature -->
You should see the Omega printing the temperature in degrees Celsius measured by the sensor once every second. Try pinching the sensor with your fingers and seeing how it reacts!

// TODO: include a screenshort of the printout, or a gif or something

#### A Closer Look at the Code

Here we've introduced **reading and writing to the filesystem**. We also introduced the concept of **scanning a bus** for devices and device addresses.

##### Reading and Writing to the Filesystem

The Omega's hardware such as the serial ports, I2C, and SPI bus are exposed as files somewhere in the system. In order for software and programs to interact with these connections, they must work with the corresponding files. This is a very important concept, so please make sure to remember it!

When working with a file from within a program, you must go through the following steps:

* **Open** the file for reading, writing, or both at the same time
* **Read** from or **write** to the file
* **Close** it when you're done

This applies to all programs that interact with the filesystem, not just Python.

In this experiment, we're taking advantage of Python's `with` statement. This allows us to cleanly open the file and automatically close it when we're done! Here's an example of all of this happening in the `oneWire.py` file:

``` python
with open(self.slaveFilePath) as slave:
    message = slave.read().split("\n")
```

This simple 2-line block reads from the slave's system file at `/sys/devices/w1_bus_master1/<address>/w1_slave"`, which triggers the Omega to physically send a request to the 1-Wire sensor and return the data to our program. The file is then automatically closed once the program exits that block.

// TODO: need to separate the explanation of reading and writing to the filesystem, and the explanation of sysfs (using the filesystem to interface with hardware)
// 1. change the above section to just talk about opening, reading, and writing filesystem
// 2. add a new section talking about sysfs, doesn't have to be long, just describe that there are 'virtual' files in the filesystem which you can read and write that use the kernel to interact with actual device hardware (see https://docs.onion.io/omega2-docs/communicating-with-i2c-devices.html#the-omega-i2c for an example). if you mention the kernel, give a one sentence description of it

##### Scanning a Bus

You may have noticed that the the `OneWire` class is used by the `TemperatureSensor` class and should not need to be imported explicitly. However, for the purposes of this experiment, we included it in the main script to use its `scanOneAddress()` function.

This is because every 1-Wire sensor has its own unique address. To work with a sensor from within a program, you would have to manually find the address and write it in your code as a variable. To make this process faster:

1. We make sure that the sensor is the only 1-Wire device connected to the bus.
1. We then query the bus for device addresses.
1. The only one that will appear is the one that corresponds to our sensor.

This is all done automatically to save you time.

If you want to find the address of a 1-Wire device to write it down for later, follow these steps:

1. Disconnect all other 1-Wire devices from the Omega, then connect your device.
1. `cd` to the folder containing `oneWire.py` and start the Python interpreter with `Python`.
1. Run these commands:

``` python
import oneWire
oneWire.scanOneAddress()
```

The device's address will then be printed on the screen.


// TODO: add a section that explains what `if __name__ == '__main__':` does


Next: [Controlling an LED Screen](#starter-kit-controlling-an-lcd-screen)
