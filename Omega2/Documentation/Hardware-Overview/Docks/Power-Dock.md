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

Your Power Dock has a 30 pin Expansion Header, allowing you to use all of your Onion Expansions. It provides the Omega with the 3.3V it needs to run, while also providing 5V for the Expansions and USB Host port.

![Power Dock Labeled](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-illustration.png)

The Power Dock is flexible: it can run off just a battery or just by drawing power from the Micro USB port. Charging the battery requires having both the battery and the Micro USB plugged in. Don't worry, the Omega will still work with no interruptions while charging.

The Micro-USB port supplies 5V to the Dock. This voltage is stepped down to the required 3.3V required to power the Omega, and also provides 5V to the Expansions and USB Host port.



### Connecting an Omega

To connect an Omega to the Power Dock, line up the Omega's edges with that of the Power Dock's as demonstrated below:

![power dock plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-top-plugged-in.JPG)

Make sure your Omega is pushed all the way down as demonstrated in the picture below:


![power dock side view](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-side-view.JPG)

You may need to line up the pins with the holes before pressing the Omega into the Dock.

<!-- ### The Power Dock at a Glance -->


### The Expansion Header

<!-- [//]: # (breakout of the Omega's GPIOs, can be connected to other circuits directly, or can use Omega expansions) -->

The Expansion Header is a convenient tool that gives you easy access to the Omega's GPIOs, and allows you to connect Onion Expansions directly. The Expansion Header is labelled to show you what GPIO is connected to each section.

<!-- expansion header pinout intro -->
```{r child = '../shared/Hardware-Overview-Component-01-expansion-header-pinout-intro.md'}
```

![expansion header pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-expansion-header-pinout.png)

<!-- expansion header pinout explanation - no pwm pins -->
```{r child = '../shared/Hardware-Overview-Component-03-expansion-header-pinout-explanation-no-pwm.md'}
```


### Micro-USB Port

<!-- The Micro-USB Port is used to supply the Power Dock with ... power! Connect it to a computer or a USB wall adapter. -->
The Micro-USB Port is used to supply power to the Power Dock. Connect the Dock to a power source such as a computer or a USB wall adapter to recharge your battery, or to use your board without a battery.

<!-- [//]: # (fix up this text...) -->


<!-- No-USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-3-No-USB-to-Serial.md'}
```


### The Power Switch

The power switch controls power to the Omega, regardless of whether it is powered from the battery or Micro-USB cable. The power switch has no effect on the battery charging, so **the battery will charge regardless of the switch position**.

The blue Power LED indicates if there is power flowing to the Omega.

<!-- [//]: # (add illustrations indicating the ON and OFF positions of the switch) -->


### Battery Level Indicator LEDs

The power dock contains 4 LEDs that indicate the current battery level and charging status. The LED closest to the Micro-USB port indicates the lowest battery level and the LED furthest away from the Micro-USB port indicates the highest battery level.

Lowest Battery Level:

![Lowest Indicator Level](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-lowest-indicator.jpg)

Highest Battery Level:

![Highest Indicator Level](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-highest-indicator.jpg)


### The Battery Connector

The Power Dock is designed for use with a **3.7V LiPo Battery** with a standard 2-pin JST-PH connector (2mm spacing between pins).

Expect a 1500mAh battery to last about 10 hours, in some cases, up to 12 hours.

<!-- It should take Y hours to fully charge it up again.  -->

**Warning:** Do not attempt to charge your battery with anything other that the Power Dock or a charger designed specifically for LiPo Batteries!


<!-- Reset Button -->
```{r child = '../shared/Hardware-Overview-Component-0-Reset-Button.md'}
```


<!-- USB Port -->
```{r child = '../shared/Hardware-Overview-Component-5-Omega-USB-Port.md'}
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




### Using the Power Dock

<!-- [//]: # (overview of what this section covers) -->

The Power Dock operates in three different modes.


<!-- Usage Modes: Battery Mode -->

#### Battery Mode

This is the most important mode; when the Omega and Power Dock are running completely off the battery. The LED Indicators will be turned off by default to conserve battery life, however they can be turned on for five seconds via a command from the Omega.

![Toggle Indicator LEDs on](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-command-line.gif)

When the battery is approaching depletion the Indicator LEDs will begin flashing the low battery warning:

![indicator flashing low battery](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-0-25.gif)


<!-- Usage Modes: Charging Mode -->

#### Charging Mode

When both the battery and Micro-USB cable are connected to the Power Dock, the battery will be charging. The Omega can still be powered on while the battery is charging, but it doesn't have to be; the battery will charge in this mode regardless of what the Omega is doing. You can even disconnect your Omega and the battery will still charge!

The Indicator LEDs will show the current charge level of the battery:

  * A solid LED means the battery has charged up to that level
  * A flashing LED means the battery is currently charging this level

**For best results, use a short Micro-USB cable when charging.**

Take a look at the animations below for more details on the battery level indicators:

Battery is **25%** charged, charging up to **50%**:

![charging - 25% full](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-25-50.gif)


Battery is **50%** charged, charging up to **75%**:

![charging - 50% full](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-50-75.gif)

Battery is **75%** charged, charging up to **100%**:

![charging - 75% full](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-75-100.gif)


<!-- Usage Modes: Stationary Mode -->

#### Stationary Mode

The Power Dock will still work when the battery is disconnected and the Power Dock is receiving power just from the Micro USB cable. The Battery Level Indicator LEDs will be flashing erratically, this is expected:

![Flickering indicators](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/power-dock-stationary-mode.gif)

The Power Dock essentially acts like the Expansion Dock in this mode.



<!-- SECTION -->
<!-- power-dock application -->

### Checking the Battery Level

<!-- [//]: # (explanation that you can visually see the battery level on the indicator LEDs AND in the operating system) -->

The `power-dock` application allows you to turn on the indicator LEDs on the Power Dock. It will only take effect when the Omega and Power Dock are being powered just by the battery.

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



#### Controlling the GPIOs

The GPIOs on the dock can be controlled using a number of tools we've included in the Omega firmware. You find more on how you can control the Omega's GPIOs in the article on [using the Omega's GPIOS](#using-gpios)
