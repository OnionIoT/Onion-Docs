---
title: Reading an I2C Sensor
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 9
---

## Reading a One-Wire Temperature Sensor {#starter-kit-reading-a-one-wire-temp-sensor}

// TODO: choose a way to write One-Wire and stick to it through the whole article, it helps to mention that One-Wire is often referred to as: (list all of the variations 1-Wire, 1-Wire, W1, etc)

<!-- // in this experiment we will:
//  * introduce the one-wire bus protocol
//  * read the ambient temperature using a sensor
//  * learn how to read and write files -->

Let's now learn about and use the **1-Wire bus protocol** to read the ambient temperature using a temperature sensor. To do that, we'll first build a circuit using the 1-Wire temperature sensor. After it's built, we'll control this circuit with a script.


<!-- one wire -->
```{r child = '../../shared/one-wire.md'}
```

There's no dedicated 1-Wire controller in the Omega. Thus to make 1-Wire work with the Omega, we must first label a GPIO as a '1-Wire master bus'. This will be the main contact point between the Omega and any 1-Wire devices. Once we have the master bus set up , we can then scan for the sensor through it and read from the sensor as needed.

Due to the lack of a dedicated controller, we'll have to send some low level instructions directly to the bus. This will be a good opportunity to learn about the process of **reading and writing files**.

#### DS18B20 Temperature Sensor

This sensor is a 1-Wire digital output sensor with high accuracy. The pin layouts can be found in the diagram below for easy reference, we'll go through how to connect it in the next section.

![TMP36 Temperature Sensor Pin Layou](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/DS18B20-pin-layout.png)

**Note**: this is the **Bottom View** of the sensor!

<!-- // TODO: need a section on 1-Wire & the Omega, describing how the Omega needs to register a 1w bus master in order to be able to communicate with the 1w sensor,
//  see the docs https://docs.onion.io/omega2-docs/communicating-with-1w-devices.html#the-omega-one-wire for an example but do not just copy the text, adapt it to this article and the beginner audience, also avoid all mentions of I2C, SPI, UART, etc -->

### Building the Circuit

We'll be building a very simple circuit to connect the 1-Wire temperature sensor to the Omega. As the name implies, only one data line is needed for communication between any and all devices on the bus!


#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Expansion Dock
* Breadboard
* 3x Jumper wires (M-M)
* 1x 5.1kΩ Resistor (yellow-purple-red)
* 1-Wire temperature sensor
    * Should read "Dallas 18B20" on the part

#### Hooking up the Components

1. Find the flat side of the temperature sensor. This is the **front** side.
1. With the front of the sensor facing to the left side of the breadboard, insert the three pins into column `e` in 3 consecutive rows, eg. 13, 14, and 15.
1. Turn the breadboard so that the front of the sensor is facing you.
1. Insert jumpers for the following connections into column `a` in the row corresponding to the pins below:
    * Middle - `DATA` or `DQ`. Connect this to the Omega's `GPIO19`.
    * Left - `GND`. Connect this to the Omega's `GND` pin.
    * Right - `Vcc`. Connect this to the Omega's `3.3V`.
1. Connect the 5.1kΩ resistor across the `DATA` and `Vcc` pins.

>The reason we have this resistor is to make sure the max voltage of the `DATA` pin is equal to the voltage provided by `Vcc`. If it isn't properly referenced, a `HIGH` from the `DATA` line might appear to be `LOW`, making the data untrustworthy!

Your circuit should look like this:

<!-- TODO: IMAGE photo -->

### Writing the Code

First, let's create a base class for any generic 1-Wire device. This class will handle all the file reading and writing needed to interface with 1-Wire devices. Creating an object of this class will associate a GPIO pin with a 1-Wire bus, and the object will act as a clean interface between code and the low level 1-Wire functions. This is exactly how libraries are written!

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

Let's create a file called `temperatureSensor.py` to hold some more code. This file will implement a `TemperatureSensor` class. Objects of this class will represent a single DS18B20 sensor in code. Inside the class, a `OneWire` object is used to operate the sensor. Functions of the `TemperatureSensor` object will send the appropriate signals, along with getting and formatting the data from the sensor. This way the operating script can focus on the logic of what to do with the data.

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

Now let's write the script for the main routine. Create a file called `STK08-temp-sensor.py` and paste the following in it. This script will use the two classes we've created to continuously check the sensor, and display the data to the console. Through abstracting out the details into two other classes, this script can be short and sweet.

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

### What to Expect

You should see the Omega printing the temperature in degrees Celsius measured by the sensor once every second. Try pinching the sensor with your fingers and seeing how it reacts!

<!-- // TODO: IMAGE include a screenshort of the printout, or a gif or something -->

### A Closer Look at the Code

Here we control a **1-Wire device through the Omega's filesystem** by reading and writing files. We also introduced the concept of **scanning a bus** for devices and device addresses. We'll also explain a bit about the `__name__ == '__main__'` business - what it does, and when should you use it.

#### Hardware and the Omega's Filesystem

The Omega's hardware such as the serial ports, I2C, and SPI bus are exposed as files somewhere in the system (in fact, this is true for most Linux systems). In order for software and programs to interact with these connections, they must work with the corresponding files by reading and writing. This is a very important concept, so please make sure to remember it!

##### Working with Files

When working with a file from within a program, you must go through the following steps:

* **Open** the file for reading, writing, or both at the same time
* **Read** from or **write** to the file
* **Close** it when you're done

This applies to all programs that interact with the filesystem, not just Python.

##### What about Hardware?

Hardware connected to the Omega's ports are represented by 'virtual' files in the system, usually listed under `/sys/devices`. The process to interact with them directly is to read and write to those files!

##### Putting it Together

Our 1-Wire connection is first initialized as a file through this line in `oneWire.py`:

```python
call(["insmod", "w1-gpio-custom", argBus])
```

This calls a system command (`insmod`) to set a specific GPIO to act as a 1-Wire master bus. The command sets up the specified GPIO as a virtual file that we can then read and write to as a 1-Wire interface - `/sys/devices/w1_bus_master1`.

To work with the 1-Wire file, we take advantage of Python's `with` statement. This allows us to cleanly open the file and automatically close it when we're done! Here's an example of all of this happening in the `oneWire.py` file:

``` python
with open(self.slaveFilePath) as slave:
    message = slave.read().split("\n")
```

This simple 2-line block reads from the slave's system file at `/sys/devices/w1_bus_master1/<address>/w1_slave"`, which triggers the Omega to physically send a request to the 1-Wire sensor and return the data to our program. The file is then automatically closed once the program exits that block. Here, the `slave` object is a python File Object and we read it just as we would a regular file!


#### Scanning a Bus

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


#### Python Modules and the `__main__` Function

When a Python file is imported as a module, any code in the lowest level of indentation will be run. This means if you want to write a Python module that stays silent until the functions are called (as good practice dicates), you can't let code that would 'do things' be inserted at the lowest level.

What if there's some important functions that you want to run by executing the module directly, but not when it's imported?

Enter:
```
if __name__ == '__main__':
```

Every file in python has a hidden `__name__` variable. When the file is imported, the value of `__name__` the filename is.


Next: [Controlling an LED Screen](#starter-kit-controlling-an-lcd-screen)
