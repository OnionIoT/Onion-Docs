## OLED Expansion Python Module {#oled-expansion-python-module}

The Onion OLED Expansion Python module, `oledExp` is based on the [C OLED Expansion Library](./OLED-Expansion-C-Library). Using this module, you will be able to control the OLED Expansion from within your Python program.

![Omega+OLED Expansion](http://i.imgur.com/tqcRlgG.jpg)


[[_TOC_]]




<!-- Programming Flow -->

### Programming Flow

After each power-cycle, the chip that controls the OLED Expansion must be programmed with an initialization sequence to setup the display and enable it to receive additional commands.

After the initialization, the other functions can be used to ajdust various screen settings or display text or images.


#### Understanding the Display

The screen has a resolution of 128x64 pixels. It is addressable by 128 vertical columns and 8 horizontal pages:

![Page and column visual](http://i.imgur.com/4JsaahS.png)

Each page consists of 8 horizontal pixel rows. When a byte is written to the display, the Least Significant Byte (LSB) corresponds to the top-most pixel of the page in the current column. The Most Significant Byte (MSB) corresponds to the bottom-most pixel of the page in the current column.

![Page detail](http://i.imgur.com/8DIiN2n.png)

So writing `0x0f` would produce the top 4 pixels being coloured in, and the bottom 4 being left blank.

<!-- LAZAR: add more examples and an image showing the examples -->

The display keeps a cursor pointer in memory that indicates the current page and column being addressed. The cursor will automatically be incremented after each byte is written, the cursor can also be moved by the user through functions discussed below.

<!-- MAJOR HEADING -->
<!-- The Python Module -->

### The Python Module

The `oledExp` Python module in the `OmegaExpansion` package provides a wrapper around the C library functions. The functions are largely the same as their C counterparts, including the arguments and return values. Any differences from the C library will be explicitly mentioned below.


<!-- Source Code -->

#### Source Code

The source code can be found in the [Onion `i2c-exp-driver` GitHub Repo](https://github.com/OnionIoT/i2c-exp-driver).


<!-- Using the Python Module -->

#### Using the Python Module

**Installing the Module**

To install the Python module, run the following commands:
```
opkg update
opkg install python-light pyOledExp
```

This will install the module to `/usr/lib/python2.7/OmegaExpansion/`

*Note: this only has to be done once.*


**Using the Module**

To add the Onion OLED Expansion Module to your Python program, include the following in your code:
``` python
from OmegaExpansion import oledExp
```

The functions are largely the same as their C counterparts, including the arguments and return values. Any differences from the C library will be explicitly mentioned below.

One major drawback is that none of the defines found in C are currently implemented in the Python module.


<!-- Python: Example Code -->

#### Example Code

Example code that uses the `oledExp` module can be [found here](https://github.com/OnionIoT/i2c-exp-driver/blob/master/examples/oled-exp.py), in the `i2c-exp-driver` Onion GitHub Repo.



<!-- Python: Return Values -->

#### Return Values

All functions follow the same pattern with return values:

If the function operation is successful, the return value will be `0`.

If the function operation is not successful, the function will return `1`.



<!-- Python: Init Function -->

#### Initialization Function

Perform the initialization sequence on the OLED Expansion, after this step is completed, the other various OLED functions can be used with success:
``` python
oledExp.driverInit()
```

**Examples**

Initialize the OLED Display:
``` c
status 	= oledExp.driverInit();
```



<!-- SUB-HEADING -->
<!-- Settings Functions -->

#### Functions to Adjust Settings

There is a series of functions that adjust various settings on the OLED Display. The adjustable settings are:
* Screen on/off
* Colour inversion
* Setting screen brightness
* Setting the memory mode
* Defining the width of each page
* Setting the cursor position


<!-- Python: Screen on/off -->

##### Turn the Screen On and Off

The screen can be turned on and off while still preserving the displayed contents:
``` python
oledExp.setDisplayPower(bPowerOn)
```

Note: turning on a screen that is already on, or turning off a screen that is already off will have no effect.

**Arguments**

The `bPowerOn` argument is detemines whether to turn the display on or off

| Value   | Meaning                   |
|---------|---------------------------|
| 0       | Turn the screen **off**   |
| 1       | Turn the screen **on**    |


**Examples**

Turn the screen off:
``` python
status = oledExp.setDisplayPower(0)
```

Turn the screen on:
``` python
status = oledExp.setDisplayPower(1)
```


<!-- Python: Invert Display Colours -->

##### Invert Display Colours

The screen driver has the ability to invert the display colours, meaning that black becomes white and vice versa:
``` python
oledExp.setDisplayMode(bInvert)
```

**Arguments**

The `bInvert` argument is detemines whether to invert the colours or not

| Value   | Meaning                   |
|---------|---------------------------|
| 0       | Normal colour settings    |
| 1       | Inverted colour settings  |

**Examples**

Invert the colours:
``` python
status = oledExp.setDisplayMode(1)
```

Return the colours to normal:
``` python
status = oledExp.setDisplayMode(0)
```


<!-- Python: Set Brightness -->

##### Set the Display Brightness

The brightness of the display can be adjusted in a granularity of 256 steps:
``` python
oledExp.setBrightness(brightness)
```

The default brightness after initialization is 207.

**Arguments**

The `brightness` argument is detemines the display brightness with a range of **0 to 255**, with 255 being the brightest setting and 0 being the dimmest.


**Examples**

Set to maximum brightness:
``` python
status = oledExp.setBrightness(255)
```

Set to lowest possible brightness:
``` python
status = oledExp.setBrightness(0)
```

Set to middle brightness:
``` python
status = oledExp.setBrightness(127)
```


<!-- Python: Dim the display -->

##### Dim the display

This function implements a 'dim' and a 'normal' setting for the display:
``` python
oledExp.setDim(dim)
```

While the brightness adjustment function described just above implements the same feature, this function simplifies the procedure with two very disctinct settings.


**Arguments**

The `dim` argument is detemines whether to enable the dim setting

| Value   | Meaning                         |
|---------|---------------------------------|
| 0       | Normal brightness: 207          |
| 1       | Dimmed screen: 0                |

**Examples**

Dim the display:
``` python
status = oledExp.setDim(1)
```

Set the display to normal brightness:
``` python
status = oledExp.setDim(0)
```


<!-- Python: Set the memory mode -->

##### Set Memory Mode

Implements the ability to select the display's memory mode:
``` python
oledExp.setMemoryMode(mode)
```

The memory mode affects how the cursor is automatically advanced when the display memory is written to with text or images.


**Horizontal Addressing Mode**

![Horizontal Addressing](http://i.imgur.com/sU0WyZY.png)

After each write, the column cursor advances horizontally to the right along the page, once the end of the page is reached, the page cursor is advanced onto the next page.


**Vertical Addressing Mode**

![Vertical Addressing](http://i.imgur.com/Dv1smND.png)

After each write, the page cursor advances vertically downward through the pages, once the last page is reached, the column cursor is advanced to the next pixel column


**Page Addressing Mode**

![Page Addressing](http://i.imgur.com/oW4giq6.png)

The column cursor advances horizontally to the right along each page, once the end of the page is reached, the column cursor wraps around to column 0 and the page cursor remains the same.

By default, **Horizontal Addressing** is used.


**Arguments**

The `mode` argument detemines which memory mode is active. Unfortunately, the C defines do not carry over to Python, follow this table for selecting the desired mode:

| Memory Mode                | `mode` Argument    |
|----------------------------|--------------------|
| Horizontal Addressing Mode | 0                  |
| Vertical Addressing Mode   | 1                  |
| Page Addressing Mode       | 2                  |

**Examples**

Set to page addressing mode:
``` python
status = oledExp.setMemoryMode(2)
```

Set to horizontal addressing mode:
``` python
status = oledExp.setMemoryMode(0)
```


<!-- Python: Set Column Addressing -->

##### Set Column Addressing

This function is used to define where each page starts and ends horizontally:
``` python
oledExp.setColumnAddressing(startPixel, endPixel)
```

Changing the start and end pixels changes the width of each page. By default, the column addressing is set from 0 to pixel 127. This means that each page has 128 usable columns, once the cursor reaches the last column, the display knows this page is filled.

For example, when writing text, the `oledWrite` function will set the columns to run from 0 to 125 in order for the characters to display properly. Since each character is 6 columns, 21 full characters can be displayed on a single line, the end pixel is set to 125 so that the 22nd character gets placed on the next line instead.

Note: the column cursor is not preserved after a column addressing change.

**Arguments**

The `startPixel` argument sets the starting column for each page.

The `endPixel` argument sets the end column for each page.

Both arguments must be between **0 and 127** and startPixel must be **less than** endPixel.

Again, the C defines do not carry over to Python, regular numbers will have to be used for the start and end pixel arguments.

**Examples**

Set the column addressing to display text:
``` python
status = oledExp.setColumnAddressing(0, 126-1)
```

Set the column addressing to the full display width
``` python
status = oledExp.setColumnAddressing(0, 128-1)
```

Set each column to start halfway across and to end three quarters of the way across the display:
``` python
status = oledExp.setColumnAddressing(63, 95)
```


<!-- Python: Set Column Addressing: Text Columns -->

###### Set Columns for Text

This function defines the column addressing specifically for text:
``` python
oledExp.setTextColumns()
```

It sets the start pixel to 0 and the end pixel to 125. This allows for 21 text characters per line. This function should be run before setting the cursor for writing text.


<!-- Python: Set Column Addressing: Image Columns -->

###### Set Columns for Images

Alternatively, this function defines the column addressing to cover the entire screen:
``` python
oledExp.setImageColumns()
```

It sets the start pixel to 0 and the end pixel to 127. This enables the use of the entire screen real estate.






<!-- Python: Set Cursor Position -->

##### Set Cursor Position

Any data written to the screen gets written to the current position of the cursor. This position can be adjusted.

Two methods exist:
* Specifying the page row and character column
* Specifying the page row and pixel column


<!-- Python: Set Cursor Position: By Character Column -->

###### Set Cursor Position by Character Column

This function is used to position the cursor on a specific page and character column. After this call, the next bytes written to the screen will be displayed at the new position of the cursor:
``` python
oledExp.setCursor(row, column)
```

Note: since the column cursor is not preserved after a column addressing change, the column addressing **needs be set to 0-125 to using the `oledExp.setTextColumns()` function to properly display text before the cursor position is programmed.**


**Arguments**

The `row` argument sets the page for the cursor, so the range is **0 to 7**

The `column` argument sets the character column position of the cursor, the range is **0 to 20**


**Examples**

Set the cursor to the start of the last page:
``` python
status = oledExp.setCursor(7, 0)
```

Set the cursor to the middle of the 4th row:
``` python
status = oledExp.setCursor(3, 10)
```

Set the cursor to the starting position at the top-right
``` python
status = oledExp.setCursor(0, 0)
```

Write 'hello' at the top left of the screen, and then write 'hi there' on the middle of the 7th row:
``` python
status 	= oledExp.setCursor(0, 0)
status	|= oledExp.write("hello")
status 	|= oledExp.setCursor(6, 10)
status	|= oledExp.write("hi there")
```


<!-- Python: Set Cursor Position by Pixel -->

###### Set Cursor Position by Pixel

This function is used to position the cursor on a specific page and pixel row. This gives more fine grain control than setting by character column. After this call, the next bytes written to the screen will be displayed at the new position of the cursor:

``` python
oledExp.setCursorByPixel(row, pixel)
```

It allows for cursor positions that are not aligned with the 21 possible character columns.

**Arguments**

The `row` argument sets the page for the cursor, so the range is **0 to 7**

The `pixel` argument sets the horizontal pixel position of the cursor, the range is **0 to 127**


**Examples**

Set the cursor to the start of the last page:
``` python
status = oledExp.setCursorByPixel(7, 0)
```

Set the cursor to the middle of the 4th row:
``` python
status = oledExp.setCursorByPixel(3, 63)
```

Set the cursor to the bottom-left
``` python
status = oledExp.setCursorByPixel(7, 0)
```

Write 'hello' at the top left of the screen, and then write 'hi there' on the middle of the 7th row:
``` python
oledExp.setCursorByPixel(0, 0)
oledExp.write("hello")
oledExp.setCursorByPixel(6, 63)
oledExp.write("hi there")
```





<!-- Clearing Function -->

#### Clear the Screen

To clear the screen and move the cursor to the starting position at the top-left of the screen:
``` python
oledExp.clear()
```



<!-- SUB-HEADING -->
<!-- Writing Text -->

#### Writing Text to the Display

Listed below are the functions that write bytes, characters, strings, or images to the display.


<!-- Python: Write Byte -->

##### Write a Single Byte

Write a single byte, eight vertical pixels, to the current position of the cursor:

``` python
oledExp.writeByte(byte)
```

**Arguments**

The `byte` argument is the eight bits that will be written to the screen. The Least Significant Bit (LSB) in the byte corresponds to the top-most pixel in the column, the Most Significant Bit (MSB) corresponds to the bottom-most pixel in the column.

![Page detail](http://i.imgur.com/8DIiN2n.png)

After the byte is set, the cursor will automatically move to the next page column.


**Examples**

Draw the following pattern:

![Page detail](http://i.imgur.com/lxs1q8J.png)

``` python
status =  oledExp.writeByte(0x01)		# 0x01 = 0b 0000 0001
status |= oledExp.writeByte(0x03)		# 0x03 = 0b 0000 0011
status |= oledExp.writeByte(0x07)		# 0x07 = 0b 0000 0111
status |= oledExp.writeByte(0x0f)			# 0x0f = 0b 0000 1111
status |= oledExp.writeByte(0x3f)			# 0x3f = 0b 0011 1111
```


<!-- Python: Write Character -->

##### Write a Single Character

Write a single character to the current position of the cursor:
``` python
oledExp.writeChar(c)
```

**Arguments**

The `c` argument is the character that is to be written to the screen.

Make sure to check the `asciiTable` dynamic array found in `oled-exp.h`, it defines the bitmap pattern of each allowed character. Any characters not found in the table will be ignored.


**Examples**

Write an 'O'
``` python
status = oledExp.writeChar('O')
```

Write an open bracket, an x, then a close bracket:
``` python
status =  oledExp.writeChar('(')
status |= oledExp.writeChar('x')
status |= oledExp.writeChar(')')
```



<!-- Python: Write String -->

##### Write a String

Write an entire string of characters, starting at the current position of the cursor:
``` python
oledExp.write(msg)
```

Underneath, this uses the `oledWriteChar` function to display characters and also implements newline functionality.

The newline functionality is implemented by using a global variable to keep track where the cursor is in each row (I know... shameful...). Once the characters '\' and 'n' are detected, the `oledWrite` function will print spaces to the display until it reaches the end of the current page and the cursor increments its position to the next page.

Note: the column addressing will be set to 0-125 to properly display text during this call, at the end of the function it will be reset back to 0-127.


**Arguments**

The `msg` argument is the string to be written to the display. Any characters not found in the `asciiTable` array will be ignored.


**Examples**

Write 'Onion Omega':
``` python
status = oledExp.write("Onion Omega");
```

Write 'Python rules!', then 'Especially on', and then 'the Omega' two lines below:
``` python
status = oledExp.write("Python rules!\nEspecially on\n\nthe Omega")
```





<!-- SUB-HEADING -->
<!-- Displaying Images -->

#### Drawing Images on the Display

The OLED Screen can also be used to display images. The Console can be used to convert existing images into a format that is compatible with the OLED Expansion and save the output to an Omega. Functions in the Python module can read the image data and display it on the OLED Expansion.


<!-- Displaying Images: Creating Image Files -->

##### Creating Image Files

The Console OLED App can be used to create OLED Expansion compatible image files. Navigate to the Image tab of the OLED App:

![OLED Console App Image Tab](http://i.imgur.com/FPCVp8x.png)

Once an image has been selected, a button and form will appear that allow you to save the OLED image file to your Omega:

![OLED Console App Loaded Image](http://i.imgur.com/xKx5KHa.png)

After the image name and location are selected, click the Save to Omega button.


<!-- Displaying Images: OLED Image File Details -->

##### OLED Image File Details

The OLED image files store the image data as 1024 bytes represented in hexadecimal. Each byte represents eight vertical pixels, with the first 128 bytes representing the columns in Page 0, the following 128 bytes representing the columns in Page 1, and so on.

If this is unclear, see the [Understanding the Display Section](#programming-flow_understanding-the-display) for details on how the display is addressed.


<!-- Displaying Images: Displaying Images from a File -->

##### Displaying Images from a File

Read the image data from a file and display on the OLED screen:
``` python
status = oledExp.drawFromFile(file)
```

**Arguments**

The `file` argument is the path to the OLED image file.


**Examples**

Read an image file located at `/root/image.lcd` and draw it on the OLED display:
``` python
status = oledExp.drawFromFile("/root/image.lcd")
```





<!-- SUB-HEADING -->
<!-- Scrolling the Display -->

#### Scrolling the Display Contents

The OLED can scroll the contents of the screen horizontally or upwards at a 45 degree angle. The displayed content will wrap around when it reaches the edge of the display.



<!-- Horizontal scrolling -->

##### Horizontal Scrolling

Scroll all or part of the screen horizontally:
``` python
oledExp.scroll(direction, scrollSpeed, startPage, stopPage)
```

**Arguments**

The `direction` argument indicates whether to scroll to the left or right:

| `direction` Value | Scrolling Direction |
|-------------------|---------------------|
| 0                 | Left                |
| 1                 | Right               |

The `scrollSpeed` argument determines the number of "frames" between each scroll step:

| Scroll Speed                      | `scrollSpeed` Argument  |
|-----------------------------------|-------------------------|
| OLED_EXP_SCROLL_SPEED_5_FRAMES	| 0                       |
| OLED_EXP_SCROLL_SPEED_64_FRAMES	| 1                       |
| OLED_EXP_SCROLL_SPEED_128_FRAMES	| 2                       |
| OLED_EXP_SCROLL_SPEED_256_FRAMES	| 3                       |
| OLED_EXP_SCROLL_SPEED_3_FRAMES	| 4                       |
| OLED_EXP_SCROLL_SPEED_4_FRAMES	| 5                       |
| OLED_EXP_SCROLL_SPEED_25_FRAMES	| 6                       |
| OLED_EXP_SCROLL_SPEED_2_FRAMES	| 7                       |


The `startPage` argument defines at which page to start scrolling, and `stopPage` defines at which page to start the scroll. The range for both is **0 to 7**, and startPage must be less than stopPage.


**Examples**

<!-- LAZAR: Add gifs to all examples -->

Scroll the entire screen to the left:
``` python
status = oledExp.scroll (0, 0, 0, 8-1)
```

![left scroll](http://i.imgur.com/nytY4Xw.gif)

Quickly scroll the bottom half of the screen to the right:
``` python
status = oledExp.scroll (1, 7, 4, 8-1)
```

Slowly scroll pages 1 to 5:
``` python
status = oledExp.scroll (1, 6, 1, 5)
```


<!-- Diagonal scrolling -->

##### Diagonal Scrolling

Scroll all or part of the screen diagonally upwards:
``` python
oledExp.scrollDiagonal(direction, scrollSpeed, fixedRows, scrollRows, verticalOffset, startPage, stopPage)
```


**Arguments**

The `direction` argument indicates whether to scroll upwards to the left or right:

| `direction` Value | Scrolling Direction |
|-------------------|---------------------|
| 0                 | Upwards and Left    |
| 1                 | Upwards and Right   |

The `scrollSpeed` argument determines the number of "frames" between each scroll step:

| Scroll Speed                      | `scrollSpeed` Argument  |
|-----------------------------------|-------------------------|
| OLED_EXP_SCROLL_SPEED_5_FRAMES	| 0                       |
| OLED_EXP_SCROLL_SPEED_64_FRAMES	| 1                       |
| OLED_EXP_SCROLL_SPEED_128_FRAMES	| 2                       |
| OLED_EXP_SCROLL_SPEED_256_FRAMES	| 3                       |
| OLED_EXP_SCROLL_SPEED_3_FRAMES	| 4                       |
| OLED_EXP_SCROLL_SPEED_4_FRAMES	| 5                       |
| OLED_EXP_SCROLL_SPEED_25_FRAMES	| 6                       |
| OLED_EXP_SCROLL_SPEED_2_FRAMES	| 7                       |

The `fixedRows` argument defines the amount of pixel rows, starting from the top, **will not** have vertical scrolling. The range is **0 to 63**.

The `scrollRows` argument defines the amount of pixel rows, starting from the top, that **will** have vertical scrolling.

The `verticalOffset` argument defines the number of vertical rows to scroll by each frame.

The `startPage` argument defines at which page to start scrolling, and `stopPage` defines at which page to start the scroll. The range for both is **0 to 7**, and startPage must be **less than** stopPage.


**Examples**

Scroll the entire screen upwards to the left:
``` python
status = oledExp.scrollDiagonal (	0,
				5,
				0,
				128-1,
				1,
				0,
				8-1
			)
```

Slowly Scroll the entire screen upwards to the right:
``` python
status = oledExp.scrollDiagonal (	1,
				1,
				0,
				128-1,
				1,
				0,
				8-1
			)
```

![diagonal-right scroll](http://i.imgur.com/9JcoKEj.gif)



<!-- Stop scrolling -->

##### Stop Scrolling

Disables all active scrolling:
``` python
oledExp.scrollStop()
```

**Examples**

Scroll the entire screen to the left, then stop it:
``` python
status = oledExp.scroll (0, 0, 0, 7)
status |= oledExp.scrollStop(0)
```
