---
title: Using a Shift Register
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 7
---

# Using a Shift Register to Control a Bunch of LEDs

Shift registers are very useful tools; using a few GPIOs connected to a shift register, we can increase the number of output data pins that are available to us.

In this experiment, we'll be using a shift register to control eight LEDs, but we'll only be using four GPIOs on the Omega.

// TODO: update the number of gpios if required


## Shift Register
<!-- {{!insert 'shift-register'}} -->

// explanation of a shift register, an external integrated circuit (ic) that takes serial input and provide the data in parallel
// it allows us to essentially expand the number of output pins available to us
// the omega can provide data serially using one data pin, and then the shift register outputs it on its eight data pins

// illustration of how a shift register works
//  - can be simple (clock, serial data in, eight outputs)
//  - explanation of the diagram
//  - the key takeaway should be, pass in 0101 get 0, 1, 0, 1 on the outputs



## Controlling a Shift Register
<!-- {{!insert 'shift-register-control'}} -->

// introduce the idea of a clock, explain that it provides the shift register with a signal to read the data that's currently on the serial data in pin. make sure to note that the data on the serial data in pin needs to be settled before the clock edge!

// show how changing the data on the serial data pin will affect the outputs
// good place to introduce the latching register ie displaying the values of each step. mention that this can be used to set up your output values (pass in all of the serial data) before actually outputting it


## Building the Circuit

// wire up the omega to the shift register
// have all shift register outputs connected to an LED circuit

### Hooking up the Components

//  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)

//  * explain all of the wiring from omega->shift reg
//    * explain each of the lines running from the Omega and what they do - according to the names from the controlling a shift register section




## Writing the Code

// create a class to abstract away all of the shift register operations
//  * input 8 data bits, the function will take care of the eight data shifts, then latch the output at the end
//  * setup function to let the object know which gpios correspond to which functionality
//  * separate functions for:
//    - inputting a single data bit
//    - latching the output
//    - clearing the values
//  * use all of these functions in that one function to pass in 8 different outputs

// note that the class should be in its own file and imported in the final program

// for loop using the object to display on all the leds
//  there should be two leds on at a time, have it run all the way to the left, and then all the way to the right


### What to Expect

// explain that the animation will be Knight Rider Kitt style: maybe throw in a gif for nostalgia
//  - it will run all the way left and then all the way right over and over again

### A Closer Look at the Code

// an overview of the code

#### Creating and Importing Modules

// describe how the import process works, make sure to note how the directory structure has to fit

#### Creating and Using Classes

// explanation of Classes
//  - definition of Classes
//  - using classes
//  - each class becomes an object when you instantiate it
//    - can call functions from the object, etc
//    - if we had two shift registers, we could have two objects to run the two different ones
//  - talk about how class functions can use other class functions
