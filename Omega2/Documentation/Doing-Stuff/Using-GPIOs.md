---
title: Using GPIOs
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

# Using the Omega's GPIOs

The Omega 2 has 5 dedicated and 12 multiplexed GPIO pins, which can be controlled via the Linux filesystem. We have provided two command line programs to control GPIOs, `gpioctl` and `fast-gpio`. This tutorial will cover `gpioctl` and its uses.


## From the Command Line

`gpio` is based on setting file values inside the `/sys/class/gpio` directory. The tool abstracts a lot of the more detailed commands from the user and simplifies them into simple commands that can control the GPIOs.

Here are some examples on how you can use `gpioctl` to control the Omega's GPIOs.
[//]: # (explanation of how gpioctl works in the linux filesystem)


To get the usage of `gpioctl`, enter it into your command line:

```
root@Omega-2757:/# gpioctl
gpioctl dirin|dirout|dirout-low|dirout-high|get|set|clear gpio
```

Here we see that we have 7 commands that are associate with `gpioctl`, and that the basic format is

```
gpioctl <COMMAND> <GPIO NUMBER>
```

Let's try reading GPIO 1 with `get`:

```
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is LOW
```

Here we see that the GPIO pin is set to `LOW` or `0`.

We can set a GPIO pin's direction via the `dirout` or `dirin` commands:

```
root@Omega-2757:/# gpioctl dirout 1
Using gpio pin 1.
```

```
root@Omega-2757:/# gpioctl dirin 1
Using gpio pin 1.
```

We can also use `dirout-low` and `dirout-high` to set the direction and output of the GPIO immediately:

```
root@Omega-2757:/# gpioctl dirout-high 1
Using gpio pin 1.
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is HIGH
root@Omega-2757:/# gpioctl dirout-low 1
Using gpio pin 1.
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is LOW
```

This can be useful if you want to make sure that the GPIO pin's direction is set to output, which is important to avoid damaging a GPIO.

The alternative to this is to use `set`, which sets the GPIO to `HIGH` or `1`, regardless of direction:

```
root@Omega-2757:/# gpioctl set 1
Using gpio pin 1.
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is HIGH
```


If you want to set the value of the GPIO to `LOW` or `0`, the command is `clear`:

```
root@Omega-2757:/# gpioctl clear 1
Using gpio pin 1.
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is LOW
```

## Multiplexing (Muxing) the GPIOs

[//]: # (brief explanation of multiplexing)

Pin Multiplexing is the process of having a set of pins able to switch between functions. This is used to incorporate the largest number of peripherals in the smallest possible package. On the Omega for example, when pins 4 & 5 are set to I2C mode they correspond to the Omega's SCL & SDA. They can also behave as GPIO pins when set to GPIO mode. To swap modes we have provided `omega2-ctrl` tool.

To get the current mode of the Omega's two pins, use the command:

```
omega2-ctrl gpiomux get
```

and you'll be given a list of as a result:

```
root@Omega-2757:/# omega2-ctrl gpiomux get
Group i2c - [i2c] gpio
Group uart0 - [uart] gpio
Group uart1 - [uart] gpio
Group uart2 - [uart] gpio pwm
Group pwm0 - [pwm] gpio
Group pwm1 - [pwm] gpio
Group refclk - refclk [gpio]
Group spi_s - spi_s [gpio]
Group spi_cs1 - [spi_cs1] gpio refclk
Group i2s - i2s [gpio] pcm
Group ephy - [ephy] gpio
Group wled - [wled] gpio
```

This list gives you the groups of multiplexed pins available, and their modes. The current mode is in the `[]`.

Let's examine the first line:
```
Group i2c - [i2c] gpio
```

Here we see the group is `i2c`, and the available modes are `[i2c] gpio`, with the current mode being `[i2c]`.

To set a particular package of hardware pins to a specified mode, use the following command:

```
omega2-ctrl gpiomux set <HARDWARE PIN GROUP> <MODE>
```

To illustrate the above, the following command will set I2C pins to GPIO mode:

```
omega2-ctrl gpiomux set i2c gpio
```
