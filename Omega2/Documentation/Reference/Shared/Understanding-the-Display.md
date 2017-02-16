### Understanding the Display

The screen has a resolution of 128x64 pixels. It is addressable by 128 vertical columns and 8 horizontal pages:

<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/4JsaahS.png)

Each page consists of 8 horizontal pixel rows. When a byte is written to the display, the Least Significant Byte (LSB) corresponds to the top-most pixel of the page in the current column. The Most Significant Byte (MSB) corresponds to the bottom-most pixel of the page in the current column.

<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/8DIiN2n.png)

So writing 0x0f would produce the top 4 pixels being coloured in, and the bottom 4 being left blank.

The display keeps a cursor pointer in memory that indicates the current page and column being addressed. The cursor will automatically be incremented after each byte is written, the cursor can also be moved by the user through functions discussed below.
