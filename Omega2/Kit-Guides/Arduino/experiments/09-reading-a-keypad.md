## Reading a Key-Pad

// intro to getting numbers as input from the user, useful in many scenarios, just think of ATMs

In this experiment, we will be reading input from a keypad and treating it as a password, if the correct password is entered, an LED will light up. This will be useful in many scenarios, such as ATMs or building access systems. In addition, we will also learn how to use Arduino libraries which are not build-in.


### Keypad
// should be in it's own separate markdown file

// explanation of the keypad:
//  - the user can press a button and the attached computer system will be able to tell which digit was pressed
//  - talk about how the signals coming from the keypad need to be decoded
//    - Note from Lazar: keypads usually have pins that identify if a button on a horizontal row is pressed, and then other pins that identify if a button on a vertical column is pressed. to read specific numbers, the user has to look for intersections
//    - need to explain the above in a concise and approachable way - include graphics

A keypad allows the user to press a button and the attached computer system will be able to tell which digit was pressed. If we were to use a pin for every button, there will be too many pins and the connection will be tedious! Instead we only use a pin for each horizontol row and a pin for each vertical column. In our case we only need 7 (4 rows and 3 columns) instead of 15.

// TODO: Image of a keypad

However, since the pins are not a direct match with the buttons, our microprocess will have to decode the signals coming from the keypad. When a button is pressed, the microprocesser should be able to detect the pin corresponding to its row and the pin corresponding to its column. We must define in our code the location of each button based on its row and column intersection.

### Building the Circuit

// simple circuit:
//  - single LED connected to the microcontroller output
//  - keypad input connected to the microcontroller

For this experiment, we will be using the keypad for the user to enter a password. If the password matches with the password set in the Arduino sketch, the blue LED on the Arduino Dock will light up for 3 seconds. For the circuit, we will be only a keypad. The on-board blue LED is used so no need to a connect external LED. The keypad as seven pins: four pins for defining which row and three pins for defining which column.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* 7x male-to-male Jumper wires
* 1x Keypad

#### Hooking Up the Components

// instructions on:
//  - connecting the led circuit (link back to single led experiment or reuse that text)
//  - connecting all of the keypad outputs to the microcontroller pins

1. Connect all the seven keypad pins to the digital pins (8, 7, 6, 5, 4, 3, 2) on the arduino dock in order from left to right, i.e. the left most keypad pin to arduino header pin 8.


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

This code will use a Keypad library which is probably not included in your the Ardiuno IDE by default. Here is two ways of including it in our code. In the first way we can install it directly from the Arduino IDE:

1. On the Arduino IDE, click Sketch > Include Library > Manage Libraries. The Library Manager will show up; type "keypad" in the search bar and install the first search result.

Another way is to manually install a library.

1. Download the Keypad library from a source: http://playground.arduino.cc/Code/Keypad#Download
2. Move the unzipped Keypad file folder to the Arduino library folder: on Windows, its located at C:/Program Files (x86)/Arduino/libraries

To use the library we need to add the following line at the top of our code:
```
#include <Keypad.h>
```

``` arduino
// download the Keypad library: http://playground.arduino.cc/Code/Keypad#Download
// move the unzipped Keypad file folder to the Arduino library folder: C:/Program Files (x86)/Arduino/libraries 
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
int LEDPin = 13;    // LED pin number to be lit when password is correct

// initializing keypad as an object from the Keypad library
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
  Serial.begin(9600);   // initializing serial communication with the Omega
  pinMode (13, OUTPUT);   // initializing pin for LED
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
          Serial.println("Correct password! LED On!");
          digitalWrite (13, HIGH);    // set the LED on
          delay(3000);    // let the LED on for 3 seconds
        }
        else
          // if any wrong key is entered, ask to entered the password again
          Serial.println("Wrong password! Press #");   
    }
  }
}
``` 


#### What to Expect

// just like any password-protected system, the LED will only turn on when the correct password has been entered
// if an incorrect digit has been entered, the user will have to start the password from the beginning

// TODO: PHOTO - GIF: include a gif of this

We will be using the keypad for a password-protected system. After the user enter the "#" key, we can enter a password. If the password entered matches with the password set in by char password[], which is by default "4321", the blue LED on the Arduino Dock will light up for 3 seconds. If the wrong password has been entered, it will ask the user to entered the "#" key again for more tries.


#### A Closer Look at the Code

// this experiment relied on arrays heavily, we'll go over some of the details now. Arrays are very useful and used all the time in programming.
For this code we will use the Arduino Keypad library. An Arduino library is very similar to a class which we talked about in the previous tutorial. To use the library, we declare an our own Keypad object (named keypad) of the Keypad class.

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

Notice we must include addition file Keypad.h which is inside the Arduino library folder. This file is where the Keypad class is defined. However, before to declare our Keypad object, we need declare the variables which needed to be passed into the Keypad object. This includes a two-dimensional array keys[][].

##### Arrays

// we will probably use arrays in an interesting way with the keypad function & the password array, go into detail about what was special in how we used arrays

In the previous tutorial we have used arrays. However, the arrays we used before are one-dimensional (1d), meaning they are made of one row of variables. However, in this code, we are using a two-dimension (2d) array made up of many rows of variables similar to a table. Using a 2d array for storing the keys of a keypad is much more conveniently and easier to visualize. Since the array is 3x4, we can easily see the position of each key in terms of its row and column:

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

### Going Further

// in this experiment we added password protection to an LED so we can show off the concept. This experiment might be useful if the correct password triggered a different action, maybe actuating a lock or moving a servo?

In this experiment we added password protection to an LED so we can show off the concept. This experiment might be useful if the correct password triggered a different action, maybe actuating a lock or moving a servo?