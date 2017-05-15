## Weather Station {#weather-station}

This project will show you how to collect temperature and humidity data from a DHT22 sensor and send it to [IBM's Watson IoT Platform](https://www.ibm.com/internet-of-things/platform/watson-iot-platform/), where you can view it on the web!

![IBM Watson weather station](./img/weather-station-populated-visualization.png)

### Overview

**Skill Level:** Intermediate

**Time Required:** 40 minutes

We'll be using the Arduino Dock to read the temperature and humidity data from the DHT22 sensor since the on-board microcontroller will make this a breeze. On the Omega side, we'll use the [Python pySerial module](https://pythonhosted.org/pyserial/) to periodically send commands to the Arduino Dock and trigger a response with the sensor data. The Omega will then read that data back and send it to IBM Watson, where you can visualize the data in real time! We will then automate the project to run automatically when the Omega is turned on.

The device code can be found in Onion's [`iot-weather-station` repo on GitHub](https://github.com/OnionIoT/iot-weather-station), while the Arduino Dock sketch can be found in the Examples of the [Onion Arduino Library](https://github.com/OnionIoT/Onion-Arduino-Library).


### Ingredients

* Onion [Omega2+](https://onion.io/store/omega2p/)
    * or [Omega2](https://onion.io/store/omega2/) standard booting from a USB storage device with at least 16 MB of free memory; see [Booting From External Storage](https://docs.onion.io/omega2-docs/boot-from-external-storage.html)
    * For convenience, this tutorial will assume you are using an Omega2+.
* Onion [Arduino Dock 2](https://onion.io/store/arduino-dock-r2/)
* [Breadboard](https://www.amazon.com/gp/product/B004RXKWDQ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B004RXKWDQ&linkCode=as2&tag=onion0e-20&linkId=3f7f512f8017eeed52768810a0deca09)
* [DHT22 temperature + humidity sensor](https://www.amazon.com/gp/product/B01IT2E4ZW/ref=as_li_tl?ie=UTF8&tag=onion0e-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B01IT2E4ZW&linkId=31db761a1d9125f7cb15120e7496d697)
* [10kΩ resistor](https://www.amazon.com/gp/product/B016NXK6QK/ref=as_li_tl?ie=UTF8&tag=onion0e-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B016NXK6QK&linkId=62595ffef640175ce3a3b44fabd712e4)
* [M-M jumper wires](https://www.amazon.com/gp/product/B01LZF1ZSZ/ref=as_li_tl?ie=UTF8&tag=onion0e-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B01LZF1ZSZ&linkId=0fa23489eefb433f7768a252eb43dbde)
* (Optional) [M-F jumper wires](https://www.amazon.com/gp/product/B01LZF1ZSZ/ref=as_li_tl?ie=UTF8&tag=onion0e-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B01LZF1ZSZ&linkId=0fa23489eefb433f7768a252eb43dbde)

### Step-by-Step

Follow these instructions to setup the Weather Station project on your very own Omega!


#### 1. Prepare

You'll have to have an Omega2+ ready to go, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.

**Note 1:** The Arduino Dock does not have a USB to serial converter chip, so [all connections to the Omega's command line must be done over SSH](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html#connecting-to-the-omega-terminal-ssh).

**Note 2:** The Omega's firmware along with this project and its dependencies will require approximately 18 MB of storage space. If you wish to install apps on the Console such as the Editor, we recommend [booting the filesystem from an external SD card or USB drive](https://docs.onion.io/omega2-docs/boot-from-external-storage.html).

After completing the first time setup, follow the steps in the [Arduino Dock guide](https://docs.onion.io/omega2-docs/flash-arduino-dock-wirelessly.html) to prepare it for flashing Arduino sketches.

#### 2. Wire Up the Sensor

We will treat the side of the DHT sensor with the holes as the **front**.

1. Insert the DHT sensor into the breadboard with the front facing the middle gap.
    * The pins will be numbered 1-4 from left to right.
1. Connect Vdd (pin 1) to the Arduino Dock's 5V pin.
1. Connect DATA (pin 2) to the Arduino Dock's digital pin 2.
1. Connect GND (pin 4) to one of the Arduino's GND pins.
    * This is not a typo. Pin 3 is unused on this DHT sensor!
1. Connect the 10kΩ resistor across Vdd and DATA.

Your setup should look something like this:

![assembled](./img/weather-station-assembled.jpg)

In the above setup, two 5.1kΩ resistors were used in series to achieve the 10kΩ pullup.

**Optional** - Remove the DHT sensor from the breadboard, and use the M-F jumper wires to connect the pins back to the breadboard. This is so you can easily move the sensor around!

![optional wires](./img/weather-station-optional-wires.jpg)

#### 3. Download the Project Code on the Omega

The code for this project can be found in Onion's [iot-weather-station repo](https://github.com/OnionIoT/iot-weather-station) on GitHub. We'll first need to [connect to the Omega's command line](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html#connecting-to-the-omega-terminal-ssh) and install the packages we need for `git`:

```
opkg update
opkg install git git-http ca-bundle
```

Then we'll [use `git` to download the project code to your Omega](https://docs.onion.io/omega2-docs/installing-and-using-git.html):

```
cd /root
git clone https://github.com/OnionIoT/iot-weather-station.git
```

Now enter the repo directory and run `install.sh` to install the required packages and dependencies:

```
cd iot-weather-station
sh install.sh
```

This may take several minutes, go grab a drink or a quick snack!

> The `install.sh` script will install Python and the additional modules needed to communicate with the Watson IoT platform. Specifically, it will install Python and PIP, the Python package manager. Then, it will use PIP to install IBM's `ibmiotf` module and all of it's dependencies.


#### 4. Find your Omega's MAC Address

Then get the Omega's MAC address for use with Watson by running the `watsonHelper.py` script:

```
python watsonHelper.py
```

You will see output that looks something like this:

![MAC address](./img/weather-station-mac-addr.png)

Copy or write down the MAC address underneath "Device ID" for later.

#### 5. Arduino IDE Setup

<!-- TODO: future: fix this up when we have the arduino library and ide stuff down-pat -->


If you don't already have it, install the [Arduino IDE](https://www.arduino.cc/en/Main/Software) on your computer. Once you're in the Arduino IDE, install the `Adafruit Unified Sensor` and `DHT sensor library` libraries from the Library Manager by following [this guide](https://www.arduino.cc/en/Guide/Libraries) guide on the Arduino website.

Then you'll need to install the Onion Arduino Library by doing the following:

1. In your web browser, download the [Onion Arduino Library ZIP file](https://github.com/OnionIoT/Onion-Arduino-Library/raw/master/Onion-Arduino-Library.zip).
1. Install the ZIP library by following the instructions in the [Arduino Library Installation guide](https://www.arduino.cc/en/Guide/Libraries#toc4).
1. Restart your Arduino IDE to reload the library.

Finally, follow [our Arduino Dock setup instructions](https://docs.onion.io/omega2-docs/flash-arduino-dock-wirelessly.html) to setup the Arduino IDE to wirelessly flash the Arduino Dock 2.

#### 6. Flash the Arduino Dock's Microcontroller

Flash the weather station sketch to the Arduino Dock by doing the following:

1. Click on `File > Examples > Onion > weatherStation` to open the weather station sketch.
1. Flash it to the Arduino Dock by following the instructions in the [Arduino Dock guide](https://docs.onion.io/omega2-docs/flash-arduino-dock-wirelessly.html).

This sketch will read the temperature and humidity measurements from the DHT22 sensor and will transmit the value via serial of the correct command is received from the other end. So the Omega will have to issue a command through UART1, in this case, the command is just the `r` character, and it will then receive a JSON-formatted string of the sensor data as a response.

<!-- Select your Omega from the listed Network Ports when you open the Tools menu and then Port:

![](./img/smart-plant-p1-arduino-port.png)

> If your Omega doesn't show up in the list of Network Ports, run `/etc/init.d/avahi-daemon restart` and it should show up in about 15 seconds.

Hit the Arrow button to upload your sketch to the Arduino Dock. It will ask for a password during the flashing sequence, this is the Omega's password that it's asking for, by default it is `onioneer`.

> See our guide on [using the Arduino Dock](https://docs.onion.io/omega2-docs/flash-arduino-dock-wirelessly.html) for more details on this process. -->


#### 7. Setup the Omega on the IBM Watson IoT Platform

We will be using [IBM's guide on registering devices in Watson](https://developer.ibm.com/recipes/tutorials/how-to-register-devices-in-ibm-iot-foundation/) as a reference for this section. Open the link in your web browser and refer to the *additional* information that we have provided for each step below.

If you're having difficulties in this section, follow these two developer recipes to become familiar with the Watson web interface:

* [Connect an Onion Omega2 to IBM Watson IoT Platform](https://developer.ibm.com/recipes/tutorials/connect-an-onion-omega2-to-ibm-watson-iot-platform/)
* [How to Register Devices in IBM Watson IoT Platform](https://developer.ibm.com/recipes/tutorials/how-to-register-devices-in-ibm-iot-foundation/)

##### Step 1 - Introduction

* You can register for an [IBM Bluemix account here](https://console.ng.bluemix.net/registration/).

##### Step 2 - Create IBM Watson IoT Platform Organization

* You can call the service "Onion IoT", "Watson IoT", or whatever you like.

##### Step 3 - Create Device Type

* Call the device type `omega`.
    * The description can be something like "Onion Omega IoT board".

* In the *Define Template* substep on the Watson website, check off only the *Model* attribute.

* In *Submit Information*, enter `omega2` for the *Model*.
    * New devices by default will have this value for their *Model* attribute unless you specify something else.
* You can leave *Metadata* blank.

##### Step 4 - Add Device in IBM Watson IoT Platform

* When adding a device, choose the `omega` device type we just created.
* In the *Device Info* substep, enter the Device ID that we got from the `watsonHelper.py` helper script a few steps back.
* You can leave the *Model* field blank and it will automatically fill it in with `omega2`.
* You can leave the *Metadata* field blank.
* In *Security*, we recommend letting Watson automatically generate an authentication token for you. Click on *Next* without entering anything.
* In the *Summary* substep, review that your information is correct, then click *Add*.

![device summary](./img/weather-station-device-summary.png)

<!-- TODO: future: take a new screenshot with the device ID shown above -->

You should see a card containing your Organization ID, Device ID, and more. Don't close this card until you've recorded the token somewhere, because there's no way to view the authentication token for this device again! Take a look at the sample card below:

![device credentials](./img/weather-station-device-credentials.png)

<!-- TODO: future: take a new screenshot with the device ID shown above -->

On the Omega, open the `device.cfg` file for editing and replace the placeholders in ALLCAPS with the information in the fields above like so:

| Watson Website       | device.cfg   |
|----------------------|--------------|
| Organization ID      | YOURORG      |
| Device ID            | YOURDEVICEID |
| Authentication Token | YOURTOKEN    |

<!-- // TODO: future: include a screenshot of the device.cfg on your Omega -->

##### Remaining steps

"Step 5 - Generate API Keys" and onwards are not necessary for this project.

#### 8. Set Up Visualization Boards and Cards on Watson

Follow the steps in [IBM's guide to configuring cards in Watson](https://developer.ibm.com/recipes/tutorials/configuring-the-cards-in-the-new-watson-iot-dashboard/) with the *additional* information we have provided below:

##### Step 2 - Overview to Boards & Cards

* You can make your own board to show the collected data from the sensor. In this example, we've called it `Weather Station`.

##### Step 3 - Realtime Data Visualization

* First create a line chart card according to the guide.
* When connecting data sets, set `weather` as the Event.
* Create a data set for temperature following the example below:

![temperature dataset](./img/weather-station-temperature-dataset.png)

* Repeat for humidity by replacing all instances of `temperature` with `humidity`.
* We recommend using an XL line chart size to be able to see enough data over time.
* Set the title to "History"

You can also add a Value card to clearly display the most recent measurement values.

* When adding the card, click on "Value" as the type.
* Use a M size chart to display both temperature and humidity at the same time.
* You can set the title of this card to "Current"

![empty graphs](./img/weather-station-empty-visualization.png)

Now you've got visualization set up on Watson!

#### 9. Running the Weather Station Project

On the Omega, navigate to the `iot-weather-station` directory and run the `main.py` file:

```
python main.py
```

You should see messages being published from the command line, and new data points in your Watson dashboard! Try placing the sensor near sources of cold or hot air, or try breathing over it to change the relative humidity and see what happens on the dashboard.

![graphs with data](./img/weather-station-populated-visualization.png)

#### 10. Run the Program on Boot

We can automate this project to run when the Omega is turned on, and we can also make it run in the background so you can use the Omega for other things while it's running! To do this, we'll place a script in  `/etc/init.d`.

In the repo folder, make the `weather-station` file executable, copy it to `/etc/init.d`, then enable it to run on boot:

```
chmod +x init.d/weather-station
cp init.d/weather-station /etc/init.d
/etc/init.d/weather-station enable
```

Reboot the Omega, and you will see the dashboard automatically being populated with data while the command line is available for you to use!

> The `/etc/init.d/weather-station` script registers the Weather Station Python script as a service with `procd`, the process management daemon of the system. `procd` then ensures that the process gets started at boot and continues to run until the service is disabled.

### Code Highlight


This project makes use of two main interfaces: the Arduino Dock and the IBM Watson IoT platform.

The Arduino Dock sketch is set to read data from the DHT sensor only when an `r` character is sent over the serial bus.

```c++
if (Serial.available() > 0) {
  // read the input
  int inByte = Serial.read();
  delay(500); // small delay before responding

  // respond only if correct command is received
  if ((char)inByte == 'r') {
    responder();
    delay(delayMS);
  }
}
```

It then sends a response in JSON.

```c++
void responder() {
  // read the weather sensor
  if (getWeather()) {
    String temperature = String(sensorResponse.temperature);
    String humidity = String(sensorResponse.humidity);

    // encode output to JSON
    String response = "{\"temperature\":" + temperature + ", \"humidity\":" + humidity + "}";
    Serial.println(response);
  }
  else {
    // send false
    Serial.println("false");
  }
}
```

JSON was chosen as it is a widely used data serialization format, and JSON parsers exist in most programming languages. You can use this example to create your own Arduino Dock apps that can collect data and send it back to the Omega, which can then run any programming language you like!

The IBM Watson IoT Python library is also useful for sending data to Watson from the Omega. You can reuse the `device.cfg` and `watsonHelper.py` files in your next IoT projects!
