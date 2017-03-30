---
title: Displaying Images on the OLED Screen
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 6
---

<!-- // DONE: be consistent, always capitalize OLED, OLED Expansion, Python -->

## Drawing on the OLED Screen {#maker-kit-oled-displaying-images}

<!-- // DONE: this intro can be better. This tutorial is exciting, we're drawing lines to the screen! Get the people stoked, this is too try! -->
<!-- // DONE: let's avoid words like simple & basic, can be intimidating to beginner -->

This tutorial will walk you through drawing to the OLED Expansion. We'll create a script that draws lines to the OLED screen, along the way, we'll learn about the essentials to create computer graphics. After all, fancy polygons and shaders in the games we love are just lines on the screen!

### Drawing to The OLED Screen

<!-- // describe how the OLED Screen works -->

The OLED is an efficient low-power screen that can be programmed to display any monochrome visuals included text, graphics, and even animations! In depth information about how the OLED operates can be found in the [OLED Expansion article](https://docs.onion.io/omega2-docs/oled-expansion.html) in the Hardware Overview section of the docs. It is highly recommended to have the [OLED Python Module](https://docs.onion.io/omega2-docs/oled-expansion-python-module.html) reference handy, as this tutorial is entirely software based.

One important concept to understand is the cursor. The cursor is essentially the position of the next byte to be written to the screen. After a byte is written, the cursor will automaticaly advance once to the next pixel column, staying in the same page. Once the cursor reaches the end of a page, it wraps around to column 0 of the next page, and so on. So simply calling `oledExp.writeByte(0xff)` multiple times is enough to light up the whole OLED display - this is a behaviour we will be using to greatly simplify drawing things to the screen.
<!-- (// DONE: what is meant by once? please go into more detail about how the cursor advances. article 4 has a good description of the cursor -->


<!-- // TODO: needs to be more clear: -->
<!-- //	* might be a better idea to first introduce how `oledExp.writeByte(0xff)` works (in terms of pages and columns) as it is fairly non-intuitive, AND THEN have this section on the cursor -->
<!-- //		* A good example is writing 0x0f or 0xf0 -->
<!-- //	* mention how many times `oledExp.writeByte(0xff)` actually needs to be called to fill in the whole screen -->
<!-- //		* explain the reason behind this again, really want to drive home how the display itself and the cursor works, it's critical to understand this before actually generating stuff to be drawn -->

### A Brief on Concepts We'll Cover

One major concept we'll be working with is a **frame buffer**.

Frame buffers work by storing a copy of the entire screen in memory for easy modification. It is then sent whole to be drawn on the screen once all the changes are finalized. 

Since a frame buffer is an abstract idea, we'll be using a multi-dimensional array to actually implement one in our code.

For bonus points, we'll get involved with input and output to customize where our lines will go.

And as always, we'll discuss all the concepts in detail after we've gotten hands on with the project.

<!-- // DONE: if i'm a beginner, I'm thinking 'what the flip is a frame buffer? better go back to the previous tutorials, I must have missed it' -->
<!-- //	* first introduce the concept briefly -->
<!-- //	* then say 'this is known as a frame buffer' (with the least amount of condescending as possible) -->

### Building the Circuit

The OLED Expansion is a complete circuit. So for this tutorial, we just need to plug it into the Expansion Dock and we'll be good to go!

#### What You'll Need

1x Omega2 plugged into the Expansion Dock
1x OLED Expansion plugged into Expansion Dock

### Writing the Code

Today's code will start to dip into low level graphics programming! On some level, all digital screens operate much the same way: turning pixels on and off. But the devil is always in the details. For our OLED screen, we can draw directly to the screen by moving the **cursor** and writing a byte. However this program will actually write to a **buffer** first, then draw the entire screen in one go, we'll explain in detail in a bit.

First, lets get to coding: copy the code below into a file named `MAK06-drawingLines.py`, and run it on your Omega to see it in action.

<!-- DONE: fix the code to be less ugly, functionalise user input retreival -->

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

	# This function writes a byte to the frame buffer at the specified location after it's checked that the coordinates don't go out of bounds - if it goes out, the program crashes!
    def writeByteToBuffer (self, seg, page, byte):
        if (page > PAGE_MAX):
            page = PAGE_MAX
        if (seg > SEG_MAX):
            seg = SEG_MAX
        self.frame[seg][page] = byte

    # Here we draw the frame buffer to the OLED screen in one fell swoop
    def drawToScreen (self):
        for seg in self.frame:
            for byt in seg:
                oledExp.writeByte (byt)

    # Creates and returns a new, empty frame buffer
    def getEmptyFrame(self):
        tmpframe = []
        # Creating an empty 128x8 array
        for x in range(0,SEG_MAX+1):
            tmpframe.append([]);
            for y in range(0,PAGE_MAX+1):
                 tmpframe[x].append(0)
        return tmpframe

# Input requesting function to obtain a 'position' has arguments that allow changing what position is asked and the limits on the position for error checking
def getPosition (maxPos, orientation, located):
    pos = 0
    while (True):
        print ('Which ' + orientation + ' should the line ' + located)
        # Getting input from user
        pos = raw_input('>>> ')

		# TODO: add comment describing the try-catch
        try:
            pos = int (pos, 10)
        except ValueError as e:
            print ('Numbers only please!')

        if (type(pos) != int or pos > maxPos or pos < 0):
            print ('That\'s out of range, please try again.')
        else:
            return pos


def main():
	# Starts up the OLED screen and sets it up to display images instead of text
    initStatus = oledExp.driverInit();
    powerStatus = oledExp.setDisplayPower(1)
    memModeStatus = oledExp.setMemoryMode(1)
    orientation = 0

    # creating a local buffer object
    currentFrame = buffer()

    # main loop
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
        startPos = getPosition(endPosMax, lineAskedWord, 'start on?')
        endPos = getPosition(endPosMax, lineAskedWord, 'end on?')


        # In case you put the numbers reversed
        if (startPos > endPos):
            tmp = startPos
            startPos = endPos
            endPos = tmp

		# This loop draws the line to the buffer based on the data obtained above - where it starts, where it ends, and the orientation
        # The data has all been error checked to keep this step super neat
        if (orientation == VER):
            for y in range (startPos, endPos):
                currentFrame.writeByteToBuffer(headPos, y, byte)
        else:
            for x in range (startPos, endPos):
                currentFrame.writeByteToBuffer(x, headPos, byte)

		# This line outputs the buffer to the screen.
        status = currentFrame.drawToScreen()


	# note that this command is outside of the while loop body
    oledExp.clear()


if __name__ == '__main__':
    main()
```

### What to Expect

<!-- // DONE: kinda convoluted to say that you need to submit a bunch of numbers and it will draw a line. and only describe what the inputs do later -->
<!-- // * a beginner friendly approach would be something like: -->
<!-- //		* the program will draw a line based on the user's input; it will prompt the user for the starting & ending positions, and whether the line is meant to be vertical or horizontal. it will then use that data to populate the frame buffer and draw the line on the screen -->

The program will first ask for the orientation (horizontal or vertical), then where the line will be placed (in which row/column), and then it will ask for the length of the line by asking for the starting point and ending point along the stated direction.

The lines you draw will stay on the screen because the buffer never gets cleared, and you can draw as many as you like. To exit the script, simply press `Ctrl-C`.

<!-- // DONE: would be nice to give a brief description of why the lines will stay on the scren -->

<!-- // TODO: IMAGE add gif or picture of lines being drawn -->

### A Closer Look at the Code

<!-- // DONE: fix this run-on sentence -->

A buffer works by storing an entire screen of output data in memory to make it easy to change. Then after all the operations to change the output image are completed, it will draw the entire thing to the screen all at once. 

In the code we do this by first creating a frame buffer as a multi-dimensional array. Then drawing the lines into it. Finally calling `oledExp.writeByte()` continuously until the entire screen is drawn (`128*8 = 1024` times, to be exact) from the data in the buffer.

<!-- // DONE: explain why it's 1024 times -->

Additionally, we did a good deal of filtering on the user inputs to ensure the data being sent to the display is error-free.

We'll break these concepts down in the next few sections

#### Multi-dimensional Arrays

A multidimensional array is an array of arrays. While that might sound a little confusing, it's actually a pretty cool concept! By default, arrays in Python are single dimensions, with each element holding some data. For example `[1, 2, 3]` is an array of three integers. A multidimensional array simply swaps those integer elements with arrays. A two dimensional array holds the data in two 'levels', for example for `Array = [ [1, 2, 3], [4, 5, 6,] ]` is a 2 by 3 matrix represented as a two dimensional array.

To access elements in two dimensional arrays, two indices are needed, In the example above, if we access `Array[0]` we'll get `[1, 2, 3]` back. Recall that arrays in Python start at 0, so the we're accessing the zeroth (yes, that's a word) element of the `Array` variable. The number '3' can be accessed with `Array[0][2]`. What we're doing is grabbing the `Array[0]` array (which is `[1, 2, 3]`) and then accessing the element indexed by `2`, which is the number '3'.

In the code, we use a two dimensional array to represent the screen. Each individual element corresponds to a byte on the screen, so if we want to write a certain byte at some page Y and segment X, the corresponding byte in the array should be the one we need written.

<!-- // DONE: good place for a brief reminder of how the screen draws a byte on a page -->

>Recall that a byte is always drawn at the position of the cursor, and the cursor will advance one segment (or one page and reset to segment 0 if the end is reached) after every writing each byte.

#### Using a Buffer

In the script provided, we create a `buffer` class which handles all the drawing to screen and filling of the buffer. When an object is created from the buffer class, it initializes an empty two dimensional array of size 128x8. This array represents the screen in terms of segments (horizontal) and pages (vertical). To borrow a film term, we'll call all the data held by the buffer as a **frame** - like a still frame from a film.

<!-- // DONE: would not recommend referencing code by line numbers, it's bound to change and what are the chances the line numbers will get updated too? -->
<!-- // * a better solution here would be to break up the code that's in the infinite loop into functions (based on what the chunk of code is trying to do, read+process input, populate the buffer, etc) and then refer to the function names -->

In the main function, we create an infinite loop to continuously populate the buffer with new lines as dictated by the orientation, which row or column it is located in, and length, right after this line:

```
# main loop
```

At the end of the loop, we call `currentFrame.writeByteToBuffer` to update the buffer with the new line we wish to draw, and `currentFrame.drawToScreen` to actually make it appear. The lines drawn previously are actually held within the buffer `currentFrame`, and since `oledExp.clear()` is never called until the end, the buffer will remember all the previously drawn lines and display them when the `currentFrame.drawToScreen` is called.

<!-- // DONE: its not so much computationally expensive, it just doesn't make sense to draw different parts of the screen individually. Give a more clear answer as to why we use a screen buffer -->

The reason buffers are used is to keep drawing to screen separated from creating a frame. If there is multiple layers to a frame and they are created by different processes, it makes good sense to assembled them all before outputting the layered result. A buffer allows us to do this quickly and effectively, since it's entirely in memory. Once the buffer is done, we send it out to be drawn to screen all at once.

So we populate the buffer with as much information as possible (the entire line) and then draw it all in one go to maximize efficiency. The same process happens in your computer when playing games, the buffer gets filled and edited by the game code iteratively: drawing a tree first, then filling in your character, and so on. When update time comes, the entire buffer is sent to the screen and displayed.

<!-- // DONE: might be a good place to mention that if you terminate the program and then start it again, the lines from the previous program won't be preserved. point out that dynamically allocated memory only sticks around while the program that created it is running -->

>If you quit the program and then restart it, you'll notices the lines disappearing. This is because all the data in the buffer is dynamic memory - it is only around when the program that generated it is still running.

#### Dynamic Errors

You'll probably notice there's a *lot* of error checking and user direction in this script. This is because the program asks for many different types of input. To make it worse, previous input will change the way future input is interpreted. As a taste, this is how complicated even 'simple' command line tools can become.

We can't use command-line arguments here because to do so would be we'd have to restart the program every time. This will clear out the line we've drawn previously as it's not saved to a file anywhere.

<!-- // DONE: that's why many command line tools use command-line arguments, to avoid all this user input processing. explain why we aren't using command-line arguments here (would overwrite our previous lines since we need to initialize the frame buffer again - refer to the last DONE in the 'Using a Buffer' section) -->

### Flexibility versus Cost

<!-- // DONE: the following sentences aren't exactly correct: -->
<!-- //	This is because it is designed to be operated by the I2C protocol, which reads and writes bytes only. For ease of manufacture, and to keep the cost under control, the screen accepts directions byte-by-byte. -->
<!-- //	* technically, I2C can have multiple-byte reads and writes. We just do single byte transactions for simplicity -->
<!-- //	* i think a better way of describing why this screen is different is because of the intended use case: -->
<!-- //		* since it's divided into pages, it's very easy to write text on it -->
<!-- //		* not intended for videos (animations), so no need to have a faster protocol, good way to save cost -->

The OLED screen we use is pretty different from the ones you have on the latest smartphones and tablets. It isn't designed to be addressable through exact pixel co-ordinates (as you already know). This is because the screen is intended to be used as a text rendering screen. There's no real reason to have expensive pixel rendering hardware if the screen isn't intended to draw graphics and animations. In fact, that's why it's divided into pages, not 'rows' - it makes it very easy at a hardware level to draw text to it!

To make the code simple to understand, we followed suit, and drew only bytes. That's why the horizontal lines are eight pixels tall, because the pages are eight pixels tall. There's definitely way to draw pixel by pixel using a pixel-based buffer and translating it to bytes. If you want to go further, try implementing it!


Next time, we [make some noise](#maker-kit-relay-controlling-circuits).
