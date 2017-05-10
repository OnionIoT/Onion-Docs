## Bluetooth Speaker {#bluetooth-audio-speaker}

The Omega can communicate with other devices using the Bluetooth Low Energy wireless protocol. In this project, we're going to turn it into a Bluetooth speaker that you can play music and control it from your phone or tablet!

![complete](./img/bluetooth-audio-complete.jpg)

<!-- // TODO: PHOTO: retake this photo so that the Omega is the focus, nicer background, make it nice and hip like (./img/airplay-receiver-dope.png) -->

### Overview

**Skill Level:** Intermediate

**Time Required:** 15 minutes

We'll first install the necessary Bluetooth and audio drivers. Then we'll learn how to pair Bluetooth devices with the Omega. Then we'll connect a speaker and play our favourite music!

### Ingredients

* Onion [Omega2](https://onion.io/store/omega2/) or [Omega2+](https://onion.io/store/omega2p/)
* Any Onion Dock with a USB host connector: [Expansion Dock](https://onion.io/store/expansion-dock/), [Power Dock](https://onion.io/store/power-dock/), [Mini Dock](https://onion.io/store/mini-dock/), [Arduino Dock 2](https://onion.io/store/arduino-dock-r2/)
	* We found the [Power Dock](https://onion.io/store/power-dock/) especially useful since you can take it on the go!
* Onion Bluetooth Expansion
* USB Audio Expansion, or any generic USB audio dongle
* USB hub with at least 2 ports
* Standard headphones or speakers with a 3.5mm audio jack

### Step-by-Step

Here's how to turn your Omega into a Bluetooth speaker!


#### 1. Prepare the Ingredients

For this project, we'll need an Omega2 ready to go. If needed, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.

#### 2. Setup the Hardware

1. Connect the Omega to the Dock.
1. Plug in the USB hub to the large USB host port.
1. Plug in the Bluetooth Expansion and USB Audio Expansion into the USB hub.
1. Do not connect your speaker just yet, as there will be loud popping and crackling when the USB Audio Expansion initializes!

![assembled](./img/bluetooth-audio-assembled.jpg)

After assembling all the components, turn on the Omega.


#### 3. Install Software

[Connect to the Omega's command line](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html#connecting-to-the-omega-terminal) and install the necessary packages by running the commands below:

```
opkg update
opkg install bluez-libs bluez-utils pulseaudio-daemon pulseaudio-tools alsa-lib alsa-utils
```

* The `bluez` packages are for controlling the Bluetooth radio.
* The `pulseaudio` and `alsa` packages are audio drivers for Linux.

#### 4. Setting Up the `pulseaudio` daemon

Run the following commands to initialize the daemon:

```
mkdir /run
udevd --daemon
chmod 0777 /dev/snd/*
mkdir -p /var/lib/pulse
pulseaudio --system --disallow-exit --no-cpu-limit &
```

##### After Rebooting

If you reboot the Omega, the daemon may still be running. Check using:

```
ps | grep pulse
```

If you see something like:

```
1124 pulse    10956 S <  /usr/bin/pulseaudio --system --disallow-exit --no-cp
```

Then it's running. You only need to run:

```
udevd --daemon
chmod 0777 /dev/snd/*
```

before moving to the next step again.

#### 5. Pairing the Omega to Your Bluetooth Device

Check that your Bluetooth Expansion is properly detected by the Omega by running:

```
hciconfig -a
```

You should see some lines with information about your device.

![hciconfig -a](./img/bluetooth-audio-cli-01.png)

Run the following commands to turn on your Bluetooth Expansion:

```
hciconfig hci0 up
hciconfig hci0 sspmode enable
hciconfig hci0 piscan
```

Enable Bluetooth on the device you wish to connect to the Omega. Then on the Omega, enter the `bluetoothctl` command to be taken into a new command prompt. Then run:

```
agent on
discoverable on
pairable on
scan on
```

You should see success messages, and a list of Bluetooth devices.

![bluetoothctl scan](./img/bluetooth-audio-cli-02.png)

If you do not see these messages try removing the Bluetooth Expansion, rebooting your Omega, and trying again.

Take note of the device address you wish to pair, or copy it down in a text editor on your computer somewhere. In this example, the device's address is the string of numbers, letters, and colons in the red bubble above.

Then run:

```
pair YOURDEVICEADDRESS
```

It will then prompt you for a PIN to secure this connection. You can enter 0, 0000, 1234, or anything you like; make sure to remember it!

![bluetoothctl pin](./img/bluetooth-audio-cli-03.png)

You should then get a prompt on your device asking you to connect to `OmegaBLE` and enter a PIN. Enter the PIN you just provided on the command line to finish connecting.

![connect prompt](./img/bluetooth-audio-connect-prompt.png)

Complete the prompt on your device, then on the Omega run:

```
trust YOURDEVICEADDRESS
```

Your device has been **paired** with the Omega, meaning it can connect at any time. However, they are still not connected yet.

Now on your device, tap on the connection again and it should connect.

![connect prompt](./img/bluetooth-audio-connected.png)

You can now quit the `bluetoothctl` program with the command:

```
quit
```

Check to make sure your device is still connected by running this command:

```
hcitool con
```

Your device should be listed. If you see nothing, try initiating the connection again from the remote device. If that doesn't work, go back to the previous step.

![check connections](./img/bluetooth-audio-cli-04.png)

#### 6. Set Up Audio Streaming From the Device

We will use a command called `pactl` to set up audio streaming from the Bluetooth connection to the USB Audio Expansion. First run:

```
pactl list sources
```

And look for the Source with `bluez_source` in the `Name` field. Copy that entire label down for later.

![check source](./img/bluetooth-audio-cli-05.png)

Substitute the `source` name into the following command:

```
pactl load-module module-loopback source=SOURCENAME sink=alsa_output.default rate=44100 adjust_time=0
```

The Omega is now ready to stream Bluetooth audio!


##### 7. Using the Bluetooth Audio Streamer

Before plugging in your speaker, make sure the volume is set as low as possible. Then start playing music or audio on your device. Gradually turn up the volume on the speaker until you can hear it. And you're done!

![complete](./img/bluetooth-audio-complete.jpg)

Enjoy your Omega-powered Bluetooth speaker!
