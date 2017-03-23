### Shift Register

// TODO: photo of the shift register IC

A shift register is an external integrated circuit (IC) that can be used to expand the number of output pins available to us. Essentially they let you turn serial input from a single pin (one bit after the other) into multiple parallel output signals (all at once on separate lines).

<!-- // DONE: graphic: block diagram of serial data coming in, parallel data coming out (ensure that the data matches the Controlling a Shift Register section below) -->
![Block diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shift-register-block-diagram.png)

The shift register used in your kit is the popular 74HC595. It has 8 output lines which allows you to manipulate and use bytes for output in your code.

#### Overview

So how does this work? The IC is made up of two **registers**, units of memory that can hold up several binary values in order (8 for the IC in your kit). They are:

* The **shift** register, which holds 8 values before they are written to the output pins. Values can be "shifted" through this register from one position to the next, starting at position "A" to position "H".
* The **storage** register, which takes values from the shift register and sends them to the data output lines, labelled `QA` to `QH`. For example, a logical `1` in position "C" of the storage register would create a HIGH signal on `QC`.

There are three pins on the IC that we use to control it with the Omega. Two of these pins are **clocks**: special inputs that trigger the IC to do something when they receive a signal that changes from LOW to HIGH (also known as a **pulse** or a **rising edge**).

| Pin | Name | Purpose |
|-|-|-|
| SER |  Serial data pin | This is the serial data input line. When we pulse the serial clock (SRCLK), the signal on this line is stored in the 1st position ("A") of the shift register.
| SRCLK | Serial clock | When pulsed, shifts each value in the shift register forwards by one position, then loads the value from the SER pin into position "A". Note that this does not change the signals on the output lines until you pulse the register clock (RCLK). |
| RCLK | Register clock, or "latch pin" | When pulsed, updates the storage register with new values from the shift register, sending a new set of signals to the 8 output pins. This happens so quickly that they all seem to change simultaneously! |

#### Bit Order

Keep in mind that the **first** value you send the shift register will be shifted towards the **last** output pin as you send it more data.

Let's say we want to send the following bits: `10101010`. Intuitively, it seems easiest to send each bit in the number from left to right as if it were a string. In Python, this would look something like:

```python
bytestring = '10101010'
bytestring = list(bytestring) # turns the string into a list: ["1", "0", "1", "0", ...]
for bit in bytestring:
    shift(bit)          # sends 1, then 0, then 1, then 0, ...
```

However, sending it this way means that after we've sent all eight, the 1st bit would actually be shifted all the way to the last output (`QH`), the 2nd bit would be shifted to the 2nd-to-last output (`QG`), and so on until everything is reversed! This way of shifting values out is known as **most-significant bit** (MSB) first. If we used this method in our shift register class, we would have to wire everything up backwards, and this could make it confusing to assemble or debug circuits.

We can get around this issue by sending the rightmost, or **least significant bit** (LSB), first. We can modify the above code into something like this:

```python
bytestring = '10101010'
bytestring = bytestring[::-1] # use Python slice notation to get a reversed copy of the string
bytestring = list(bytestring) # turns the string into a list: ["0", "1", "0", "1", ...]
for bit in bytestring:
    shift(bit)          # sends 0, then 1, then 0, then 1, ...
```

#### Pinout Diagram

The pinout diagram for the 74HC595 is shown below:

![595-pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/595-shift-register-pinout.png)

On the right side of the chip, you can see the three control pins described above, as well as the first output (QA). On the left side, you can see the other 7 outputs (QB - QH).

#### Controlling a Shift Register

So how can this let us control multiple outputs with one data pin? Well, let's say we have 8 LEDs hooked up to the data lines, and we want to turn on the 2nd, 4th, and the 8th LEDs like so:

| LED | Data Line | Desired Value |
|-|-----------|---------------|
|1| QA | LOW |
|2| QB | HIGH |
|3| QC | LOW |
|4| QD | HIGH |
|5| QE | LOW |
|6| QF | LOW |
|7| QG | LOW |
|8| QH | HIGH |

First, we'll clear out the register so all LEDs are off by writing eight 0's to the shift register, then pulsing the latch pin to write the outputs to the data lines. This is done by setting and holding SER LOW, then pulsing SRCLK 8 times, then pulsing RCLK once.

Then, using the LSB method, we will reverse the bytestring to get `10001010`. For each of these values:

1. Set SER to the specified value (HIGH or LOW).
1. Pulse SRCLK from LOW to HIGH to shift the value of SER into the shift register.

We repeat the 2 steps above (for example, by using a loop) until all 8 values have been shifted in. Then pulse the RCLK pin to write these values to the storage register and data lines, which turns on the LEDs!

In this way, we can control up to 8 different outputs with only 3 GPIOs. This is an incredibly powerful technique that you can use to work with many components at once.

<!-- // DONE: graphic: can resuse the block diagram graphic mentioned above -->
![Block diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shift-register-block-diagram.png)

#### Daisy-Chaining

Shift registers can also be connected in series to each other to extend the number of data lines that can be controlled at once.

Simply connect the SER pin of one shift register to the `QH'` pin on another, and connect their SRCLK and RCLK pins together. That way, when you pulse SRCLK, the 2nd chip will read from the last output of the 1st, and when you pulse RCLK, both chips will update their output lines. This is great because this **does not require any additional GPIOs from the Omega!**

You've now just created a 16-bit shift register. This is known as **daisy-chaining**.

#### Detailed Specifications

if you're curious about the clock cycle timings or other information about the IC, you can refer to the [datasheet for the SN74HC595 shift register](http://www.ti.com/lit/ds/symlink/sn74hc595.pdf). The clock cycle timing diagram can be found on page 8.



<!-- // explanation of a shift register, an external integrated circuit (ic) that takes serial input and provide the data in parallel
// it allows us to essentially expand the number of output pins available to us
// the omega can provide data serially using one data pin, and then the shift register outputs it on its eight data pins

// illustration of how a shift register works
//  - can be simple (clock, serial data in, eight outputs)
//  - explanation of the diagram
//  - the key takeaway should be, pass in 0101 get 0, 1, 0, 1 on the outputs -->
