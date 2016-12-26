<!-- Prepare the Hardware -->

## Powering the Omega with No Dock {#hardware-prep-no-dock}

**Unpack**

Unpack the Omega from its box

![omega2 alone](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/omega-2-alone.jpg)


**Providing Power**

The Omega needs to be powered by 3.3V DC, and without a Dock, we can't use a MicroUSB to provide the power. So we'll need to build a *regulator* circuit that can be supplied with a wide range of input, but still provide the Omega with the precise 3.3V that is needs.

<!-- // TODO: add affiliate amazon links to all of these items -->

We'll need the following

* A breadboard  <!-- https://www.amazon.ca/Elenco-Breadboard-Prototype-Design-Aid-9830/dp/B0002H4W2S/ref=sr_1_3?ie=UTF8&qid=1482440562&sr=8-3&keywords=breadboard -->
* 2 male-to-male jumper wires <!-- https://www.amazon.ca/120pcs-Multicolored-Dupont-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_1?ie=UTF8&qid=1482441078&sr=8-1&keywords=jumper+wires -->
* 2 male-to-female jumper wires <!-- https://www.amazon.ca/120pcs-Multicolored-Dupont-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_1?ie=UTF8&qid=1482441078&sr=8-1&keywords=jumper+wires -->
* LD1117 3.3V Regulator <!-- https://www.amazon.ca/Power-Module-AMS1117-3-3-Step-Down-Regulator/dp/B01GNKSWSC/ref=sr_1_1?ie=UTF8&qid=1482441028&sr=8-1&keywords=voltage+regulator+3.3 -->
* DC Barrel Jack (breadboard friendly) <!-- https://www.amazon.ca/OSEPP-Barrel-Adapter-Female-Components-LS-00015/dp/B00EFZV24Y/ref=sr_1_3?ie=UTF8&qid=1482441122&sr=8-3&keywords=dc+barrel+jack -->
* DC Power Supply <!-- https://www.amazon.ca/SAWAKE-Universal-Adapter-Charger-Security/dp/B00SKPIA1S/ref=sr_1_3?ie=UTF8&qid=1482441210&sr=8-3&keywords=dc+power+adapter -->

**Building the Circuit**


Voltage regulators normally have at least three legs: Input, Output, and Ground. The LD1117 regulator we're using has the legs arranged in the order shown in the image below. Consult your regulator's datasheet for specifics.
![voltage regulator](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/no-dock-ld1117-regulator-pinout.png)



Take your voltage regulator and plug it into your breadboard so that each leg is in a different row.

![voltage regulator](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/no-dock-voltage-regulator.jpg)


You'll then want to connect your barrel jack *ground* to the regulator's *ground*, and the barrel jack's *output* to the regulators *input*.

![omega2 alone](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/no-dock-barrel-jack.jpg)


Now you're ready to power the Omega.


**Provide Power to the Omega**


With your regulator circuit built you can provide a steady 3.3V to the Omega. Take one male-to-female jumper cable and insert the male end into the row with the ground leg of the regulator. Then take another male-to-female jumper cable and connect it to the output leg of the regulator. This leg is outputting 3.3V.

Now take a look at the Omega's pinout diagram, we'll connect the ground cable to the ground pin, and the 3.3V cable to the 3.3V VIN (input) pin.

They are right next to each other on the right side of the Omega:

![pinout](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/Omega-2-Pinout-Diagram.png)

![plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/no-dock-plugged-in.jpg)


Connect your *DC* power supply to the barrel jack and your Omega will begin booting.

![powered on](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/no-dock-powered-on.jpg)

**Wait till it boots**

<!-- LED at Boot text -->
```{r child = './Hardware-Prep-Component-LED-at-boot.md'}
```


Your Omega's AP will then become available, allowing connections from other devices.


**Continue the Setup Process**

If this is your first time powering on the Omega, you can now follow the rest of the setup steps as if you had the Omega connected to a Dock. See our guide on [using the browser-based Setup Wizard](#first-time-setup-wizard) or the [Command Line setup guide](#first-time-setup-command-line-steps) for info on how to complete your Omega's setup.

If you opt for the command line setup, you will only be able to connect to the Omega via SSH. Connecting via serial is possible only if you have a USB-to-UART serial converter.
