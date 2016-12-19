
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

#### What to Expect

// instructions to turn the pot and observe how the led changes
// correlate turning the pot to increasing/decreasing the resistance

#### A Closer Look at the Code
// anything new that we introduced

##### Polling
// see the 'reading a switch' article in the starter kit for an idea of what to write
