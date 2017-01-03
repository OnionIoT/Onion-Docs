## Controlling Servos

// intro to using pwm to control servos, this experiment will involve controlling servos using physical buttons


// ### What is Pulse Width Modulation?

<!-- pwm -->
```{r child = '../../shared/pwm.md'}
```

// ### Servo-Motors

<!-- servo -->
```{r child = '../../shared/servos.md'}
```

## Building the Circuit

// simple circuit with both the small and regular servo attached - when one button is pressed, they both turn to one direction, when the other button is pressed, they both turn to the other direction

### Hooking Up the Components

// wiring the servos: vcc, gnd, and a separate signal wire for each servo
// wiring the two push-button switches: can reuse the wiring push button text from previous articles

## Writing the Code

// introduce the use of classes in arduino sketches: create a class to control servos
//  - need to pass in the signal pin number & minimum and maximum pulse widths in the constructor
//    -> do this in the setup() function
//    -> the constructor should calculate the pulse width change for each degree - should be a class member
//  - function where you pass in an angle and it programs the duty cycle for the pin of the servo
//  implementation details:
//    - will need to define the class at the beginning of the sketch
//    - have two global objects of the class
//    - instantiate the two global objects in the setup function
//    - will be available for use once the setup function is run

// set the servos to 90˚ in the setup function

// have polling code to increment/decrement the angle of both of the servos while a button is pressed


### What to Expect

// description of how both servos will turn in a particular direction while a button is depressed, the buttons control the direction of rotation

### A Closer Look at the Code

// introduced object oriented programming for the first time in this code

#### Object Oriented Programming

// talk about how we're using two servos, they operate in the same way but some parameters are slightly different. So we wrote a class that can be used to control both servos independently.
// this is accomplished by instantiating two objects of the class - talk about the constructors and how we input the pertinent values

// talk about constructors and class members

// can borrow from the starter kit - 7seg article
