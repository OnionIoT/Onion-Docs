---
title: Controlling an LCD Screen
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 10
---

## Controlling an LCD Screen {#starter-kit-controlling-an-lcd-screen}

<!-- // in this experiment, we will:
//  * be building on the previous experiment
//  * writing to an lcd screen
//    * using the i2c protocol -->

In this experiment, we will be building on the previous experiment by writing to an LCD screen using the I2C protocol.

<!-- lcd -->
```{r child = '../../shared/lcd.md'}
```

<!-- i2c -->
```{r child = '../../shared/i2c.md'}
```

### Building the Circuit

<!-- // start from the temperature sensor circuit
// straight-forward addition: I2C SCL+SDA, Vcc (3.3V), GND -->
We'll be using the same temperature sensor circuit from the previous experiment, but we'll also be connecting the I2C display to the Omega.

#### What You'll Need

If you've taken apart your temperature sensor circuit, wire it back up according to the instructions in the [previous experiment](#starter-kit-reading-one-wire-temperature-sensor).

Then grab the following from your kit:

* Jumper wires
    * 4x M-F

#### Hooking up the Components

// refer them back to the temp sensor article for that part

// some i2c devices will require pull-up resistors on one, or both of SCL and SDA
// [experiment with the i2c screen and see if it needs the resistors]
// Gabe: the community member's tutorial has the screen hooked straight to the GPIOs, no pullups, but requires 5V power

1. If you've taken apart your temperature sensor circuit, wire it back up according to the instructions in the [previous experiment](#starter-kit-reading-one-wire-temperature-sensor).
1. Connect the pins from the I2C display to the Expansion Dock according to this table:

| I2C Pin | Expansion Dock |
|---------|----------------|
| GND     | GND            |
| VCC     | 5V             |
| SDA     | SDA            |
| SCL     | SCL            |

<!-- TODO: photo -->

### Writing the Code

<!-- // have a script that:
//  * reads the temperature data
//  * writes the time and temperature to the display once a minute
//    * use the onion i2c module to write to the display -->

For this experiment, we'll be using our Onion I2C Python library which conveniently exposes some I2C functionality. If you're curious, you can see how it works in our [I2C Python module reference](#i2c-python-module).

First, let's create a file containing a class to work with the I2C bus. Create a file called `i2cLib.py` and paste the following code:

``` python
from time import sleep
from OmegaExpansion import onionI2C

sleepInterval = 0.0001

class I2CDevice:
    def __init__(self, address, port=1):
        self.address = address
        self.i2c = onionI2C.OnionI2C(port)

    # write a single command
    def write_cmd(self, cmd):
        self.i2c.write(self.address [cmd])
        sleep(sleepInterval)

    # write a command and argument
    def write_cmd_arg(self, cmd, data):
        self.i2c.writeByte(self.address cmd, data)
        sleep(sleepInterval)

    # write a block of data
    def write_block_data(self, cmd, data):
        self.i2c.writeBytes(self.address cmd, [data])
        sleep(sleepInterval)
```

Next, let's create a file that has all the low level code needed to drive the LCD display. Create a file called `lcdDriver.py` and paste the following in it:

``` python
import i2cLib
from time import sleep

## commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

## flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

## flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

## flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

## flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

## flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit

class Lcd:
    #initializes objects and lcd
    def __init__(self, address):
        self.address = address
        self.lcdbacklight = LCD_BACKLIGHT #default status
        self.line1= "";
        self.line2= "";
        self.line3= "";
        self.line4= "";
        
        self.lcd_device = i2cLib.I2CDevice(self.address)

        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x02)

        self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
        self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
        self.lcd_write(LCD_CLEARDISPLAY)
        self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
        sleep(0.2)

    # clocks EN to latch command
    def lcd_strobe(self, data):
        self.lcd_device.write_cmd(data | En | self.lcdbacklight)
        sleep(.0005)
        self.lcd_device.write_cmd(((data & ~ En) | self.lcdbacklight))
        sleep(.0001)

    def lcd_write_four_bits(self, data):
        self.lcd_device.write_cmd(data | self.lcdbacklight)
        self.lcd_strobe(data)

    # write a command to lcd
    def lcd_write(self, cmd, mode=0):
        self.lcd_write_four_bits(mode | (cmd & 0xF0))
        self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

    # write string display
    def lcd_display_string(self, string, line):
        if line == 1:
            self.line1 = string;
            self.lcd_write(0x80)
        if line == 2:
            self.line2 = string;
            self.lcd_write(0xC0)
        if line == 3:
            self.line1 = string;
            self.lcd_write(0x94)
        if line == 4:
            self.line4 = string;
            self.lcd_write(0xD4)

        for char in string:
            self.lcd_write(ord(char), Rs)
        
    def lcd_display_strings_array(self, strings)
        for i in range(min(len(strings), 4)):
            self.lcd_display_string(strings[i], i+1)

    # clear lcd and set to home
    def lcd_clear(self):
        self.lcd_write(LCD_CLEARDISPLAY)
        self.lcd_write(LCD_RETURNHOME)
      
    def refresh(self):
        self.lcd_display_string(self.line1,1)
        self.lcd_display_string(self.line2,2)
        self.lcd_display_string(self.line3,3)
        self.lcd_display_string(self.line4,4)
    
    #def backlight
    def backlightOn(self):
        self.lcdbacklight = LCD_BACKLIGHT
        self.refresh()
       
    def backlightOff(self):
        self.lcdbacklight = LCD_NOBACKLIGHT
        self.refresh()
```

Now let's write the main routine for the experiment. Create a file called `temperatureLCD.py` in `/root`. Paste the code below in it:

``` python
import lcdDriver
from temperatureSensor import TemperatureSensor
import oneWire
import time

lcdAddress = 0x3f                                       # default address of i2c backpack is 0x3f by default



# setup one wire temperature sensor object
oneWireGpio = 19 # set the GPIO that we've connected the sensor to
pollingInterval = 1 # seconds

def __main__():
    # check if 1-Wire was setup in the kernel
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

    # setup LCD
    lcd = lcddriver.Lcd(lcdAddress)                         # instantiate lcd object
    lcd.backlightOn()                                       # turn backlight on    
    
    # periodically check and print the temperature
    while 1:
        value = sensor.readValue()
        lcd.lcd_display_strings_array([
            "Temperature:",
            str(value) + " C"
        ])
        time.sleep(pollingInterval)

if __name__ == '__main__':
    __main__()
```

#### What to Expect

// calling the script will update the lcd screen, but wouldn't it be nice if something could run the script for us every minute to actually update the lcd?

#### A Closer Look at the Code

// intro to the onion i2c module

Here we've introduced 

##### The Onion I2C Module

// introduce the onion i2c module, written by Onion to facilitate the easy use of the i2c bus
// give a brief overview of the functions that we used and point them to the documentation reference (need to include docs.onion.io link, not markdown tag)

##### Multiple Different Objects

// small blurb about how the main program uses two objects of different classes to accomplish its purpose - make a note that this is an incredibly common programming method/technique

#### Going Further: Automating the Script

<!-- // introduce cron
// show example of how to setup cron to run the script we wrote once every minute -->

We can use the `cron` Linux utility to automatically run the script once every minute, without having to tie up your system by leaving Python running.

<!-- TODO: this is taken from the latest article on docs.onion. fix this entire process for python, it doesn't work on gabe's omega2p -->

First, create a file in `/root` called `runTemperatureSensorScript.sh` and write the following in it:

```
##!/bin/sh -e
/usr/bin/python /root/temperatureLCD.py
```

Then change the file permissions so it becomes executable:

```
chmod +x runTemperatureSensorScript.sh
```

Run `crontab -e` to edit the file that contains commands and schedules to run them, and add this segment at the end of the file:

```
##
*/1 * * * * /root/runTempSensorScript.sh
##
```

Finally, run the following command to restart cron so it can start running your script:

```
/etc/init.d/cron restart
```

Your LCD should now update once a minute, and you're free to use your Omega for other things in the meantime!