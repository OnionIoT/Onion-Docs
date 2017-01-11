
# Controlling a 7-Segment Display

// TODO: insert shared article about the 7seg display


## Building the Circuit

// Atmega->shift register->7seg display
<!-- Jumper wires -->
```{r child = '../../shared/jumper-wires.md'}
```

<!-- Breadboard -->
```{r child = '../../shared/breadboard.md'}
```
8 1K resistors
1 4-digit Seven-segment display


### Hooking up the Components

// copy from the starter kit 7seg article

Pin 1 is the bottom left pin when facing the seven segment display

Digit pins - 4 pins from the seven segment display representing one of the 4 digits

6,8,9,12 connect to 2,3,4,5 Arduino pins


Segment pins - 8 pins from the seven segment display each represent a segment of one digit 

1,2,3,4,5,7,10,11 each to a different 1K reistor then to the 6,7,8,9,10,11,12,13 Arduino pins


## Writing the Code

// write a sketch that takes input from the Serial (ie the Omega) and writes it to the 7 seg display
//  * ensure proper input validation is done so that only  hex numbers can be written to the display

``` arduino
// download the SevSeg library: http://playground.arduino.cc/Main/SevenSegmentLibrary
// move the unzipped file folder to C:/Program Files (x86)/Arduino/libraries
#include <SevSeg.h>

SevSeg sevseg; //Instantiate a seven segment controller object
int displayNum = 1111;
char charArray[5]="abcd"; //char array to be displayed, the array length is one more than the string length because string is terminated with a null char '\0' 

void setup()
{

  Serial.begin(9600);           // initialize serial communication with the Omega
  
  byte numDigits = 4;   
  byte digitPins[] = {5, 4, 3, 2}; //Digits: 1,2,3,4
  byte segmentPins[] = {13, 11, 7, 9, 10, 12, 6, 8}; //Segments: A,B,C,D,E,F,G,Period 
  bool resistorsOnSegments = true; // 1K ohm resistors attached between the 8 segment pins and the arduino dock pins
  
  sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, true);
  sevseg.setBrightness(50); //set brightness level from 0 to 100
  
}

void loop()
{
  sevseg.setChars(charArray);      // display the char array
  sevseg.refreshDisplay(); // Must run repeatedly; don't use blocking code (ex: delay()) in the loop() function or this won't work right

  // if there is serial data from the Omega, then display the first 4 characters
  if (Serial.available() > 0){     // constantly check if there is serial data
      String serialString = Serial.readString();      // read incoming data from the Omega as a string
      serialString.toCharArray(charArray,5);      // convert the incoming string to char array
  }
}
```


### What to Expect

// explanation of what the user should expect when they enter valid numbers

### A Closer Look at the Code

// something interesting about the code

#### Serial Input

// explain how we wait for input to be available and then read it in

### Going Further: Automating the Script

// introduce cron
// show example of how to setup cron to output the time from the omega once a minute
