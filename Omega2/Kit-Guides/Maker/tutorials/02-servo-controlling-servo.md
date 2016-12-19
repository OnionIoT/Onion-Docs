---
title: Controlling Servos with the Servo Expansion
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 2
---

// Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example, this (or something similar) is what the final result will be

# Controlling Servos with the Servo Expansion

// this tutorial will show how the PWM expansion can be used to control servos and the programming that comes along with it

## Servo-Motors
// should be in it's own markdown file

// * explanation of servo motors, how you send it a pwm signal and based on the duty cycle of the signal, it goes to a specific relative angle
//  - include a picture here illustrating what angle we mean (the servo should be standing up on it's short end and 90˚ should show the horn being vertical)

// * standard servos have a range of 180 degrees

// * explanation of how servos interpret duty cycle into degrees
//  * how there's a minimum duty cycle and a maximum duty cycle, how we can start with those two values and build out a way to convert degrees into the corresponding duty cycle


## Building the Circuit

// very easy to build

### Hooking up the Components

// - talk about how to connect a servo to the pwm expansion
// - make sure to mention that an external power supply is required for more servos and larger loads
// can totally rip off large chunks of the pwm expansion hardware article from the documentation
//  * should isolate that text from the pwm hw article into markdown files that can be included here



## Writing the Code

// Note from Lazar: for this and the rest of the pwm expansion articles, see https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py for code example

// * create a class that uses the omegapwm class from the previous example to drive a servo
//    * essentially create the servo class (from the file above), can skip the getSettings, setupMinAngle, and setupMaxAngle functions for the purposes of this example
//    * make sure the class follows the angle described in the servo section above ie 0˚->180˚ as opposed to -90-˚>90˚
// * the program should be something along the lines of setting the servo to 0˚, 45˚, 90˚, 135˚, 180˚, and then back down by 45˚ steps, have a noticeable but not annoyingly long delay between the steps
//  * have it run in an infinite loop

### What to Expect

// explain that the servo will go from 0˚ up to 180˚ and then back down to 0˚ in 45˚ increments with a small pause between each step

// gif of a servo connected to the omega doing this
//  - make sure in the gif it's oriented in the same way as above in the servo section

// mention ctrl+c to quit the infinite loop


### A Closer Look at the Code

// this code introduced
// * doing math in python
// * brought back the idea of using a class within a class (link back to the first time this was introduced in the 7seg article)
// * brought back the infinite loop

#### Math in Pyton

// introduce the idea of floating point numbers and how computer variables need to be differentiated between integers and decimal numbers

// have example code (can be just a few print statements) that shows what happens if you don't divide using float numbers
// reference https://github.com/OnionIoT/i2c-exp-driver/blob/master/src/python/omegaMotors.py#L146 for context
