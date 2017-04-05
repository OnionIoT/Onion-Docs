### The SN754410 H-Bridge Chip

<!--
// TODO:
//	* need to include a diagram of the chips inputs and outputs before mentioning the names of the pins (1A, 2A, 1Y, etc)
// 	* mention that the chip conveniently handles short circuits etc at the very bottom of this passage. the idea is to first explain what is going on, and then draw the conclusion
//	* include a truth table when describing how the inputs relate to the outputs
//	* describe specifically how we'll be using the h-bridge (for example: 1A=L, 2A=H, 1,2EN=H to make the motor spin clockwise)
-->

The [SN754410 chip](http://www.ti.com/lit/ds/symlink/sn754410.pdf) contains two H-bridges, giving us four outputs, thereby allowing us to control two DC motors. For now, we'll just be controlling a single motor. The chip conveniently handles short circuit situations and simplifies the operation of an H-bridge to two switches from four.

<!-- // DONE: IMAGE diagram of the SN754410 -->
![Pinout diagram of the SN754410 IC](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/h-bridge-pinout.png)


So instead of S1/S2/S3/S4 (as seen above), we'll be switching `1A` and `2A` (as seen in the datasheet). For this tutorial, we'll be using one of the two H-bridges to control power sent to the two inputs of your DC motor. Specifically, the pair of inputs and outputs (`1A`, `2A` and `1Y`, `2Y`) on the left side of the chip.


On the chip, `1A` controls the polarity of `1Y`, same goes for `2A` and `2Y`. At a very high level, this H-bridge chip changes the output voltage (to the pins labelled `Y`) according to the input voltage sent to the pins labelled `A`. For example, sending a 'high' to `1A` will send the same to `1Y`. The difference is the signal sent out to `Y` pins use the voltage supplied to pin `8` regardless of what the input voltage is.

Voltage acts kind of like a waterfall - it always sends the current flowing from the voltage **source** (top) to the **ground** (bottom). You can think of the source as `HIGH` and ground as `LOW`. So if you connect a motor to `1Y` and `2Y`, it'll only move if they're sending out **different** signals.

The `1,2EN` pin simply turns the H-bridge on or off. If `1,2EN` sees a 'high', then everything we've covered above happens as normal, if it's off, then there won't be anything sent to the outputs no matter what `1A` and `2A` are set to.
