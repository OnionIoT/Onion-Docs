## Reading an Analog Temperature Sensor

// description of what this experiment will accomplish and what we'll learn

### Analog Temperature Sensor
// should be its own markdown file

// detects the ambient air temperature
// outputs different voltage based on the temperature

### Building the Circuit

// very straight-forward circuit: provide power and ground to the sensor, connect the signal to an atmega analog pin

#### Hooking up the Components

// walkthrough all of the wiring
// potentially isolate the push button instructions into it's own markdown file


## Writing the Code

// write code that:
//  * reads the sensor voltage
//  * converts it to degrees
//  * prints it on the serial line
//    * maybe make it detect once every 10 seconds

``` arduino
int sensorPin = A0; //the analog pin the TMP36's Vout (sense) pin is connected to
                        //the resolution is 10 mV / degree Celsius with a 500 mV offset to allow for negative temperatures
                        
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

### What to Expect

// make the omega connect to the microcontroller using uart1 (link to the article), read the temperature data


### A Closer Look at the Code

#### Math Operations

// give an overview of how we did that convertsion math
