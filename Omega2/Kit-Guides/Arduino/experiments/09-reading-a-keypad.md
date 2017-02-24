## Reading a Key-Pad {#arduino-kit-reading-a-keypad}

In this experiment, we will be reading input from a keypad and treating it as a password, if the correct password is entered, an LED will light up. This will be useful in many scenarios, such as ATMs or building access systems. In addition, we will also learn how to use Arduino libraries which are not built-in.


### Keypad
// TODO: should be in it's own separate markdown file


A keypad allows the user to press a button and the attached computer system will be able to tell which digit was pressed. If keypads were to use a pin for every button, there would be way too many data pins to connect! Instead, keypads only have pins for each horizontal row and pins for each vertical column. In our case we only need 7 (4 rows and 3 columns) instead of 15.

// TODO: graphic of a keypad

// TODO: potentially reword the next paragraph for clarity
However, since the pins are not directly mapped to the buttons, our computer system will have to decode the signals coming from the keypad. When a button is pressed, the corresponding row and column pins will become logical high. Our code will have to define the location of each button based on its row and column intersection.

### Building the Circuit

<!-- // simple circuit:
//  - single LED connected to the microcontroller output
//  - keypad input connected to the microcontroller -->

For this experiment, we will be using the keypad to allow the user to input a password. If the password matches with the password set in the Arduino sketch, the blue LED on the Arduino Dock will light up for 3 seconds. For the circuit, we will only need a keypad, and since we'll be using the on-board blue LED, there is no need to a connect external LED.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* 7x male-to-male Jumper wires
* 1x Keypad

#### Hooking Up the Components

// TODO: add an intro, mention: 'The keypad as seven pins: four pins for the rows and three pins for the columns.''

1. Connect all the seven keypad pins to the digital pins (8, 7, 6, 5, 4, 3, 2) on the Arduino Dock in order from left to right, i.e. the left most keypad pin to arduino header pin 8.

// TODO: add a photo of the completed circuit and a blurb about 'this is more or less how your circuit should look'

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

This code will use a Keypad library which is probably not included in your the Ardiuno IDE by default. There are two ways of getting ahold of the library and including it in our code. In the first way we can install it directly from the Arduino IDE:

1. On the Arduino IDE, click `Sketch > Include Library > Manage Libraries`. The Library Manager will show up; type `keypad` in the search bar and install the first search result.

The other way is to manually install a library.

1. Download the Keypad library from a source: http://playground.arduino.cc/Code/Keypad#Download
2. Move the unzipped Keypad file folder to the Arduino library folder: on Windows, its located at C:/Program Files (x86)/Arduino/libraries
// TODO: add locations for OS X and Linux (can look this up online)

To use the library we need to add the following line at the top of our code:
```
#include <Keypad.h>
```

// TODO: verify this code works

``` arduino
// include the Keypad library
#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};        // a 4x3 array of all the keys as chars

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


#### What to Expect

// TODO: PHOTO - GIF: include a gif of this

We will be using the keypad for a password-protected system. After the user presses the `#` key, they will be prompted via serial to enter a password. If the entered password matches with the password set in by `char password[]`, which is by default `4321`, the blue LED on the Arduino Dock will light up for 3 seconds. If the wrong password has been entered, it will ask the user to press the `#` key again to retry.




#### A Closer Look at the Code

// TODO: fill in the link

This code uses the Arduino Keypad library. Remember the `ServoMotor` class we wrote in the [previous tutorial](//TODO: fill in this link)? Well a library usually contains the definition of a class and then the implementation of the methods (functions) of that class. To use the class, we include the library's header file in our code, and then we are free to create a `Keypad` object in our code. We've creatively name the object `keypad`.

```
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
```

Try commenting out the `#include 'Keypad.h'` line, you'll see that the compiler will complain, saying that it doesn't know what a Keypad is! This file is in the Arduino Keypad library and it defines the `Keypad` class. However, before we instantiate our `Keypad` object, we need  to declare the variables which needed to be passed into the Keypad object. This includes a two-dimensional array `keys[][]`.

##### Two-Dimensional Arrays

// TODO: clean up this paragraph, it's going in the right direction but doesn't include enough details:
//	* expand on what is meant by a single row of variables
//	* expand on the 2d array is similar to a table bit
//	* talk about how 2d arrays need to be indexed in both dimensions

In previous experiments, we've used arrays. However, the arrays we used before were one-dimensional (1d), meaning they are made of one row of variables. However, in this code, we are using a two-dimension (2d) array made up of many rows of variables similar to a table. Using a 2d array for storing the keys of a keypad is much more convenient and easier to visualize. Since the array is `3x4`, we can easily see the position of each key in terms of its row and column:

```
const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};        // a 4x3 array of all the keys as chars
```

// TODO: include some examples of accessing the array: like keys[2][3] = 6, give a few

### Going Further

In this experiment, we password protected an LED just to illustrate the concept. It would be a little more useful if the correct password triggered a different action, maybe moving a servo or actuating a lock? You can replace the contents of the `passwordSuccess` function to implement other password protected actions. Have fun!
