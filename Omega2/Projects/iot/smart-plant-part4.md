## Smart Plant - Automatic Plant Watering {#smart-plant-p4}

Now that our plant is smart enough to Tweet us when it needs water, let's see if we can make it even smarter and have it water itself! For this project, we'll add a water pump to our work in [Smart Plant Part 3](#smart-plant-p3) so we can automate the watering process.

// TODO: this photo shows the sensor disconnected... retake it ;-;

![](./img/smart-plant-p4-complete.jpg)

### Overview

**Skill Level:** Intermediate-Advanced

**Time Required:** 1 Hour

For this project, we'll be using the Relay Expansion to switch a water pump on and off, enabling our smart plant to water itself! To do that, we'll build a circuit to power the water pump, and use the [Relay Expansion Python Module](https://docs.onion.io/omega2-docs/relay-expansion-python-module.html) to control the pump with out script.

Once our pump works as expected, we'll build a new Losant **workflow** to test it out. Finally, we'll add it to the Losant workflow we've built in [Smart Plant Part 3](#smart-plant-p3) to get our plant to water itself!

The complete project code can be found in Onion's [`smart-plant` repo on GitHub](https://github.com/OnionIoT/smart-plant).

### Ingredients

We'll need all of the same materials as in the previous parts:

* Onion Omega2 or Omega2+
* Arduino Dock 2
* Onion OLED Expansion
* Soil Moisture Sensor
* 3x Male-to-Female Jumper Wires

And some new ingredients:

* Onion Relay Expansion
* DC Barrel Jack Adapter
* [Water Pump (12V DC)](http://www.canadarobotix.com/index.php?route=product/search&search=pump)
* 3x Male-to-Male Jumper Wires
* 12V 1A DC Power Supply
* Flexible Plastic Tubing
    * Make sure to match the tubing's **inner** diameter (ID) is slightly less than the pump's ports' **outer** diameter (OD). This is so the tubing will stretch and grip the ports, preventing any leaks!
    * [This mini water pump's](http://www.canadarobotix.com/pump/2033) ports have a 0.34 inch OD, and we found vinyl tubing with 0.25 inch ID provides a great seal when coupled together.

Tools:

* Flat-head screwdriver
* Eletrical Tape // TODO: this really depends on if the water pump has leads attached, see the 'Prepare the Pump' section below
* Wire Cutters	// TODO: this really depends on if the water pump has leads attached, see the 'Prepare the Pump' section below
* Wire Strippers 	// TODO: this really depends on if the water pump has leads attached, see the 'Prepare the Pump' section below

<!-- TODO: find water pump from a US retailer -->
<!-- TODO: add specific tubing -->

// TODO: retake this photo with the soil moisture sensor included and the breadboard circuit taken apart

![](./img/smart-plant-p4-ingredients.jpg)



### Step-by-Step

Follow these instructions to set this project up on your very own Omega!


// TODO: enumerate the steps correctly (when you're done all of the other TODOs)

#### 1. Prepare

You'll have to have an Omega2 ready to go, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.


#### 1. Complete the Previous Parts of the Project

This project builds on the previous parts of the Smart Plant project. If you haven't already completed the [first](#smart-plant-p1), [second](#smart-plant-p2), and [third parts](#smart-plant-p3), go back and do them now!


#### 1. Install Required Software on the Omega

To control the Relay Expansion from a Python program, you'll need to install the [Onion Relay Expansion Python Module](https://docs.onion.io/omega2-docs/relay-expansion-python-module.html):

```
opkg update
opkg install pyRelayExp
```

#### 1. Prepare the Pump

// TODO: add a note that not all water pumps come with wires attached to the leads:
//	* walk them through identifying which lead is positive and which is negative
//		* this is super important since connecting it wrong will, at best, reverse the in and out ports and, at worst, break the pump
//	* the user will need to strip a jumper wire and connect it to the leads, just twisting it around and then covering with electrical tape is enough
//		* for users skilled with a soldering iron, they can add in some soldering to make the connection more secure (don't forget to add the regular disclaimer about soldering)


#### 1. Wire up the Pump

We'll wire up the Water Pump with the Relay Expansion before connecting the Relay Expansion to the Dock.

![](./img/smart-plant-p4-4-1.jpg)

>To set up the terminals on the Relay Expansion, turn the screw on the terminal counterclockwise until the metal clamp inside is sitting a bit less than halfway in the bottom of the housing, not too much or the screw might pop out.
>The screw terminal on the barrel jack adapter is a bit different, it will rise and sink depending on the clamp position. When the screw is roughly flush with the top, it is open. To close it, turn clockwise until the screw sinks to about halfway, or until it becomes difficult to continue turning.

// TODO: photo: retake these 3 photos so that all of the components are in the same place for each photo

1. Run a jumper wire from the **negative terminal** of the DC Barrel Jack Adapter to the **negative terminal** of the Water Pump

  ![](./img/smart-plant-p4-4-2.jpg)

1. Run a jumper wire from the **positive terminal** of the DC Barrel Jack Adapter to the **IN** screw terminal on Channel 0 of the Relay Expansion

  ![](./img/smart-plant-p4-4-3.jpg)

1. Run a jumper wire from the **OUT** screw terminal on Channel 0 of the Relay Expansion to the **positive terminal** of the Water Pump

  ![](./img/smart-plant-p4-4-4.jpg)



#### 1. Connect the Relay Expansion and Provide Power

Grab your Smart Plant Omega and Arduino Dock and unplug it from power. Take off the OLED Expansion and plug in your freshly wired Relay Expansion.

![](./img/smart-plant-p4-5-1.jpg)

You can then plug the OLED Expansion into the Relay Expansion.

![](./img/smart-plant-p4-5-2.jpg)

Power the Omega and Arduino Dock through the Micro-USB port and connect the 12V power supply to the DC Barrel Jack Adapter:

![](./img/smart-plant-p4-5-3.jpg)


#### 1. Test your Setup

When your Omega boots up again, login to the Omega's command line and run the following command to turn on the relay connected to the water pump:

```
relay-exp 0 on
```

Your pump should now come to life!

To turn off the pump, run the following:

```
relay-exp 0 off
```

> For more info on the `relay-exp` command, see our [Relay Expansion documentation](https://docs.onion.io/omega2-docs/using-relay-expansion.html).


#### 1. Water Pump Setup

Before we connect the tubing, disconnect the motor from the circuit. This is so you can more easily work with the pump and avoid spilling water on your components.

// TODO: throw in an explanation and a photo of how to identify the inlet and outlet of the pump. 'Ours had the words "In" and "Out" embossed on the plastic.'

Now prepare a water reservoir; it can be as simple as a glass of water. Then measure a length of tubing that would go from the bottom of your reservoir to the inlet of the pump. Cut off the tubing, then first fit one end to the pump's inlet.

![](./img/smart-plant-p4-tubing-01.jpg)

Then insert the other end into your reservoir. We recommend securing it to the reservoir using some tape so that the tubing stays inside.

Repeat this process for another piece of tubing that will go from the pump outlet to your plant.

![](./img/smart-plant-p4-tubing-02.jpg)

Now connect the motor back to the circuit, and plug in the power supplies for the Omega and pump:

<!-- // TODO: this photo shows the sensor disconnected... retake it ;-; -->

![](./img/smart-plant-p4-complete.jpg)



// TODO: since we changed the first part to setup an init.d script, we need to update this step
// The new step should entail:
//	* running `/etc/init.d/smart-plant stop`
//		-> before putting this step in, confirm that it actually stops the existing python script instance on the Omega

#### 1. Stop the Existing Program

In the first part of the project, we modified `/etc/rc.local` to automatically run the smart plant program on boot. We'll now need to find the program and stop it before running it again manually.

Find the process of the running smart plant program:

```
root@Omega-F11D:~# ps | grep smart
 1999 root     17568 S    python /root/smart-plant/smartPlant.py --oled --quiet
 2185 root      1184 S    grep smart
```

Kill the process to stop the program:

```
root@Omega-F11D:~# kill 1999
```


#### 1. Pump Calibration

We'll need to play with the pump a little to see how long it should be enabled in order to properly water the plant.

Let's first run the Smart Plant program with the pump option enabled:

```
python /root/smart-plant/smartPlant.py --oled --quiet --losant /root/smart-plant/losant.json --pump
```

// TODO: need to explain the pump option:
// * enables receiving and reacting to commands from Losant
// * the `pumpWater` command has a payload that specifies the duration (in seconds) that the pump should be on for

Now, let's create a Losant workflow where we can use a virtual button to turn on our pump. We'll use this workflow now to find the optimal watering duration for your plant, and then afterwards you can use it to water your plant from anywhere in the world!

Head over to [Losant.com](https://www.losant.com/) and log in. Select your Smart Plant Application, click on the `Workflows` menu and then `Create Workflow`. Give your workflow a name and a description:

![new worfklow](./img/smart-plant-p4-0-pump-test-0-new-workflow.png)

Add a `Virtual Button` block to your workflow:

![add button](./img/smart-plant-p4-0-pump-test-1-button.png)

For completeness, have the button send a payload:

![setup button](./img/smart-plant-p4-0-pump-test-2-button-setup.png)

Now add a `Device Command` block:

![add device command](./img/smart-plant-p4-0-pump-test-3-device-command.png)

Set it up to use the device associated with your Smart Plant Omega, in our case, that was `omega-f11d`:

![device command: set device](./img/smart-plant-p4-0-pump-test-4-set-device.png)

Now we need to setup the command to send to the device. The name of command the program on the Omega is expecting is `waterPlant`, the payload is a string that is the number of seconds to keep the pump enabled. In our case, we started with 4 seconds:

![device command: set command](./img/smart-plant-p4-0-pump-test-5-set-command.png)

Let's also add a `Debug` block:

![add debug](./img/smart-plant-p4-0-pump-test-6-debug.png)

Set the debug message to something simple so we know our button click has gone through, and Deploy the workflow:

![deploy](./img/smart-plant-p4-0-pump-test-7-debug-setup.png)


Try pressing the button and seeing how much water actually makes it to your plant:

![](./img/smart-plant-p4-0-pump-test-8-button-pressed.png)


Experiment with the payload of the `Device Command` block to see how much water suits your plant. Also, keep in mind the `LOW_MOISTURE` and `OK_MOISTURE` levels we set in the [previous part of the project](#smart-plant-p3), when your plant is watered at the `LOW_MOISTURE` level, the amount of water added should take it back up above `OK_MOISTURE` level.

We found a duration of **7 seconds** to work well for our plant.



// TODO: since we changed the first part to setup an init.d script, we need to update this step
// This step should entail:
//	* updating /etc/init.d/smart-plant to have the OPT argument include `--pump`
//	* restarting the process: `/etc/init.d/smart-plant restart`


#### 1. Update Program Run at Boot

Since we now need to run the Smart Plant program with additional arguments to enable the pump, we'll need to update the `/etc/rc.local` file.

Open the `/etc/rc.local` file using the Vi editor: `vi /etc/rc.local`. Hit `i` and paste in the additional arguments, your file should look like this:

```
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

python /root/smart-plant/smartPlant.py --oled --quiet --losant /root/smart-plant/losant.json --pump
exit 0
```
Hit `esc` and type `:wq` to save and close the file.

Try rebooting your Omega (enter `reboot` in the command line), and you'll see that your program will start up again when the Omega boots up.


#### 1. Update the Existing Workflow

To make our smart plant truly automated, we need to add sending the `waterPlant` command to the notification workflow made in the [previous part of the project](#smart-plant-p3):

![existing workflow](./img/smart-plant-p4-1-edit-workflow-0-existing-workflow.png)

Add a `Device Command` Block to the bottom:

![device command block](./img/smart-plant-p4-1-edit-workflow-1-device-command.png)

Like before, we need to set it up to use the device associated with your Smart Plant Omega:

![device command: set device](./img/smart-plant-p4-1-edit-workflow-2-set-device.png)

Create a global variable, `PUMP_DURATION` to store the duration for which the pump will be active:

![global for pump duration](./img/smart-plant-p4-1-edit-workflow-3-set-global.png)

Now, go back to the `Device Command` block to setup the command name and payload. It will be the same as in the testing workflow used above, just this time, use `{{globals.PUMP_DURATION}}`, the global variable we just created:

![device command: set command](./img/smart-plant-p4-1-edit-workflow-4-set-command.png)

Connect the `Device Command` block to the output of the `Tweet` block so that the plant gets watered right after the Tweet is sent out:

![connect device command](./img/smart-plant-p4-1-edit-workflow-5-connect.png)

Let's also add a `Debug` block that will output that the command indeed got sent out:

![debug block](./img/smart-plant-p4-1-edit-workflow-6-debug.png)

It might also be a good idea to change the contents of the Tweet:

![tweet content](./img/smart-plant-p4-1-edit-workflow-7-tweet.png)

Connect the `Debug` block to the `Device Command` block and hit `Deploy Workflow`:

![](./img/smart-plant-p4-1-edit-workflow-8-deploy.png)


#### 1. Sit Back and Relax

Now whenever your plant's soil moisture level falls below the level in the `LOW_MOISTURE` global variable, your plant will water itself and alert you with a Tweet!

![command sent](./img/smart-plant-p4-2-plant-is-smart-0-debug-messages.png)

![tweet](./img/smart-plant-p4-2-plant-is-smart-1-tweet.png)

// TODO: add a note that users will have to experiment with the values for their `LOW_MOISTURE`, `OK_MOISTURE`, and `PUMP_DURATION` variables to see what is best for their plant



// TODO: add:
//	* "wow, revel in your achievements, you've made your plant so smart that all it needs you for is refilling the water reservoir"
//	* teaser for the next part
