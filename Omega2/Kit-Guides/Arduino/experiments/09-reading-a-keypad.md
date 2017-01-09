## Reading a Key-Pad

// intro to getting numbers as input from the user, useful in many scenarios, just think of ATMs

// in this experiment, we will be reading input from a keypad and treating it as a password, if the correct password is entered, an LED will light up


### Keypad
// should be in it's own separate markdown file

// explanation of the keypad:
//  - the user can press a button and the attached computer system will be able to tell which digit was pressed
//  - talk about how the signals coming from the keypad need to be decoded
//    - Note from Lazar: keypads usually have pins that identify if a button on a horizontal row is pressed, and then other pins that identify if a button on a vertical column is pressed. to read specific numbers, the user has to look for intersections
//    - need to explain the above in a concise and approachable way - include graphics


### Building the Circuit

// simple circuit:
//  - single LED connected to the microcontroller output
//  - keypad input connected to the microcontroller

#### Hooking Up the Components

// instructions on:
//  - connecting the led circuit (link back to single led experiment or reuse that text)
//  - connecting all of the keypad outputs to the microcontroller pins

### Writing the Code

// create a function that takes the keypad pins as input, and returns the number(s) that are currently pressed in an array, the array should be empty if no buttons are pressed
// note from Lazar: up to you if the array should be static or dynamic

// have a function to turn on the LED

// have an array that holds the "password" and a variable to index the array (initialized to zero)
// in the loop function:
//  - check for valid input from the keypad
//  - if the input matches the currently indexed digit in the password array, increment the index variable
//  - if the input does not match, reset the index variable to 0
//  - once the index variable reaches sizeof(password array), we consider to password to have been typed in, and we can turn on the LED (using the action function)

#### What to Expect

// just like any password-protected system, the LED will only turn on when the correct password has been entered
// if an incorrect digit has been entered, the user will have to start the password from the beginning

// TODO: PHOTO - GIF: include a gif of this


#### A Closer Look at the Code

// this experiment relied on arrays heavily, we'll go over some of the details now. Arrays are very useful and used all the time in programming.

##### Arrays

// we will probably use arrays in an interesting way with the keypad function & the password array, go into detail about what was special in how we used arrays



### Going Further

// in this experiment we added password protection to an LED so we can show off the concept. This experiment might be useful if the correct password triggered a different action, maybe actuating a lock or moving a servo?
