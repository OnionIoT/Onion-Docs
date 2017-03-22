## Using a Buzzer {#arduino-kit-using-a-buzzer}

<!-- // TODO: ay-ay-ay this intro is so boring, please spice it up (hell yeah) -->

In this experiment, we'll be sounding a buzzer from a button. Think of it as a model for your doorbell! We will build a circuit with a buzzer and a button, then we'll cover two ways to get the buzzer buzzing: polling the input and using a interrupt. In the process, we'll learn about the pros and cons of polling versus interrupts. As a required secondary superpower, we'll use a switch debouncing circuit (the same one as in [experiment 04](#arduino-kit-reading-a-push-button)) to make sure our button presses come in clear.

### The Buzzer
<!-- // should be its own markdown file
// description of the buzzer: we apply current, it buzzes, have some photos -->

A buzzer can be described as audio signaling device, an alternative way to describe it is an annoying sound device. It has two pins and if we connect the positive (marked with +) end to power and the other end (negative) to the ground through a current limiting resistor, it will make a (potentially annoying) buzzing sound. The buzzer which is included in our kit is electromagnetic: it uses electromagnetism to generate repetitive mechanical motion which creates the buzzing sound.

<!-- // TODO: IMAGE of a buzzer -->

If we connect the positive end of the buzzer to a pin on our Arduino Dock, we can use software to control the buzzing!

### Building the Circuit

For this experiment, we will be using a push button again for the input and a buzzer for output. Pressing the button will make the buzzer buzz. For the circuit we will need a buzzer, an 100Ω current limiting resistor, and a push button with its debounce circuit setup on a breadboard.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* 6x Jumper wires (M-M)
* Resistors
    * 1x 100Ω
    * 1x 5.1kΩ
    * 1x 51kΩ
* 1x 100nF Capacitor
* 1x Tactile button
* 1x Buzzer

#### Hooking up the Components

<!-- // DONE: add an intro (d)-->
<!-- // TODO: IMAGE add a circuit diagram of the circuit we will be building -->

Once you have all the components ready, it's time to build!

1. First, let's set up the push button with debounce circuit similar to [tutorial 4](#arduino-kit-04-reading-a-push-button), we'll connect this to the Arduino Dock in a bit.

1. Now let's get the buzzer connected - plug the Buzzer across the channel of your breadboard.
1. Using a jumper, connect the negative end of the buzzer (the pin WITHOUT a plus sign) to the `GND` rail.
1. Plug in a 100Ω current limiting resistor across the (+) row of the buzzer and an empty row.

1. Connect the `GND` rail to a `GND` pin on the Arduino Dock.
1. Connect the point in the debounce circuit between the 5kΩ resistor and the capacitor to pin `2` of the Arduino Dock.
1. Take a jumper and use it to connect the end of 100Ω resistor and pin `9` on the Arduino Dock
1. Connect the `Vcc` (red) rail to `5V`

And you're done! For reference your circuit should look a little like this:

<!-- // TODO: IMAGE add a photo of the completed circuit -->

<!-- TODO and a blurb about 'this is more or less how your circuit should look' (d) -->

### Writing the Polling-based Code

<!-- // TODO: intro to the code, in broad strokes talk about what we hope to accomplish (d) -->

This program will continuously check an input pin to see if anything changes, and then fire the buzzer whenever it does see the appropriate change.

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

   // we want to:
   //   ring the buzzer (buzzer HIGH) when the button is pressed (button LOW)
   //   not buzz (buzzer LOW) when the button is released (button HIGH)
   // note that the buzzer state is opposite of the button state
   digitalWrite(buzzerPin, !state);

   delay(10);
}
```

### What to Expect

When the button is pressed, the buzzer will buzz until the button is released. Pretty simple right?

### A Closer Look at the Code

<!-- // TODO: link to the polling and interrupt articles (d) -->

We will approach the simple task of pressing button to make the buzzer buzz in two different ways. The first method, covered here, is constantly polling the push button input. The second method is to get the button to interrupt the program. Check out the experiments on [polling](#arduino-kit-reading-a-pot) and [interrupts](#arduino-kit-reading-a-push-button) if you want to go in a bit more detail on either of the methods. For now, let's start by examining the code above that implements polling.

#### Polling a Value

<!-- // talk about polling and how we continuously read the input value coming from the push button and then act on it
// make a note about how this is expensive/wasteful for the microcontroller since you can't do anything else during the polling -->

In the first method, we poll the input of the push button at a regular interval by setting an ATmega pin as input. Remember from the previous tutorial that the push button input is inverted; therefore, we continuously read the state of the input and continuously write the opposite state `!state` of the input to the buzzer pin.

<!-- // TODO: expand on how polling is taxing on the processor (but don't make it sound dangerous)-->

Polling has some issues with waste. The idea is to just check the input continuously until an event happens. The problem is that up until the event does happen, all that checking doesn't do anything useful! To avoid wasting CPU cycles like this, it's common practice to add a delay to the polling loop to avoid wasting CPU cycles.

Of course the downside is that this delay will make your program less responsive. Not only that, if the delay is too long, a short button press might actually be missed! In addition to the fact that we might not successfully capture all inputs, we're also locked in to just checking the state of that button - our program can't do anything else!

There must be a better way!


### Writing the Interrupt-based Code

<!-- // an alternative to polling is interrupt-based inputs
// to implement the same functionality as we have above, we'll need to set an action - the interrupt - that will trigger a response - the interrupt service routine.
// in our case, the interrupt action will be a change in the signal coming from the push button (both rising and falling edges), and we will write a function that we will register as the interrupt service routine, ie it will run when the interrupt is triggered - nothing of interest happens in the loop() function -->

An alternative to polling is using interrupt-based inputs. In this approach, we set up code so that when the button changes state, an 'interrupt' will be fired off and the appropriate change to the buzzer will be made. This is actually a much better method because there is little to no chance of missing any button presses. Even better, it allows us to do other things because the burden of checking has been lifted. To illustrate the point, we'll toss in a blinking LED that operates alongside the interrupt code.

<!-- // new code:
// have an interrupt routine programmed to the button input, when an edge is detected, flip the value that controls the buzzer and write it to the output connected to the buzzer
// have an led blinking in the loop() function -->

Without further ado, here's the code to do the same thing, but with an interrupt:

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

### What to Expect

<!-- // highlight that the loop function is able to do its thing - keep the LED blinking steadily AND take care of the button input -->
When the button is pressed, the buzzer will buzz until the button is released. However, this time the blue LED on the Arduino Dock will be able to blink steadily.


### A Closer Look at the Code

In this code, we initalize the interrupt by the following line:

```
attachInterrupt(digitalPinToInterrupt(interruptPin), changeState, CHANGE);
```

<!-- // TODO: complete the two links to previous experiments -->

This will attach the built-in Arduino interrupt to an interrupt pin (2 or 3). It will call on the interrupt service routine (ISR) function `changeState()` whenever there is a `CHANGE` in the push button input. The keyword `CHANGE`, as described in [push button experiment](#arduino-kit-reading-a-push-button), represents either `FALLING` edge (`HIGH` to `LOW`) or RISING edge (`LOW` to `HIGH`). This means if there the button is pressed or released, the `changeState()` function will be called. The task of the ISR `changeState()` is to simply write the opposite state of the push button to the buzzer. Notice we use the keyword `volatile` before `int` when declaring the `state` variable in line 4. Although the variable `state` is global and can be used in the ISR, to make sure the variable is updated correctly between the main program and the ISR, we declare them as `volatile`.


In addition, we added the standard LED blinking code to our `loop()` similar to the [blinking LED experiment](#arduio-kit-blinking-led). However, now we use pin 13 which will blink the blue LED on the Arduino Dock.

<!-- // TODO: go into a bit more detail about the volatile keyword (d) -->

>For the curious, `volatile` means a variable will be directly modified by something other than the 'main body' of the program, and should be loaded from RAM instead of a CPU register - as that is generally where the 'reference' value of a variable is stored. Interrupts don't exactly operate within the main program body, which is why we used `volatile` here to make sure the value of `state` is properly read.
