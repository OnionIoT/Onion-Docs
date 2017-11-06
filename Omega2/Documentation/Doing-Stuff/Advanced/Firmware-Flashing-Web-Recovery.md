## Firmware Flashing With Web Recovery Mode {#Firmware-Flashing-Web-Recovery}

If your Omega got "bricked" or your firmware became corrupted and you cannot boot into your OS, do not panic as it can be fixed. This guide will teach you how to flash your Omega with new firmware through the Omega's Bootloader.

![ethernet-main-setting](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/ethernet-flash-main-setting.JPG)

### Step 1: Ingredients

* The Omega2 or Omega2+ that needs to be flashed with new firmware
* Expansion Dock
	* Must be the Expansion Dock since we will need to connect the Ethernet Expansion and connect to the Omega’s command line via serial
* Ethernet Expansion
* Ethernet Cable
* MicroUSB Cable

### Step 2: Downloading Firmware

Before we proceed to the actual flashing process, we need to download the firmware we wish to flash on the Omega to your computer. Open your web browser and go to the [Onion firmware repo](http://repo.onion.io/omega2/images/). We will flash firmware `v0.1.10 b160`, which is the latest at the time of writing.

### Step 3: Activating Web Recovery Mode

Now, plug your Omega and Ethernet Expansion to the Expansion Dock and connect the Omega to your computer with the ethernet cable. But do not power on the device just yet!

[First, connect to the Omega’s command line through serial](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html#connecting-to-ssh-windows). Then, power on the device **and** press the **_Reset_** button on the Expansion Dock at the same time.  This will get you to the bootloader and you’ll see the following menu: 

![bootloader-menu](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/bootloader-menu.PNG)

We need to activate `Web Recovery Mode` by pressing `0`. Be quick, you only have 40 seconds until the Omega reboots and tries to boot normally. After pressing `0`, you shoid see the following output:
```
Bringing Eth0 (10/100-M) up...

RT2880 ETH setup done.

HTTP server starting at 192.168.8.8 ...

HTTP server is up and running.
```

### Step 4: Configuring computer's ethernet network

In this step we will configure your computer's ethernet network to set it to an IP address that can reach the Omega's Web Recovery IP, `192.168.8.8`. The following procedure outlines the instructions for Windows:

* You should notice a new device in the Network and Sharing center:

![ethernet-flash-network-sharing](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/ethernet-flash-network-sharing.png)

* We need to set up an IP address corresponded to our Omega's ethernet settings. Click on `Local Area Connection`, under the Undefined Network and select `Properties`.

![ethernet-flash-lan](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/ethernet-flash-lan.png)

* Select `Internet Protocol Version 4 (TCP/IPv4)` and click `Properties`.

![ethernet-flash-ip-setting](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/ethernet-flash-ip-setting.png)

* Check `Use the following IP address:` radio button and manually type `192.168.8.100`. Once finished, the subnet mask will be created automatically. Click `Ok`. Now you are all set.

### Step 5: Actual Flashing

Open your Browser and type `192.168.8.8` in the search window. You will be presented with the web recovery page. Use it to **choose** the firmware to be flashed on your Omega. We will want to choose the .bin file we downloaded previously and start the flashing process. 

![ethernet-flash-web-page](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/ethernet-flash-web-page.png)

When you see that you file is successfully added, hit the `Update!` button and you will see the following output in your serial screen:

![ethernet-flash-start-process](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/ethernet-flash-start-process.png)

This will take several minutes to reflash and reboot your device. Once it is done, you will see `Onion Omega Logo` and the version number.

![ethernet-flash-end-process](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/ethernet-flash-end-process.png)

Please, note that it matches the firmware we downloaded: `Ω - ware: 0.1.10 b160`. 

### Going Further

Having an Ethernet Expansion is handy since it not only can it allow you to de-brick your Omega, but also enable you to make a variety projects. Please refer to our Docs on [how to use the Ethernet Expansion](https://docs.onion.io/omega2-docs/using-ethernet-expansion.html#using-ethernet-expansion) and the [Wireless Projects from the Omega2 Project Book](https://docs.onion.io/omega2-project-book-vol1/wireless-projects.html)
Happy Hacking!

