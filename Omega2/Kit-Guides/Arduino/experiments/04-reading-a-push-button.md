## Reading a Push Button

// description of what this experiment will accomplish and what we'll learn

// TODO: include push button shared article

// TODO: include debouncing switches shared article

### Interrupts

// description of what an interrupt is in the context of computer hardware:
//  - trigger for an action
//  - requires an interrupt service routine (ISR)

### Building the Circuit

// push button connected as input
// 5-8 leds connected

For this experiment we will be using the same components from the multiple LEDs tutorial (6 LEDs, 6 200 ohm resistors, breadboard and jumper wires). In addition, we will connect a push-button along with its debounce ciruit to a ATmega pin which is capable of using external interrupts (only pin 2 or 3 for ATmega328). The push button will be used as input (either pressed or not pressed) and the LEDs will show the desired state of the output pins.

<!-- Push Button -->
```{r child = '../../shared/switches-push-button.md'}
```

<!-- Debouncing a Push Button -->
```{r child = '../../shared/switches-debouncing.md'}
```

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* Resistors
    * 6x 200Ω
    * 1x 5.1kΩ
    * 1x 51kΩ
* 1x 100nF Capacitor
* 6x LED color of your choice! 
* 1x Tactile button

#### Hooking up the Components

//  * reiterate on the LED circuit, say we can repeat it
//  * wiring of a push-button
//    * needs to be wired to atmega gpio 2 or 3 so we can use it as an interrupt trigger

1. Connect the LEDS and resistors the same way as in the multiple LED tutorial.
    1. Plug in six LEDs onto the breadboard in parallel, each across the middle channel of the breadboard.
    2. Connect the six anodes of LEDs (left to right) to six digital pins (9, 8, 7, 6, 5, 4) on the Arduino Dock (near the jack barrel connector).
    3. Connect cathodes of the LEDs to ground (GND) each through a different 200Ω current limiting resistor.
2. Plug the push button onto the breadboard and setup its debounce circuit. 
3. Connect the 5V and ground of the debounce circuit.
4. Connect the point in the debounce circuit between the 5kΩ resistor and the capacitor to pin 2 of the Arduino Dock using a jumper wire.

### Writing the Code

// desired action:
//  * when the button is pressed an led turns on
//  * for each additional button press, another led will turn on
//  * when all leds are on and the button is pressed, turn all of the leds off

// find a clever implementation for this, maybe for each button press shift in a 1 to a uint variable, when it reaches the max number of leds, have it reset to 0 - this part should be done in the ISR
// each led is controlled by a specific bit in the uint variable, use bit-wise operations to figure it out - this part will happen in the loop function

// implementation:
//  * write a function to implement the above
//  * register that function as an interrupt service routine for the push button connected gpio

``` arduino
int interruptPin = 2;       // the pin number connected to the push button interrupt
int ledPins[] = {9, 8, 7, 6, 5, 4};       // an array of GPIO numbers with LED attached
int pinCount = 6;           // number of GPIOs used
int currentLED = 0;         // the current LED being light up in from 0 to pinCount-1

void setup() {
  // initialize the interrupt pin and set it to call setLED function only when the button is pressed (FALLING edge trigger)
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), setLED, FALLING);
  
  // loop for initializing the LED GPIOs as output
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
  }
}

void loop() {
    // stay idle until the interrupt activates
}

void setLED() {
  // if the last LED is already turned on, turn off all the LEDs and exit the function
  if (currentLED == pinCount){
      currentLED = 0;
     // loop for turn off GPIOs one-by-one going left to right 
     for (int thisPin = 0; thisPin < pinCount; thisPin++) {
         digitalWrite(ledPins[thisPin], LOW);
     }
     return;
  }

  // turn on the current LED and increment the counter to the next LED
  digitalWrite(ledPins[currentLED], HIGH);
  currentLED ++;
}
```

#### What to Expect

// explanation of how the button presses interact with the leds

#### A Closer Look at the Code

// talk about something interesting in the code

##### Interrupt implementation

// talk about what we accomplished with the interrupts: attaching a service routine for a particular interrupts

##### Bit-wise operations

// introduce logical and's and or's
// provide a link to an in-depth reference
