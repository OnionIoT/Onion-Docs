// TODO: general arduino dock: fix tenses and pluralization

## Reading a Push Button {#arduino-kit-reading-a-push-button}

<!-- // description of what this experiment will accomplish and what we'll learn -->

// TODO: try to see if this intro can be worded better

So far, our programs have been continuously running and performing actions. In this tutorial, we will tell our program to only perform an action when we need it to! This will involve writing interrupt code that listen for an event and then trigger certain code to be run when the event happens. We will again be using physical user input to control our software. However this time instead of using a trimpot as input, we will be using a push button. Along the way, we're also going to learn about bitwise operations.

<!-- Push Button -->
```{r child = '../../shared/switches-push-button.md'}
```

<!-- Debouncing a Push Button -->
```{r child = '../../shared/switches-debouncing.md'}
```

// LAZAR: bookmark

### Interrupts

<!-- // description of what an interrupt is in the context of computer hardware:
//  - trigger for an action
//  - requires an interrupt service routine (ISR) -->

We can use a interrupt to our program to only perform an action when we need it to. An interrupt is a signal send to the microprocessor through hardware or software as a immediate trigger for an action. After the microprocessor has received the interrupt signal, it will immediately call a function called the interrupt service routine (ISR).

### Building the Circuit

<!-- // push button connected as input
// 5-8 leds connected -->

For this experiment we will be using the same components from the multiple LEDs tutorial (six LEDs, six 200Ω resistors, breadboard and jumper wires). In addition, we will connect a push-button along with its debounce ciruit to a ATmega pin which is capable of using external interrupts (only pin 2 or 3 for ATmega328). The push button will be used as input (either pressed or not pressed) and the LEDs will show the desired state of the output pins.

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

<!-- //  * reiterate on the LED circuit, say we can repeat it
//  * wiring of a push-button
//    * needs to be wired to atmega gpio 2 or 3 so we can use it as an interrupt trigger -->

1. Connect the LEDS and resistors the same way as in the multiple LED tutorial.
    * Plug in six LEDs onto the breadboard in parallel, each across the middle channel of the breadboard.
    * Connect the six anodes of LEDs (left to right) to six digital pins (9, 8, 7, 6, 5, 4) on the Arduino Dock (near the jack barrel connector).
    * Connect cathodes of the LEDs to the negative (-) power rail on the breadboard each through a different 200Ω current limiting resistor.
2. Plug the push button onto the breadboard and setup its debounce circuit as show below:
    ![push-button-breadboard](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/push-button-breadboard.jpg)

    <!-- // TODO: photo of button and debouncer circuit with LEDs only-->

    * Connect one end of the switch to the 51kΩ resistor, and the other end of that resistor to 5V on Arduino Dock.
    * Connect the other end of the switch to negative (-) power rail .
    * Connect one end of the 5.1kΩ resistor to the same point where the switch and 51kΩ resistor are connected
    * Connect the other end of the 5.1kΩ resistor to one end of the 100nF capacitor.
    * Connect the other end of the capacitor to the negative (-) power rail.
3. Connect the negative (-) power rail to ground (GND).
4. Connect the point in the debounce circuit between the 5.1kΩ resistor and the capacitor to pin 2 of the Arduino Dock.

<!-- // TODO: photo of assembled circuit with Arduino-->

### Writing the Code

<!-- // desired action:
//  * when the button is pressed an led turns on
//  * for each additional button press, another led will turn on
//  * when all leds are on and the button is pressed, turn all of the leds off

// find a clever implementation for this, maybe for each button press shift in a 1 to a uint variable, when it reaches the max number of leds, have it reset to 0 - this part should be done in the ISR
// each led is controlled by a specific bit in the uint variable, use bitwise operations to figure it out - this part will happen in the loop function

// implementation:
//  * write a function to implement the above
//  * register that function as an interrupt service routine for the push button connected gpio -->

``` c++
int interruptPin = 2;       // the pin number connected to the push button interrupt
int ledPins[] = {9, 8, 7, 6, 5, 4};       // an array of GPIO numbers with LED attached
int pinCount = 6;           // number of GPIOs used
int currentLED = 0;         // the current LED being light up in from 0 to pinCount-1
byte byteOfLEDs = B01000000;    // byte of LEDs representing which LEDs are on. Since theres six LEDs, we use the seventh bit to represent all LEDs off.

void setup() {
  Serial.begin(9600);           // initialize serial communication with the Omega

  // initialize the interrupt pin and set it to call setLED function only when the button is pressed (FALLING edge trigger)
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
  // if all the six LED are turned on, turn off all the LEDs and exit the function
  if (byteOfLEDs == B00111111){
      currentLED = 0;
      byteOfLEDs = B01000000;
     // loop for turn off GPIOs one-by-one going left to right
     for (int thisPin = 0; thisPin < pinCount; thisPin++) {
         digitalWrite(ledPins[thisPin], LOW);
     }
     Serial.println(byteOfLEDs & B00111111, BIN);  // print the six least significant bits of byteOfLEDs to the Omega
     return;
  }

  // turn on the current LED and increment the counter to the next LED
  digitalWrite(ledPins[currentLED], HIGH);
  currentLED ++;

  // bit-wise operation used on byteOfLEDs to imitate actual LEDs turning on (1) and off (0)
  byteOfLEDs = (byteOfLEDs | (byteOfLEDs >> 1)) & B00111111;
  Serial.println(byteOfLEDs, BIN);   // print the byteOfLEDs to the Omega
}
```

#### What to Expect

When the button is pressed, the left most LED should turn on. For each additional button press, another led will turn on, going from left to right. When all leds are on and the button is pressed, all the LEDs will turn off at once. Additional button presses will repeat the previous actions.

<!-- // TODO: gif -->

In addition, if we use the `cat` command on our Omega like previous tutorial, we will see a bitwise representation of our actual LEDs.

// TODO: screenshot of the cat command showing the bitwise operations

#### A Closer Look at the Code

In this code, we implemented an more efficient method of read inputs called interrupt, where as in the previous tutorial we used the method of polling. Notice we use two `for` loops: one for setting all LED pins to output and another to turn all the LEDs off without any delay.

##### Interrupt implementation

Interrupts are are a more effecient way of reading input. Instead of continously reading the input (polling), we only read it when there's a change or when it is at a certain state (`HIGH` or `LOW`).  A `CHANGE` could be defined as the `RISING` (`LOW` to `HIGH`) and/or `FALLING` (`HIGH` to `LOW`) edge of the input signal. Interrupts reduces the need of extra computational process and saves a lot time.

In the first line of the `setup()` we attach a interupt to a pin using the build-in Arduino function `attachInterrupt()`. This function takes in three parameters. The first parameter is the pin number of a digital pin coverted to an interrupt pin using another build-in function digitalPinToInterrupt(pin).

The second parameter is the interrupt service routine (ISR). The ISR is a special kind of function which is called when the interrupt triggers. In our example, it's the `setLED()` function which turns on LED or turn all LEDs off if all the LEDs are lit. An ISR function have a few limitations. It must be short and fast, which means time delay should not be used. In addition, ISR does not have parameters and should not return any output value.

The last parameter of `attachInterrupt()` function is the condition in which the interrupt triggers, either HIGH, LOW, RISING, FALLING or CHANGE as described earlier in this section. For our case, we use FALLING since the debounce circuit inverts the state of the button: HIGH when not press and LOW when pressed. So whenever the button is pressed, the ISR function `setLED()` will be called. The release of the button would fit as the RISING condition and does not matter in our case.

##### Bitwise operations

In this code we also added a byte variable `byteOfLEDs` to demonstrate how bitwise operation works. For in-depth reference, visit:

[hyperlink text](http://playground.arduino.cc/Code/BitMath)

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

We use a `for` loop to set all the LEDs off and set the `byteOfLEDs` back to `B01000000`, representing all LEDs are off.
