### DS18B20 Temperature Sensor

The DS18B20 sensor is a 1-Wire digital output sensor with high accuracy. The pin layouts can be found in the diagram below:

![TMP36 Temperature Sensor Pin Layout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/DS18B20-pin-layout.png)

The `Vdd` and `GND` pins are for power and ground, and the `DQ` pin is the data line (both input and output).

You will typically need a pullup resistor (approximately 5.1kΩ at 3.3V) between the `DQ` and `Vdd` lines so that you can properly read the sensor's output.