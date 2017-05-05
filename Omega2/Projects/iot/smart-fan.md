## Temperature-Based Smart Fan {#smart-fan}


Mornings too cold, but gets too hot by noon? By hooking up a temperature sensor to the Omega, we can use the data it provides to modulate the speed of a fan - cooling us down only when we need it!

// TODO: mention a use-case of using this to cool down electronics or some homebrewing setup, anything where temperature control is required

![Smart fan all set up!](./img/smart-fan-example.jpg)

### Overview

**Skill Level:** Intermediate ~ Advanced

**Time Required:** 40 Minutes

<!-- // go into some detail here about how we're going to be implementing the project //	eg. which programming language we'll be using, APIs //	include links to any api or module references -->

There's a lot of implementation details in this project that will change depend on the exact hardware you have access to. We used a D18B20 1Wire temperature sensor, for example. For the fan, we recommend a computer case fan, since those are quite easy to come by and works decently well.

We also cooked up a DC motor with a 3D printed rotor setup just like in the [Omega2 Maker Kit](https://docs.onion.io/omega2-maker-kit/maker-kit-servo-h-bridge.html) since we had all of those handy.

To control the fan, we'll be using a python script and the [Onion PWM Expansion Python Module](https://docs.onion.io/omega2-docs/pwm-expansion-python-module.html) to control the fan speed. We also use a library to operate the 1Wire sensor, but your methods may vary depending on your exact sensor.

All the code we used is written for a case fan with a transistor switching it. It can be found in Onion's [`iot-smart-fan` repository](https://github.com/OnionIoT/iot-smart-fan) on GitHub.

### Ingredients

* Onion Omega2 or Omega2+
* Any Onion Dock that supports Expansions: Expansion Dock, Power Dock, Arduino Dock 2
* Onion Servo (PWM) Expansion
* Breadboard (optional, but it helps a lot)
* Computer case fan
* D18B20 1-Wire Temperature Sensor
	* The Omega accepts I2C, 1Wire, and SPI, among other protocols, so other digital sensors will work as well.
* 12V DC supply capable of supplying at least 0.5A
* 1x 5.1kΩ Resistor
* 1x 10 μF Capacitor
* NPN Transistor rated for 12V at 0.5A
* Jumpers
    * 3x M-F
    * 3x M-M



### Step-by-Step

Follow these instructions to set this project up on your very own Omega!


#### 1. Prepare

First let's get the Omega ready to go. if you haven't already, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.

Plug in the PWM Expansion to the Dock and grab all the components:

// TODO: insert photo with PWM Expansion plugged into Expansion dock


#### 2. Install the Required Software

We need Python and the [Onion PWM Expansion Python Module](https://docs.onion.io/omega2-docs/pwm-expansion-python-module.html)  to make this work:

```
opkg update
opkg install python-light pyPwmExp
```

Everything else will be included in the GitHub repo.

#### 3. Connect the Fan

Computer case fans are voltage driven, but we can cheat by using PWM with a transistor to switch the supply voltage.

If you have jumpers handy, we recommend using them as a bridge between the header of the fan and the PWM expansion.

First, we'll have to set up the transistor. For our lab setup, we used a STS8050 NPN transistor with a 2-wire PC case fan. If you use a different model, make sure to note which pin is the base/collector/emitter.

>If you use a PNP transistor, your fan will automatically turn on unless you set the PWM output to 100%. This is because PNP transistors turn 'on' when the base draws current, when the PWM channel is at 0% duty, it draws a tiny bit of current - enough to turn on the transistor!

Most commonly, case fans have three pins/wires - one of which is a tachometer output. If you're using one of these, make sure there's no power being supplied to the output pin, this will cause damage to the fan.

>The output pin sends the current speed of the fan, it can be used in your code to check if the fan is working as a bonus!

We connected the power supply to the PWM expansion for cleaner wiring.

// TODO: need photos for these steps (doesn't have to be a photo for each step btw)

1. Connect the `GND` from the fan to the collector pin on the transistor (right pin when looking at the flat side of the 8050).
1. Connect the Signal pin from the PWM Expansion channel 0 (`S0`) to the base pin of the transistor.
1. Connect the emitter pin from the transistor to any `GND` pin on the PWM Expansion.
1. Plug one end of the 10 μF capacitor to the emitter row of the transistor.
1. Plug the other end to an empty row.
1. Connect the `VDC` of the fan to the row where the capacitor ends.
1. Finally, connect the `Vcc` pin on the PWM Expansion to the row with the capacitor and the fan `VDC`.

This circuit will now switch the Fan's voltage based on the PWM signal from channel 0!

>The capacitor and fan creates a **second order band-pass filter**. The capacitor will absorb high-frequency signals inside a certain frequency range, leaving DC power to be routed to the fan.

#### 4. Wire up the Temperature Sensor

This part is written assuming you're working with the D18B20, if your sensor is different, you may have to find a guide elsewhere on wiring it properly.

The D18B20 has a pinout that looks like this:

![D18B20 Temperature Sensor Pin Layout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/DS18B20-pin-layout.png)

**NOTE**: the second graphic is a **bottom** view, where the pins are pointing towards you (we may have fried a sensor by misreading this one).

You'll need to grab your breadboard and plug the sensor into three different rows. This sensor requires a pull-up resistor on that data line, so connect the 5.1kΩ resistor to the `VDD` and `DQ` rows:

![temperature sensor wired](./img/smart-fan-sensor-circuit.jpg)

Now we can connect the sensor to the Expansion Headers.

* First, connect the `GND` pin of the sensor to a `GND` pin on the Expansion Header
* Next, connect the middle pin (`DQ`) to GPIO1 on the Expansion Header
* Finally, connect the `VDD` pin to a `3.3V` pin on the Expansion Header


#### 5. Get the Project Code

// TODO: this whole step is awful
// TODO: see smart-plant-p1 for an example of how this step should look: we describe what we're going, provide them a link to learn more about Git, but we don't require them to look at the link to actually execute what we're asking them to do

Head over to the [iot-smart-fan repository](https://github.com/OnionIoT/iot-smart-fan) on GitHub, and download the repo.

Copy the all the files to the same directory in your omega. If you're using your own temperature sensor, you'll have to make some changes before it'll run.

#### 5. (and a half) Using a Different Sensor

There's a good bit of setup for the temperature sensor - initialization, communicating, and parsing.

If you have a different sensor than the the one we're using, you'll have to modify the project code. The code that sets up the D18B20 1-wire sensor can be found in the lines between `#~~~ SENSOR SETUP BEGIN` and `#~~~ SENSOR SETUP END`.

Additionally, you'd probably need to change the function used to get the sensor data:

``` python
        temp = sensor.readValue()
```


One important thing to note is that the values assigned to the `temp` variable must be integer or float.

#### 6. Calibrate and Customize

By editing the `config.json`, you can change the possible speed range of the fan and restrict the temperature range to which the fan reacts:

```
{
    "tempMax" : "40",
    "tempMin" : "18",
    "dutyMin" : "60",
    "dutyMax" : "100",
    "frequency" : "1000",
    "fanType" : "case"
}
```

The `dutyMin` and `dutyMax` parameters control the minimum and maximum duty cycle of the signal being sent to the fan, thereby controlling the fan speed. The `tempMin` and `tempMax` parameters specify the temperature range in which to enable the fan. The fan speed has a linear relationship with the temperature when it is between the min and max temperature.


### A Different Fan

If you would rather use the H-Bridge and DC Motor setup, you'll have to make some changes to the code. Namely, you'll have to swap out the `OmegaPwm` class with the `hBridgeMotor` class from `omegaMotors.py`. Check the pin-outs that we've put in by default in `iotSmartFan.py` to make sure you're correctly connecting the H-Bridge to the Servo Expansion.

For a detailed guide on how to set this up, check out the wiring instructions in the [Maker Kit DC Motor experiment](https://docs.onion.io/omega2-maker-kit/maker-kit-servo-dimming-led.html).


To change up the code, open up `iotSmartFan.py` and change this line:

``` python
    fan = OmegaPwm(FAN_PWM_CHANNEL)
```


To this:

``` python
    fan = hBridgeMotor(FAN_PWM_CHANNEL, H_BRIDGE_1A_CHANNEL, H_BRIDGE_2A_CHANNEL)
```

And this line:

``` python
        fan.setDutyCycle(duty)
```

To this:

``` python
        fan.spinForward(duty)
```

### Code Highlight

Two of the key components in this project are the temperature sensor and the motor drivers, found in `temperatureSensor.py` and `omegaMotors.py`.

The output from the 1-Wire temperature sensor contains a lot of unnecessary information such as the device address, connection acknowledgements, and other fields. The `__readOneWire()` internal method of the `TemperatureSensor` class extracts the temperature value and converts it to degrees Celsius:

```python
def __readOneWire(self):
        # device typically prints 2 lines, the 2nd line has the temperature sensor at the end
        # eg. a6 01 4b 46 7f ff 0c 10 5c t=26375
        rawValue = self.driver.readDevice()

        # grab the 2nd line, then read the last entry in the line, then get everything after the "=" sign
        value = rawValue[1].split()[-1].split("=")[1]

        # convert value from string to number
        value = int(value)

        # DS18B20 outputs in 1/1000ths of a degree C, so convert to standard units
        value /= 1000.0
        return value
```

The method to set the duty cycle for a servo fan, `setDutyCycle()` uses the Onion `pwmExp` class to easily control it:

```python
def setDutyCycle(self, duty):
		"""Set duty cycle for pwm channel"""
		ret 	= pwmExp.setupDriver(self.channel, duty, 0)
		if (ret != 0):
			print 'ERROR: pwm-exp setupDriver not successful!'

		return ret
```