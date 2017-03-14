### How H-bridges Work


// an h-bridge is an integrated circuit that allows us to apply current to a load in either direction, in this case we will be controlling a dc motor, a very common application for h-bridges

// explain the usage of an h-bridge:
//  * one input is the duty cycle input for the load, regardless of the direction it tells the motor how hard to spin
//  * two inputs that determine the direction in which the current will be applied to the load, in our case, this translates to the direction in which the motor will turn
//    * have a truth table indicating the inputs and what they mean for the motor
//    * make sure to say that setting both inputs to 1 will likely damage your h-bridge IC -->

// TODO: be consistent! always have H-Bridge

An H-Bridge is a circuit that allows voltages to be applied across a load in either direction (//TODO: expand on this just a bit, will not be very clear to newbies). An H-Bridge is made up of four switches: two in series, and two in parallel, with the load placed in between the switches. In this configuration the circuit takes an "H" shape.

![Hbridge](https://en.wikipedia.org/wiki/H_bridge#/media/File:H_bridge.svg)

// TODO: talk about how the h-bridge structure allows us to switch the polarity of the voltage accorss the load

// DONE: changed usage to a list

#### Typical Applications

A few of the typical applications of H-Bridge circuits:
* Construct AC (Alternating Current) from a DC source. // TODO: add a brief description, add a link for more details
* Provide the ability to reverse current across a DC motor, allowing for rotation in either direction



// TODO: this was the old Usages section
H-Bridges allow AC Voltages to be constructed from an DC source. They allow loads to be powered independently from the control signals that are controlling them, providing circuit isolation.

H-bridges provide the ability to reverse current across a DC motor allowing for bi-directional rotation.


// TODO: this applies more to the Integrated circuit chip, not to H-Bridges in general, maybe move this to the section where we talk about our H-Bridge IC
H-bridges typically have 6 pins. 2 supply pins for the load and 4 control pins for each of the transistor switches.
