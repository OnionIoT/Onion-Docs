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

## Building the Circuit

Before we start building our experiment, let's first go over some of the building blocks when it comes to experimenting with electronics.

<!-- Jumper wires -->
```{r child = '../../shared/jumper-wires.md'}
```

<!-- Breadboard -->
```{r child = '../../shared/breadboard.md'}
```

### Hooking up the Components

Ok, here we go, let's put together our circuit. We're going to be connecting an LED's anode to a GPIO on the Arduino Dock, and cathode to Ground through a current limiting resistor.

## Writing the Code

First, prepare your computer by following [our guide to flashing sketches wirelessly to the Arduino Dock](#flash-arduino-dock-wirelessly).

Then fire up the Arduino IDE on your computer and paste the following:

```arduino
int ledPin = 0;             // LED on pin 0
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

### What to Expect

// flashing wirelessly using the IDE

### A Closer Look at the Code

// highlight something interesting about the code

#### Setting GPIOs to Output

// go through the setup commands we used to use a gpio as an output

#### Variable Scope

// talk about how we defined the LED gpio globally, and can therefore use it everywhere in the program
// give an example of a local variable
