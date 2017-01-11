---
title: Displaying Images on the OLED Screen
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 6
---

# Drawing on the OLED Screen

// this tutorial will show how to draw lines on the oled display using text-based user input

## The OLED Screen & Images

// describe how the OLED Screen works
The OLED is an efficient low-power screen that can be programmed to display any monochrome visuals included text, graphics, and even animations! In depth information about how the OLED operates can be found in the [OLED Expansion article](https://docs.onion.io/omega2-docs/oled-expansion.html) in the Hardware Overview section of the docs. It is highly recommended to have the [OLED Python Module](https://docs.onion.io/omega2-docs/oled-expansion-python-module.html) reference handy, as this project is entirely software.

One important concept to understand is the cursor. The cursor is essentially the position of the next byte to be written to the screen. After a byte is written, the cursor will automaticaly advance once. As an example, mply calling oledExp.writeByte(0xff) multiple times is enough to light up the whole OLED display.
// can be largely copied from the understanding the display section of the oled hw article

We'll be creating a line drawing python script using a Frame Buffer to more manage sending drawings to the screen. More specifically, the frame buffer will be implemented with a multi-dimensional array. If this sounds daunting, fear not, it's really a fairly simple concept. As a bonus, some basic input and output will be done as well.

## Building the Circuit

The OLED Expansion is a complete circuit. So for this tutorial, we just need to plug it into the expansion board and we'll be good to go!

## Writing the Code

// write a program that draws vertical or horizontal lines with the length and direction being set by interactive user input
//  * the user must input:
//    - vertical or horizontal
//    - column number for vertical/ row number for horizontal
//    - starting row/column number
//    - ending row/column number
//  * isolate everything drawing related into a class, the class functions will hold a multi-dimensional array that acts as a buffer for the screen, updating as more lines are added

### What to Expect

// walkthrough of drawing a few lines using the interactive program, complete with pictures
This program will ask you to submit a bunch of numbers and draw a line based on them. You control the line's orientation (either vertical or horizontal) and the length based on your inputs.

### A Closer Look at the Code

// introduced the concept of using a multi-dimensional array as a buffer
The way a buffer works is it stores an entire screen of output data in memory first, then after all the operations to change the output image is completed, it draws the entire thing to the screen all at once by calling `oledExp.writeByte()` continuously until the entire screen is drawn (exactly 1024 times). There can be lots of optimizations done to make this script faster, for example skipping blank bytes, or skipping bytes that have already been drawn previously. Feel free to experiment and see if you can make it run faster.

#### Multi-dimensional Arrays

// explain how multi-dimensional arrays work
A multidimensional array is an array of arrays. Arrays in python are by default single dimensions, with each element holding some data. For example `[1, 2, 3]` is an array of three integers. A multidimensional array simply swaps those integers for more arrays. A two dimensional array holds the data in two 'levels', for example `[ [1, 2, 3], [4, 5, 6,] ]` is a 2 by 3 matrix represented as a two dimensional array.

To access elements in two dimensional arrays, two indices are needed, In the example above, the number '3' can be accessed via `Array[0][2]`, recall that arrays in python start at 0, so the zeroeth element here is the array `[1, 2, 3]` and the second element of that array is '3'.

In the code, we use a two dimensional array to represent the screen. Each individual element corresponds to a byte on the screen, so if we want to write a certain byte at some page Y and segment X, the corresponding byte in the array should be the one we need written.

#### Using a Buffer

// talk about how the class' init function initialized the buffer to all 0
//  * then explain how we access it to update for our additional lines
//  * we write to the display after every update
