### Analog Temperature Sensor

An analog temperature will detect the ambient air temperature and output a voltage signal based on the temperature.

<!-- // TODO: Image of a temperature sensor -->

The TMP36 in your Kit is a standard linear sensor. The higher the temperature, the higher the returned signal. It has a few important specs that you should get familiar with: 

* Voltage offset
* Operating range
* Scale factor
* Resolution

Typically, temperature sensors include a **voltage offset** to account for negative temperatures. This means 0°C won't correspond to 0V, and in the case of the TMP36, 500mV corresponds to 0°C. 

The sensor's **operating range** is the range in which it'll record accurate data. The TMP36 will accurately read temperatures between -40°C to 125°C. 

Another important parameter of the temperature sensor is its **scale factor**, the change in voltage signal per degree Celsius. The TMP36's scale factor is 10 mV/°C. 

The **resolution** of a sensor is the smallest change that it can detect. It's a combination of the sensor's innate resolution and the resolution of the reading device. In our case, the ATmega's `analogRead()` function has a 10-bit resolution (1024 steps). If we use an input voltage of 5V, the smallest change in temperature that we can detect is 4.88mV (5V/1024 steps). Using the scale factor above, this means we can detect changes of **0.488°C**, or about **0.87°F**!