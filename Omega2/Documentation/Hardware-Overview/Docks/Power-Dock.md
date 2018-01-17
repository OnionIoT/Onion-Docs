---
title: Power Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---


## Power Dock {#power-dock}

<!-- [//]: # (Brief overview on the Power Dock. Highlight the features such as battery management, battery recharge, mobility (completely wireless).) -->
<!-- [//]: # (Briefly mention that the power dock is similar to but not the same as the expansion dock.) -->

Bring your next project on the go with the Power Dock! Equipped with on-board battery management, the Power Dock allows you to recharge and monitor battery levels, while providing a header to connect Onion Expansions.

![Power Dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-image.jpg)

### The Hardware

```{r child = './Power-Dock/00-hardware-overview-section.md'}
```


### Connecting an Omega

```{r child = './Power-Dock/01-connecting-an-omega.md'}
```

To connect an Omega to the Power Dock, line up the Omega's edges with that of the Power Dock's as demonstrated below:

![power dock plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-top-plugged-in.JPG)

Make sure your Omega is pushed all the way down as demonstrated in the picture below:


![power dock side view](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-side-view.JPG)

You may need to line up the pins with the holes before pressing the Omega into the Dock.

<!-- ### The Power Dock at a Glance -->


### The Expansion Header

```{r child = './Power-Dock/02-expansion-header.md'}
```

<!-- [//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions) -->

The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each section.

```{r child = '../shared/Hardware-Overview-Component-01-expansion-header-pinout-intro.md'}
<!-- expansion header pinout intro -->
```

![expansion header pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-expansion-header-pinout.png)

<!-- expansion header pinout explanation - no pwm pins -->
```{r child = '../shared/Hardware-Overview-Component-03-expansion-header-pinout-explanation-no-pwm.md'}
```


### Micro-USB Port

```{r child = './Power-Dock/03-micro-usb-port.md'}
```

<!-- No-USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-3-No-USB-to-Serial.md'}
```


### The Power Switch

```{r child = './Power-Dock/04-power-switch.md'}
```

The power switch controls power to the Omega, regardless of whether it is powered from the battery or Micro-USB cable. The power switch has no effect on the battery charging, so **the battery will charge regardless of the switch position**.

The blue Power LED indicates if there is power flowing to the Omega.

<!-- [//]: # (add illustrations indicating the ON and OFF positions of the switch) -->


### Battery Level Indicator LEDs

```{r child = './Power-Dock/05-battery-level-leds.md'}
```

The power dock contains 4 LEDs that indicate the current battery level and charging status. The LED closest to the Micro-USB port indicates the lowest battery level and the LED furthest away from the Micro-USB port indicates the highest battery level.

Lowest Battery Level:

![Lowest Indicator Level](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-lowest-indicator.jpg)

Highest Battery Level:

![Highest Indicator Level](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-highest-indicator.jpg)


### The Battery Connector

```{r child = './Power-Dock/06-battery-connector.md'}
```



### Differences from the Expansion Dock
<!-- [//]: # (thinking about removing this e) -->

Note some of the differences between the Expansion Dock and the Power Dock:

![Hardware Differences](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-differences.jpg)

The main differences are:
  * Addition of battery management circuits and battery level indicator LEDs
  * Addition of 2-pin JST-PH connector for batteries
  * All circuit components are surface-mount
  * No USB-to-Serial Chip
  * No RGB LED


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

The `power-dock` application allows you to turn on the indicator LEDs on the Power Dock. It will only take effect when the Omega and Power Dock are being powered just by the battery. You would notice that the output on the `5V` is 3.4V initially. Since the Power Dock is designed for power-saving, it provides only the voltage that the battery has. In order to get desired 5V on the output you need to activate it by issuing `power-dock` command. This event triggers the voltage regulator to 5V. 

#### Install

To install the power-dock application, run the following commands:

```
opkg update
opkg install power-dock
```

#### Usage

The application will turn on the Battery Level Indicator LEDs, allowing you to visually check the battery charge level. To do this simply enter the following command:

```
power-dock
```

You'll see the following output in the command line:

```
root@Omega-2757:/# power-dock
> Enabling Battery Level Indicator
```

And the battery LEDs will turn on for 5 seconds:

![Toggle Indicator LEDs on](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-command-line.gif)

<!-- [//]: # (Add section describing the text output of the battery level) -->


<!-- TODO: add a section on reading the battery level, ask Lazar -->


#### Controlling the GPIOs
```{r child = './Power-Dock/09-controlling-gpio.md'}
```

The GPIOs on the dock can be controlled using a number of tools we've included in the Omega firmware. You find more on how you can control the Omega's GPIOs in the article on [using the Omega's GPIOS](#using-gpios)
