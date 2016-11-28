---
title: Using GPIOs
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

# Using the Omega's GPIOs

The Omega 2 has 5 dedicated and 12 multiplexed GPIO pins, which can be controlled via the linux files system. We have provided two command line programs to control Gpios, gpioctl and fast-gpio. The former is based on setting file values inside the `/sys/class/gpio` directory, the latter is based on setting gpio registers and is inherently a faster process.


## From the Command Line

We have provided some examples on how to control gpios.

### gpioctl

To set a gpio high:
```
gpioctl dirout-high gpio_number
```

To set a gpio low:
```
gpioctl dirout-low gpio_number
```
### fast-gpio

To set a gpio high:
```
fast-gpio set gpio_number 1
```

To set a gpio low:
```
fast-gpio set gpio_number 0
```


## Muxing the GPIOs

For robustness, gpios are multiplexed with other hardware pins. For example, when pins 4 & 5 are set to I2C mode they correspond to the Omega's SCL & SDA, and behave as GPIO when set to GPIO mode. To swap modes we have provided `omega2-ctrl` tool.

To get the current mode of the Omega's two pins, use the command:

```
omega2-ctrl gpiomux get
``` 

To set a particular package of hardware pins to a specified mode, use the following command:

```
omega2-ctrl gpiomux set hardware_pins mode
```

To illustrate this the following command will set I2C pins to Gpio mode:

```
omega2-ctrl gpiomux set i2c gpio
```