### How H-Bridges Work

<!--
// an h-Bridge is an integrated circuit that allows us to apply current to a load in either direction, in this case we will be controlling a dc motor, a very common application for h-Bridges
// explain the usage of an h-Bridge:
//  * one input is the duty cycle input for the load, regardless of the direction it tells the motor how hard to spin
//  * two inputs that determine the direction in which the current will be applied to the load, in our case, this translates to the direction in which the motor will turn
//    * have a truth table indicating the inputs and what they mean for the motor
//    * make sure to say that setting both inputs to 1 will likely damage your h-Bridge IC 
-->
<!-- // DONE: be consistent! always type out H-Bridge, don't vary the dash or capitalization -->

An H-Bridge is a circuit that allows voltages to be applied across a load in either direction. Electric current flows from the source to ground, and many components need to be oriented according to the direction of current to work as expected. An H-Bridge is a circuit built to change the direction of the voltage and thus the current flowing to a load.

<!-- // DONE: expand on this just a bit, will not be very clear to newbies -->

>In electrical terms, a **load** is any piece of a circuit that consumes electric energy to do things - heating, turning, lighting up, and so on.

An H-Bridge is made up of four switches: two in series, and two in parallel, with the load placed in between the switches. In this configuration the circuit takes an "H" shape.


![H-Bridge diagram](https://upload.wikimedia.org/wikipedia/commons/d/d4/H_bridge.svg)


<!-- // DONE: talk about how the h-bridge structure allows us to switch the polarity of the voltage across the load -->

In order to change the direction of the voltage supplied, the H-Bridge controls the switches that deliver power to the load (`S1`). Looking at the diagram, if we close `S1` and `S4` while leaving the rest open, the voltage will be applied from left to right across the motor. If `S2` and `S3` are closed instead and the others open, the voltage will be applied from right to left.

>This configuration has potential to create a short circuit, so most H-Bridges do not allow direct control of these switches.

<!-- // DONE: changed usage to a list -->

#### Typical Applications

A few of the typical applications of H-Bridge circuits:
* Construct AC (Alternating Current) from a DC source by using a PWM signal to control the H-Bridge. This is a process known as [power inversion](https://en.wikipedia.org/wiki/Power_inverter).
* Provide the ability to reverse current across a DC motor, allowing for rotation in either direction.

<!-- // TODO: add a brief description, add a link for more details -->
<!-- // DONE: this was the old Usages section
- cleaned it up
-->

Additionally, H-Bridges allow loads to be powered independently from the control signals that are controlling them, providing circuit isolation.

<!-- // DONE: this applies more to the Integrated circuit chip, not to H-Bridges in general, maybe move this to the section where we talk about our H-Bridge IC 
-->

