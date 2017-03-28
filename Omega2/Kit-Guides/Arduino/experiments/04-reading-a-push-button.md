## Reading a Push Button {#arduino-kit-reading-a-push-button}

<!-- // description of what this experiment will accomplish and what we'll learn -->

So far, our programs have been looping continuously without stopping. In this tutorial, we get it to stop and listen for once! We'll be writing code that will patiently listen for an event, and perform an action only when it happens. We will still be using physical input to control our software, however this time instead of a trimpot we will be using a push button. Along the way, we're also going to learn about bitwise operations.

<!-- Push Button -->
```{r child = '../../shared/switches-push-button.md'}
```

<!-- Debouncing a Push Button -->
```{r child = '../../shared/switches-debouncing.md'}
```


### Interrupts

<!-- // description of what an interrupt is in the context of computer hardware:
//  - trigger for an action
//  - requires an interrupt service routine (ISR) -->

An interrupt is a signal sent to a microprocessor or microcontroller through hardware or software that is an immediate trigger for a defined action. After the microprocessor has received the interrupt signal, it will stop what it is currently doing and will execute a function called the interrupt service routine (ISR). Once the ISR completes, the program will go back to executing what it was doing before the interrupt was received. When an interrupt is defined, both the trigger and the ISR need to be defined. For the interrupt trigger, first the source must be selected (in this case selection of the hardware pin to observe), and then the action to actually fire the interrupt. The possible trigger actions are:

* Rising - a change from logical low to logical high
* Falling - a change from logical high to logical low
* Both - any change in the signal

This is a powerful tool since we can use interrupts in our programs to perform an action only when a certain trigger is detected (like a button being pressed), while allowing the rest of the program to behave normally.


### Building the Circuit

For this experiment we will start with the circuit from the [multiple LEDs tutorial](#arduino-kit-multiple-leds) and add a push-button along with it's debouncing circuit. The push-button will be connected to a ATmega pin which is capable of triggering external interrupts (only pin 2 or 3 for ATmega328). The push button will be used as input (either pressed or not pressed) and the LEDs will animate the the button presses

<!-- DONE: missing circuit diagram -->

![Debouncing circuit for the push button](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/diagrams/04-circuit-diagram.png)


#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* 10x Jumper wires (M-M)
* Resistors
    * 6x 200Ω
    * 1x 5.1kΩ
    * 1x 51kΩ
* 1x 100nF Capacitor
* 6x LED color of your choice!
* 1x Tactile button

#### Hooking up the Components



1. First, let's setup the debouncing circuit:
    * Connect one end of the 51kΩ resistor to one side of the switch. This can be either pin, but make sure you remember which side is which
    * Connect the other end of the 51kΩ resistor to an empty row, this will be where we connect our voltage reference.
    * Connect the end of the switch that is currently empty to the `GND` rail with a jumper; again, either pin will do.
    * Plug one end of the 5.1kΩ resistor to the same row where the switch and 51kΩ resistor are connected
    * Plug the other end of the 5.1kΩ resistor to an empty row.
    * Using the 100nF capacitor, connect the row where the 5.1kΩ resistor terminates to the `GND` rail.

<!-- // DONE: photo of button and debouncer circuit with LEDs only -->

![Debouncing circuit for the push button](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/04-debouncing-circuit.jpg)

1. Connect the LEDs and resistors the same way as in the [multiple LED tutorial](#arduino-kit-02-multiple-leds).
    * Plug in six LEDs onto the breadboard, each across the middle channel of the breadboard.
    * Connect cathodes of the LEDs to the rail on the breadboard each through a different 200Ω current limiting resistor.
1. Plug the push button onto the breadboard with the channel on the bottom of the button perpendicular to the channel on the breadboard. The circuit looks something like this:

Now let's connect the circuit to the Dock:

1. Connect the `GND` rail to a `GND` pin on the Arduino Dock.
1. Connect the six anodes of LEDs (left to right) to six digital pins (`9`, `8`, `7`, `6`, `5`, `4`) on the Arduino Dock (near the jack barrel connector).
1. From the debounce circuit, connect the row containing the 5.1kΩ resistor and the capacitor to GPIO pin `2` of the Arduino Dock.
1. Finally, use a jumper wire to connect the other end of the 51kΩ resistor to `5V` on Arduino Dock.

<!-- // DONE: photo of assembled circuit with Arduino-->
![The circuit fully assembled](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/04-assembled-circuit.jpg)

### Writing the Code

<!-- // DONE: Lazar to re-write this code -->

The program for this experiment won't loop at all! Instead it'll setup a interrupt, and perform actions only when the interrupt is activated.

Copy the code below and flash it to give it a spin.

``` c
#define NUM_LEDS		6

// the pin number connected to the push button interrupt
int interruptPin = 2;
// an array of pins with LEDs attached
int ledPins[] = {9, 8, 7, 6, 5, 4};
// pin connected to the Arduino Dock LED
int statusLedPin = 13;
// a byte representing which LEDs are on
//	we're only using 6 of the 8 bits since we've connected 6 LEDs
volatile byte ledValues = B00000000;

// This code runs once when the program starts, and no more
void setup() {
  // initialize serial communication with the Omega
  Serial.begin(9600);

  // initialize the interrupt pin and set it to call setLED function only when the button is released (RISING edge trigger)
  attachInterrupt(digitalPinToInterrupt(interruptPin), setLedChain, RISING);

  // loop for initializing the LED GPIOs as output
  for (int thisPin = 0; thisPin < NUM_LEDS; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
  }

  // initialize the Arduino Dock LED GPIO to output
  pinMode(statusLedPin, OUTPUT);
}

// The code in here will run continuously until we turn off the Arduino Dock
void loop() {
	// blink the status LED
	digitalWrite(statusLedPin, HIGH);
	delay(1000);
	digitalWrite(statusLedPin, LOW);
	delay(1000);
}

// ISR for a button press
void setLedChain() {
	// decide whether enabling or disabling LEDs
	if ((ledValues >> (NUM_LEDS-1) ) & B00000001 == B00000001) {
		// the last LED is on, start disabling the LEDs
		//	shift all of the existing bits by 1, the least significant bit will be 0 (disabling the LED)
		ledValues = ledValues << 1;
	}
	else {
		// the last LED is not yet on, keep turning LEDs on
		//	shift all of the existing bits by 1, set the least significant bit to 1
		ledValues = (ledValues << 1) | B00000001;
	}

	// set all of the LEDs according to the ledValues byte
	for (int index = 0; index < NUM_LEDS; index++) {
		int value = (ledValues >> index) & B00000001;
		digitalWrite(ledPins[index], value);
	}

}
```

You know the drill, save it to `SKA04-readingPushButton.ino`, then get ready to press a button!

### What to Expect

When the button is pressed, the left most LED should turn on. For each additional button press, another led will turn on, going from left to right. When all leds are on and the button is pressed, the LEDs will turn off one by one in the same order. All the while, the LED connected to GPIO13 will continue blinking steadily on and off.

<!-- // TODO: gif -->


<!-- // DONE: screenshot of the cat command showing the bitwise operations - commented out no longer relevant, file is still on server -->
<!-- ![Serial output from the ATmega](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/04-serial-output.png) -->

### A Closer Look at the Code

**COMING SOON!**

<!---
// TODO: needs to be updated to match the re-written code

In this code, we implemented an more efficient method of read inputs called interrupt, where as in the previous tutorial we used the method of polling. Notice we use two `for` loops: one for setting all LED pins to output and another to turn all the LEDs off without any delay.

#### Interrupt implementation

Interrupts are are a more effecient way of reading input. Instead of continously reading the input (polling), we only read it when there's a change or when it is at a certain state (`HIGH` or `LOW`).  A `CHANGE` could be defined as the `RISING` (`LOW` to `HIGH`) and/or `FALLING` (`HIGH` to `LOW`) edge of the input signal. Interrupts reduces the need of extra computational process and saves a lot time.

In the first line of the `setup()` we attach a interupt to a pin using the built-in Arduino function `attachInterrupt()`. This function takes in three parameters. The first parameter is the pin number of a digital pin coverted to an interrupt pin using another built-in function digitalPinToInterrupt(pin).

The second parameter is the interrupt service routine (ISR). The ISR is a special kind of function which is called when the interrupt triggers. In our example, it's the `setLED()` function which turns on LED or turn all LEDs off if all the LEDs are lit. An ISR function have a few limitations. It must be short and fast, which means time delay should not be used. In addition, ISR does not have parameters and should not return any output value.

The last parameter of `attachInterrupt()` function is the condition in which the interrupt triggers, either HIGH, LOW, RISING, FALLING or CHANGE as described earlier in this section. For our case, we use FALLING since the debounce circuit inverts the state of the button: HIGH when not press and LOW when pressed. So whenever the button is pressed, the ISR function `setLED()` will be called. The release of the button would fit as the RISING condition and does not matter in our case.

#### Bitwise operations

In this code we also added a byte variable `byteOfLEDs` to demonstrate how bitwise operation works. For in-depth reference, check out this [Bit Math](http://playground.arduino.cc/Code/BitMath) in the Arduino Playground.

We use the following bitwise operation on byteOfLEDs to imitate actual LEDs turning on `1` and off `0`:

```
byteOfLEDs = (byteOfLEDs | (byteOfLEDs >> 1)) & B00111111;
```

Since we have six LEDs, we initalize set the seventh bit of our `byteOfLEDs` to `1` to represent all LEDs off `B01000000`. Everytime the button is pressed we need to represent the next LED turning on by using the bitwise **SHIFT** to move the `1` bit to the right `byteOfLEDs >> 1`. For example, `B01000000 >> 1` will become `B00100000`.

However, our previous LED is still on; therefore, we need to do "add" the shifted bit to the previous bit. For this operation we use the bitwise **OR** `|` which is similar to bitwise addition. For example, `B01000000 | B00100000` will become `B01100000`.

Lastly, we need to "filter out" the seventh bit because it is only used for coding purpose and does not actually represent any LEDs. For this, we use the bitwise **AND** `&` operation. For example, `B01100000 & B00111111` will result in only `B00100000`.

If the button is pressed again after the LEDs are on,

```
if (byteOfLEDs == B00111111)
```

We use a `for` loop to set all the LEDs off and set the `byteOfLEDs` back to `B01000000`, representing all LEDs are off.-->
