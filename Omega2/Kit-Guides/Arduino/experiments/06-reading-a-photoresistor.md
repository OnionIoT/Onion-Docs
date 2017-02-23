## Reading a Photoresistor {#arduino-kit-reading-a-photoresistor}

<!-- // description of what this experiment will accomplish and what we'll learn -->
In this tutorial, we will use a photoresistor to detect the ambient light intensity. In order to be able to actually detect the light intensity, we'll need a voltage divider in our circuit. We'll also be sending data from the ATmega to the Omega through the serial port. Let's dive in!

### Photoresistor
// TODO: move this to its own markdown file

A photoresistor has a variable resistance based on the intensity of the light hitting it. However, its light intensity measured in a unit called lux is inversely proportional to its resistance: the resistance will decrease when the environment has more light, and increase when there is less light. The photoresistor is made out of a semiconductor with high resistance and can go up to megohms when the environment is dark.

<!-- // TODO: Image of a photoresistor -->

### Building the Circuit

For this circuit we will need use a photoresistor and a 10K resistor to make a voltage divider on a breadboard. We will be using jumper wires for the connections.

<!-- // TODO: diagram and equation for a voltage divider -->

Using the equation for the voltage divider, we will be able to determine the resistance of the photoresistor and then calculate the light intensity.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 1x Photoresistor
* 1x 10kΩ Resistor

#### Hooking up the Components

// TODO: add an intro
// TODO: add a circuit diagram of the circuit we will be building

1. Connect one end of the photoresistor to 5V and the other end to the 10K resistor (the polarity does not matter).
1. Connect the other end of the 10K resistor to GND.
1. Connect the middle point between the photoresistor and resistor to the A0 analog pin on the Arduino Dock

// TODO: add a photo of the completed circuit and a blurb about 'this is more or less how your circuit should look'

### Writing the Code

// TODO: intro to the code

``` arduino
int lightPin = A0;  //the pin number connected to the photoresistor
int R1 = 10000;   // resistor value between photoresistor and GND

void setup()
{
    Serial.begin(9600);  //initializing serial communication with the Omega2 for sending sensor data
}

void loop()
{
    // read a value (0 to 1023) from the analog pin and print to the Omega through serial
    int reading = analogRead(lightPin);
    Serial.println(reading);   

    // convert the reading to voltage level (0 to 5V)
    float voltage = reading * 5.0 / 1024.0;
    Serial.print(voltage); Serial.println(" volts");

    // calculate the resistance of the photoresistor based on voltage level and the voltage divider formula:
    // V(A0) = R1/(R1 + Rphoto) * 5V
    float Rphoto = 5.0 / voltage * R1 - R1;
    Serial.print(Rphoto/1000); Serial.println(" kohms");

    // convert photoresistance resistance to light intensity in lux
    float lightIntensity = 500/(Rphoto/1000);
    Serial.print(lightIntensity); Serial.println(" lux");

    delay(1000);     //1 second delay between the readings
}
```

#### What to Expect

<!-- // make the omega connect to the microcontroller using uart1 (link to the article), read the light intensity data
// have the user cover the photoresistor with their hand and observe the change in value, have them shine a light at it -->

The ATmega will print the output voltage of the voltage divider, the resistance of the photoresitor and the light intensity in lux through the serial port. We can then read the data on the serial port on the Omega with the following command:

```
cat /dev/ttyS1
```
If we cover the photoresistor with our hand, we should see on our Omega terminal that the light intensity (lux) value decrease significantly. The resistance of the photoresistor is inverse proportional to the light intensity (lux).

#### A Closer Look at the Code

// TODO: change this text so that it doesn't talk about the previous experiment

This code is very similar to the previous tutorial. We use analogRead to obtain a digital value (0 to 1023) of analog voltage level at the output of the voltage divider. We first convert the digital value (0 to 1023) to the the output voltage level (0 to 5V) same as previous tutorial. We can then calculate the resistance of the photoresistor based on voltage level and the voltage divider formula. Lastly we convert the photoresistor resistance to light intensity using the formula for a typical photoresistor: light intentisty (lux) is equal to 500 divide by the photoresistor resistance (kΩ).

We also use `Serial.print()` to send the values at all the stages of the calcuation to the Omega for better understanding the calculation process.

##### Output on serial

// TODO: dive in a little more on this explanation
We can obtain the output of the ATmega on our Omega through serial as explained in the previous tutorial.

```
cat /dev/ttyS1
```
