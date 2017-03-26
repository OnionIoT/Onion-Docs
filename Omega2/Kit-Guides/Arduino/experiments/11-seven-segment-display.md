// TODO: overall: fix the grammar and typos

## Controlling a 7-Segment Display {#arduino-kit-seven-segment-display}

For this tutorial, we will learn how to use a seven-segment display. In addition, we will learn how to send data **from** the Omega **to** the ATmega through serial that will be displayed on the seven-segment. This way we don't have to reflash the ATmega everytime we want to display something new on the display.


<!-- Seven Segment Display-->
```{r child = '../../shared/seven-segment.md'}
```

### Building the Circuit

// Atmega->shift register->7seg display

For this experiment, we will send a string from the Omega to the ATmega through the serial port. We will then convert the string on the ATmega into an array of characters and display the first four characters on the seven segment display, but only if each of the characters (letter or a number) can be represented using seven segments.	// TODO: maybe break up this run-on sentence

For the circuit, we will need the four-digit seven-segment display and eight 1kΩ current limiting resistors for each of the eight segment pins. The current limiting resistors are essential since there is an LED in each of the segments. The 12 pins of the seven-segment display can be grouped into two types: digit pins and segments pins. There are four digits and for each digit, there are eight segments including the decimal point. Therefore, there are a total of `4 x 8 = 32` LEDs.	// TODO: segment pins? lets refer to them as scan pins like we did in the shared article


#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
    * 12x Male-to-Female
    * 6x Male-to-Male
* 8x 1kΩ Resistors
* 1x Seven Segment display

#### Hooking up the Components

// TODO: copy from the starter kit 7seg article, this is an old TODO, please compare against the starter kit article

// TODO: fix this sentence, the grammar is poor and its not very clear
The seven segment display from the kit is common cathode, which mean the cathode of LEDs are connected to the digit pins and their anodes are connected to the segment pins.

![Seven-segment display pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/seven-seg-pinout.jpg)

The seven segment display is not labelled, so we'll have to reference the pinout diagram to make sure the correct connections are being made. When facing the front of seven segment display with decimal points at the bottom, the bottom row of pins are numbered 1 to 6 going from left to right and the top row of pins are numbered 7 to 12 going from right to left.


<!-- // DONE: do we use the shift reg here? LAZAR -->
<!-- discussed with Gabe, nope. JAMES -->

// TODO: fix build instructions to include images

We will need to connect all 12 pins of the seven segment display to 12 digital pins of the Arduino Dock.

<!-- DONE: CIRCUIT DIAGRAM -->
![Circuit diagram for this experiment](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/diagrams/11-circuit-diagram.png)

1. Connect the digit pins (`6`,`8`,`9`,`12`) of the seven seg to the GPIO pins `2`,`3`,`4`,`5` on the Arduino Dock respectively.
2. Cconnect the segment pins (`1`,`2`,`3`,`4`,`5`,`7`,`10`,`11`) of the seven seg each to a different 1K resistor then to the pins `6`,`7`,`8`,`9`,`10`,`11`,`12`,`13` on the Arduino Dock respectively.

<!-- DONE: PHOTO assembled circuit -->
![That's a lot of jumpers](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/11-assembled-circuit.jpg)


### Writing the Code

<!-- // write a sketch that takes input from the Serial (ie the Omega) and writes it to the 7 seg display
//  * ensure proper input validation is done so that only  hex numbers can be written to the display -->

// TODO: LAZAR to revise code

``` arduino
#define NUM_7SEG_DIGITS 		4
#define NUM_7SEG_SEGMENTS 		8
#define NUM_INPUT_CHARS			9

// array of bytes, each byte represents how different characters will be displayed on the 7-seg
static const byte digitCodeMap[] = {
 //DPGFEDCBA  Element  Char   7-segment map:
  B00111111, // 0   "0"          AAA
  B00000110, // 1   "1"         F   B
  B01011011, // 2   "2"         F   B
  B01001111, // 3   "3"          GGG
  B01100110, // 4   "4"         E   C
  B01101101, // 5   "5"         E   C
  B01111101, // 6   "6"          DDD
  B00000111, // 7   "7"
  B01111111, // 8   "8"
  B01101111, // 9   "9"
  B01110111, // 10  'A'
  B01111100, // 11  'b'
  B00111001, // 12  'C'
  B01011110, // 13  'd'
  B01111001, // 14  'E'
  B01110001, // 15  'F'
  B00111101, // 16  'G'
  B01110110, // 17  'H'
  B00000110, // 18  'I'
  B00001110, // 19  'J'
  B01110110, // 20  'K'  Same as 'H'
  B00111000, // 21  'L'
  B00000000, // 22  'M'  NO DISPLAY
  B01010100, // 23  'n'
  B00111111, // 24  'O'
  B01110011, // 25  'P'
  B01100111, // 26  'q'
  B01010000, // 27  'r'
  B01101101, // 28  'S'
  B01111000, // 29  't'
  B00111110, // 30  'U'
  B00111110, // 31  'V'  Same as 'U'
  B00000000, // 32  'W'  NO DISPLAY
  B01110110, // 33  'X'  Same as 'H'
  B01101110, // 34  'y'
  B01011011, // 35  'Z'  Same as '2'
  B00000000, // 36  ' '  BLANK
  B01000000, // 37  '-'  DASH
};

// number of digits
// array of pins to control the digits: 1,2,3,4
byte digitPins[] = {5, 4, 3, 2};
// array of pins to control the segments: A,B,C,D,E,F,G,Period
byte segmentPins[] = {13, 11, 9, 7, 6, 12, 10, 8};

// array of 4 bytes to be displayed, each byte representing a digit
// 	initially set to represent '1234'
byte currentDigitCode[NUM_7SEG_DIGITS] = {digitCodeMap[1],digitCodeMap[2],digitCodeMap[3],digitCodeMap[4]};

// declare functions that will be used in the loop() function
void 	displayDigits();
void 	stringToDigits(String inputString);


// This code runs once when the program starts, and no more
void setup()
{
	// initialize serial communication with the Omega
	Serial.begin(9600);

	// loop for setting all the digit pins to output and then off (HIGH)
	for (byte digitIndex = 0 ; digitIndex < NUM_7SEG_DIGITS ; digitIndex++) {
		pinMode(digitPins[digitIndex], OUTPUT);
		digitalWrite(digitPins[digitIndex], HIGH);
	}

	// loop for setting all the segment pins to output and then  off (LOW)
	for (byte segmentIndex = 0 ; segmentIndex < NUM_7SEG_SEGMENTS ; segmentIndex++) {
		pinMode(segmentPins[segmentIndex], OUTPUT);
		digitalWrite(segmentPins[segmentIndex], LOW);
	}
}

// The code in here will run continuously until we turn off the Arduino Dock
void loop()
{
	// display the digits stored in the currentDigitCode array
	displayDigits();

	// check for serial data coming from the Omega
	if (Serial.available() > 0){
		// read the incoming data as a string
		String serialString = Serial.readString();      // read incoming data from the Omega as a string
		Serial.println(serialString);

		// convert the string into bytes that can be displayed on the 7seg (and store them in the currentDigitCode array)
		stringToDigits(serialString);
	}
}



//// function definitions
// write the digits currently stored in the currentDigitCode to the 7-segment display
void displayDigits()
{
	//// nested for loop for displaying all the digits and their segments based on currentDigitCode[], which is an array of 4 bytes
	// for each digit, set the specific digit pin LOW, turn on the correct segments, set the digit pin HIGH again
	for (byte digitIndex = 0 ; digitIndex < NUM_7SEG_DIGITS ; digitIndex++) {
		// pull the current digit pin LOW to enable displaying the segments
		digitalWrite(digitPins[digitIndex], LOW);

		// set the correct segments on for current digit based on the current element of the currentDigitCode[] array
		for (byte segmentIndex = 0 ; segmentIndex < NUM_7SEG_SEGMENTS ; segmentIndex++) {
			// to the pin associated with the current segment,
			// write the bit from the current element of the currentDigitCode[] array that corresponds to the current segment
			digitalWrite(segmentPins[segmentIndex], (currentDigitCode[digitIndex] >> segmentIndex) & 0x01);
		}

		// delay before disabling the current digit so the human eye can observe it
		delay(5);
		// pull the current digit pin HIGH to disable display of the segments
		digitalWrite(digitPins[digitIndex], HIGH);
	}
}

// convert an input string into bytes can be displayed on the 7seg,
//	store them in the currentDigitCode array
void stringToDigits(String inputString)
{
	byte 	digitIndex = 0; // keep track of which digit on the display we're currently setting up
	char 	inputCharacters[NUM_INPUT_CHARS];

	// convert the incoming data into a char array
	inputString.toCharArray(inputCharacters,NUM_INPUT_CHARS);

	// attempt to match each character from the input to bytes that can be displayed on the 7-seg
	for (byte index = 0 ; index < NUM_INPUT_CHARS ; index++) {
		// convert a character to a integer (based on the ASCII table)
		int charToInt = inputCharacters[index];
		Serial.println(charToInt);

		// case statement for matching the integer value of each character the an element from the digitCodeMap[] array
		switch (charToInt) {
			case 48 ... 57:   //0-9
				currentDigitCode[digitIndex] = digitCodeMap[charToInt-'0'];	// subtract the integer ASCII value for '0' to be able to correctly index our digitCodeMap array
				break;

			case 65 ... 90: // A-Z
				currentDigitCode[digitIndex] = digitCodeMap[charToInt-'0'-7]; // subtract the integer ASCII value for '0' and 7 to correctly map the A-Z ASCII values to our digitCodeMap array
				break;

			case 97 ... 122: // a-z
				currentDigitCode[digitIndex] = digitCodeMap[charToInt-'0'-39];	// subtract the integer ASCII value for '0' and 7 to correctly map the a-z ASCII values to our digitCodeMap array
				break;

			case 45:  //dash
				currentDigitCode[digitIndex] = digitCodeMap[37];
				break;

			case 32:  //space
				currentDigitCode[digitIndex] = digitCodeMap[36];
				break;

			case 46: //dot
				// set the decimal segment for the previous digit
				//	but only if we've already setup a previous digit (to prevent unforseen errors)
				if (digitIndex > 0) {
					currentDigitCode[digitIndex-1] = currentDigitCode[digitIndex-1] | B10000000;
				}
				break;

			default: // not mapped by digitCodeMap, set to blank
				currentDigitCode[digitIndex] = digitCodeMap[36];
				break;
		}

		// increment the digit index to the next index
		//	but only if the character we just looked at was not a dot
		//	since dots get added to the previous digit
		if (charToInt != 46) {
			digitIndex++;
		}

		// prematurely end the loop if we've decoded enough digits to fill the entire display
		if (digitIndex >= NUM_7SEG_DIGITS) {
			break;
		}
	}
}
```


#### What to Expect

When the code has being flashed on the ATmega, the seven segment display should display the characters `1234`. If we use the following command on our Omega:

```
echo -ne 'AAAA' > /dev/ttyS1
```

<!-- // TODO: gif of 7seg showing 1234 and then changing to AAAA -->

We should see the characters inside the single quoation mark '' displayed on our seven segment display.  By default echo will send the data and start a new line ('/n') after the data; we use the `-ne` operator to remove the new line. We can send any number and alphabet except for 'M' and 'W'. There will only be one way to display an alphabet regardless of its case. We can also send space ' ' and dash '-'; any undisplayable characters will be displayed as blank space ' '.  

In addition, we can also add one decimal point in the string we send from the Omega. If multiple decimal points are used, only the right most one will be displayed. If the first character sent is a decimal point, it will not be displayed.


#### A Closer Look at the Code


<!-- First we include the Arduino SevSeg library. We then initalize our own SevSeg object:

```
sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, resistorsOnSegments);
```

The first parameter is the configuration of the seven segment display, either common cathod or common anode. The second parameter defines the number of digits the display has, which is four. The third parameter is an array of pins on the Arduino Dock that is connected to the four digit pins and the fourth parameter is an array of pins that is connected to the eight segment pins. The last parameter is set true since we connected the current limiting resistors to the segment pins instead of the digit pins.

Furthermore, we store the characters to be displayed inside an array of chars:

char charArray[5]="abcd";

When we set the array of char with a string, there will be an extra char at the end called the null terminator "\0"; therefore our array needs to be five chars long in order to store "abcd". -->

// TODO: please fix the grammar and flow of everything here on out

We start by making an array of bytes to represent how different number or alphebat can be displayed. Each byte in the array has eight bits and set all the segments of a character. We start by turning all the LEDs segments off. Since the anodes are connected to the segment pins, we will set them `LOW`. The cathodes are connected to the digit pins, we set them `HIGH`. This way the current is flowing in the reverse bias direction and the LED will not light up. // TODO: whoa, this last sentence came out of left-field, maybe an explanation of what reverse bias means

To display all the digits correctly, we must turn all on the segments of one digit on before we turn off that digit and turn on the next digit. If we cycle through turning on and off each digit faster than the human eye can see, it will look like all the digits are displayed correctly. However, we must add one extra cycle of delay between turning on and off each digit for some characters to be displayed properly; try remove the following `for` loop and see what happens:

```
for (byte cycle = 0 ; cycle < 2 ; cycle++) { }
```

The cycling of digits is required because due to the configuration of the LEDs, we can not have different characters display on all four digits at once.

You might be wondering how exactly can we set the correct segments for one digit on based on 8 bits. First we use a index byte (initally `B00000001`) to represent which bit we are currently setting using `digitalWrite()`.

```
digitalWrite(segmentPins[segmentNum], currentDigitCode[digit] & index);
```

We use the bitwise AND operation `&` of the index and the character code to determine whether the bit is to be set `HIGH` or `LOW`. After we set one bit we shift the 1 bit of the the index to the left (from `B00000001` to `B00000010`)

```
index = index << 1;
```

and determine set the `digitWrite()` the next segment based on the index byte and the character code byte. We use a `for` loop to repeat 8 times for all the segments. Don't forget to set the index byte back to `B00000001` after the loops.


##### Serial Input and Conversions

In our `loop()` function we first initialize the display by displaying the characters store initially in our array `1234`. After which, the ATmega will continously check for serial (UART1) input. When we use the echo command on our Omega we send a string to the ATmega through serial. Once the ATmega detects data on the serial line, it will read the data and store it in a string variable.

```
String serialString = Serial.readString();
```

We will need to process the string we received in order to display it. We must then convert the received string into an array of char using the Arduino built-in `toCharArray()` function. We will then need to convert a character to a integer and subtract from it the integer value of '0' according to the ASCII table. After that, we need to match the integer value of each character the an element from the digitCodeMap[] array using a case statement. A case statement is essentially an easier and more structured way of writing a bunch of if statements.

For example, if we get the character 'A', we subtract '0' from it. According to their decimal value from the ASCII table, we have `65-48=17`. Then in our case statement, 17 matches the `case 17 ... 42:`, in which we subtract 17 by 7 to get the element 10 from `digitCodeMap[]`, which corresponds to the segments to be displayed for 'A'.

When we convert the string to a character array, we will get an extra character at the end of the array called the null terminator '/0'. This is how we determine how many characters to be displayed. If a string of only one char is send, our second element in the char array will be the null terminator, which will be -48 after subtracting '0' from it. In this case, we set the rest of our digits to display blank spaces.

The decimal point character '.' is special in the sense that it needs to be displayed by setting the most significant bit of the byte code for the previous digit.

```
currentDigitCode[decimalPlace] = currentDigitCode[decimalPlace] | B10000000;
```

In addition, we need to move the rest of the array after the decimal point one element forward to replace the decimal point character. This is done in the `checkDecimalPoint()` function.

#### Going Further: Automating the Script

// TODO: introduce cron
// show example of how to setup cron to output the time from the omega once a minute
