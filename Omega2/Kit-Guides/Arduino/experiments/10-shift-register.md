
# Using a Shift Register to Control a Bunch of LEDs

// intro on using a shift register to increase the number of available digital outputs
// explanation of controlling a bunch of LEDs using only a few microcontroller pins


// TODO: insert shift register shared content

// TODO: insert controlling shift register shared content


## Building the Circuit

// wire up the microcontroller outputs to the shift register
// have all shift register outputs connected to an LED circuit

### Hooking up the Components

//  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)

//  * explain all of the wiring from microcontroller->shift reg
//    * explain each of the lines running from the Omega and what they do - according to the names from the controlling a shift register section


## Writing the Code

// create functions for using the shift register
// create knight rider kitt animation with the leds, see the starter kit shift register article for details


``` arduino
int latchPin = 5;   // the pin number connected to the latch pin (12 of the 74HC595)
                    // setting the latch LOW will send the 8 bits in storage to the output pins
int clockPin = 6;   // the pin number connected to the clock pin (11 of the 74HC595)
int dataPin = 4;    // the pin number connected to the input data pin (11 of the 74HC595)

byte storageByte = 0x01;  // the byte (8 bits) to be stored in the shift register
                          // initalized it as 00000001 representing the first LED on

void setup() 
{
  // initialize all the shift register pins as output
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);  
  pinMode(clockPin, OUTPUT);
}

// function which sends the stored byte to the output pins by setting the latch pin LOW
void updateShiftRegister()
{
  digitalWrite(latchPin, LOW);    // set the latch pin LOW
  // send the storage byte from arduino to the shift register withe LSB first
  // since the latch is still LOW, set the 8 output pins based on the stored byte and in turn light the correct LED
  shiftOut(dataPin, clockPin, LSBFIRST, storageByte);    
  digitalWrite(latchPin, HIGH);   // set the latch pin HIGH again
}

void loop() 
{
  // send 00000001 to the shift register, set the latch LOW and light the first LED
  updateShiftRegister();

  // shift 1 bit to the left 7 times, each time set the only corresponding LED on
  for (int i = 0; i < 7; i++)
  {
    delay(100);   // wait 0.1 second between lighting each LED
    storageByte = storageByte << 1;   // shift 1 bit to the left, the left most bit disappears and the right most bit is replaced by 0
                                      // i.e. 00000001 to 00000010
    updateShiftRegister();      // send the 8 bits to the shift register and set latch LOW
    
  }

  // shift 1 bit to the right 7 times, each time set the only corresponding LED on
  for (int i = 0; i < 7; i++)
  {
    delay(100);   // wait 0.1 second between lighting each LED
    storageByte = storageByte >> 1;   // shift 1 bit to the right, the right most bit disappears and the left most bit is replaced by 0
                                      // i.e. 10000000 to 01000000
    updateShiftRegister();      // send the 8 bits to the shift register and set latch LOW
  }
}
``` 

### What to Expect

// explain that the animation will be Knight Rider Kitt style: maybe throw in a gif for nostalgia
//  - it will run all the way left and then all the way right over and over again

### A Closer Look at the Code

// an overview of the code, go into detail about something interesting
