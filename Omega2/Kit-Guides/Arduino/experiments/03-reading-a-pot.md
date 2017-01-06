
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

#### Hooking up the Components

// details on how to connect everything

### Writing the Code

// write a sketch that polls the input voltage from the trimpot circuit
// uses that reading to set the output strength (pwm duty cycle) for the led circuit
// ensure that everything is written cleanly, using functions for each separate action, don't want the setup function to be full of all sorts of different code

``` arduino
int potPin = A0;    // analog pin for reading the potentiometer value
int ledPin = 9;     // pwm pin for setting LED brightness
int potValue = 0;   // potentiometer output as a value between 0 and 1023

void setup() {
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
  
// loop the potentiometer reading and the LED setting  
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
