
## Reading an Potentiometer

// this experiment will use a potentiometer to control Brightness of an LED


### Potentiometer

// description that a pot is essentially a variable resistor, we can tell

### Dimming an LED

// leds are brighter the more voltage is applied, dimmer the less we apply

// the microcontroller is able to output an analog signal, meaning we can control how much voltage is going to the led, directly controlling its brightness
// add a note saying that the analog signal is actually pwm, but don't go into heavy detail

So far we've been turning LEDs fully on and fully off, but it's also possible have LEDs dimmed to somewhere between on and off. And that's what we're going to do in this experiment: we're going to use Pulse Width Modulation (PWM) to create a dimming effect on an LED.

### Pulse Width Modulation

Pulse Width Modulation (PWM) sounds complicated but in it's essence it's just turning a digital signal on and off at regular intervals. It allows us to easily control how much power is supplied to a component. In our case that component will be an LED and the less power we provide, the dimmer the light the LED will produce.

<!-- PWM Signals -->
```{r child = '../../shared/pwm.md'}
```

### Building the Circuit

// will need a pull-up resistor connected to the trim-pot, and an arduino dock analog input sampling the voltage

// an LED connected to one of the (pwm) outputs

For this experiment, we will use the knob of the trimpot (trimmer potentiometer) to control the brightness of the LED. We will connect a potentiometer to the analog input and an LED to a PWM pin with a current-limiting resistor. 

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

When the code has been flashed on the ATmega, we will be able to adjust the brightness of the LED by turning the knob of the trimpot. This is because we can use the trimpot to set duty cycle to increase up to 100% (fade in to 100%), and then we begin to decrease the duty cycle down to 0% (fade out to 0%). In addition, we can use the following command line on our Omega to read the serial output of the ATmega:

```
cat < /dev/ttyS1
```

It will print a digital value (0 to 1023), which has been converted from the analog output of the potentiometer. This value should also correspond to the brightness of the LED.

#### A Closer Look at the Code
// anything new that we introduced
In this code we introduced several new concepts: analog read and analog (PWM) write; whereas previously we are using digital write. In addition, we will introduce a concept called polling. Let's take a look. 

##### Analog Read
First we start by looking at the readPotValue() function, in which we use analogRead to get the output value of the potentiometer. The output of the potentiometer circuit is basically the output voltage of a voltage divider circuit. Since the input voltage is 5V, the output voltage will vary from 0V to 5V depending on the position of trimpot knob. The Arduino build-in function analogRead will convert that voltage (0-5V) to a digital value (0 to 1023). Lets store this value in the variable potValue for later use.

For analogRead to work we should use an analog pin (A0 - A6) on the Arduino Dock. Moreover, analogRead takes in only one parameter, the pin number. Also notice that we do not need to set the pinMode of the pin reading the potentiometer to INPUT. This is because as mention earlier, the GPIOs are INPUT by default.

##### Analog (PWM) Write
Similar to previous tutorials, we set a pin output for light the LED. However this time, we will use a PWM (~) pin and instead of digitalWrite, we'll use analogWrite. The name analogWrite might be confusing at first since we are using a digial PWM pin to light the LED. However, PWM is actually a form of digital-to-analog conversion.

The Arduino build-in function analogWrite takes in two parameters: the pin number and a value representing the PWM duty cycle between 0 (always off) and 255 (always on). Notice this range (0 to 255) is about one fourth the range of the output from the analogRead (0 to 1023). So let's take our variable potValue from before and divide by four to set the brightness of the LED.

##### Polling
// see the 'reading a switch' article in the starter kit for an idea of what to write

Polling is the process of repeatedly checking an input.

YOu may notice in the code there is a 0.1s delay in the readPotValue() function between reading the trimpot and the setting the LED. This delay was added for stability so that the CPU has some time to rest between every check on the LED. We don't want to burn up the CPU by constantly checking the same thing - remember that it runs incredibly fast!

Some of the issues during polling are as follows:

* You can't do anything else in the program.
* You need to find a polling speed that balances the time delay and stress on the CPU.

If only there were a better way of doing this!