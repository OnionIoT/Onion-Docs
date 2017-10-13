
## Power Dock 2 {#power-dock-2}

<!-- [//]: # (Brief overview on the Power Dock. Highlight the features such as battery management, battery recharge, mobility (completely wireless).) -->
<!-- [//]: # (Briefly mention that the power dock is similar to but not the same as the expansion dock.) -->

Bring your next project on the go with the Power Dock! Equipped with on-board battery management, the Power Dock allows you to recharge and monitor battery levels, while providing a header to connect Onion Expansions.

![Power Dock 2](https://raw.githubusercontent.com/OnionIoT/Onion-Media/master/Product%20Photos/Power%20Dock%202/Power-Dock2-45deg.JPG)

<!--- https://raw.githubusercontent.com/OnionIoT/Onion-Media/master/Product%20Photos/Power%20Dock%202/Power-Dock2-45deg.JPG --->

### The Hardware

```{r child = './Power-Dock/00-hardware-overview-section.md'}
```

What makes our Power Dock 2 more useful and unique is a additional battery level ADC. A simple chip that allows you to monitor your battery charge.


### Connecting an Omega

```{r child = './Power-Dock/01-connecting-an-omega.md'}
```

### The Expansion Header

<!-- [//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions) -->

The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each section.

<!-- expansion header pinout intro -->
```{r child = '../../shared/Hardware-Overview-Component-01-expansion-header-pinout-intro.md'}
```

![expansion header pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/expansion-dock-expansion-header-pinout.png)

<!-- expansion header pinout explanation - no pwm pins -->
```{r child = '../../shared/Hardware-Overview-Component-03-expansion-header-pinout-explanation-no-pwm.md'}
```

### Micro-USB Port

```{r child = './Power-Dock/03-micro-usb-port.md'}
```

### The Power Switch

```{r child = './Power-Dock/04-power-switch.md'}
```


### Battery Level Indicator LEDs

```{r child = './Power-Dock/05-battery-level-leds.md'}
```


### Battery Level ADC


We have added an ADC chip to the Power Dock 2 in order to measure the voltage level of an attached LiPo battery. From now on, you can get a precise voltage of a battery just by issuing a single command. It will give you a better idea of how much charge is left in order to satisfy your needs.

### The Battery Connector

```{r child = './Power-Dock/06-battery-connector.md'}
```



### Differences from the Expansion Dock
<!-- [//]: # (thinking about removing this e) -->
```{r child = './Power-Dock/07-expansion-dock-vs-power-dock.md'}
```

### Differences from the original Power Dock


What differs Power Dock 2 from the original Power Dock is that it has the Battery Level ADC that allows you to accurately monitor the voltage of your battery. Another update is that GPIOs 18 & 19 are now available on the Expansion Header! 

![comparison picture](https://raw.githubusercontent.com/OnionIoT/Onion-Media/master/Product%20Photos/Power%20Dock%202/Power-Dock2-original-comparison.JPG)


<!--- TODO: IMAGE mechanical drawing of the power dock, recheck link and uncomment when drawing available
### Mechanical drawing

We've made available a detailed [diagram](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-D-PWR.PDF) of the dimensions and geometry of the Power Dock.
--->

### Using the Power Dock

```{r child = './Power-Dock/08-using-power-dock.md'}
```

<!-- SECTION -->
<!-- power-dock application -->

### Checking the Battery Level

<!-- [//]: # (explanation that you can visually see the battery level on the indicator LEDs AND in the operating system) -->


The `power-dock2` application allows you to turn on the Battery Level indicator LEDs as well as output the current voltage of the battery on the screen. You can monitor the voltage on the command line while it is in Battery mode or Stationary mode. However, for the Batttery Indicator LEDs, it will only take effect when Power Dock is in the Battery mode.

#### Install

To install the `power-dock2` application, run the following commands:

```
opkg update
opkg install power-dock2
```

#### Usage

The application will turn on the Battery Level Indicator LEDs, allowing you to visually check the battery charge level as well as read the battery voltage level using the onboard ADC. To do this simply enter the following command:

```
power-dock2
```

You'll see the following output in the screen:

```
root@Omega-2757:/# power-dock2
Battery Voltage Level: 4.10 V
```

And the battery LEDs will turn on for 5 seconds:

![Toggle Indicator LEDs on](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-command-line.gif)

<!-- [//]: # (Add section describing the text output of the battery level) -->



#### Controlling the GPIOs

```{r child = './Power-Dock/09-controlling-gpio.md'}
```