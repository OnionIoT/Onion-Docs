### Slide Switches

A three-terminal slide switch like the one included in your kit is commonly used in electronics. It's what's known as a SPDT switch, this stands for Single Pole Double Throw. All this means is that the switch is a change-over switch; it can electrically connect the common pin in the middle to one of the two other pins.

<!-- // DONE: IMAGE: Slide Switch -->
![Slide switch](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/switches-slide.jpg)

SPDT switches are useful when it comes to choosing between two options: imagine an electrical outlet on the wall that has two plugs and a switch that allows you to choose which one of plugs can provide power.

<!-- // DONE: IMAGE: side by side schematic and image of switch showing the two different switch settings -->
![A red LED](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/switches-slide-sidebyside.png)

You don't always have use an SPDT switch to choose between two options. It can be used just like any regular on-off switch by leaving one of the pins disconnected, or **floating**. This breaks the circuit path and prevents any current from flowing, like a simple power switch.

**Note:** Floating pins are open to the outside world and are not connected to any other part of the circuit. They can be affected by discharges of static electricity from the air or from contact with objects; for example, your fingers! These tiny discharges can cause voltage fluctuations at the pin, and any circuit that's connected to them may mistakenly read HIGH or LOW pulses.

If an SPDT switch is being used for input, it is highly recommended to make sure all pins are connected to either a HIGH, LOW, or other circuit pin.

<!-- // DONE: finish the sentence above that just trails off -->
