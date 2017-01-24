## Reading an Analog Temperature Sensor

<!-- // description of what this experiment will accomplish and what we'll learn -->
In this tutorial, we will learn how to read the ambient temperature using a temperature sensor. In addition, we will learn to how to do mathematical calculations in our code.

### Analog Temperature Sensor
<!-- // should be its own markdown file

// detects the ambient air temperature
// outputs different voltage based on the temperature -->

An analog temperature will detect the ambient air temperature and outputs different voltage based on the temperature. 

// TODO: Image of a temperature sensor

There will typically be a offset the voltage to account for negative temperature. In addition, there will be a limit to the sensor's operating temperature, in our case the TMP36 will withstand a temperature range from 40°C to 125°C. Another important parameter of the temperature sensor is its scale factor, which is 10 mV/°C for the TMP36. The resolution of a sensor is the smallest change that it can detect. The resolution is effected by the ATmega, which performs analogRead() at a 10-bit resolution (1024 steps), allowing for the smallest change to be 4.88mV if the input voltage is 5V.

### Building the Circuit

<!-- // very straight-forward circuit: provide power and ground to the sensor, connect the signal to an atmega analog pin -->
For this experiment we will be using the TMP36 temperature sensor to measure the temperature in Celsius and Fahrenheit. We will connect the temperator sensor to an analog pin of the ATmega.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 1x TMP36 temperature sensor

#### Hooking up the Components

<!-- // walkthrough all of the wiring
// potentially isolate the push button instructions into it's own markdown file -->

1. Plug the TMP36 onto the breadboard.
2. When facing the flat side of the device, connect the left pin to 5V, the middle pin to analog pin A0, and the right pin to ground (GND). 

### Writing the Code

<!-- // write code that:
//  * reads the sensor voltage
//  * converts it to degrees
//  * prints it on the serial line
//    * maybe make it detect once every 10 seconds -->

``` arduino
//the scale factor of TMP36 (temperature sensor) is 10 mV/°C with a 500 mV offset to allow for negative temperatures

int sensorPin = A0; // the analog pin number connected to the TMP36
                                           
void setup()
{
  Serial.begin(9600);  //initializing serial communication with the Omega2 for sending sensor data
}
 
void loop()
{
 //getting the voltage reading from the temperature sensor
 int reading = analogRead(sensorPin);  
 
 // convert the analog reading (0 to 1023) to voltage (0 - 5V)
 float voltage = reading * 5.0;
 voltage /= 1024.0; 
 
 // print out the voltage to Omega2
 Serial.print(voltage); Serial.println(" volts");
 
 // convert voltage to degree Celsius including the 500mV offset adjustment
 float temperatureC = (voltage - 0.5) * 100 ;  
 Serial.print(temperatureC); Serial.println(" degrees C");
 
 // convert from Celsius to Fahrenheit and print to Omega2
 float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
 Serial.print(temperatureF); Serial.println(" degrees F");
 
 delay(10000);         //waiting 10 seconds between readings since the change is gradual
}
```

#### What to Expect

<!-- // make the omega connect to the microcontroller using uart1 (link to the article), read the temperature data -->
The ATmega will read the output of the temperature sensor and converted it to degrees celcius and fahrenheit. Then, it will send the voltage output of the temperature sensor and the converted degrees to the Omega through serial communication using UART1. We can use the following command line on our Omega to read the serial output of the ATmega:

```
cat < /dev/ttyS1
```

#### A Closer Look at the Code

Let's first take a closer look at how we can communicate between the Omega and the ATmega. We initialize the serial communication between the Atmega and the Omega using `Serial.begin(9600)` where 9600 is baud rate. The baud rate is the rate (in bits/second) at which the data is being transferred over the serial port. Notice we didn't include the baud rate when we use `cat < /dev/ttyS1` to read on the Omega side. This is because the default baud rate of cat is 9600. After the serial initialization, we use the build-in Arduino function `Serial.print()` to send data from the ATmega or `Serial.println()` when you need a new line.

For reading the analog signal from the temperature sensor, we use analogRead, similar to the previous tutorial when reading from the trimpot. Notice we are using a much longer delay (10 seconds) between the readings of the temperature sensor since the output from the temperature sensor changes very slowly. 

##### Math Operations

<!-- // give an overview of how we did that convertsion math -->
The temperature sensor, when powered by 5V will output a voltage between (0V to 5V) to its middle pin, depending on what the temperature is. Analog read will take that voltage and converted it to a digital value (0 to 1023). So first we need to convert the digital value back to a voltage value between 0V and 5V. We can do that by mulitplying the digital value by 5 and divide by 1023. Notice the variable for the storing the digital value (0 to 1023) is an integer `int`; however, however the variable for storing the voltage is a `float`. This is because float variables will allow us to have decimal places.

From the TMP36 datasheet, temperature sensor has a scale factor of 10 mV/°C with a offset of 500mV to account for negative temperatures. This means, for example, the sensor will output 0.5V at 0°C, 0.51V at 1°C and 0.49V at -1°C. Using the the scale factor and offset, we can convert the voltage input to temperature in degree celsius. This is done by subtracting the voltage by 0.5 and multiplying by 100.

We can convert the degree celsius value to degree fahrenheit by multiplying by (9/5) and adding 32.