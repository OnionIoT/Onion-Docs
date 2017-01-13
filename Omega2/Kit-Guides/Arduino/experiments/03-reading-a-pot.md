
## Reading an Potentiometer

// this experiment will use a potentiometer to control Brightness of an LED


### Potentiometer

// description that a pot is essentially a variable resistor, we can tell

### Dimming an LED

// leds are brighter the more voltage is applied, dimmer the less we apply

// the microcontroller is able to output an analog signal, meaning we can control how much voltage is going to the led, directly controlling its brightness
// add a note saying that the analog signal is actually pwm, but don't go into heavy detail

### Building the Circuit

// will need a pull-up resistor connected to the trim-pot, and an arduino dock analog input sampling the voltage

// an LED connected to one of the (pwm) outputs

For this experiment, we will use the knob of the trimpot (trimmer potentiometer) to control the brightness of the LED. We will connect a potentiometer to the analog input and an LED to a PWM pin with a current-limiting resistor. 

<!-- PWM Signals -->
```{r child = '../../shared/pwm.md'}
```

Let's take a more detailed look at the ATMega pins on the Arduino dock since we'll be using them mostly throughout these tutorials. Analog pins are from prefixed with capital A (A0 to A5). Pins 0 to 13 are digital pins. If there is a tilde sign (~) in front of the pin number, it means it can be used as a PWM pin. Pin 0 and 1 are serial pins and should not be used if we want to do serial communication between the ATmega and the Omega.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 1x 10K Trimpot
* 1x 200Ω Resistor
* 1x LED color of your choice! 

#### Hooking up the Components

// details on how to connect everything

1. First plug the potentiometer on the breadboard with each of the three pins in a different row.
2. Connect the middle pin of the trimpot to the analog pin (A0 defined in code) on the Arduino dock using a jumper wire.
3. Connect one of the remaining pin to GND and the other one to 5V (the polarity does not matter). 
4. Connect the anode of LED to a PWM pin (~9 defined in code) on the Arduino Dock. Connect the cathode to the ground through the 200Ω current limiting resistor.

### Writing the Code

// write a sketch that polls the input voltage from the trimpot circuit
// uses that reading to set the output strength (pwm duty cycle) for the led circuit
// ensure that everything is written cleanly, using functions for each separate action, don't want the setup function to be full of all sorts of different code

``` arduino
int potPin = A0;    // analog pin for reading the potentiometer value
int ledPin = 9;     // pwm pin for setting LED brightness
int potValue = 0;   // potentiometer output as a value between 0 and 1023

void setup() {			// codes to be ran once
  Serial.begin(9600);     // initializing serial communication for sending potentiometer value to the Omega
  pinMode(ledPin, OUTPUT);
}

// read the potentiometer output as a value between 0 and 1023 and print it out to the Omega through serial
void readPotValue()
{
  potValue = analogRead(potPin);
  Serial.println(potValue);
  delay(100);     //0.1s delay between reads for stability
}

//use the potentiometer value to set the LED brightness using pwm duty cycle
void setLED()
{
  analogWrite(ledPin, potValue/4);
}
  
// continuously read the potentiometer and set the LED  
void loop() {
  readPotValue();
  setLED();
}

```

// TODO: mention about using the omega as serial monitor using cat or screen ttyS1

#### What to Expect

// instructions to turn the pot and observe how the led changes
// correlate turning the pot to increasing/decreasing the resistance

#### A Closer Look at the Code
// anything new that we introduced

##### Polling
// see the 'reading a switch' article in the starter kit for an idea of what to write
