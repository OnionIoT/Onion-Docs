## Reading a Key-Pad {#arduino-kit-reading-a-keypad}

In this experiment, we will make a circuit that can read input from a keypad. To make it more interesting, we'll treat the input as a password such that if the correct password is entered, an LED will light up. The way we will build our circuit and accept input is very similar to the way computer keyboards work! When writing the code, we will also learn how to use Arduino libraries that are not preloaded by default.

<!-- // TODO: should be in it's own separate markdown file -->
```{r child = '../../shared/keypad.md'}
```


### Building the Circuit

// TODO: let's change it so that we use an external led, makes it feel more dramatic

For the circuit, we will only need a keypad and some jumpers. We'll be using the on-board blue LED instead of connecting our own to keep it simple.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* 7x male-to-male Jumper wires
* 1x Keypad

// TODO: add in our external LED

#### Hooking Up the Components

<!-- // TODO: add an intro, mention: 'The keypad as seven pins: four pins for the rows and three pins for the columns.'' -->

Once you have the components ready to go, we can begin putting it together. Keep in mind the keypad has seven pins, one for each row and column - not one pin per button.

1. Connect all the seven keypad pins to the digital pins (8, 7, 6, 5, 4, 3, 2) on the Arduino Dock in order from left to right, i.e. the left most keypad pin to arduino header pin 8.

// TODO: add info about wiring up the LED

<!-- // TODO: IMAGE add a photo of the completed circuit and a blurb about 'this is more or less how your circuit should look' -->

### Writing the Code

<!-- // create a function that takes the keypad pins as input, and returns the number(s) that are currently pressed in an array, the array should be empty if no buttons are pressed
// note from Lazar: up to you if the array should be static or dynamic

// have a function to turn on the LED

// have an array that holds the "password" and a variable to index the array (initialized to zero)
// in the loop function:
//  - check for valid input from the keypad
//  - if the input matches the currently indexed digit in the password array, increment the index variable
//  - if the input does not match, reset the index variable to 0
//  - once the index variable reaches sizeof(password array), we consider to password to have been typed in, and we can turn on the LED (using the action function) -->

This code will use a Keypad library which is probably not included in  the Ardiuno IDE by default. There are two ways of getting ahold of the library and including it in our code. In the first way we can install it directly through the Arduino IDE:

1. On the Arduino IDE, click `Sketch > Include Library > Manage Libraries`. The Library Manager will show up; type `keypad` in the search bar and install the first search result.

The other way is to manually install a library.

1. Download the Keypad library from a source: http://playground.arduino.cc/Code/Keypad#Download
2. Move the unzipped Keypad file folder to the Arduino library folder: on Windows, its located at `C:\Program Files (x86)\Arduino\libraries`
    * Linux - `~/Arduino/Libraries`
    * MacOS - `~/Documents/Arduino/libraries`
3. Restart your IDE, and it should be useable in your sketches!

<!-- // TODO: add locations for OS X and Linux (can look this up online) -->

To use the library we need to add the following line at the top of our code:

```
#include <Keypad.h>
```

// TODO: verify this code works

```c++
// include the Keypad library
#include <Keypad.h>

const byte ROWS = 4;	 //four rows
const byte COLS = 3;	 //three columns
char keys[ROWS][COLS] = {    // a 4x3 array of all the keys as chars
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

byte rowPins[ROWS] = {8, 7, 6, 5};     //connect to the row pinouts of the keypad
byte colPins[COLS] = {4, 3, 2};     //connect to the column pinouts of the keypad
char password[] = {'4', '3', '2', '1'};   // array of chars as password
int ledPin = 13;    // LED pin number to be lit when password is correct

// initializing keypad as an object from the Keypad library
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
  Serial.begin(9600);   // initializing serial communication with the Omega
  pinMode (ledPin, OUTPUT);   // initializing pin for the LED
}

void loop(){

  // set LED off
  digitalWrite (13, LOW);

  char key = keypad.getKey();   // read the key entered as a char
  int keyCheck = 0;   // index for the number of correct keys entered after #
  int i = 0;      // index for the number of keys entered after #
  if (key != NO_KEY){   // wait until a key has been pressed
    // print the key and ask to press #
    Serial.println(key);   
    Serial.println("Please press # to enter the password");

    // if # is pressed ask for the password
    if (key == '#'){
        Serial.println("Please enter the password");

        // using a loop, let the user enter the same number of keys as the password length, whether correct or not
        while (i != sizeof (password)){
          key = keypad.getKey();    // read the key entered as a char
          if (key != NO_KEY){   // wait until a key has been pressed
          Serial.println(key);   

              // if the correct key is entered in the same order as the password, increment keyCheck
              if (key == password[i]){
                 keyCheck ++;
                 i++;
              }
              // if any wrong key is entered, reset keyCheck
              else{
                 keyCheck = 0;
                 i++;
              }
          }
        }

        // after the user entered the same number of keys as the password length, check if password is correct
        if (keyCheck == sizeof (password)){
          // if the keys are correctly entered, light the LED for 3 seconds
          passwordSuccess();
        }
        else
          // if any wrong key is entered, ask to entered the password again
          Serial.println("Wrong password! Press #");   
    }
  }
}

void passwordSuccess(){
	Serial.println("Correct password! LED On!");
	digitalWrite (ledPin, HIGH);    // turn the LED on
	delay(3000);    // keep it on for 3 seconds
	digitalWrite (ledPin, LOW);    // turn the LED off again
}
```


### What to Expect

<!-- // TODO: PHOTO - GIF: include a gif of this -->

We will be using the keypad to create a password protected system. After the user presses the `#` key, they will be prompted via serial to enter a password. If the entered password matches with the password set in by `char password[]`, which is `4321` by default, the blue LED on the Arduino Dock will light up for 3 seconds. If the wrong password has been entered, it will ask the user to press the `#` key again to retry.




### A Closer Look at the Code

<!-- // TODO: fill in the link -->

This code uses the Arduino Keypad library. Remember the `ServoMotor` class we wrote in the [previous tutorial](#arduino-kit-using-a-servo)? Well a library usually contains the definition of a class and then the implementation of the methods (functions) of that class. To use the class, we include the library's header file in our code, and then we are free to create a `Keypad` object in our code.

// TODO: change this object's name everywhere to keypadObject

We've creatively name the object `keypad`.

```
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
```

Try commenting out the `#include <Keypad.h>` line, you'll see that the compiler will complain, saying that it doesn't know what a Keypad is! This file is in the Arduino Keypad library and it defines the `Keypad` class. However, before we instantiate our `Keypad` object, we need  to declare the variables which needed to be passed into the Keypad object. This includes a two-dimensional array `keys[][]`.

#### Two-Dimensional Arrays

<!-- // TODO: clean up this paragraph, it's written well and going in the right direction but doesn't include enough details: -->
<!-- //	* expand on what is meant by a single row of variables -->
<!-- //	* expand on the 2d array is similar to a table bit -->
<!-- //	* talk about how 2d arrays need to be indexed in both dimensions -->

We're no strangers to arrays by now, so this time we can dive a bit deeper into their capabilities. At the lowest level, arrays are actually represented as a hex number that represents a location in computer memory - the location of the start of the array. This means that arrays can store other arrays just as well as regular numbers (TODO: expand on this mind-expanding statement). In practise, this means we can create arrays that work like tables. Using this kind of two-dimensional (2D) array, we can map the keypad directly to an array without jumping any calculation hoops. To get a better visual, let's take a look at the code:

```c++
const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};        // a 4x3 array of all the keys as chars
```

Our keypad does not have a pin for each button, instead it has a pin for each row and column. The signals our code obtains is the row and column number of the button being pressed. To best mirror that in code, the 2D array `keys[][]` does pretty much the same thing. Each button is represented by an element of the array, and each element can be accessed by a unique pair of numbers - the indices of `keys`.

In this example, the 2D array is passed into a `keypad` object and the object will do the translation internally. We simply have to call the `getKey()` function to have the keypad return the value of the button that was pressed.

Internally, the `keypad.getKey()` function does something like this:

* Read in the data from the keypad.
* Convert the input data into a row value and a column value.
* Return the value of the array that the row/column values specify.

<!-- // TODO: include some examples of accessing the array: like keys[2][3] = 6, give a few -->

### Going Further

In this experiment, we password protected an LED just to illustrate the concept. It would be a little more useful if the correct password triggered a different action, maybe moving a servo or actuating a lock? You can replace the contents of the `passwordSuccess` function to implement other password protected actions. Have fun!
