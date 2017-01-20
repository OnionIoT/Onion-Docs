
## Controlling a 7-Segment Display

// TODO: insert shared article about the 7seg display


### Building the Circuit

// Atmega->shift register->7seg display

For this experiment, we will send a string from the Omega to the ATmega through serial communication. On the ATmega, we will then convert the string into an array of characters and display the first four characters on the seven segment display if each of the character (a letter or a number) can be represented using seven segments.

For the circuit, we will need the 4-digit seven-segment display and eight 1kΩ current limiting resistors for each of the eight segment pins. The current limit resistor are essential since there is a LED in each segment. The 12 pins of the seven-segment display can be grouped into two types: digit pins and segments pins. There are 4 digits and for each digit, there are 8 segments including the decimal point. Therefore, there are a total of 4 x 8 = 32 LEDs.


#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 8x 1kΩ Resistors
* 1x 7 Segment display

#### Hooking up the Components

// copy from the starter kit 7seg article

The seven segment display from the kit is common cathode, which mean the cathode of LEDs are connected to the digit pins and their anodes are connected to the segment pins.

![Seven-seg-pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/Seven-seg-pinout.jpg)

Lets first look at how the 12 pins at the back of the seven segment display are defined. When facing the front of seven segment display with decimal points at the bottom, the bottom row of pins are numbered 1 to 6 going from left to right and the top row of pins are numbered 7 to 12 going from right to left. We will need to connect all 12 pins of the seven-segment display to 12 digital pins of the Arduino Dock (Pin 2 to 13).

1. Connect the digit pins (6,8,9,12) of the seven seg to the pins (2,3,4,5) the Arduino dock correspondingly.
2. Cconnect the segment pins (1,2,3,4,5,7,10,11) of the seven seg each to a different 1K resistor then to the pins (6,7,8,9,10,11,12,13) of the Arduino dock rcorrespondingly.

### Writing the Code

// write a sketch that takes input from the Serial (ie the Omega) and writes it to the 7 seg display
//  * ensure proper input validation is done so that only  hex numbers can be written to the display

``` arduino
// download the SevSeg library: http://playground.arduino.cc/Main/SevenSegmentLibrary
// move the unzipped file folder to the Arduino library folder: C:/Program Files (x86)/Arduino/libraries
#include <SevSeg.h>

SevSeg sevseg; //Instantiate a seven segment controller object
char charArray[5]="abcd"; //char array to be displayed, the array length is one more than the string length because string is terminated with a null char '\0' 

void setup()
{

  Serial.begin(9600);           // initialize serial communication with the Omega
  
  byte numDigits = 4;   
  byte digitPins[] = {5, 4, 3, 2}; //Digits: 1,2,3,4
  byte segmentPins[] = {13, 11, 9, 7, 6, 12, 10, 8}; //Segments: A,B,C,D,E,F,G,Period
  bool resistorsOnSegments = true; // 1K ohm resistors attached between the 8 segment pins and the arduino dock pins
  
  sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, resistorsOnSegments);
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


#### What to Expect

// explanation of what the user should expect when they enter valid numbers
When the code has being flashed on the ATmega, the seven segment display should display the letters "AbCd". If we use the following command on our Omega:

```
echo -ne '1111' > /dev/ttyS1
```

We should see the characters inside the single quoation mark '' displayed on our seven segment display. By default echo will send the data and start a new line ('/n') after the data; we use the (-ne) operator to remove the new line.


#### A Closer Look at the Code

// something interesting about the code

First we include the Arduino SevSeg library. We then initalize our own SevSeg object:

```
sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, resistorsOnSegments);
```

The first parameter is the configuration of the seven segment display, either common cathod or common anode. The second parameter defines the number of digits the display has, which is four. The third parameter is an array of pins on the Arduino Dock that is connected to the four digit pins and the fourth parameter is an array of pins that is connected to the eight segment pins. The last parameter is set true since we connected the current limiting resistors to the segment pins instead of the digit pins.

Furthermore, we store the characters to be displayed inside an array of chars: 

char charArray[5]="abcd";

When we set the array of char with a string, there will be an extra char at the end called the null terminator "\0"; therefore our array needs to be five chars long in order to store "abcd".

##### Serial Input

// explain how we wait for input to be available and then read it in
In our loop() function we first initialize the display by displaying the characters store initially in our array "abcd". After which, the ATmega will continously check for serial (UART1) input. When we use the echo command on our Omega we send a string to the ATmega through serial. Once the ATmega detects data on the serial line, it will read the data and store it in a string variable. 

```
String serialString = Serial.readString(); 
```

We must then convert the received string into an array of char using the Arduino build-in toCharArray() function in order to display the characters on the seven segment dislpay.

#### Going Further: Automating the Script

// introduce cron
// show example of how to setup cron to output the time from the omega once a minute
