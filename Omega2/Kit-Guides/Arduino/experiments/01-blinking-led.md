## Blinking an LED {#arduino-kit-blinking-led}

In our very first experiment, we will turn an LED on and off. This is the hardware equivalent of the 'Hello World' program. This first experiment will start small but it will be a solid foundation for the rest of the experiments.

<!-- // TODO: IMAGE insert a gif of what this experiment will accomplish, need to get people excited! -->

Remember, when inventing and building new things, try to break the work down into bite sized chunks, that way you'll see progress much sooner and it will motivate you to keep going!

<!-- LEDs -->
```{r child = '../../shared/led.md'}
```

### How to Build Circuits

Before we start building our experiment, let's first go over some of the building blocks when it comes to experimenting with electronics.

<!-- Jumper wires -->
```{r child = '../../shared/jumper-wires.md'}
```

<!-- Breadboard -->
```{r child = '../../shared/breadboard.md'}
```

Last thing before we build - getting to know the Arduino Dock. The double-row headers beside the Omega and the three male pins near the OMEGA_RESET are pins connected to the **Omega**. The rest of the headers are connected to the **ATmega** and have the same layout as that of an Arduino UNO. We will be using the ATmega pins mostly throughout these tutorials, with the Omega used to flash the chip and connect to the internet!


### Building the Circuit

Now that we have an idea of what we're going to accomplish, let's get doing!

Here's a diagram of the completed circuit for easy reference:

<!-- // TODO: CIRCUIT DIAGRAM -->

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* 2x Jumper wires (M-M)
* 1x 200Ω Resistor
* 1x LED color of your choice!

#### Hooking up the Components

The circuit is super straight-forward, just need to connect the LED to a GPIO, make sure the resistor is placed appropriately, close the circuit, and we're done!

1. Plug in the LED into the breadboard, make sure you plug the anode and cathode into different rows and that you know which is plugged where - if you don't, it won't turn on!
2. Connect the anode of the LED (the longer leg) to pin 4 on the Arduino Dock.
3. Connect the cathode of the LED (the shorter leg) to one end of the resistor and the other end of the resistor to ground (GND).

It should look something like this when it's all set up:

<!-- // TODO: IMAGE of finished circuit -->

### Writing the Code

If you haven't already done so, you'll need to prepare your computer by following [our guide to flashing sketches wirelessly to the Arduino Dock](#flash-arduino-dock-wirelessly).

Then fire up the Arduino IDE on your computer and write the following:

```c
int blinkTime = 1000;  // duration to keep the LED on/off in milliseconds
int ledPin = 4;        // We set a variable for the LED pin number as good
                       // practice -
                       // we just need to change it here to change it everywhere

// This code runs once when the program starts, and no more
void setup() {			
    pinMode(ledPin, OUTPUT);
}


// The code in here will run continuously until we turn off the Arduino
void loop() {			
    digitalWrite(ledPin, HIGH); // turn the LED on
    delay(blinkTime);           // This line pauses the program for the amount
                                // set by blinkTime

    digitalWrite(ledPin, LOW);  // turn the LED off
    delay(blinkTime);
}
```

Let's save the code below as `SKA01-blinkingLed.ino` so you can revisit it!

### What to Expect

After the ATmega Micro-Controller on your Arduino Dock has been successfully flashed, your LED should start blinking: it should turn on for a second, and then turn off for a second, repeating until you flash a new sketch on to it. If you press the `MCU_RESET` button, the program will stop and restart from the beginning.

### A Closer Look at the Code

While this is a small program, there are quite a few things going on, let's take a closer look. First let's take a look at the typical format of an Arduino Sketch. We start by defining our variables. Then we put code that need to be run once at the very beginnig of the program inside the `setup()` function. This codes\e will be the first to be ran. Lastly, we put the codes that repeats over and over again in the void `loop()` function.

For our example, we need two variables: one for the pin number the LED is attached to and other to define the duration of the blink. We want to only set the GPIO as output only once but blink the LED continuously.

#### Setting GPIOs to Output

A GPIO can be set as either an input or output pin. ATmega pins are set to input as default. Input pins are mainly used for reading the the state (`ON` and `OFF`) or voltage level from a sensor or button. Input pin are in high-impedance state, meaning a very small amount of current will be able to change its state between LOW and HIGH. For our application, we want our GPIO to supply more current so we have to set it as `OUTPUT`: `pinMode(ledPin, OUTPUT)`. However, keep in mind that input pins can also supply a very small amount of current (very dim LED).

After we set the pin to output, we will use `digitalWrite` to set the pin either `HIGH` to turn on the LED or `LOW` to turn off the LED, as seen inside the `loop()`.

#### Variable Scope

For this code, we declared our two variable (`ledPin` and `blinkTime`) at the beginning of the code outside of any function brackets `{}`. This means the variable is globally defined and can be used anywhere in the sketch. However, if we define a variable inside a function, we will only be able to use it inside that function. This is a concept known as **scope**.

For example let's say we defined `ledPin` inside the `setup()` function like so:

```c
int blinkTime = 1000;       // duration to keep the LED on/off in ms

void setup() {			// code to be run once at the start of the program
	int ledPin = 4;             // LED on pin 4
    pinMode(ledPin, OUTPUT);
}

void loop(){
	...
}
```

Then if we were to try to use `ledPin` in `loop()`, we will get a scope error when the code is compiled. The scope of a variable defines which part of the code it can be used.
