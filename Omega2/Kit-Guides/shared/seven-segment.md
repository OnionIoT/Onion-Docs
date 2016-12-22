### 7-Segment Display

If you're wondering why it's called a 7-segment display, wonder no more!
// description of how a digit on the 7seg display is broken up into segments, with a separate input controlling each one

If you take a look at a 7-segment display closely you'll see that each digit is split into seven different segments. Each segment is connected directly to an input pin and is controlled individually.


// include illustration of 7-seg display here with all of the segments labelled
![labelled segments](../../img/seven-segment-display-segments.png)

If you're controlling a 7-segment display that has many digits you'll need to control each segment individually. This can really add up so we can use a shift register to increase the number of output pins available to us.

// description of how the scan pins work on displays with multiple digits: two (to 4) pins control which digit is currently being edited

// [make sure to note that]: usually seven segment displays are used in conjunction with shift registers to minimize the number of pins used on the controller
