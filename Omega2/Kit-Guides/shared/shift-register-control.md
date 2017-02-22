<!-- this content is rewritten in shift-register.md
// keeping it here for reference -->

### Controlling a Shift Register
<!-- {{!insert 'shift-register-control'}} -->

There are two clocks on the shift register included in your kit: SRCLK (serial clock) and the RCLK (register clock).  We will refer to the register clock as the **latch pin**.

The SRCLK is used to set up the pins on the shift register. When the SRCLK is pulled **high** the shift register reads the value on the SER pin. How does this let us control LEDs again? Well, say you have 8 LEDs hooked up to the shift registers outputs, and we want to turn on the 1st, 3rd and the 8th LED. So what we do is clear out the register so all LEDs are off. Then we set the SER pin to 1, and pulse the SRCLK (pull it high and then low). We repeat this for four 0s, one 1, one 0, then one last 1. This leaves us with `10000101`.

Every time we want to add a new value to the shift register, we pulse the SRCLK. This moves all the values on the shift register's output pins forwards by one position, and inserts the current value of the data pin into position 1.


The RCLK, or latch pin, is used as a signal to set the output pins to the values to those of the new shift register values. When this is pulled **high** the values that the SRCLK set up are sent out to the output pins. We pulse this pin in order to show the new values on the shift register's output pins.

// TODO: should use common nomenclature (SRCLK, RCLK, SER) in this and the other shift register snippet. go back to the previous shift register snippet and explicityl introduce the data, clock, and latch lines, introduce the SRCLK, RCLK, and SER names as well


You can refer to the [datasheet of the SN74HC595 shift register](http://www.ti.com/lit/ds/symlink/sn74hc595.pdf) for more information. The clock cycle timing diagram can be found on page 8.

<!-- // introduce the idea of a clock, explain that it provides the shift register with a signal to read the data that's currently on the serial data in pin. make sure to note that the data on the serial data in pin needs to be settled before the clock edge!

// show how changing the data on the serial data pin will affect the outputs
// good place to introduce the latching register ie displaying the values of each step. mention that this can be used to set up your output values (pass in all of the serial data) before actually outputting it -->
