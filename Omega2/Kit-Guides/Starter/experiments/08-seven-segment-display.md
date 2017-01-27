---
title: Seven Segment Display
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 8
---

## Controlling a 7-Segment Display

We've just learned about shift registers, now let's apply that knowledge to control a 7-segment Display so we can display numbers (and a few letters) in the physical world.


<!-- seven segment -->
```{r child = '../../shared/seven-segment.md'}
```


### Building the Circuit

Using the shift register and a few additional GPIO from the Omega, we will control what's displayed on all four digits of the 7-segment display.


#### Hooking up the Components

/<!-- / TODO: research how many scan pins there are, then decide how many gpios on the omega are required -->

// omega -> shift register -> 7seg display a-g segment pins
// omega -> 7seg scan pins

// keep the shift register wired up like the previous experiment (point them to the prev shift register experiment)
// wire the shift register outputs to the 7seg a-g segment pins

// connect additional gpios to the scan pins of the-7 segment display





### Writing the Code

We'll be developing a program that takes input from command line arguments when it's launched and displays them on the 7-segment display.

To accomplish this, we will write a new class that uses the shift register class we wrote for the previous experiment and introduces it's own variables and functions.

// [notes on the code]
// create a class that uses the shift reg class but specifically to control the 7seg display
//  * the 7seg class has self.shiftReg
//  functions:
//  * setup function to let the object know which gpios correspond to which functionality
//  * writing a single digit (have a dictionary in the 7seg class that maps each hex digit to a binary to be mapped to the segments)
//  * selecting which digit to write to (controls scan pins)
//  * function to write a value to a specific digit (combines the two above functions)
// command line arguments:
//  * make sure to check that a command line argument is present, if not, print an error message and exit the program
//  * input sanitization to ensure they only enter hex numbers (really good practise)
//  * write the sanitized input to the 7seg

#### What to Expect

// walk them through running a program from the command line with arguments

// description of whatever they put as the argument will be display
// example: display the numbers from your Omega name

#### A Closer Look at the Code

// small overview of the new things we introduced
//  * command line arguments
//  * a class using another class
//  * a dictionary variable

##### Command Line Arguments

// explanation of how they work, why we have to use the os module, etc

##### Classes using Classes

// description of how the 7seg class has a member variable that is the shift register class, and how we use it to use the shift register functons

##### Dictionary

// explanation of the dictionary variable type: many elements, all have an id and a value
