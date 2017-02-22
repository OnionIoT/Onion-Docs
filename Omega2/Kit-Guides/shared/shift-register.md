### Shift Register


A shift register is an external integrated circuit (IC) that can be used to expand the number of output pins available to us. Essentially they let you take serial inputs (one bit after the other) and output them in parallel (all at once on separate data lines).


So how does this work? Well, the shift register is named that way because it contains two **registers** that it **shifts** values through. The register is basically a unit of memory that stores 8 binary values (bits).

* The storage register stores 8 binary values before they are written to the output register and the output lines.
* The output register controls the 8 output lines on the IC, and takes on the values from the storage register whenever the latch pin is pulsed (more on this below).

we use three pins on the Omega in order to control the shift register. 

* The data pin, labelled SER, is read by the shift register whenever we pulse the clock pin.

* The clock pin, labelled SRCLK, is used to trigger the shift register to shift each bit in the storage register forwards by one position, then loads the value from the SER pin into the 1st position. 

* The latch pin, labelled RCLK, notifies the shift register that it's time to output the values that are currently on the shift registers data pins. All of this happens incredibly quickly so it seems to us that it happens simultaneously.

// TODO: the latch pin explanation is confusing!

// TODO: this example isn't too clear

That last paragraph was a little abstract, so as an example if you were to send `1011` from the Omega to the shift register it would get 1, 0, 1, 1, on four of its data output pins. This would be sent out in parallel on separate data lines making it seem like there were additional 4 data pins connected to the Omega!

<!-- TODO: Add an illustration of the shift register where you send 1011 on data pin, and it shows up as 1, 0, 1, 1 on the output pins -->


<!-- // explanation of a shift register, an external integrated circuit (ic) that takes serial input and provide the data in parallel
// it allows us to essentially expand the number of output pins available to us
// the omega can provide data serially using one data pin, and then the shift register outputs it on its eight data pins

// illustration of how a shift register works
//  - can be simple (clock, serial data in, eight outputs)
//  - explanation of the diagram
//  - the key takeaway should be, pass in 0101 get 0, 1, 0, 1 on the outputs -->
