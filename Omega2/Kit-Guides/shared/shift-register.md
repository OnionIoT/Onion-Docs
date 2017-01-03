### Shift Register


A shift register is an external integrated circuit (IC) that can be used to expand the number of output pins available to us. Essentially they let you take serial inputs (one bit after the other) and output them in parallel.


So how does this work? Well we use three pins on the Omega in order to get everything working. One pin, the data pin, is used to send the value we want the shift register to output to *one* of its output pins. The second pin is used to notify the shift register that the data pin has changed and needs to be read. The last pin, the latch pin, notifies the shift register that it's time to output the values that are currently on the shift registers data pins. All of this happens incredibly quickly so it seems to us that it happens simultaneously.


That last paragraph was pretty technical so as an example if you were to send `1011` from the Omega to the shift register it would get 1, 0, 1, 1, on four of its data output pins. This would be sent out in parallel making it seem like there were 4 data pins connected to the Omega!

<!-- TODO: Add an illustration of the shift register where you send 1011 on data pin, and it shows up as 1, 0, 1, 1 on the output pins -->


<!-- // explanation of a shift register, an external integrated circuit (ic) that takes serial input and provide the data in parallel
// it allows us to essentially expand the number of output pins available to us
// the omega can provide data serially using one data pin, and then the shift register outputs it on its eight data pins

// illustration of how a shift register works
//  - can be simple (clock, serial data in, eight outputs)
//  - explanation of the diagram
//  - the key takeaway should be, pass in 0101 get 0, 1, 0, 1 on the outputs -->
