## Thermal Printer - A Compact Version {#thermal-printer-p2}

In this project, we'll build on the [Thermal Printer Project](#thermal-printer-p1). While the Expansion Dock definitely suits this purpose well, we make the same thing in a very compact package using the Mini Dock and a little bit of wire splicing and soldering.

![Thermal printer compact](./img/thermal-printer-2-1.jpg)

// TODO: another photo of how compact this is

### Overview

**Skill Level:** Advanced

**Time Required:** 1 Hour

We'll need a 3D printed plastic base for this project - if you have it printed out already, this will save you some trouble. Additionally, we'll wire up a DC barrel connector for power and wires for serial communication with the Omega instead of powering it from the Expansion dock.

This tutorial will require you to solder a wire to one of the components on the Mini Dock. Please familiarize yourself with proper soldering technique and safety procedures when working with soldering irons, as there is a risk of injury due to the high heat!

If you are not comfortable soldering, try finding a friend or professional who can quickly solder it for you. Or practice soldering wires together and then work your way up to soldering on actual electronics.

// TODO: is there a better way to say this?
**Note:** Solder at your own risk, Onion is not responsible for any injury or damage!

### Ingredients

* Omega2 / Omega2+
* Mini Dock
* [Thermal Printer](https://www.adafruit.com/product/2751)
    * comes with a 2-pin JST power cable and a 5-pin TTL cable that we will be using in this project
* [2.1 mm power jack adapter](https://www.adafruit.com/product/368)
* [5V / 2A Power supply](https://www.adafruit.com/product/276)
* [3D printed base](http://www.thingiverse.com/thing:1272778)

Tools:

1. Soldering iron + solder
1. Double-sided tape

![Ingredients](./img/thermal-printer-2-ingredients.jpg)

### Step-by-Step

Follow these steps to turn your Omega into a web-based printer!

#### 1. 3D Print the Base

3D print the base to hold our components together. If you do not have a 3D printer available nearby, there are online services available such as [3DHubs](https://www.3dhubs.com/).

#### 2. Install in the Power Jack

Insert the power jack adapter into the printer base. Do this first, since the other pieces will cover up the base later.

![How the power jack fits](./img/thermal-printer-2-base.jpg)

#### 3. Trim the cable

Next we need to cut one end of the 5-pin TTL cable that came with the thermal printer. This is so we can re-route the wires to where they need to go. The other end we'll leave alone, since that goes into the printer.

Cut only **one** of these ends off, leaving bare wire:

![Cut one of these off](./img/thermal-printer-2-cable.jpg)

#### 4. Assemble the Circuit

This is the circuit diagram for our printer:

![Circuit Diagram](./img/thermal-printer-2-circuit-diagram.png)

// TODO: convert this into a list of steps. If it gets too long, consider splitting it into two different sections (providing power and providing communication)

Plug in the 2-pin JST power cable into the left side of the bottom of the printer above. Route the red and black wires to the barrel jack; make sure the red wire is connected to the "(+)" terminal and the black to the "(-)" terminal.

Then plug the non-cut end of the 5-pin TTL cable into the printer as shown above. Route the wires through the gap in the printer case on the right side of the USB connector.

Route the black, green, and yellow TTL wires to the highlighted pins on the Mini Dock above. Then solder the red power cable to the pin on the regulator on the Mini Dock as shown above. Take care that you solder to the correct pin or you may damage your board!

To insert the wires into the Mini Dock, you can strip and twist the ends like so:

![Stripped wires](./img/temperature-monitor-assembly-01.jpg)

The wiring on the underside of the printer should look something like this:

![Thermal printer 3](./img/thermal-printer-2-3.jpg)

Insert your printer into the base from the top so that the 5-pin cable is visible as shown above. If your wires are all connected, you can then flip the printer back over so the paper can be printed.

**Do not plug in the power supply just yet,** as we still need to connect and solder some wires to the Omega.

// TODO: missing step numbering
#### Assemble the Omega
// TODO: need a more descriptive step title

Plug the Omega into the Mini Dock. The pins should push the wires into the Dock and make contact as the Omega is inserted.

Use double-sided tape or putty to affix the Omega to the rear of the printer like so:

![Affixed Omega](./img/thermal-printer-2-assembled-01.jpg)

![Affixed Omega](./img/thermal-printer-2-assembled-02.jpg)

Now plug in the 5V power supply into the barrel jack and turn the switch on the Mini Dock to ON.

// TODO: missing step numbering
#### Download the Code

// TODO: again, not a huge fan of pointing them to an article on how to install git, maybe just include a step to install git?
// TODO: see smart-plant-p1 for an example of how this step should look: we describe what we're going, provide them a link to learn more about Git, but we don't require them to look at the link to actually execute what we're asking them to do

The code for this project is all done and can be found in Onion's [iot-thermal-printer repo](https://github.com/OnionIoT/iot-thermal-printer) on GitHub.

[Connect to the Omega's Command line](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html#connecting-to-the-omega-terminal-ssh) and follow the [instructions on installing Git](https://docs.onion.io/omega2-docs/installing-and-using-git.html), navigate to the `/root` directory, and clone the GitHub repo:

```
git clone https://github.com/OnionIoT/iot-thermal-printer.git
```

After cloning the repo, enter the repo directory and run the `install.sh` script:

```
cd iot-thermal-printer
sh install.sh
```

// TODO: include a '>' section that explains what the install.sh script actually does


// TODO: missing step numbering
#### Running the Printer

1. Connect your Omega to your WiFi network, or connect your computer to the Omega's WiFi network.
1. In a web browser, navigate to omega-ABCD.local/printer.html, where ABCD is the last 4 digits on the sticker on the Omega.
1. Type in text in the box in the middle of the webpage.
1. Click print to print it!

![Web Interface](./img/thermal-printer-web-page.png)

// TODO: include a photo of the real printed output

<!-- ### Code Highlight -->
