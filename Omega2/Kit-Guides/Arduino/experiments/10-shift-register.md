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


``` arduino
#define NUM_LEDS 	8

// duration to pause
int delayTime = 100;

// the pin connected to the latch pin, RCLK (pin 12 of the shift register)
//	setting the latch LOW will send the 8 bits in storage to the output pins
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
  // 	since the latch is LOW, set the 8 output pins based on the stored 8 bits and in turn light the correct LED
  shiftOut(dataPin, clockPin, LSBFIRST, storageByte);

  // set the latch pin HIGH again
  digitalWrite(latchPin, HIGH);
}

// The code in here will run continuously until we turn off the Arduino Dock
void loop()
{
  // the byte (8 bits) to be stored in the shift register
  //	initialize to 00000001, representing the first LED on
  byte storageByte = 0x01;

  // create the effect of having the light travel to the left
  for (int i = 0; i < NUM_LEDS-1; i++)
  {
	// send the 8 bits to the shift register and set latch LOW
    updateShiftRegister(storageByte);

	// bitwise shift to the left by 1 bit
	//	the MSB will disappear and a 0 will be shifted in for the LSB
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
	//	the LSB will disappear and a 0 will be shifted in for the MSB
	// 	i.e. 10000000 to 01000000
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

<!-- // TODO: GIF of experiment -->

See, just like KITT:

<!-- // DONE: GIF of KITT -->
![Knight Industries Two Thousand](https://media.giphy.com/media/Bo2WsocASVBm0/giphy.gif)

### A Closer Look at the Code

We are only using three Arduino Dock pins to control eight LEDs by taking advantage of the shift register. Lets begin by declaring the three pin variables (`latchPin`, `clockPin` and `dataPin`) and initializing the three pins as output in `setup()`.

Each time we want to light up a different LED (change the output of the Shift Register), we use the `updateShiftRegister()` function in a loop to continuously change the outputs.


#### Updating the Shift Register

First, let's take a look at what happens inside `updateShiftRegister()`. In this function, we send the 8 bits from the ATmega to the shift register:

```
shiftOut(dataPin, clockPin, LSBFIRST, storageByte);
```

The `storageByte` variable contains our data, while the others tell the function which pins is the shift register hooked up to.

Once the data is sent, we'll need to flip a switch to get the shift register to spit the data out as signals to our LEDs:

```
digitalWrite(latchPin, LOW);
```

When the latch is set to low, the stored bits in the shift register will be sent out to the output pins in parallel. We must set the latch back high again to reset the shift register and allow further input to be properly stored. This completes one update cycle for the shift register and `updateShiftRegister()` returns at this point.

<!-- // DONE: at this point, we need to make it clear that we WERE talking about the inner workings of the `updateShiftRegister` function. and that FROM NOW ON, we're talking about the operation of the loop function, and how it creates the KITT effect -->

#### Looping and Bitshifting

So how does the KITT effect happen? Through bitshifting our input byte, then sending it out through `updateShiftRegister()`. Doing this repeatedly results in an effect that looks like the light is moving back and forth!

Before any looping is done, we initialize `storageByte` to `0x01`, or `00000001` in binary. During the loop function, there's two `for` loops that will shift the single `1` back and forth, sending the result to the LEDs through the shift register. That is how we get our light to move just like KITT.

The first `for` loop shifts the `1` bit from the least significant bit `00000001`  to the most significant bit `10000000`. We shift one bit at a time for seven times, each time using the bitwise shift left operation:

```
storageByte = storageByte << 1;
```

the second `for` loop shifts the `1` bit back to the least significant bit `00000001` one bit at a time for seven times with:

```
storageByte = storageByte >> 1;
```

You'll notice we left in a slight delay before every update. This is because if we let it run as fast as possible, we won't get to see the light move, instead the speed of the CPU will make it appear as though all the lights are on at the same time. The Shift register can accurately update at 100MHz - much faster than we can percieve! So in order to actually see the effect, we slow it down by adding the delay.

<!-- // DONE: expand on this sentence, this was lazy -->
