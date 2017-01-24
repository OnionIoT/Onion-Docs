## Controlling Many LEDs

"We've blinked one LED sure, but what about a second LED?"

In this experiment, we're going to use what we learned in the first experiment and wire up a bunch of LEDs. Then we're gonna make some visual effects.

### Building the Circuit

Similar to the previously experiment, we need our breadboard and jumper wires. However, now we will use 6 LEDs along with 6 current limiting resistors. We will makes the LEDs turn on one-by-one going left to right, and then turn them off one-by-one again going left to right.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* Resistors
  * 6x 200Ω
* 6x LED color of your choice!

#### Hooking up the Components

<!-- // look to the multiple leds article in the starter kit for ideas of what needs to be covered
// make sure the physical order of the LEDs is kept when increasing the gpio number -->

1. Plug in six LEDs onto the breadboard in parallel, each across the middle channel of the breadboard.
2. Connect the six anodes of LEDs (left to right) to six digital pins (9, 8, 7, 6, 5, 4) on the Arduino Dock (near the jack barrel connector).
3. Connect cathodes of the LEDs to negative rail marked '-' on the breadboard each through a different 200Ω current limiting resistor.
4. Connect a jumper wire from the `-` negative rail on the breadboard to a ground (GND) pin on the Arduino Dock. 

### Writing the Code

<!-- // write an arduino sketch that makes the LEDs turn on one-by-one going left to right, and then turn off, again going left to right
// look to the multiple leds article in the starter kit for details -->

``` arduino
int timer = 100;           // time delay between each LED in ms
int ledPins[] = {9, 8, 7, 6, 5, 4};       // an array of GPIO numbers with LED attached
int pinCount = 6;           // number of GPIOs used

void setup() {      // codes to be ran once
  // loop for initializing the GPIOs
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
  }
}

void loop() {     // codes to be ran continously
  // loop for turn on GPIOs one-by-one going left to right
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);
  }

  // loop for turn off GPIOs one-by-one going left to right 
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], LOW);
    delay(timer);
  }
}
```

#### What to Expect

Your line-up of LEDs will be essentially chasing it's tail: the left-most LED will turn on, and then the next one, and the next and so on. When all of them turn on, the left-most one will turn off, and the rest will follow suit.

// TODO: GIF: Showing this experiment with the LEDs lighting up one after another and then turning off one after another

#### A Closer Look at the Code

// talk about the topics we introduced here
In this code, we introduced some new concepts: arrays and "for" loops. Let's take a look.

##### Arrays

<!-- // talk about arrays, how we use an array to hold the gpio numbers in order -->

The second line the code, we defined the ledPins[] variable, which is new to us: it's creating an array. An array variable is a list of variables, with the ability to access each individual variable. A single variable in an array is referred to as an element. The ledPins array is meant to hold the GPIO pin numbers that control our LEDs. So this array will hold a bunch of integers, and we're **populating** the array as soon as we declare it.

An important thing to remember is that the the **first** element is element **0** and second element is element 1, and so on. The last element is numbered one less than the length of the array.

In addition, notice the square brackets [] of the array variable ledPins[], it will have different use for when declaring the array and when actually using the array. When declaring the array, we can specify the length of the array; however, the length will automatically be set if no number is specified. When using the array, we can use the square brackets to specify which element of the array we wil be using. For example, ledPin[0] will call the first element of the array, which is 9.

Arrays are a very common data structure used in programming and you'll soon see why.

##### For Loop

// talk about how we use the for loop to make sure we cycle through all of our leds
Loops are incredibly common in literally every type and form of programming. We already saw an example of it in the previous tutorial where we talked about the loop() function. However, we can create our own loop within the loop() function so that we can specify the conditions for our loop. For our example, we want have three loops: one for setting all pins as output pins, one for turn on all the LEDs and one to turn off all the LEDs. For each loop, we want to perform an action at the current pin and increment the pin number by one, and repeat for all the pins. The type of loop we're using here is called a 'for' loop. It fits very well with going through an array. We will use the 'for' to go through all elements (pins) of the array and light up the LED at each pin.

The 'for' loops has three parts in the header brackets () separated by semi-colons:

```
for (int thisPin = 0; thisPin < pinCount; thisPin++) {
```

The first part declares a counter variable indicating the number for the current iteration. We initalize it as 0 to fit the array element number.

The second part specifies a condition, which if became false, will end the loop. For our case, we want to continue the loop until the loop counter is at the last element of the array. We use a variable called pinCount to specify the length of the array which we manually set as 6 at the beginning. Instead of pinCount variable, we can also use sizeof(ledPins) to the same effect. The build-in Arduino function sizeof(), if used with an array, will give you the total number of elements in it. 

The third part indicates whether the loop counter increments or decrements after each iteration and by how much does it increment or decrement. For our example, we want to increment our counter by 1 as to go through all the elements of the array once.

Since we have two separate loops, the first loop will go through all its iterations before the second loop start to run through its iterations. Notice how our first and second for loop are exactly the same except that each iteration of the first loop will turn the current LED on and each iteration of the second loop will turn the current LED off.

If you're wondering why we make the program sleep for a second during each loop iteration, it's because computers execute program code **really** fast. Try increasing, decreasing, or getting rid of the sleep instruction all-together and rerunning the program. See what happens with our LED.
