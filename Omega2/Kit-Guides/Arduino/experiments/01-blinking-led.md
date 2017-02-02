## Blinking an LED {#blink-led-arduino-kit}

In our very first experiment, we're going to blink an LED on and off. This is the hardware development equivalent of the 'Hello World' program. This first experiment will start small but it will be a solid foundation for the rest of the experiments.

Remember, when inventing and building new things, try to break the work down into bite sized chunks, that way you'll see progress much sooner and it will motivate you to keep going!

<!-- LEDs -->
```{r child = '../../shared/led.md'}
```

### Building the Circuit

Before we start building our experiment, let's first go over some of the building blocks when it comes to experimenting with electronics.

<!-- Jumper wires -->
```{r child = '../../shared/jumper-wires.md'}
```

<!-- Breadboard -->
```{r child = '../../shared/breadboard.md'}
```

Let's also take a look at the headers on the Arduino Dock. The double-row headers beside the Omega and the three male pins near the OMEGA_RESET are pins connected to the Omega. The rest of the headers are connected to the ATmega and have the same layout as that of an Arduino UNO. We will be using the ATmega pins mostly throughout these tutorials. 

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* Resistors
  * 1x 200Ω
* 1x LED color of your choice!

#### Hooking up the Components

1. Plug in the LED into the breadboard, make sure you plug the anode and cathode into different rows and that you know which is plugged where.
2. Connect the anode of the LED (the longer leg) to pin 4 on the Arduino Dock.
3. Connect the cathode of the LED (the shorter leg) to one end of the resistor and the other end of the resistor to ground (GND).

<!-- // TODO: photo -->

### Writing the Code

First, prepare your computer by following [our guide to flashing sketches wirelessly to the Arduino Dock](#flash-arduino-dock-wirelessly).

Then fire up the Arduino IDE on your computer and paste the following:

```arduino
int ledPin = 4;             // LED on pin 4
int blinkTime = 1000;       // duration to keep the LED on/off in ms

void setup() {			// codes to be ran once
    pinMode(ledPin, OUTPUT);
}

void loop() {			// codes to be ran continously
    digitalWrite(ledPin, HIGH);
    delay(blinkTime);
    digitalWrite(ledPin, LOW);
    delay(blinkTime);
}
```

#### What to Expect

After your ATmega has been succesfully flashed, your LED should start blinking: it should turn on for a second, and then turn off for a second, repeating until you flash a new sketch on to it. If you press the `MCU_RESET` button, the program will stop and restart from the beginning.

#### A Closer Look at the Code

While this is a small program, there are quite a few things going on, let's take a closer look. First let's take a look at the typical format of an Arduino Sketch. We start by defining our variables. Then we put codes that need to be ran once inside the `setup()` function. These codes will be the first to be ran. Lastly, we put the codes that repeats over and over again in the void `loop()` function.

For our example, we need two variables: one for the pin number the LED is attached to and other to define the duration of the blink. We want to only set the GPIO as output only once but blink the LED continously.

##### Setting GPIOs to Output

A GPIO can be set as either an input or output pin. ATmega pins are set to input as default. Input pins are mainly used for reading the the state (`ON` and `OFF`) or votlage level from a sensor or button. Input pin are in high-impedance state, meaning a very small amount of current will be able to change its state between LOW and HIGH. For our application, we want our GPIO to supply more current so we have to set it as `OUTPUT`: `pinMode(ledPin, OUTPUT)`. However, keep in mind that input pins can also supply a very small amount of current (very dim LED).

After we set the pin to output, we will use `digitalWrite` to set the pin either `HIGH` to turn on the LED or `LOW` to turn off the LED, as seen inside the `loop()`.

##### Variable Scope

For this code, we declared our two variable (`ledPin` and `blinkTime`) at the beginning of the code, outside of any function brackets `{}`. This means the variable is globally defined and can be used anywhere in the sketch. However, if we define a variable inside a function, we will only be able to use it inside that function. This is a concept known as **scope**.

For example if we defined `ledPin` inside the `setup()` function :

```arduino
int blinkTime = 1000;       // duration to keep the LED on/off in ms

void setup() {			// codes to be ran once
	int ledPin = 4;             // LED on pin 4
    pinMode(ledPin, OUTPUT);
}

void loop(){
	...
}
```
Then if we were to try to use `ledPin` in `loop()`, we will get a scope error when the code is compiled. The scope of a variable defines which part of the code it can be used.