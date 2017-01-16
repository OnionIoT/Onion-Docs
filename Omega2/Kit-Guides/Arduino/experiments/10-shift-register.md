
## Using a Shift Register to Control a Bunch of LEDs

// intro on using a shift register to increase the number of available digital outputs
// explanation of controlling a bunch of LEDs using only a few microcontroller pins

Shift registers are very useful tools; using a few pins connected to a shift register, we can increase the number of output data pins that are available to us.

In this experiment, we'll be using a shift register to control eight LEDs, but we'll only be using three pins from the ATmega.

<!-- // TODO: update this number if required -->


<!-- Shift Register -->
```{r child = '../../shared/shift-register.md'}
```
<!-- Controlling shift register -->
```{r child = '../../shared/shift-register-control.md'}

// TODO: insert shift register shared content

// TODO: insert controlling shift register shared content


### Building the Circuit

// wire up the microcontroller outputs to the shift register
// have all shift register outputs connected to an LED circuit

For this experiment we will use the send a byte (8 bits) signal from the ATmega to the shift register. When the latch pin of the shift register is set LOW, the shift register will use the stored 8 bits to set its 8 output pins accordingly. We will attach one LED to each of the 8 output pin to check if their state (1 or 0).

We will also make the eight LEDs light up in the knight rider KITT pattern using only three ATmega pins! For this circuit, we will need the 74HC595 shift register and 8 LEDS with 8 current limiting resistors (200 ohms).

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 8x 200Ω Resistor
* 8x LED color of your choice!
* 1x 74HC595 Shift register

#### Hooking up the Components

//  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)

//  * explain all of the wiring from microcontroller->shift reg
//    * explain each of the lines running from the Omega and what they do - according to the names from the controlling a shift register section

// TODO: add pinout of 74HC595

The IC should be plugged in across the channel of your breadboard (the slot running down the middle separating the `abcde` columns from the `fghij` columns). If you don't do this you will short out the pins across your IC. You may need to bend the pins just a bit in order to get it to fit.

![shift-register-diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shift-register-diagram.jpg)

Lets take a look at how the 16 pins of the 74HC595 shift register chip are defined.  We'll be referring to each pin by the numbers provided in the diagram above. When plugged in with the letters being right-side up, the bottow row of pins are pin 1 to 8 going from left to right. The top row of pins are pin 9 to 16 going from right to left. 

>Note: Your IC will have a semi-circle indentation that indicates "up". Make sure that you plug it in properly.

1. Connecting your shift register to the breadboard

  - Start by plugging in your shift register across the channel so that the each pin has its own row.
  - Connect pin 16 and pin 10 to the positive rail (Vcc) on the breadboard
  - Connect pin 8 and pin 13 to the negative rail (Ground) on the breadboard

  <!-- TODO: Insert picture of this stage -->

2. Connecting your LEDs

  - Connect the anodes of the 8 LED each to one of the 8 output pins of the 74HC595 (pin 15 and pin 1 to 7). Place the LEDs left to right in the following pin order: 15, 1, 2, 3, .. 7.
  - Attach the eight current limiting resistors from cathodes of LEDs to the negative rail (Ground) on the breadboard.

 <!-- TODO: Insert picture of this stage -->

3. Connecting your Arduino Dock 

  - Connect digital pin 4 to pin 14 on the shift register
  - Connect digital pin 5 to pin 12 on the shift register
  - Connect digital pin 6 to pin 11 on the shift register
  - Connect the Ground header to the negative rail on the breadboard
  - Connect the 5V header to the positive rail on the breadboard

  <!-- TODO: Insert picture of this stage -->

### Writing the Code

// create functions for using the shift register
// create knight rider kitt animation with the leds, see the starter kit shift register article for details


``` arduino
int latchPin = 5;   // the pin number connected to the latch pin (12 of the 74HC595)
                    // setting the latch LOW will send the 8 bits in storage to the output pins
int clockPin = 6;   // the pin number connected to the clock pin (11 of the 74HC595)
int dataPin = 4;    // the pin number connected to the input data pin (14 of the 74HC595)

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
  // since the latch is LOW, set the 8 output pins based on the stored 8 bits and in turn light the correct LED
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

#### What to Expect

// explain that the animation will be Knight Rider Kitt style: maybe throw in a gif for nostalgia
//  - it will run all the way left and then all the way right over and over again

#### A Closer Look at the Code

// an overview of the code, go into detail about something interesting
