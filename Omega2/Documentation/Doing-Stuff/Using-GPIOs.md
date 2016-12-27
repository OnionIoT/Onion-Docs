---
title: Using GPIOs
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Using the Omega's GPIOs {#using-gpios}

The Omega2 has twelve General-Purpose Input/Output pins (commonly referred to as GPIOs) that can be fully controlled by you, the user. GPIO pins on most chips generally go unused, but on the Omega we can use these GPIOs to connect to, communicate with, and control external circuits.

On the Omega, we can control GPIO pins with a command-line tool known as `gpioctl`. This article will go through how `gpioctl` works, and the ways in which you can use it.


<!-- TODO: add section describing GPIO in output direction with an example -->

<!-- TODO: add section describing gpio in input direction with an example -->

### GPIO Electrical Ratings

**The Omega2's GPIOs are not 5V input tolerant!**

See the table below for the GPIOs' operating voltages:

| Parameter | Minimum (V) | Maximum (V) |
|-|-|-|
| Input `HIGH` | 2.0 | 3.6 |
| Input `LOW` | -0.3 | 0.8 |
| Output `HIGH` | 2.4 | --- |
| Output `LOW` | --- | 0.4 |

**Warning: Connecting a signal to an input pin below the minimum `LOW` or above the maximum `HIGH` voltages may damage your Omega!**

### From the Command Line

The command-line tool `gpioctl` comes pre-installed on your Omega. `gpioctl` is based on setting file values inside the `/sys/class/gpio` directory. This is made possible with `sysfs`, a pseudo-file system that holds information about the Omega's hardware in files, and lets the user control the hardware by editing the files.

The tool abstracts a lot of the more detailed commands from the user and simplifies them into easy-to-run commands that can control the GPIOs.

#### Using `gpioctl`

There are 7 options associated with `gpioctl`. The syntax of the command is as follows:

```
gpioctl <OPTION> <GPIO NUMBER>
```

Here are some examples on how you can use `gpioctl` to interact with the Omega's GPIOs.

##### Reading an Input

If you want your Omega to interface with a switch or button then you'll need to use a GPIO to read the input of the switch.

To read an input of a GPIO we'll need to first set the direction to `input`, connect an external circuit, and then read the value.

To set the direction of GPIO1 to `input`, enter the follow command:

```
root@Omega-2757:/# gpioctl dirin 1
Using gpio pin 1.
```

**Now** you're ready to read from an external circuit!

**Note: You will damage your Omega if your GPIO is set to `output` and you try to drive external current to the pin**.

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

### Multiplexed GPIOs {#using-gpios-multiplexing}

Multiplexed GPIOs are pins that can be used for **multiple purposes** other than input/output when needed. For example, the UART pins are designated as UART, but are **multiplexed** so that you can designate and use them as GPIO pins when you want. This is used to incorporate the largest number of peripherals in the smallest possible package.

![omega2-pinout-diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/Omega-2-Pinout-Diagram.png)

You can use the `omega2-ctrl` tool to change the function of your GPIOs


To get the current mode of the Omega's multiplexed pins, use the command:

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

The current mode for each group is indicated with the `[]`.

Let's examine the UART1 line:

```
Group uart1 - [uart] gpio
```

Here we see the group is `uart1`, and the available modes are `[uart] gpio`, with the current mode being `[uart]`.

#### Changing the GPIO Function

To set a particular group of hardware pins to a specified mode, use the following command:

```bash
omega2-ctrl gpiomux set <HARDWARE PIN GROUP> <MODE>
```

To illustrate the above, the following command will set UART1 pins to operate in GPIO mode:

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


### Fast-GPIO

The `fast-gpio` command is similar to `gpioctl` in that it is used to control the Omega's GPIOs. The difference is that while `gpioctl` worked by setting file values inside the `/sys/class/gpio` directory, `fast-gpio` works by setting GPIO registers directly on the processor and is inherently a faster process.

#### Command Usage:

For a print-out of the usage, run `fast-gpio` on the command line:

```
root@Omega-2757:/# fast-gpio
Usage:
 fast-gpio set-input <gpio>
 fast-gpio set-output <gpio>
 fast-gpio get-direction <gpio>
 fast-gpio read <gpio>
 fast-gpio set <gpio> <value: 0 or 1>
 fast-gpio pwm <gpio> <freq in Hz> <duty cycle percentage>
```

#### Setting a GPIO pin's direction:

```bash
fast-gpio set-input <GPIO>
fast-gpio set-output <GPIO>
```

A pin can be configured to either be input or output.

**To avoid damaging your Omega, set a pin to the input direction before driving any voltage to it!!**


#### Reading a GPIO pin's direction:

It may be handy to check a pin's programmed direction before doing anything with it. The command to check a GPIO looks like the following:

```bash
fast-gpio get-direction <GPIO>
```

For example, if GPIO `14` is set to `output` and `13` to `input`:

```
fast-gpio get-direction 14
> Get direction GPIO14: output
fast-gpio get-direction 13
> Get direction GPIO13: input
```


#### Reading a GPIO pin's value:

You can read a pin's value whether it's in `input` or `output` mode.

```
fast-gpio read <gpio pin>
```

For example, to read pin `14`:

```
root@Omega-2757:/# fast-gpio read 14
> Read GPIO14: 0
```

#### Setting a GPIO pin's value:
This will drive the selected pin to the value desired.

```
fast-gpio set <gpio pin number> <value to set; 0 or 1>
```

If the pin is not in `output` mode, `fast-gpio` will silently change it to `output` before setting the value.

<!-- Gabe: removed bit about "digital input"; was the same part of fast-gpio as the input section -->
