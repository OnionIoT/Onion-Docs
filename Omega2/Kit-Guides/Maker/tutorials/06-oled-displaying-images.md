---
title: Displaying Images on the OLED Screen
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 6
---

## Drawing on the OLED Screen {#maker-kit-oled-displaying-images}

This tutorial will walk you through drawing to the OLED Expansion. It will demonstrate a simple line drawing script and go through how to represent images and image data in your scripts.

### The OLED Screen & Images

<!-- // describe how the OLED Screen works -->

The OLED is an efficient low-power screen that can be programmed to display any monochrome visuals included text, graphics, and even animations! In depth information about how the OLED operates can be found in the [OLED Expansion article](https://docs.onion.io/omega2-docs/oled-expansion.html) in the Hardware Overview section of the docs. It is highly recommended to have the [OLED Python Module](https://docs.onion.io/omega2-docs/oled-expansion-python-module.html) reference handy, as this project is entirely software.

One important concept to understand is the cursor. The cursor is essentially the position of the next byte to be written to the screen. After a byte is written, the cursor will automaticaly advance once. As an example, simply calling `oledExp.writeByte(0xff)` multiple times is enough to light up the whole OLED display.

<!-- // can be largely copied from the understanding the display section of the oled hw article -->

We'll be creating a line drawing python script using a Frame Buffer to more manage sending drawings to the screen. More specifically, the frame buffer will be implemented with a multi-dimensional array. If this sounds daunting, fear not, it's really a fairly simple concept. As a bonus, some basic input and output will be done as well.

### Building the Circuit

The OLED Expansion is a complete circuit. So for this tutorial, we just need to plug it into the Expansion Dock and we'll be good to go!

#### What You'll Need

1x Omega2 plugged into the Expansion Dock
1x OLED Expansion plugged into Expansion Dock

### Writing the Code

Today's code will start to dip into low level graphics programming! On some level, all digital screens operate much the same way: turning pixels on and off. But the devil is always in the details. For our OLED screen, we can draw directly to the screen by moving the **cursor** and writing a byte. However this programm will actually write to a **buffer** first, then draw the entire screen in one go, we'll explain in detail in a bit.

First, lets get to coding: copy the code below into a file named `MAK06-drawingLines.py`, and run it on your Omega to see it in action.

<!-- TODO: fix the code to be less ugly, functionalise user input retreival -->

``` python
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


def getPosition (maxPos, orientation, located):
    pos = 0
    while (True):
        print ('Which ' + orientation + ' should the line ' + located)
        # Getting input from user
        pos = raw_input('>>> ')

        try:
            pos = int (pos, 10)
        except ValueError as e:
            print ('Numbers only please!')

        if (type(pos) != int or pos > maxPos or pos < 0):
            print ('That\'s out of range, please try again.')
        else:
            return pos


def main():
    initStatus = oledExp.driverInit();
    powerStatus = oledExp.setDisplayPower(1)
    memModeStatus = oledExp.setMemoryMode(1)
    orientation = 0

    # creating a buffer
    b = buffer()

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
            endPosMax = PAGE_MAX
            headAskedWord = 'column'
            lineAskedWord = 'row'
        else:
            headPosMax = PAGE_MAX
            endPosMax = SEG_MAX
            headAskedWord = 'row'
            lineAskedWord = 'column'

        # Obtaining the column or row the line will exist in
        headPos = getPosition(headPosMax, headAskedWord, 'occupy?')

        # Obtaining the starting and ending positions of the line
        startPos = getPosition(startPosMax, lineAskedWord, 'start on?')
        endPos = getPosition(endPosMax, lineAskedWord, 'end on?')


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

### What to Expect

This program will ask you to submit a bunch of numbers and draw a line based on them. You control the line's orientation (either vertical or horizontal) and the length based on your inputs.

The lines you draw will stay on the screen, and you can draw as many as you like. To exit the script, simply press `Ctrl-C`.

<!-- // TODO: IMAGE add gif or picture of lines being drawn -->

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

The reason we use a buffer is because actually drawing to the screen is computationally expensive, so we populate the buffer with as much correct information as possible (the entire line) and then draw it all in one go to maximize efficiency. The same process happens in your computer when playing games, the buffer gets filled and edited by the game code iteratively: drawing a tree first, then filling in your character, and so on. When update time comes, the entire buffer is sent to the screen and displayed.

#### Dynamic Errors

You'll probably notice there's a *lot* of error checking and user direction in this script. This is because the program asks for many different types of input. To make it worse, previous input will change the way future input is interpreted. There's no new concepts regarding input and output here, but as a taste, this is how complicated even 'simple' commandline tools can become.

### Flexibility versus Cost

The OLED screen we use is pretty different from the ones you have on the lastest smartphones and tablets. It isn't designed to be addressable through exact pixel co-ordinates (as you already know). This is because it is designed to be operated by the I2C protocol, which reads and writes bytes only. For ease of manufacture, and to keep the cost under control, the screen accepts directions byte-by-byte. To make the code simple to understand, we followed suit, and drew only bytes - that's why the horizontal lines are eight pixels wide. There's definitely way to draw pixel by pixel using a pixel-based buffer and translating it to bytes. If you want to go further, try implementing it!


Next time, we [make some noise](#maker-kit-relay-controlling-circuits).
