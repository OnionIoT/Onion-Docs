### 7-Segment Display

If you're wondering why it's called a 7-segment display, wonder no more!

If you take a look at a 7-segment display closely you'll see that each digit is split into seven different segments. Each segment is connected directly to an input pin and is controlled individually. See the diagram below for a typical labelling scheme:

![labelled segments](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/seven-segment-display-segments.png)

Now, if you're controlling a 7-segment display that has more than one digit, each segment is usually **connected in parallel** across all of the digits; this is to save pins on the display module itself. For example, this means that turning on segment A means that it will light up everywhere! // TODO: this was confusing and didn't convey the idea clearly

This isn't really useful, so each digit has its own **scan** pin that groups segments for each digit together. This pin then controls whether the digit's LEDs can be turned on or not.

To control the segments on a single-digit 7-seg display, you need at least seven GPIOs. And in order to control multiple digits at once, we need one additional GPIO for each scan pin. This can really add up, so we can use a shift register to increase the number of output pins available to us. This is usually how 7-segs are incorporated into a project in order to minimize the number of pins used on the controller.

7-segment displays are sometimes called "7-segs" for short.
