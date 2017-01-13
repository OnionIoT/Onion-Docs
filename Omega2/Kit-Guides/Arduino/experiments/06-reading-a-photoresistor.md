## Reading a Photoresistor

// description of what this experiment will accomplish and what we'll learn

### Photoresistor
// should be its own markdown file

// explanation that a photoresistor puts out a variable resistance based on the intensity of the light hitting it

### Building the Circuit

For this circuit we will need use a photoresistor and a 10K resistor to make a voltage divider on a breadboard. We will be using jumper wires for the connections.

// TODO: diagram and equation for a voltage divider

Using the equation for the voltage divider, we will be able to determine the resistance of the photoresistor and therefore calculate the light intensity.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 1x Photoresistor
* 1x 10kΩ Resistor

#### Hooking up the Components

// walkthrough all of the wiring
// 5V <-> photoresistor <-> 10K resistor <-> GND
// A0 pin connected to between photoresistor and 10k resistor

1. Connect one end of the photoresistor to 5V and the other end to the 10K resistor (the polarity does not matter). 
1. Connect the other end of the 10K resistor to GND.
1. Connect the middle point between the photoresistor and resistor to an analog pin on the Arduino Dock (A0 is defined in the code).

### Writing the Code

// write code that:
//  * reads the sensor voltage
//  * converts it to light intensity
//  * prints it on the serial line
//    * maybe make it detect once every 1 seconds

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

// make the omega connect to the microcontroller using uart1 (link to the article), read the light intensity data
// have the user cover the photoresistor with their hand and observe the change in value, have them shine a light at it


#### A Closer Look at the Code

// highlight something interesting about this code

##### Output on serial

// explanation of how the omega and atmega chip are linked, go into a little bit of detail
