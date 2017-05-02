## Thermal Printer {#thermal-printer-p1}

In this project, we'll be using the Omega to control a thermal printer via a web interface. Simply type text in a box, and click Print to print it out in real life!

![Thermal printer 1](./img/thermal-printer-1-1.jpg)

![Web Interface](./img/thermal-printer-web-page.png)

// TODO: need a photo of the printed output

### Overview

**Skill Level:** Intermediate

**Time Required:** 20 minutes

This tutorial will use the Omega to control a thermal printer - most often seen at cash registers and restaurant checkouts. We'll be using connectors and cables that come with the printer to provide it with power and communicate serially.

Optionally, we'll 3D print a base to clean up the cabling and give the printer some polish.

### Ingredients

* Omega2 / Omega2+
* Any Onion Dock that exposes the Omega's GPIOs: Expansion Dock, Arduino Dock R2, Power Dock, Breadboard Dock
* [Thermal Printer](https://www.adafruit.com/product/2751)
    * comes with a 2-pin JST power cable and a 5-pin TTL cable
* [2.1 mm power jack adapter](https://www.adafruit.com/product/368)
* [5V / 2A Power supply](https://www.adafruit.com/product/276)
* [3D printed base](http://www.thingiverse.com/thing:1272778)
* Male-to-Male Jumper Wires

![Ingredients](./img/thermal-printer-1-ingredients.jpg)

### Step-by-Step

Follow these steps to turn your Omega into a web-based printer!

// TODO: fix the step numbering

#### 1. Prepare

You'll have to have an Omega2 ready to go, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.


#### 1. Wire Up the Thermal Printer

// TODO: not really a circuit diagram, lets not call it as such
This is the circuit diagram for our printer:

<!-- TODO: new circuit diagram -->
![Circuit Diagram](./img/thermal-printer-1-circuit-diagram.png)

For these wiring instructions, we're assuming you're working with an Onion Expansion Dock. Other docks may have different pin layouts than pictures show.

// TODO: break this up into a numbered list of steps

First make sure the Omega is off and seated in the Expansion Dock.

Then, plug in the 2-pin power cable into the left side of the bottom of the printer above. Route the black wire to the `GND` pin on the Expansion Dock headers.

Next we'll connect the serial wires. First plug one end of the 5-pin TTL cable into the socket at the bottom of the printer. Using a jumper (preferably green to keep it clear) connect the green wire pin on the TTL connector to the `TX` pin on the Omega Expansion header. Same goes for the yellow wire pin on the TTL connector, except this one goes to the `RX` pin. Lastly, do the same for the black wire to the `GND` pin on the Expansion Dock header - we used a breadboard intermediary in the diagram to show how the connection is supposed to go.

Finally, connect the red wire from the JST connector to a `5V` pin on the Expansion Dock headers.


#### 2. Download the Project Code

// TODO: see smart-plant-p1 for an example of how this step should look: we describe what we're going, provide them a link to learn more about Git, but we don't require them to look at the link to actually execute what we're asking them to do

The code for the thermal printer can be found in Onion's [`iot-thermal-printer` repo](https://github.com/OnionIoT/iot-thermal-printer) on GitHub. Follow the [instructions on installing Git](https://docs.onion.io/omega2-docs/installing-and-using-git.html), navigate to the `/root` directory, and clone the GitHub repo:

```
git clone https://github.com/OnionIoT/iot-thermal-printer.git
```

After cloning the repo, enter the repo directory and run the `install.sh` script:

```
cd iot-thermal-printer
sh install.sh
```

#### 3. Running the Printer

1. Connect your Omega to your WiFi network, or connect your computer to the Omega's WiFi network.
1. In a web browser, navigate to omega-ABCD.local/printer.html, where ABCD is the last 4 digits on the sticker on the Omega.
1. Type in text in the box in the middle of the webpage.
1. Click print to print it!

![Web Interface](./img/thermal-printer-web-page.png)

// TODO: include a photo of the real printed output

### Code Highlight

This project uses the `cgi-bin` method to run scripts on the Omega via a web interface. In the following line, we send the data from the text box to the script in the `/cgi-bin` directory using asynchronous JavaScript (AJAX):

```javascript
$.ajax({
    type: "POST",
    url: "/cgi-bin/print.sh",
    data: $('#printContent').val().split('\n').join('\r'), // <-- We need to replace \n with \r
    contentType: 'text/plain'
})
```

The `print.sh` script works like a simple API endpoint that takes data and does something with it; in this case, sending it to the printer via serial:

```sh
#!/bin/sh

echo "Content-type: application/json"
echo ""

if [ "$REQUEST_METHOD" = "POST" ]; then
    read -n $CONTENT_LENGTH line
    echo $line > /dev/ttyS1
    # feed paper
    echo '' > /dev/ttyS1
fi

echo '{"success":"ok"}'

exit 0
```

This is just one of many methods to create your own endpoints and services easily and quickly on the Omega!
