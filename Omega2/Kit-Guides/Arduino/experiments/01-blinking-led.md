---
title: Blinking an LED
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 1
---

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
* 1x 200Ω resistor
* 1x LED color of your choice!

#### Hooking up the Components

1. Plug in the LED into the breadboard, make sure you plug the anode and cathode into different rows and that you know which is plugged where.
2. Connect the anode of the LED (the longer leg) to pin 4 on the Arduino Dock.
3. Connect the cathode of the LED (the shorter leg) to one end of the resistor and the other end of the resistor to ground (GND).

### Writing the Code

First, prepare your computer by following [our guide to flashing sketches wirelessly to the Arduino Dock](#flash-arduino-dock-wirelessly).

Then fire up the Arduino IDE on your computer and paste the following:

```arduino
int ledPin = 4;             // LED on pin 0
int blinkTime = 1000;       // duration to keep the LED on/off

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

// write an arduino sketch to blink an LED

#### What to Expect

// flashing wirelessly using the IDE

#### A Closer Look at the Code

// highlight something interesting about the code

##### Setting GPIOs to Output

// go through the setup commands we used to use a gpio as an output

##### Variable Scope

// talk about how we defined the LED gpio globally, and can therefore use it everywhere in the program
// give an example of a local variable
