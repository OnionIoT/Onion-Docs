---
title: Controlling an LCD Screen
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 10
---

# Controlling an LCD Screen {#starter-kit-controlling-an-lcd-screen}

<!-- // in this experiment, we will:
//  * be building on the previous experiment
//  * writing to an lcd screen
//    * using the i2c protocol -->

In this experiment, we will be building on the previous experiment by writing to an LCD screen using the I2C protocol.

## LCD Screen
<!-- // should be in its own markdown file -->
```{r child = '../../shared/lcd.md'}
```

## The I2C Bus
<!-- // should be in its own markdown file -->

```{r child = '../../shared/i2c.md'}
```


## Building the Circuit

// start from the temperature sensor circuit
// straight-forward addition: I2C SCL+SDA, Vcc (3.3V), GND


### Hooking up the Components

// refer them back to the temp sensor article for that part

// some i2c devices will require pull-up resistors on one, or both of SCL and SDA
// [experiment with the i2c screen and see if it needs the resistors]
// Gabe: the community member's tutorial has the screen hooked straight to the GPIOs, no pullups, so I'll try that

## Writing the Code

// have a script that:
//  * reads the temperature data
//  * writes the time and temperature to the display once a minute
//    * use the onion i2c module to write to the display

Let's create a file called `temperatureLCD.py` in `/root`. Paste the code below in it:

``` python

# default address of i2c backpack with no jumpers is 0x27: http://store.alhekma4u.com/content/Displays/I2C%20LCD%20interface.pdf
```

### What to Expect

// calling the script will update the lcd screen, but wouldn't it be nice if something could run the script for us every minute to actually update the lcd?

### A Closer Look at the Code

// intro to the onion i2c module

#### The Onion I2C Module

// introduce the onion i2c module, written by Onion to facilitate the easy use of the i2c bus
// give a brief overview of the functions that we used and point them to the documentation reference (need to include docs.onion.io link, not markdown tag)

#### Multiple Different Objects

// small blurb about how the main program uses two objects of different classes to accomplish its purpose - make a note that this is an incredibly common programming method/technique

### Going Further: Automating the Script

<!-- // introduce cron
// show example of how to setup cron to run the script we wrote once every minute -->

We can use the `cron` Linux utility to automatically run the script once every minute, without having to tie up your system by leaving Python running.

<!-- TODO: this is taken from the latest article on docs.onion. fix this entire process for python, it doesn't work on gabe's omega2p -->

First, create a file in `/root` called `runTemperatureSensorScript.sh` and write the following in it:

```
#!/bin/sh -e
/usr/bin/python /root/temperatureLCD.py
```

Then change the file permissions so it becomes executable:

```
chmod +x runTemperatureSensorScript.sh
```

Run `crontab -e` to edit the file that contains commands and schedules to run them, and add this segment at the end of the file:

```
#
*/1 * * * * /root/runTempSensorScript.sh
#
```

Finally, run the following command to restart cron so it can start running your script:

```
/etc/init.d/cron restart
```

Your LCD should now update once a minute, and you're free to use your Omega for other things in the meantime!