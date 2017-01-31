---
title: Displaying Images on the OLED Screen
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 6
---

## Drawing on the OLED Screen {#drawing-on-the-oled-screen}

This tutorial will walk you through drawing to the OLED Expansion. It will demonstrate a simple line drawing script and go through how to represent images and image data in your scripts.

### The OLED Screen & Images

// describe how the OLED Screen works

The OLED is an efficient low-power screen that can be programmed to display any monochrome visuals included text, graphics, and even animations! In depth information about how the OLED operates can be found in the [OLED Expansion article](https://docs.onion.io/omega2-docs/oled-expansion.html) in the Hardware Overview section of the docs. It is highly recommended to have the [OLED Python Module](https://docs.onion.io/omega2-docs/oled-expansion-python-module.html) reference handy, as this project is entirely software.

One important concept to understand is the cursor. The cursor is essentially the position of the next byte to be written to the screen. After a byte is written, the cursor will automaticaly advance once. As an example, simply calling `oledExp.writeByte(0xff)` multiple times is enough to light up the whole OLED display.

// can be largely copied from the understanding the display section of the oled hw article

We'll be creating a line drawing python script using a Frame Buffer to more manage sending drawings to the screen. More specifically, the frame buffer will be implemented with a multi-dimensional array. If this sounds daunting, fear not, it's really a fairly simple concept. As a bonus, some basic input and output will be done as well.

### Building the Circuit

The OLED Expansion is a complete circuit. So for this tutorial, we just need to plug it into the expansion board and we'll be good to go!

#### Writing the Code

In case you haven't already, you can install the libraries needed to play with the OLED screen by running the following:
```
opkg update
opkg install python-light
opkg install pyOledExp
```
// TODO: remove opkg commands

If you'd like to play with the console commands to test things out, the `oled-exp` package should be installed as well.

Here's the script we'll be working with:
```
from OmegaExpansion import oledExp

initStatus = 0
powerStatus = 0
memModeStatus = 0

HOR = True
VER = False

X_MAX = 127
Y_MAX = 63
SEG_MAX = 127
PAGE_MAX = 7

byte = 0xff

class buffer:
    def __init__ (self):
        self.frame = self.getEmptyFrame()

    def writeByteToBuffer (self, seg, page, byte):
        if (page > PAGE_MAX):
            page = PAGE_MAX
        if (seg > SEG_MAX):
            seg = SEG_MAX
        self.frame[seg][page] = byte

    def drawToScreen (self):
        for seg in self.frame:
            for byt in seg:
                oledExp.writeByte (byt)

    def getEmptyFrame(self):
        tmpframe = []
        # Creating an empty 128x8 array
        for x in range(0,SEG_MAX+1):
            tmpframe.append([]);
            for y in range(0,PAGE_MAX+1):
                 tmpframe[x].append(0)
        return tmpframe

def main():
    initStatus = oledExp.driverInit();
    powerStatus = oledExp.setDisplayPower(1)
    memModeStatus = oledExp.setMemoryMode(1)
    orientation = 0

    # creating a buffer
    b = buffer()

    // TODO: create a function for user input, replace all of these repeated While (True) code blocks

    while (True):
        # Obtain the orientation of the line
        while (True):
            print ('Enter the orientation of the line (0 for vertical, 1 for horizontal): ')
            orientation = raw_input()
            orientation = int(orientation, 10)
            if (orientation != 0 and orientation != 1):
                print ('Please enter either 1 or 2')
            else:
                break

        # Changing the questions asked depending according to orientation
        if (orientation == VER):
            headPosMax = SEG_MAX
            linePosMax = PAGE_MAX
            headAskedWord = 'column'
            lineAskedWord = 'row'
        else:
            headPosMax = PAGE_MAX
            linePosMax = SEG_MAX
            headAskedWord = 'row'
            lineAskedWord = 'column'

        # Obtaining the column or row the line will exist in
        while (True):
            print ('Which ' + headAskedWord + ' should the line occupy? ')
            headPos = raw_input()
            headPos = int (headPos, 10)
            if(headPos > headPosMax or headPos < 0):
                print ('That\'s out of range, please try again.')
            else:
                break

        # Obtaining the starting and ending positions of the line
        while (True):
            print ('Which ' + lineAskedWord + ' should the line start on?')
            startPos = raw_input()
            startPos = int (startPos, 10)
            if (type(startPos) != int or startPos > linePosMax or startPos < 0):
                print ('That\'s out of range, please try again.')
            else:
                break

        while (True):
            print ('Which ' + lineAskedWord + ' should the line end on?')
            endPos = raw_input()
            endPos = int (endPos, 10)
            if (type(endPos) != int or endPos > linePosMax or endPos < 0):
                print ('That\'s out of range, please try again.')
            else:
                break

        # In case you put the numbers reversed
        if (startPos > endPos):
            tmp = startPos
            startPos = endPos
            endPos = tmp

        if (orientation == VER):
            for y in range (startPos, endPos):
                b.writeByteToBuffer(headPos, y, byte)
        else:
            for x in range (startPos, endPos):
                b.writeByteToBuffer(x, headPos, byte)

        status = b.drawToScreen()

    oledExp.clear()

if __name__ == '__main__':
    main()
```


#### What to Expect

This program will ask you to submit a bunch of numbers and draw a line based on them. You control the line's orientation (either vertical or horizontal) and the length based on your inputs.

The lines you draw will stay on the screen, and you can draw as many as you like. To exit the script, simply press `ctrl`+`c`.

// TODO: IMAGE add gif or picture of lines being drawn

### A Closer Look at the Code

A buffer works by storing an entire screen of output data in memory first, then after all the operations to change the output image is completed, it draws the entire thing to the screen all at once by calling `oledExp.writeByte()` continuously until the entire screen is drawn according to the data in the buffer (exactly 1024 times). Our buffer is created with a multidimensional array in code.

Additionally, we did a good deal of filtering the user's inputs, so to ensure the data being sent to the display is error-free.

We'll break these concepts down in the next few sections

#### Multi-dimensional Arrays

A multidimensional array is an array of arrays. Arrays in python are by default single dimensions, with each element holding some data. For example `[1, 2, 3]` is an array of three integers. A multidimensional array simply swaps those integers for more arrays. A two dimensional array holds the data in two 'levels', for example for `Array = [ [1, 2, 3], [4, 5, 6,] ]` is a 2 by 3 matrix represented as a two dimensional array.
To access elements in two dimensional arrays, two indices are needed, In the example above, the number '3' can be accessed via `Array[0][2]`, recall that arrays in python start at 0, so the zeroeth element here is the array `[1, 2, 3]` and the second element of that array is '3'.

In the code, we use a two dimensional array to represent the screen. Each individual element corresponds to a byte on the screen, so if we want to write a certain byte at some page Y and segment X, the corresponding byte in the array should be the one we need written.

#### Using a Buffer

In the script provided, we create a `buffer` class which handles all the drawing to screen and filling of the buffer. When an object is created from the buffer class, it initialises an empty two dimensional array of size 128x8. This array represents the screen in terms of segments (horizontal) and pages (vertical).

In the main function, we call an infinite loop to continuously populate the buffer with new lines as dictated by the orientation, which row or column it is located in, and length - this happens in lines 64 to 138. At the end of the loop, we call `b.writeByteToBuffer` to update the buffer with the new line we wish to draw, and `b.drawToScreen` to actually make it appear. The lines drawn previously are actually held within the buffer `b`, and since `oledExp.clear()` is never called until the end, the buffer will remember all the previously drawn lines and display them when the `b.drawToScreen` is called.

#### Input and output

You'll probably notice there's a lot of checking for what kind of input you give the script, this is done to make sure the script doesn't 'crash' when incorrect information is sent. This can include numbers that are too large, things that may not be numbers at all, and all kinds of other things. Often users give unexpected input to programs, filtering and catching errors is needed to make sure your scripts don't crash during the middle of asking for input.


### Hack the Script

There can be lots of optimizations done to make this script faster, for example skipping blank bytes, or skipping bytes that have already been drawn previously. Feel free to experiment and see if you can make it run faster.
