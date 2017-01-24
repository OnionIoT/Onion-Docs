## Using a Buzzer

// description of what this experiment will accomplish and what we'll learn
In this tutorial, we will use a push button and a buzzer. If the push button is pressed the buzzer will buzz until the button is released. We learn to do this two ways: polling the input and using a interrupt.

### The Buzzer Element
// should be its own markdown file
// description of the buzzer: we apply current, it buzzes, have some photos

A buzzer can be describedd as audio signalling device. They have two pin; if we connect the positive (marked with +) end to power and the other end (negative) to the ground through a current limiting resistor, it will make a buzz sound. The buzzer which is included in our kit is electromagnetic. It uses electromagetism to generate repetitive mechancial motion. This mechanical vibration is what makes the buzz sound.

// TODO: Image of a buzzer

If we connect the positive end of the buzzer to a pin on our Arduino Dock, we can control its buzzing!

### Building the Circuit

// build a circuit with a push button input and a buzzer
For this experiment, we will be using a push button again for the input and a buzzer for output. Pressing the button will make the buzzer buzz. For the circuit we will need a buzzer, an 100Ω current limiting resistor, and a push button with its debounce circuit setup on a breadboard.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* Resistors
    * 1x 100Ω
    * 1x 5.1kΩ
    * 1x 51kΩ
* 1x 100nF Capacitor
* 1x Tactile button
* 1x Buzzer

#### Hooking up the Components

// in depth wiring details on building the circuit
// should be pretty straight-forward for the buzzer, look it up online

// reuse the push button instructions from the push button article
// PIN 9 <-> 100 ohm resistor <-> buzzer <-> GND
// PIN 2 <-> push button debounce circuit

1. Connect the negative end of the buzzer (the pin WITHOUT a plus sign) to ground (GND).
1. Connect the positive end (+) of the buzzer to the pin 9 through an 100 ohm current limiting resistor.
1. Connect the push button with debounce ciruit to pin 2: 
    * Set up the push button with debounce circuit similar to tutorial 4, don't connect to Arduino Dock yet. 
    * Connect the point in the debounce circuit between the 5kohm resistor and the capacitor to pin 2 of the Arduino Dock.
    * Connect positive (+) power rail to 5V and negative (-) power rail to ground (GND) on the Arduino Dock. 

### Writing the Code

// in the loop function, read the input value of the push button. if the button is pressed, activate the buzzer, when it is released, stop buzzing

``` arduino
int buzzerPin = 9;      // the pin number connect to the buzzer            
int pollingPin = 2;     // the pin number connected to the push button

void setup() {
   // initialize the buzzer pin as output
   pinMode(buzzerPin, OUTPUT);

   // initialize the polling pin as input
   pinMode(pollingPin, INPUT);
}

void loop() {
   int state = digitalRead(pollingPin);   // read the state of the push button
   digitalWrite(buzzerPin, !state);    // ring the buzzer (buzzer HIGH) when the button is pressed (button LOW) 
                                         // not buzz (buzzer LOW) when the button is released (button HIGH)
                                       // buzzer state is opposite of the button state
   delay(100); 
}
```

#### What to Expect

// explanation that pressing the button will make the buzzer sound
When the button is pressed, the buzzer will buzz until the button is released.

#### A Closer Look at the Code

// we'll be looking at the difference between polling and interrupt based input
We will approach the simple task of pressing button to make the buzzer buzz in two different ways. The first method is to poll the push button input  and the second is to use an interrupt. Check out tutorial 3 (polling) and 4 (interrupt) if you haven't already. We'll be looking at the difference between polling and interrupt based input, starting with above code (polling).

##### Polling a value

// talk about polling and how we continuously read the input value coming from the push button and then act on it
// make a note about how this is expensive/wasteful for the microcontroller since you can't do anything else during the polling

In our first method, we poll the input of the push button by setting an ATmega pin as input. Remember from the previous tutorial that the push button input is inverted; therefore, we continously read the state of the input and continously write the opposite state (!state) of the input to the buzzer pin. This is demanding and wasteful for the microcontroller since you can't do anything else during the polling. In addition, you should add a delay in the loop() to avoid stressing the microcontroller too much. This delay will make your program less responsive and if the delay is too long, a short button press might actually be missed!


##### Interrupt Alternative

// an alternative to polling is interrupt-based inputs
// to implement the same functionality as we have above, we'll need to set an action - the interrupt - that will trigger a response - the interrupt service routine.
// in our case, the interrupt action will be a change in the signal coming from the push button (both rising and falling edges), and we will write a function that we will register as the interrupt service routine, ie it will run when the interrupt is triggered - nothing of interest happens in the loop() function

An alternative to polling is interrupt-based inputs. In this approach, instead of continously reading the button input state and writing the buzzer output state, we only write the output buzzer state when there's a change in the button input state (either press or release). This is a lot more efficient as we demonstrated by performing an extra action: blinking the LED.

// new code:
// have an interrupt routine programmed to the button input, when an edge is detected, flip the value that controls the buzzer and write it to the output connected to the buzzer
// have an led blinking in the loop() function

``` arduino
int buzzerPin = 9;      // the pin number connect to the buzzer            
int interruptPin = 2;     // the pin number connected to the push button interrupt
int LEDPin = 13;        // the pin number connected to an LED, 13 is the blue LED on board
volatile int state = LOW;   // the state of the buzzer - LOW for not buzzing

void setup() {
  // initialize the buzzer pin as output
  pinMode(buzzerPin, OUTPUT);

  // initialize the LED pin as output
  pinMode(LEDPin, OUTPUT);
  
  // initialize the interrupt pin, calling the changeState function every time there is button press or release
  attachInterrupt(digitalPinToInterrupt(interruptPin), changeState, CHANGE);
}

void loop() {
  // blinking LED regardless of the buzzer
  digitalWrite(LEDPin, HIGH);   
  delay(1000);             
  digitalWrite(LEDPin, LOW);    
  delay(1000);              
}

// start at the not buzzing state, change to buzzing everytime the button is pressed and not buzzing when released
void changeState() {
  state = !state;
  digitalWrite(buzzerPin, state);
}
```

#### What to Expect

// highlight that the loop function is able to do its thing - keep the LED blinking steadily AND take care of the button input
When the button is pressed, the buzzer will buzz until the button is released. However, this time the blue LED on the Arduino Dock will be able to blink steadily.


#### A Closer Look at the Code

In this code, we initalize the interrupt by the following line:

```
attachInterrupt(digitalPinToInterrupt(interruptPin), changeState, CHANGE);
```

This will attach the build-in Arduino interrupt to an Interrup pin (2 or 3). It will call on the interrupt service routine (ISR) function changeState() whenever there is a CHANGE in the push button input. The keyword CHANGE, as descripted in tutorial 4 represents either FALLING edge (HIGH to LOW) or RISING edge (LOW to HIGH). This means if there the button is pressed or released, the changeState() function will be called. The task of the ISR changeState() is to simply write the opposite state of the push button to the buzzer. Notice we use the keyword "volatile" before int when declaring the "state" variable in line 4. Although the variable "state" is global and can be used in the ISR, to make sure the variable is updated correctly between the main program and the ISR, we declare them as volatile.

In addition, we added the standard LED blinking code to our loop() similar to tutorial 1. However, now we use pin 13 which will blink the blue LED on the Arduino Dock.