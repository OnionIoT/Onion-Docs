A number of the available pins can be used for **multiple purposes** other than general purpose input/output when needed. Such pins are referred to as **multiplexed pins**. For example, the UART pins are designated as UART, but are **multiplexed** so that you can designate and use them as GPIO pins when you want. This is used to incorporate the largest number of protocol support in the smallest possible package.

![omega2-pinout-diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Media/master/Pinouts/Omega2.png)

You can use the `omega2-ctrl` tool to change the function of your pins.


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

#### Changing the Pin Function

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
