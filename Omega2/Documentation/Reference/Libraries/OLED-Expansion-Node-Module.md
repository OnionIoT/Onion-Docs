## OLED Expansion Node Module

As a part of our efforts to add expansion support to node.js, we have added control of the OLED expansion by way of node.js module. To use the display within your node.js programs, all you have to do is import the OLED module in the same way as a module and call methods to control the display.

<!-- TODO: IMAGE reupload this to github -->

![Omega+OLED Expansion](http://i.imgur.com/tqcRlgG.jpg)

The module is a wrapper around the OLED C library. The library's documentation can be found [here](https://docs.onion.io/omega2-docs/oled-expansion-c-library.html), many of the node functions follow the same input-output structure as the C library.


### Programming Flow {#oled-node-programming-flow}


After each power-cycle, the chip that controls the OLED Expansion must be programmed with an initialization sequence to setup the display and enable it to receive additional commands.

After the initialization, the other functions can be used to adjust vaious screen settings or display text or images.


```{r child = '../Shared/Understanding-the-Display.md'}
```


### The Node Module {#oled-node-description}


The OLED Expansion module exposes a series of methods that perform all of the actions specified in the Programming Flow section.


#### Install the Module

Install the module on your Omega:

``` bash
opkg update
opkg install node-oled-exp
```

NodeJS will need to be installed for Node programs to actually run:

``` bash
opkg install nodejs
```

#### Importing the module into your Node Script

To use the module within your script you have to import it into your node program as you would a module. Use the following command in your node script.

``` javascript
var oledExp = require("/usr/bin/node-oled-exp");
```




#### Example Code

Example code that uses the `node-oled-exp` module can be [found here](https://github.com/OnionIoT/i2c-exp-node-addons/blob/master/Examples/oled_node_example.js) in the `i2c-exp-node-addons` Onion GitHub Repo.


#### Return Values

All of the functions will either return a 0 indicating success or 1 indicating failure.


#### Calling Methods

Methods are called in the following format.

``` javascript
oledExp.method();
```
Replace method with your funcion of interest.

### Available Methods {#oled-node-function-table}

Refer to the table below for a list and brief description of available OLED methods.

| Method                                                                                                                          | Inputs                             | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------|-----------------------------------------------------------------------------------------|
| [init()](#oled-node-init)                                                                                                                          | none                               | Initializes the display                                                                 |
| [clear()](#oled-node-clear)                                                                                                                         | none                               | Clears the Display                                                                      |
| [setDisplayPower(int)](#oled-node-set-display-power)                                                                                                            | 1,0                                | Turns the screen on or off                                                              |
| [setDisplayMode(int)](#oled-node-set-display-mode)                                                                                                             | 1,0                                | Inverts the color settings                                                              |
| [setBrightness(int)](#oled-node-set-brightness)                                                                                                              | 0-255                              | Adjust display brightness                                                               |
| [setDim(int)](#oled-node-set-dim)                                                                                                                     | 1,0                                | Dims/brightens display to preset value.                                                 |
| [setMemoryMode(int)](#oled-node-set-memory-mode)                                                                                                             | 0,1,2                              | Sets the display's memory mode                                                          |
| [setCursor(int row, int column)](#oled-node-set-cursor)                                                                                                  | 0-7,0-20                           | Position the cursor on a specific page and character column.                            |
| [setCursorByPixel(int row, int pixel)](#oled-node-set-cursor-by-pixel)                                                                                            | 0-7,0-127                          | Positions the cursor on a specific page and pixel row                                   |
| [setColumnAddressing(int startPixel, int endPixel)](#oled-node-set-column-addressing)                                                                               | 0-127,0-127                        | Sets where each page starts and ends horizontally                                       |
| [setTextColumns()](#oled-node-set-text-columns)                                                                                                                | none                               | Sets the column addressing for text display                                             |
| [setImageColumns()](#oled-node-set-image-columns)                                                                                                               | none                               | Sets the column addressing to default                                                   |
| [writeChar(char "A")](#oled-node-write-char)                                                                                                             | single character in a string input | Writes a single character to the current position of the cursor.                        |
| [write(msg)](#oled-node-write)                                                                                                                      | string "HelloWorld"                | Writes a string of characters, starting at the current positon of the cursor            |
| [writeByte(int byte)](#oled-node-write-byte)                                                                                                             | 0x00 - 0xFF                        | Write a single byte to the current position of the cursor.                              |
| [scroll(int direction, int scrollSpeed, int startPage, int stopPage)](#oled-node-scroll)                                                             | \*                                 | Scroll all or part of the screen horizontally - contents will wrap        |
| [scrollDiagonal( int direction, int scrollSpeed, int fixedRows, int scrollRows, int verticalOffset, int startPage, int stopPage)](#oled-node-scroll-diagonal) | \*\*                               | Scroll all or part of the screen diagonally upwards - contents will wrap                |
| [scrollStop()](#oled-node-scroll-stop)                                                                                                                    | none                               | Disables all active scrolling                                                           |
| [readLcdFile("path")](#oled-node-read-lcd-file)                                                                                                             | "Path to LCD File"                 | Displays lcd image file on the screen                                                   |


### Initialization {#oled-node-init}

This function programs the initilization sequence on the OLED Expansion, after this step is completed, the various OLED functions can be used with success:

``` javascript
oledExp.init();
```


### Clearing the Display {#oled-node-clear}
To clear the screen and move the cursor to the starting position at the top-left of the screen:
``` javascript
oledExp.clear();
```


### Functions to Adjust Settings {#oled-node-adjust-settings}

There is a series of functions that adjust various settings on the OLED Display. The adjustable settings are:

 * [Screen on/off](#oled-node-set-display-power)
 * [Color inversion](#oled-node-set-display-mode)
 * [Setting screen brightness](#oled-node-set-brightness)
 * [Setting the memory mode](#oled-node-set-memory-mode)
 * [Defining the width of each page](#oled-node-set-column-addressing)
 * [Setting the cursor position](#oled-node-set-cursor)


### Turn Display Off/On {#oled-node-set-display-power}
The screen cab be turned on and off while still preserving the displayed contents.Note: turning on a screen that is already on, or turning off a screen that is already off will have no effect.
``` javascript
oledExp.setDisplayPower(int bPowerON);
```

#### Arguments

The `bPowerOn` argument determines whether to turn the display on or off.

|Value|Meaning             |
|-----|--------------------|
|0    |Turn the screen off |
|1    |Turn the screen on  |

#### Examples

Turn the screen off with:

``` javascript
oledExp.setDisplayPower(0);
```
Turn the screen on with:

``` javascript
oledExp.setDisplayPower(1);
```


### Invert Display Color {#oled-node-set-display-mode}
The screen driver has the ability to invert the display colors, meaning that black becomes white and vice versa. To invert the colors:
``` javascript
oledExp.setDisplayMode(int bInvert);
```

#### Arguments

The `bInvert` argument determines whether to inver the colors or not.

|Value|Meaning                 |
|-----|------------------------|
|0    |Normal color settings   |
|1    |Inverted color settings |


#### Examples

To invert the colors:
``` javascript
oledExp.setDisplayMode(1);
```

To revert back to the normal colors:
``` javascript
oledExp.setDisplayMode(0);
```


### Set the Display Brightness {#oled-node-set-brightness}

The brightness of the display can be adjusted in a granularity of 256 steps. The default brightness after initialization is 207.
``` javascript
oledExp.setBrightness(int brightness);
```

#### Arguments

The `brightness` argument determines the brightness with a range of `0-255`, with `255` being the brightest setting and `0` being the dimmest.

#### Examples

So to set the maximum brightness:
``` javascript
oledExp.setBrightness(255);
```

To set the lowest brightness:
``` javascript
oledExp.setBrightness(0);
```

And to set the middle brightness:
``` javascript
oledExp.setBrightness(127);
```

### Dim the Display {#oled-node-set-dim}

This function implements a 'dim' and a 'normal' setting for the display:

``` javascript
oledExp.setDim(int dim);
```

While the brightness adjustment function described just above impleents the same feature, this function
simplifies the procedure with two distinct settings.

#### Arguments

The `dim` argument determines whether to enable the dim setting

|Value |Meaning                |
|------|-----------------------|
|0     |Normal Brightness: 207 |
|1     |Dimmed Screen:0        |


#### Examples

Dim the Display:
``` javascript
oledExp.setDim(1);
```

Set the Display to normal brightness:

``` javascript
oledExp.setDim(0);
```

### Set Memory Mode {#oled-node-set-memory-mode}

Implements the ability to select the display's memory mode:
``` javascript
oledExp.setMemoryMode(int mode);
```
The memory mode affects how the cursor is automatically advanced when the display memory is written with text or images.

**Horizontal Addressing Mode**

<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/sU0WyZY.png)

After each write, the column cursor advances horizontally to the right along the page, once the end of the page is reached, the page cursor is advanced onto the next page.

**Vertical Addressing Mode**

<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/Dv1smND.png)

After each write, the page cursor advances vertically downward through the pages, once the last page is reached, the column cursor is advanced to the next pixel column.

**Page Addressing Mode**

<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/oW4giq6.png)

The column cursor advances horizontally to the right along each page, once the end of the page is reached, the column cursor wraps around to column 0 and the page cursor remains the same.

By default, **Horizontal Addressing** is used.

#### Arguments

The `mode` argument determines which memory mode is active.

|Memory Mode                |Input |
|---------------------------|------|
|Horizontal Addressing Mode |0     |
|Vertical Addressing Mode   |1     |
|Page Addressing Mode       |2     |

#### Examples

Set to the page addressing mode:
``` javascript
oledExp.setMemoryMode(2);
```


### Set Column Addressing {#oled-node-set-column-addressing}

This function is used to define where each page starts and ends horizontally:
``` javascript
oledExp.setColumnAddressing(int startPixel, int endPixel);
```

Changing the start and end pixels changes the width of each page. By default, the column addressing is set from 0 to pixel 127. This means that each page has 128 usable columns, once the cursor reaches the last column, the display knows this page is filled.

For example, when writing text, the oledWrite function will set the columns to run from 0 to 125 in order for the characters to display properly. Since each character is 6 columns, 21 full characters can be displayed on a single line, the end pixel is set to 125 so that the 22nd character gets placed on the next line instead.

Note: the column cursor is not preserved after a column addressing change.

#### Arguments

|  Argument  |    Values    |  Description                              |
|------------|--------------|-------------------------------------------|
| startPixel | `0 - 127`  |  Sets the starting column for each page.  |
| endPixel   | `0 - 127`  |  Sets the ending column for each page.    |

Both arguments must be between the 0-127 and the startPixel must be **less than** endPixel.

#### Examples

Set the column addressing display text:
``` javascript
oledExp.setColumnAddressing(0,127);
```

Set the column addressing to the full display width:
``` javascript
oledExp.setColumnAddressing(0,63);
```

Set each column to start halfway across an to enf three quartes of the way accross the display:
``` javascript
oledExp.setColumnAddressing(63,95);
```

### Set Columns for Text {#oled-node-set-text-columns}

A function exists to define the column addressing specifically for text:
``` javascript
oledExp.setTextColumns();
```

It sets the start pixel to 0 and the end pixel to 125. This allows for the 21 text characters per line This function should be run, before setting the cursor for writing text.

### Set Columns for Images {#oled-node-set-image-columns}

Also, a function exists to define the column addressing to cover the entire screen:
``` javascript
oledExp.setImageColumns();
```

It sets the start pixel to 0 and te end pixel to 127. This enables the use of the entire screen.

### Set Cursor Position {#oled-node-set-cursor-position}


Any data written to the screen gets writting to the current position of the cursor. This position can be adjusted.

Two methods exist:

 * [Specifying the page row and character column](#oled-node-set-cursor)
 * [Specifying the page row and pixel column](#oled-node-set-cursor-by-pixel)

### Set Cursor Position by Character Column {#oled-node-set-cursor}

This function is used to position the cursor on a specific page and character column. After this call, the next bytes written to the screen will be displayed at the new position of the cursor:
``` javascript
oledExp.setCursor(int row, int column);
```

Note: since the column cursor is not preserved after a column addressing change, the column addressing **needs be set to 0-125 using the oledSetTextColumns() function to properly display text before the cursor position is programmed.**

#### Arguments

|  Argument  |    Values    |  Description                                        |
|------------|--------------|-----------------------------------------------------|
| row        | `0 - 7`    |  Sets the page for the cursor.                      |
| column     | `0 - 20`   |  Sets the character column position of the cursor.  |

The `column` argument sets the character column position of the cursor, the range is 0 to 20.

#### Examples

Set the cursor to the start of the last page:
``` javascript
oledExp.setCursor(7,0);
```

Set the cursor to the middle of the 4th row:
``` javascript
oledExp.setCursor(3,10);
```

Set the cursor to the starting position at the top-left:
``` javascript
oledExp.setCursor(0,0);
```



### Set Cursor Position by Pixel {#oled-node-set-cursor-by-pixel}
This function is used to position the cursor on a specific page and pixel row. This gives more fine grain control than setting by character column.

After this call, the next bytes written to the screen will be displayed at the new position of the cursor:
``` javascript
oledExp.setCursorByPixel(int row, int pixel);
```

It allows for cursor positions that are not aligned with the 21 possible character columns.

#### Arguments

This function requires two arguments, that define vertical row and horizontal pixel position.

|  Argument  |    Values    |  Description                                        |
|------------|--------------|-----------------------------------------------------|
| row        | `0 - 7`    |  Sets the page for the cursor.                      |
| pixel      | `0 - 127`  |  Sets the horizontal pixel position of the cursor.  |


#### Examples

Set the cursor to the start of the last page:
``` javascript
oledExp.setCursorByPixel(7,0);
```

Set the cursor to the middle of the 4th row:
``` javascript
oledExp.setCursorByPixel(3,63);
```

Set the cursor to the bottom-left
``` javascript
oledExp.setCursorByPixel(7,0);
```




### Writing Text to The Display {#oled-node-writing-text}

Listed below are the functions that write bytes, characters, strings, or images to the display.

* [Write a single byte](#oled-node-write-byte)
* [Write a single character](#oled-node-write-char)
* [Write a string](#oled-node-write)

### Write a Single Byte {#oled-node-write-byte}
Write a single byte, eight vertical pixels, to the current position of the cursor:
``` javascript
oledExp.oledWriteByte(int byte);
```

#### Arguments

The `byte` argument holds the eight bits that will be written to the screen. The Least Significant Bit (LSB) in the byte corresponds to the top-most pixel in the column, the Most Significant Bit (MSB) corresponds to the bottom-most pixel in the column.

<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/8DIiN2n.png)

After the byte is set, the cursor will automatically move to the next page column.

#### Examples

Draw the following pattern:

<!-- TODO: IMAGE reupload this to github -->

![imgur](http://i.imgur.com/lxs1q8J.png)

``` javascript
oledExp.writeByte(0x3f);
```

### Write a Single Character {#oled-node-write-char}

Write a single character to the current position of the cursor:
``` javascript
oledExp.writeChar(character);
```

#### Arguments

The `character` argument is the character that is to be written to the screen.

Make sure to check the asciiTable dynamic array found in oled-exp.h, it defines the bitmap pattern of each allowed character. Any characters not found in the table will be ignored.

#### Examples

Write an 'O'
``` javascript
oledExp.writeChar('O');
```

### Write a String {#oled-node-write}

Write an entire string of characters, starting at the current position of the cursor:
``` javascript
oledExp.write(msg);
```

Underneath, this uses the writeChar function to display characters and also implements newline functionality.

The newline functionality is implemented by using a global variable to keep track where the cursor is in each row (I know... shameful...). Once the characters '\' and 'n' are detected, the write function will print spaces to the display until it reaches the end of the current page and the cursor increments its position to the next page.

Note: the column addressing will be set to 0-125 to properly display text during this call, at the end of the function it will be reset back to 0-127.

#### Arguments

The `msg` argument is the string to be written to the display. Any characters not found in the asciiTable array will be ignored.

#### Examples

Write 'Onion Omega':
``` javascript
oledExp.write('Onion Omega');
```

Write 'Onion Omega', then 'Inventing the Future' on the next line, and then 'Today' two lines below:

``` javascript
oledExp.write("Onion Omega\nInventing the Future\n\nToday");
```

### Scrolling the Display Contents {#oled-node-scrolling}
The OLED can scroll the contents of the screen horizontally or upwards at a 45 degree angle. The displayed content will wrap around when it reaches the edge of the display.

* [Scroll horizontally](#oled-node-scroll)
* [Scroll diagonally](#oled-node-scroll-diagonal)
* [Stop scrolling](#oled-node-scroll-stop)

### Horizontal Scrolling {#oled-node-scroll}
Scroll the contents of the screen horizontally or upwards at a 45 degree angle. Contents will wrap around after reaching edge of display
``` javascript
oledExp.scroll(int direction, int scrollSpeed, int startPage, int stopPage);
```

#### Arguments

**Direction**

Indicates whether to scroll left or right.

|Value              | Scrolling Direction |
|-------------------|---------------------|
| 0                 | Left                |
| 1                 | Right               |

**scrollSpeed**

Determines the number of frames between each scroll step.

|Value  |Scroll Speed   |
|-------|---------------|      
|0      |5 Frames       |
|1      |64 Frames      |
|2      |128 Frames     |
|3      |256 Frames     |
|4      |3 Frames       |
|5      |4 Frames       |
|6      |25 Frames      |
|7      |2 Frames       |

**startPage and stopPage**

Thes two arguments define which page to start and stop scrolling at respectively. Both can have values between 0-7, however **startPage must be less than stopPage**.


#### Examples

Let's scroll the entire screen to the left
``` javascript
oledExp.scroll(0,0,0,7);
```

### Diagonal Scrolling {#oled-node-scroll-diagonal}
Scroll all or part of the screen diagonally upwards:

``` javascript
scrollDiagonal(int direction, int scrollSpeed, int fixedRows, int scrollRows, int verticalOffset, int startPage, int stopPage);
```
#### Arguments

**Direction**

Indicates whether to scroll up-left or up-right.

| Value             | Scrolling Direction |
|-------------------|---------------------|
| 0                 | Upwards and Left    |
| 1                 | Upwards and Right   |

**scrollSpeed**

Determines the number of frames between each scroll step.

| Value | Scroll Speed  |
|-------|---------------|
|0      |5 Frames       |
|1      |64 Frames      |
|2      |128 Frames     |
|3      |256 Frames     |
|4      |3 Frames       |
|5      |4 Frames       |
|6      |25 Frames      |
|7      |2 Frames       |


**fixedRows**

Defines the amount of pixel rows, starting from the top, that will not have vertical scrolling. Can take a range from 0-63.

**scrollRows**

Defines the amount of pixel rows, starting from the top, that will have vertical scrolling. Can take a range from 0-63.

**verticalOffset**

Defines the number of vertical rows to scroll by each frame.

**startPage and stopPage**

Thes two arguments define which page to start and stop scrolling at respectively. Both can have values between 0-7, however **startPage must be less than stopPage**.

#### Examples

Let's scroll the entire screen upwards to the left.
``` javascript
oledExp.scrollDiagonal(0,5,0,127,1,0,7);
```

### Stop Scrolling {#oled-node-scroll-stop}

Disables all active scrolling
``` javascript
oledExp.scrollStop();
```
