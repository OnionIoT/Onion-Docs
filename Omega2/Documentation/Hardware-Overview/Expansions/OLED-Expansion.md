---
title: OLED Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## OLED Expansion {#oled-expansion}

<!-- // intro to the oled expansion - power efficient, tiny screen, mention the resolution and that it's monochrome
<!-- // can write text, draw images, adjust settings, do some little animations (scrolling) -->


The OLED Expansion is an extremely power efficient 0.96″ monochrome (black and white) OLED display for your Omega. With a resolution of 128×64, it is very handy for displaying text, drawing images, and even animation!

This Expansion communicates with the Omega using the I2C protocol. If you're curious, check out the [article on I2C](#communicating-with-i2c-devices).

<!-- // mention this expansion is controlled with i2c -->

### The Hardware

<!-- // Overview of the hardware: -->
<!-- //  - the screen -->

The main purpose of the OLED expansion is to display things on a screen. That's why the only significant hardware on the Expansion is an OLED screen.

![photo](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/oled-onion-display.png)


#### Connecting to a Dock

<!-- // plugged into the expansion Header -->
<!-- // have photos of it plugged into the Exp dock, power dock, and arduino dock 2 -->

The OLED Expansion plugs into a Dock with an Expansion Header. You can also stack it on top of other Expansions and use them together.

<!-- // mention that it's headers are blind - can't stack other expansions on top of it, but you wouldn't want to anyways since it would cover your screen? -->

![oled expansion dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-top-expansion-dock.JPG)

![oled power dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-top-power-dock.JPG)

![oled arduino dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-top-arduino-dock.JPG)


The OLED Expansion headers are blind, meaning you can't stack other Expansions on top. Otherwise you wouldn't be able to see the screen!

#### At a Glance

<!-- // illustration -->

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-expansion-illustration.png)

#### The Screen

<!-- // talk about how it's an OLED screen, mention the size and resolution, and mention resolution in terms of text characters -->

The screen is a 0.96″ OLED (organic light-emitting diode) screen and so the display makes its own light, no backlight is required. This reduces the power required to run the OLED and is why the display has such high contrast. The resolution of the screen is 128x64 (Length x Width), and when displaying text there are 8 rows, with 21 possible characters in each row.


#### Understanding the Display

<!-- // see the following section: https://wiki.onion.io/Documentation/Libraries/OLED-Expansion-C-Library#programming-flow_understanding-the-display -->

<!-- // include it and expand on it/make it sound nice -->

The OLED display is addressable by 128 columns and 8 rows (referred to as pages), as seen in the picture below:

![the columns and rows](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-expansion-column-rows.png)

Each page consists of 8 pixel rows. When a byte is written to the display, the Least Significant Byte (LSB) corresponds to the top-most pixel of the page in the current column. The Most Significant Byte (MSB) corresponds to the bottom-most pixel of the page in the current column.

![not-colored-in-example](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-expansion-not-colored-in.png)

So writing `0x0f` to `SEG0` would produce the top 4 pixels being colored in, and the bottom 4 being left blank in that column:

![colored-in-example](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-expansion-colored-in.png)

### Using the OLED Expansion

<!-- // give an example of when this would be useful: displaying some data using your omega -->

The OLED Expansion is incredibly useful because it gives you the ability to display information using your Omega. It can be used in your projects to display things like you twitter feed, stock prices, or even just information about your Omega (disk space, memory usage).


For more on using the Omega Expansion you can check out our [guide to using the OLED Expansion](#using-oled-expansion).

### Technical Drawing

We have provided a [PDF](https://raw.githubusercontent.com/OnionIoT/technical-drawings/master/Mechanical/OM-E-OLE.PDF) here.

<!-- // point them to the article on using the oled expansion -->
<!-- // this article can be heavily based on the existing doc: https://wiki.onion.io/Tutorials/Expansions/Using-the-OLED-Expansion -->
