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
// can be largely copied from the understanding the display section of the oled hw article

// talk about the multi-dimensional array that's required to hold the data that we'll be displaying on the array

## Building the Circuit

// keep the oled plugged in :)

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

### A Closer Look at the Code

// introduced the concept of using a multi-dimensional array as a buffer

#### Multi-dimensional Arrays

// explain how multi-dimensional arrays work

#### Using a Buffer

// talk about how the class' init function initialized the buffer to all 0
//  * then explain how we access it to update for our additional lines
//  * we write to the display after every update
