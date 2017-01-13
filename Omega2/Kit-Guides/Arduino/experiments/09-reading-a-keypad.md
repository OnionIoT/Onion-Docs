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

For the circuit, we will be needing only a keypad. The on-board blue LED is used so need to a connect external LED.

#### Hooking Up the Components

// instructions on:
//  - connecting the led circuit (link back to single led experiment or reuse that text)
//  - connecting all of the keypad outputs to the microcontroller pins

Connect all the seven keypad pins to the digital pins (8, 7, 6, 5, 4, 3, 2) on the arduino dock in order from left to right, i.e. the left most keypad pin to arduino header pin 8.


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

``` arduino
// download the Keypad library: http://playground.arduino.cc/Code/Keypad#Download
// move the unzipped Keypad file folder to C:/Program Files (x86)/Arduino/libraries 
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


#### A Closer Look at the Code

// this experiment relied on arrays heavily, we'll go over some of the details now. Arrays are very useful and used all the time in programming.

##### Arrays

// we will probably use arrays in an interesting way with the keypad function & the password array, go into detail about what was special in how we used arrays



### Going Further

// in this experiment we added password protection to an LED so we can show off the concept. This experiment might be useful if the correct password triggered a different action, maybe actuating a lock or moving a servo?
