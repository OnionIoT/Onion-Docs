### The OLED Display

<!-- // DONE: come back to this when merged with master branch -->
<!-- //	-> can reuse this text in all of the OLED articles (Hardware Overview, C Library, Python Module, Node Module) -->

The OLED Expansion has a resolution of 128x64 pixels. It is addressable by 128 vertical columns and 8 horizontal pages.

![display](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-expansion-column-rows.png)

Each page consists of 8 horizontal pixel rows. When a byte is written to the display, the Least Significant Byte (LSB) corresponds to the top-most pixel of the page in the current column. The Most Significant Byte (MSB) corresponds to the bottom-most pixel of the page in the current column.

![display](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/oled-expansion-not-colored-in.png)

The display keeps a cursor pointer in memory that indicates the current page and column being addressed. The cursor will automatically be incremented after each byte is written, the cursor can also be moved by the user through functions discussed later. When writing text to the display, each character is 6 columns wide and 1 page long. This means that 8 lines of text each 21 characters long, can be written to the OLED display.
