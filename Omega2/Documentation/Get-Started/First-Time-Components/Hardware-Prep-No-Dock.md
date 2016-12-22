<!-- Prepare the Hardware -->

### Unboxing and Getting the Hardware Ready

**Unpack**

Unpack the Omega from its box

// TODO: picture of unboxed Omega


**Providing Power**

The Omega needs to be powered by 3.3V DC, and without a Dock, we can't use a MicroUSB to provide the power. So we'll need to build a *regulator* circuit that can be supplied with a wide range of input, but still provide the Omega with the precise 3.3V that is needs.

// TODO: add affiliate amazon links to all of these items

We'll need the following
* A breadboard
* 2 male-to-male jumper wires
* 2 male-to-female jumper wires
* LD1117 3.3V Regulator
* DC Barrel Jack (breadboard friendly)
* DC Power Supply

**Building the Circuit**


Voltage regulators normally have three legs: Input, Output, and Ground. Take your voltage regulator and plug it into your breadboard so that each leg is in a different row. You'll then want to connect your barrel jack *ground* to the regulator's *ground*, and the barrel jack's *output* to the regulators *input*. Now you're ready to power the Omega.


**Provide Power to the Omega**


With your regulator circuit built you can provide a steady 3.3V to the Omega. Take one male-to-female jumper cable and insert the male end into the row with the ground leg of the regulator. Then take another male-to-female jumper cable and connect it to the output leg of the regulator. This leg is outputting 3.3V.

Now take a look at the following pinout and connect the ground cable to the ground pin, and the 3.3V cable to the 3.3V VIN (input) pin. They are right next to each other:

![pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/Omega-2-Pinout-Diagram.png)


Connect your *DC* power supply to the barrel jack and your Omega will begin booting.

**Wait till it boots**

<!-- LED at Boot text -->
```{r child = './Hardware-Prep-Component-LED-at-boot.md'}
```

![Omega is on](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/unbox-6-omega-led-detail.jpg "Omega is on")


Your Omega's AP will become available for you to connect to on other devices.
