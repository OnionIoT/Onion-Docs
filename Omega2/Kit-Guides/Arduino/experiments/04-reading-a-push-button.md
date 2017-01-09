# Reading a Push Button

// description of what this experiment will accomplish and what we'll learn

// TODO: include push button shared article

// TODO: include debouncing switches shared article

### Interrupts

// description of what an interrupt is in the context of computer hardware:
//  - trigger for an action
//  - requires an interrupt service routine (ISR)

### Building the Circuit

// push button connected as input
// 5-8 leds connected

#### Hooking up the Components

//  * reiterate on the LED circuit, say we can repeat it
//  * wiring of a push-button
//    * needs to be wired to atmega gpio 2 or 3 so we can use it as an interrupt trigger


### Writing the Code

// desired action:
//  * when the button is pressed an led turns on
//  * for each additional button press, another led will turn on
//  * when all leds are on and the button is pressed, turn all of the leds off

// find a clever implementation for this, maybe for each button press shift in a 1 to a uint variable, when it reaches the max number of leds, have it reset to 0 - this part should be done in the ISR
// each led is controlled by a specific bit in the uint variable, use bit-wise operations to figure it out - this part will happen in the loop function

// implementation:
//  * write a function to implement the above
//  * register that function as an interrupt service routine for the push button connected gpio


#### What to Expect

// explanation of how the button presses interact with the leds

#### A Closer Look at the Code

// talk about something interesting in the code

##### Interrupt implementation

// talk about what we accomplished with the interrupts: attaching a service routine for a particular interrupts

##### Bit-wise operations

// introduce logical and's and or's
// provide a link to an in-depth reference
