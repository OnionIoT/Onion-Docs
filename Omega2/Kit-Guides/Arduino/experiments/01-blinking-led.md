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

Last thing before we build - getting to know the Arduino Dock. The double-row headers beside the Omega and the three male pins near the OMEGA_RESET are pins connected to the **Omega**. The rest of the headers are connected to the **ATmega** Micro-Controller and have the same layout as that of an Arduino UNO. We will be using the ATmega pins mostly throughout these tutorials, with the Omega used to flash the chip and connect to the internet!


### Building the Circuit

Now that we have an idea of what we're going to accomplish, let's get doing!

Here's a diagram of the completed circuit for easy reference:

<!-- // DONE: CIRCUIT DIAGRAM -->
![Circuit diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/diagrams/01-circuit-diagram.png)

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* 2x Jumper wires (M-M)
* 1x 200Ω Resistor
* 1x LED color of your choice!

#### Hooking up the Components

To hook up the circuit, we need to connect the LED to a GPIO, make sure the resistor is placed appropriately, close the circuit, and we're done! Follow the steps below:

1. Plug in the LED into the breadboard, make sure you plug the anode and cathode into different rows and that you know which is plugged where.
1. Now connect one end of a 200Ω resistor to the the cathode row, and the other end to an empty row nreaby.
1. Grab a jumper and connect one end to the row with just the resistor in it, the other end goes to a Ground (`GND`) pin on the Arduino Dock.
1. Let's choose digital pin `4` on the Arduino Dock to drive our LED, so connect a jumper wire from pin `4` to the LED's anode.

It should look something like this when it's all set up:

<!-- // DONE: IMAGE of finished circuit -->
![Blinking LED circuit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/01-assembled-circuit.jpg)



### Writing the Code

If you haven't already done so, you'll need to prepare your computer by following [our guide to flashing sketches wirelessly to the Arduino Dock](#flash-arduino-dock-wirelessly).

Then fire up the Arduino IDE on your computer and write the following:

```c
// duration to keep the LED on/off in milliseconds
int blinkTime = 1000;
// We set a variable for the LED pin number as good practice -
//    we just need to change it here to change it everywhere in the program
int ledPin = 4;


// This code runs once when the program starts, and no more
void setup() {            
    pinMode(ledPin, OUTPUT);
}


// The code in here will run continuously until we turn off the Arduino Dock
void loop() {            
    // turn the LED on
    digitalWrite(ledPin, HIGH);
    // pause the program for the amount set by blinkTime
    delay(blinkTime);

    // turn the LED off
    digitalWrite(ledPin, LOW);
    // pause again
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
// duration to keep the LED on/off in milliseconds
int blinkTime = 1000;

// This code runs once when the program starts, and no more
void setup() {
    // LED on pin 4
    int ledPin = 4;
    pinMode(ledPin, OUTPUT);
}

void loop(){
    ...
}
```

Then if we were to try to use `ledPin` in `loop()`, we will get a scope error when the code is compiled. The scope of a variable defines which part of the code it can be used.
