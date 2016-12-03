---
title: Using GPIOs
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Using the Omega's GPIOs

[//]: # (Lazar: copy kit guide text on gpios, put it here)
General-Purpose Input/Output (GPIO) is a generic pin whose behaviors are controlled by the user. These pins have no predefined purpose and go unused by default.

The Omega2 has 5 dedicated and 12 multiplexed GPIO pins, which can be controlled via the Linux filesystem.

We can control these GPIO pins with a command-line tool known as `gpioctl`. This article will go through how `gpioctl` works, and how you can use it to control the GPIOs.




### From the Command Line

The command-line tool `gpioctl` comes pre-installed on your Omega. `gpioctl` is based on setting file values inside the `/sys/class/gpio` directory. This is made possible with `sysfs`, a pseudo file system that holds information about the Omega's hardware in files, and lets the user control the hardware by editing the files.


The tool abstracts a lot of the more detailed commands from the user and simplifies them into easy-to-run commands that can control the GPIOs.



#### Using `gpioctl`

There are 7 options associated with `gpioctl`. The syntax of the command is as follows:

```
gpioctl <OPTION> <GPIO NUMBER>
```


Here are some examples on how you can use `gpioctl` to interact with the Omega's GPIOs.




##### Reading an Input

If you want your Omega to interface with a switch or button then you'll need to use a GPIO to read the input of the switch.

To read an input of a GPIO we'll need to first set the direction to input, connect an external circuit, and then read the value.


To set the direction of GPIO1 to `in`, enter the follow command:

```
root@Omega-2757:/# gpioctl dirin 1
Using gpio pin 1.
```

**Now** you're ready to connect an external circuit. You **will** damage your Omega if your GPIO is set to output and you try to drive current to the pin.

Let's try reading GPIO1 with `get`:

```
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is LOW
```

Here we see that the GPIO pin is reading a digital `LOW` or `0`.


##### Setting a Value

You can configure your GPIO pin to supply power to a load with your Omega, for example, if you were powering an LED.

We first set a GPIO pin's direction via the `dirout` command:

```
root@Omega-2757:/# gpioctl dirout 1
Using gpio pin 1.
```


We then use the `dirout-high` option, which sets the GPIO to `HIGH` or `1`:

```
root@Omega-2757:/# gpioctl dirout-high 1
Using gpio pin 1.
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is HIGH
```


Or we use the `dirout-low` option, which sets the value of the GPIO to `LOW` or `0`:

```
root@Omega-2757:/# gpioctl dirout-low 1
Using gpio pin 1.
root@Omega-2757:/# gpioctl get 1
Using gpio pin 1.
Pin 1 is LOW
```

> You can use the `gpioctl get <PIN>` command to read a pin regardless of its direction.


### Multiplexed GPIOs

Multiplexed GPIOs are pins that are given a special function to carry out, as opposed to being unused pins. For example, the UART pins are designated as UART, but are multiplexed so that you can designate and use them as GPIO pins when you want. This is used to incorporate the largest number of peripherals in the smallest possible package.

![omega2-pinout-diagram](../Hardware-Overview/img/Omega-2-pinout-diagram.png)

You can use the `omega2-ctrl` tool to change the function of your GPIOs


To get the current mode of the Omega's two pins, use the command:

```
omega2-ctrl gpiomux get
```

and you'll be given a list as a result:

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
Group wled - wled [gpio]
```

This list gives you the groups of multiplexed pins available, and their modes. The current mode for each group is indicated with the `[]`.

Let's examine the UART1 line:

```
Group uart1 - [uart] gpio
```

Here we see the group is `uart1`, and the available modes are `[uart] gpio`, with the current mode being `[uart]`.

#### Changing the GPIO Function

To set a particular group of hardware pins to a specified mode, use the following command:

```
omega2-ctrl gpiomux set <HARDWARE PIN GROUP> <MODE>
```

To illustrate the above, the following command will set I2C pins to GPIO mode:

```
omega2-ctrl gpiomux set uart1 gpio
```

and running the `get` command from above to confirm our changes:

```
root@Omega-2757:/# omega2-ctrl gpiomux get
Group i2c - [i2c] gpio
Group uart0 - [uart] gpio
Group uart1 - uart [gpio]
Group uart2 - [uart] gpio pwm
Group pwm0 - [pwm] gpio
Group pwm1 - [pwm] gpio
Group refclk - refclk [gpio]
Group spi_s - spi_s [gpio]
Group spi_cs1 - [spi_cs1] gpio refclk
Group i2s - i2s [gpio] pcm
Group ephy - [ephy] gpio
Group wled - wled [gpio]
```

We see:
```
Group uart1 - uart [gpio]
```
indicating that our change has indeed been applied. 
