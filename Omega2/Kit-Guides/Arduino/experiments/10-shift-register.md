## Using a Shift Register to Control a Bunch of LEDs {#arduino-kit-shift-register}

<!-- // intro on using a shift register to increase the number of available digital outputs
// explanation of controlling a bunch of LEDs using only a few microcontroller pins -->

Shift registers are very useful tools; using a few pins connected to a shift register, we can increase the number of output data pins that are available to us.

In this experiment, we'll be using a shift register to control eight LEDs, but we'll only be using three pins from the ATmega.


<!-- Shift Register -->
```{r child = '../../shared/shift-register.md'}
```

<!-- TODO: is this section needed anymore? -->
<!-- Controlling shift register -->
<!-- ```{r child = '../../shared/shift-register-control.md'} -->


### Building the Circuit

<!-- // wire up the microcontroller outputs to the shift register
// have all shift register outputs connected to an LED circuit -->

For this experiment we will use the send a byte (8 bits) serially from the ATmega to the shift register. When the latch pin of the shift register is set LOW, the shift register will use the stored 8 bits to set its 8 output pins accordingly. We will attach one LED to each of the 8 output pin to check if their state (1 or 0).	// TODO: what? this makes no sense, an led to check the state of an output pin? And then below we also make the eight LEDs light up? fix this section pls

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

<!-- //  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)

//  * explain all of the wiring from microcontroller->shift reg
//    * explain each of the lines running from the Omega and what they do - according to the names from the controlling a shift register section

// TODO: add pinout of 74HC595 -->

The IC should be plugged in across the channel of your breadboard (the slot running down the middle separating the `abcde` columns from the `fghij` columns). If you don't do this you will short out the pins across your IC. You may need to bend the pins just a bit in order to get it to fit.

![shift-register-diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shift-register-diagram.jpg)

Lets take a look at how the 16 pins of the 74HC595 shift register chip are defined.  We'll be referring to each pin by the numbers provided in the diagram above. When plugged in with the letters being right-side up, the bottow row of pins are pin 1 to 8 going from left to right. The top row of pins are pin 9 to 16 going from right to left.

>Note: Your IC will have a semi-circle indentation that indicates "up". Make sure that you plug it in properly so you know which pins are where.

<!-- // DONE: add a little blurb here: 'The Procedure:' or something along those lines, something to make it make sense with the tenses used in the list items -->

Here's the steps to get there:

1. Connecting your shift register to the breadboard
  * Start by plugging in your shift register across the channel so that the each pin has its own row.
  * Connect the supply voltage pin (`Vcc`) and the master reset pin (`MR`) on the IC to the `Vcc` rail on the breadboard
  * Connect the `GND` pin and output enable pin (`OE`) to the `GND` rail on the breadboard

  <!-- TODO: Insert picture of this stage -->

2. Connecting your LEDs
    * Connect the anodes of the eight LED each to one of the eight output pins of the 74HC595 - pin `15` and pin `1` to `7`, corresponding to `Q0` to `Q7`. Place the LEDs left to right in the following pin order: `Q0`, `Q1`, `Q2`, `Q3`, `Q4`, `Q5`, `Q6`, `Q7`. 

<!-- // DONE: if it's just 8 pins and it's crucial to the experiment, list them all out -->

  * Attach eight 100Ω current limiting resistors from cathodes of the LEDs to the `GND` rail on the breadboard.

 <!-- TODO: Insert picture of this stage -->

3. Connecting your Arduino Dock
  * Connect the Ground header to the negative rail on the breadboard	// TODO: what is meant by Ground header?
  * Connect Arduino Dock digital pin 4 to `DS` on the shift register - this is where our input is sent.
  * Connect Arduino Dock digital pin 5 to `STCP` on the shift register.
  * Connect Arduino Dock digital pin 6 to `SHCP` on the shift register.
  * Connect the `Vcc` rail to a `5V` pin on the Arduino Dock
  
  <!-- // TODO: what is meant by 5V header? -->

  <!-- TODO: Insert picture of this stage -->

### Writing the Code

<!-- // create functions for using the shift register
// create knight rider kitt animation with the leds, see the starter kit shift register article for details -->


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

<!-- // explain that the animation will be Knight Rider Kitt style: maybe throw in a gif for nostalgia
//  - it will run all the way left and then all the way right over and over again -->
The eight LEDs will light up like KITT from Knight Rider. The first LEDs will turn on, then the next will turn on and the previous one will turn off. This will repeat for all the LEDs in a loop from left to right and then from right to left. Only one LED should be lit up at a time.

// TODO: GIF of experiment

See, just like KITT:

// TODO: GIF of KITT

#### A Closer Look at the Code

We are only using three Arduino Dock pins to control eight LEDs by taking advantage of the shift register. Lets begin by declaring the three pin variables (`latchPin`, `clockPin` and `dataPin`) and initializing the three pins as output in `setup()`.

Each time we want to light up a different LED (change the output of the Shift Register), we use the `updateShiftRegister()` function. In this function, we send the 8 bits from the ATmega to the shift register:

```
shiftOut(dataPin, clockPin, LSBFIRST, storageByte);  
```

We set the latch `LOW` so that the 8 bits stored in the shift register will control the 8 output pins of the shift register:

```
digitalWrite(latchPin, LOW);
```

We must set the latch back high again after or else the output won't be set in the correct order.

// TODO: at this point, we need to make it clear that we WERE talking about the inner workings of the `updateShiftRegister` function. and that FROM NOW ON, we're talking about the operation of the loop function, and how it creates the KITT effect

After we turn on the first LED by sending `00000001`, we use a `for` loop to shift the `1` bit from the least significant bit `00000001` the
most significant bit `10000000`. We shift one bit at a time for seven times, each time using the bitwise shift left operation:

```
storageByte = storageByte << 1;
```

After shifting to the most significant bit `10000000`, we want to shift `1` bit back to the least significant bit `00000001` one bit at a time for seven times using

```
storageByte = storageByte >> 1;
```

We must `updateShiftRegister()` after each bit shift and each time include a slight delay for the CPU to process and for our eyes to see whats going on.
// TODO: expand on this sentence, this was lazy
