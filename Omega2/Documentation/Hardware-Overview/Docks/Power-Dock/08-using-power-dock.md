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