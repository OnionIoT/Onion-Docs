## Reading an Analog Temperature Sensor {#arduino-kit-reading-a-temp-sensor}

<!-- // description of what this experiment will accomplish and what we'll learn -->
In this tutorial, we will learn how to read the ambient temperature using a temperature sensor. In addition, we will learn to how to do mathematical calculations in our code and how our

// LAZAR

### Analog Temperature Sensor
<!-- // should be its own markdown file

// detects the ambient air temperature
// outputs different voltage based on the temperature -->

An analog temperature will detect the ambient air temperature and outputs different voltage based on the temperature.

<!-- // TODO: Image of a temperature sensor -->

Typically, temperature sensors include a voltage offset to account for negative temperatures. In addition, there will be a limit to the sensor's operating temperature, in our case the TMP36 will withstand a temperature range from -40°C to 125°C. Another important parameter of the temperature sensor is its scale factor, which is 10 mV/°C for the TMP36. The resolution of a sensor is the smallest change that it can detect.

The resolution of the measurement also depends on how the microcontroller interprets analog input. In our case, the ATmega's `analogRead()` function has a 10-bit resolution (1024 steps), allowing for the smallest detectable change to be 4.88mV, assuming the input voltage is 5V.

### Building the Circuit

// TODO: spice up this sentence a bit, so dry rn
For this experiment we will be using the TMP36 temperature sensor to measure the temperature in Celsius and Fahrenheit. We will connect the temperature sensor to an analog pin of the ATmega.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* 1x TMP36 temperature sensor

#### Hooking up the Components

// TODO: add an intro
// TODO: add a circuit diagram of the circuit we will be building

1. Plug the TMP36 onto the breadboard.
2. When facing the flat side of the device, connect the left pin to 5V, the middle pin to analog pin A0, and the right pin to ground (GND).

// TODO: add a photo of the completed circuit and a blurb about 'this is more or less how your circuit should look'

### Writing the Code

// TODO: add an intro to the code

``` c++
//the scale factor of TMP36 (temperature sensor) is 10 mV/°C with a 500 mV offset to allow for negative temperatures

int sensorPin = A0; // the analog pin number connected to the TMP36

void setup()
{
  Serial.begin(9600);  //initializing serial communication with the Omega2 for sending sensor data
}

void loop()
{
 // getting the voltage reading from the temperature sensor
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
The ATmega will read the output of the temperature sensor and convert it to degrees celsius and fahrenheit. Then, it will send the voltage output of the temperature sensor and the converted degrees to the Omega through serial communication using UART1. We can use the following command line on our Omega to read the serial output of the ATmega:

```
cat /dev/ttyS1
```

#### A Closer Look at the Code

A few new things were introduced here, primarily the math operations and you may have noticed that we used the `float` variable type as well. We'll also go into some detail about serial communication between the ATmega microcontroller and the Omega.

##### Serial Communication

// TODO: add to this, mention how the Arduino Dock directly connects the Omega's UART1 serial port with the ATmega's serial port (there is a logic level shifter in between), talk about how this provides a great means of communication between the two devices. Only then dive into the specifics outlined below

Let's first take a closer look at how we can communicate between the Omega and the ATmega. We initialize the serial communication between the Atmega and the Omega using `Serial.begin(9600)` where 9600 is baud rate. The baud rate is the rate (in bits/second) at which the data is being transferred over the serial port. Notice we didn't include the baud rate when we use `cat /dev/ttyS1` to read on the Omega side. This is because the default baud rate of cat is 9600. After the serial initialization, we use the built-in Arduino function `Serial.print()` to send data from the ATmega or `Serial.println()` when you need a new line.

For reading the analog signal from the temperature sensor, we use analogRead, similar to the previous tutorial when reading from the trimpot. Notice we are using a much longer delay (10 seconds) between the readings of the temperature sensor since the output from the temperature sensor changes very slowly.

##### Number Variable Types

// TODO: write a section about the difference between int and floats, make sure to talk about how casting is required when performing math operations between floats and intensity
// ie describe how you'll get different results between:
//  * float var = someIntegerNumber / 5
//  and
//  * float var = someIntegerNumber / 5.0
// use this to introduce the topic of casting, potentially change the code above

##### Math Operations

// TODO: fix up the english here, the content is good but maybe create separation between the sentences that describe the calculation of each value (voltage, deg celsius, deg fahrenheit)

The temperature sensor, when powered by 5V will output a voltage between (0V to 5V) to its middle pin, depending on what the temperature is. Analog read will take that voltage and converted it to a digital value (0 to 1023). So first we need to convert the digital value back to a voltage value between 0V and 5V. We can do that by mulitplying the digital value by 5 and divide by 1023. Notice the variable for the storing the digital value (0 to 1023) is an integer `int`; however, however the variable for storing the voltage is a `float`. This is because float variables will allow us to have decimal places.

From the TMP36 datasheet, temperature sensor has a scale factor of 10 mV/°C with a offset of 500mV to account for negative temperatures. This means, for example, the sensor will output 0.5V at 0°C, 0.51V at 1°C and 0.49V at -1°C. Using the the scale factor and offset, we can convert the voltage input to temperature in degree celsius. This is done by subtracting the voltage by 0.5 and multiplying by 100.

We can convert the degree celsius value to degree fahrenheit by multiplying by (9/5) and adding 32.
