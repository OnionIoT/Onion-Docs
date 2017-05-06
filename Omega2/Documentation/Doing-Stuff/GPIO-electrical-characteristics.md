**The Omega2's GPIOs are not 5V input tolerant!**

See the table below for the GPIOs' operating voltages:

| Parameter | Minimum (V) | Maximum (V) |
|-|-|-|
| Input `HIGH` | 2.0 | 3.6 |
| Input `LOW` | -0.3 | 0.8 |
| Output `HIGH` | 2.4 | 3.3 |
| Output `LOW` | --- | 0.4 |

**Warning: Connecting a signal to an input pin below the minimum `LOW` or above the maximum `HIGH` voltages may damage your Omega!**

Standard 5V logic devices typically accept 3.3V as a logical `HIGH`, however, they output logical `HIGH` in the range of 4.4V to 5V. This means that the Omega can *output* to a 5V logical device, but *input* from the 5V logic device would damage the GPIO input circuitry. 
