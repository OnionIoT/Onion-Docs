## Using a Shift Register to Control a Bunch of LEDs {#arduino-kit-shift-register}

<!-- // intro on using a shift register to increase the number of available digital outputs
// explanation of controlling a bunch of LEDs using only a few microcontroller pins -->

Shift registers are very useful tools; using a few pins connected to a shift register, we can increase the number of output data pins that are available to us.

In this experiment, we'll be using a shift register to control eight LEDs, but we'll only be using three pins from the ATmega.


<!-- Shift Register -->
```{r child = '../../shared/shift-register.md'}
```

### Building the Circuit

<!-- // wire up the microcontroller outputs to the shift register
// have all shift register outputs connected to an LED circuit -->

For this experiment, we will send a 8 bits (a byte) serially from the ATmega to the shift register. When the latch pin of the shift register is set LOW, the shift register will use the stored 8 bits to set its 8 output pins accordingly. We will attach one LED to each of the 8 output pins and make them light up like Knight Rider's KITT. By the power of the shift register, we can do this using only three ATmega pins!

<!-- // DONE: add the circuit diagram -->

This is the diagram of the circuit we'll be building:

![Circuit diagram of the shift register experiment](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/diagrams/10-circuit-diagram.png)

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

// DONE: add pinout of 74HC595 -->

<!-- // DONE: don't need to repeat this image, already included in the shift reg section above -->
<!-- ![The shift register with pins labelled](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/74HC595-pinout.png) -->

The IC should be plugged in across the channel of your breadboard (the slot running down the middle separating the `abcde` columns from the `fghij` columns). If you don't do this you will short out the pins across your IC. You may need to bend the pins just a bit in order to get it to fit.


<!-- // DONE: don't need to repeat this image, already included in the shift reg section above -->
<!-- ![Shift register data flow](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shift-register-block-diagram.png) -->

Lets take a look at how the 16 pins of the 74HC595 shift register chip are defined.  We'll be referring to each pin by the numbers provided in the diagram above. When plugged in with the letters being right-side up, the bottow row of pins are pin 1 to 8 going from left to right. The top row of pins are pin 9 to 16 going from right to left.

>Note: Your IC will have a semi-circle indentation that indicates "up". Make sure that you plug it in properly so you know which pins are where.


Here's the steps to get there:

1. Connecting your shift register to the breadboard
  * Start by plugging in your shift register across the channel so that the each pin has its own row.
  * Connect the supply voltage pin (`Vcc`) and the master reset pin (`MR`) on the IC to the `Vcc` rail on the breadboard
  * Connect the `GND` pin and output enable pin (`OE`) to the `GND` rail on the breadboard

  <!-- DONE: Insert picture of this stage -->
![Shift register wired](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/10-shift-reg-wired.jpg)

>The jumpers at the top will be wired to the LEDs eventually.

2. Connecting your LEDs
    * Connect the anodes of the eight LED each to one of the eight output pins of the 74HC595 - pin `15` and pin `1` to `7`, corresponding to `Q0` to `Q7`. Place the LEDs left to right in the following pin order: `Q0`, `Q1`, `Q2`, `Q3`, `Q4`, `Q5`, `Q6`, `Q7`.

<!-- // DONE: if it's just 8 pins and it's crucial to the experiment, list them all out -->

  * Attach eight 100Ω current limiting resistors from cathodes of the LEDs to the `GND` rail on the breadboard.

 <!-- DONE: Insert picture of this stage -->
![](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/10-led-shift-reg-wired.jpg)

3. Connecting your Arduino Dock
  * Connect the `GND` pin on the Dock to the `GND` rail on the breadboard.
  <!-- // DONE: what is meant by Ground header? -->
  * Connect Arduino Dock digital pin 4 to `DS` on the shift register - this is where our input is sent.
  * Connect Arduino Dock digital pin 5 to `STCP` on the shift register.
  * Connect Arduino Dock digital pin 6 to `SHCP` on the shift register.
  * Connect the `Vcc` rail to a `5V` pin on the Arduino Dock

  <!-- // DONE: what is meant by 5V header? -->

  <!-- DONE: Insert picture of this stage -->
![Circuit complete, ready to code!](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/10-assembled-circuit.jpg)


### Writing the Code

<!-- // create functions for using the shift register
// create knight rider kitt animation with the leds, see the starter kit shift register article for details -->


``` c
#define NUM_LEDS     8

// duration to pause
int delayTime = 100;

// the pin connected to the latch pin, RCLK (pin 12 of the shift register)
//    setting the latch LOW will send the 8 bits in storage to the output pins
int latchPin = 5;
// the pin connected to the clock pin, SRCLK (pin 11 of the shift register)
int clockPin = 6;
// the pin connected to the serial data pin, SER (pin 14 of the shift register)
int dataPin = 4;


// This code runs once when the program starts, and no more
void setup()
{
  // initialize all the pins connected to the shift register as outputs
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);  
  pinMode(clockPin, OUTPUT);
}

// function which sends the stored byte to the output pins by setting the latch pin LOW
void updateShiftRegister(byte storageByte)
{
  // set the latch pin LOW
  digitalWrite(latchPin, LOW);

  // send the storage byte to the shift register with the LSB first
  //     since the latch is LOW, set the 8 output pins based on the stored 8 bits and in turn light the correct LED
  shiftOut(dataPin, clockPin, LSBFIRST, storageByte);

  // set the latch pin HIGH again
  digitalWrite(latchPin, HIGH);
}

// The code in here will run continuously until we turn off the Arduino Dock
void loop()
{
  // the byte (8 bits) to be stored in the shift register
  //    initialize to 00000001, representing the first LED on
  byte storageByte = 0x01;

  // create the effect of having the light travel to the left
  for (int i = 0; i < NUM_LEDS-1; i++)
  {
    // send the 8 bits to the shift register and set latch LOW
    updateShiftRegister(storageByte);

    // bitwise shift to the left by 1 bit
    //    the MSB will disappear and a 0 will be shifted in for the LSB
    //  ex. 10000001 to 00000010
    storageByte = storageByte << 1;

    // wait before moving on to the next LED to enhance the animation
    delay(delayTime);   
  }

  // create the effect of having the light travel in the opposite direction
  for (int i = 0; i < NUM_LEDS-1; i++)
  {
    // send the 8 bits to the shift register and set latch LOW
    updateShiftRegister(storageByte);

    // bitwise shift to the right by 1 bit
    //    the LSB will disappear and a 0 will be shifted in for the MSB
    //     i.e. 10000000 to 01000000
    storageByte = storageByte >> 1;

    // wait before moving on to the next LED to enhance the animation
    delay(delayTime);   
  }
}
```

### What to Expect

<!-- // explain that the animation will be Knight Rider Kitt style: maybe throw in a gif for nostalgia
//  - it will run all the way left and then all the way right over and over again -->
The eight LEDs will light up like KITT from Knight Rider. The first LEDs will turn on, then the next will turn on and the previous one will turn off. This will repeat for all the LEDs in a loop from left to right and then from right to left. Only one LED should be lit up at a time.

<!-- // DONE: GIF of experiment -->
It should look a little like this:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/j6YaJ_SOlA8" frameborder="0" allowfullscreen></iframe>

See, just like KITT:

<!-- // DONE: GIF of KITT -->
![Knight Industries Two Thousand](https://media.giphy.com/media/Bo2WsocASVBm0/giphy.gif)

### A Closer Look at the Code

We are only using three Arduino Dock pins to control eight LEDs by taking advantage of the shift register. Lets begin by declaring the three pin variables (`latchPin`, `clockPin` and `dataPin`) and initializing the three pins as output in `setup()`.

Each time we want to light up a different LED, we **update the shift register** to send the shift register new signals for each LED.

#### Updating the Shift Register

We control the shift register using a single function `updateShiftRegister`. The first thing it does is to set the latch pin low using a call to `digitalWrite()`:

```c
digitalWrite(latchPin, LOW);
```

Then we use a function that's included in the default Arduino libraries, `shiftOut()`, to send the byte:

```c
shiftOut(dataPin, clockPin, LSBFIRST, storageByte);
```

This function does the following actions:

1. Sets the SER pin to either HIGH or LOW according to the bit of the byte you want to send
1. Sets the clock pin HIGH, then LOW to load the SER bit into the shift register
1. Repeats the above two steps until all bits in the byte have been sent

The function takes an argument, `bitOrder`, which determines whether it sends the right-most (least significant) bit, or the left-most (most significant) bit first. Here we've decided to send it least significant bit first (`LSBFIRST`) so that our wiring order can match the order of the shift register's outputs.

Once the byte has been sent, we set the latch pin HIGH to trigger the clock that updates the shift register's outputs. This is done with another call to `digitalWrite()`:

```c
digitalWrite(latchPin, HIGH);
```

You'll notice we left in a slight delay before every update. This is because if we let it run as fast the CPU can go,it will be too fast for us to see. Instead, the lights will appear as if they were all on at the same time. The shift register can accurately update at 100MHz - much faster than our eyes can perceive! In order to actually see the effect, we slow it down by adding the delay.