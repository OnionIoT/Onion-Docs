## Firmware Flashing from USB Storage {#Firmware-Flashing-from-USB-storage}

If your Omega got "bricked" or your firmware became corrupted and you cannot boot into your OS, do not panic as it can be fixed. This guide will teach you how to flash your Omega with new firmware through the Omega's Bootloader.

![Usb Flashing Components](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/usb-firmware-flashing-components.jpg)

### Step 1: Ingredients

In general, the USB method will give you more options to re-flash your Omega as it does not require the Ethernet Expansion or a Dock with an expansion header.

We will need the following ingredients:

* The Omega2 or Omega2+ that needs to be flashed with new firmware
* A dock with a USB-to-Serial chip
	* Expansion Dock
	* Mini Dock
* USB stick
* MicroUSB Cable

### Step 2: Downloading Firmware

Before we proceed to the actual flashing process, we need to download the firmware we wish to flash on the Omega to your computer. Open your web browser and go to the [Onion firmware repo](http://repo.onion.io/omega2/images/). We will flash firmware `v0.1.10 b160`, which is the latest at the time of writing. Copy it to your USB stick (formatted in **FAT-32**) and put it in the root directory - the top level of your USB drive, not in a folder or directory. Rename it to `omega2.bin` and your recovery USB stick is ready

### Step 3: Activating Recovery mode from USB storage

Now, plug your Omega and the USB stick into the Dock and connect to your computer but do not power on the device just yet.

[First, connect to the Omega’s command line through serial](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html#connecting-to-the-omega-terminal-serial). Then, power on the device **and** press the **_Reset_** button on the Dock at the same time.  This will get you to the bootloader and you’ll see the following menu: 

![bootloader-menu](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/bootloader-menu.PNG)
<!-- Bootloader menu -->

> Note that the **_Reset_** button is connected to the _active-high_ FW_RST/GPIO38 pin. To get to the bootloader prompt when using an Omega2S module, hold the SW_RST/GPIO38 pin at logical high while the device is booting.

We need to choose `Flashing firmware from USB storage` by pressing `2`. Be quick, you only have 40 seconds until the Omega reboots and tries to boot normally. After pressing `2`, you should see the following output:

![bootloader-usb-firmware](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/bootloader-usb-firmware.PNG)
<!-- Screenshot of the USB being recognized -->

### Step 4: Actual Flashing

The bootloader is accessing the USB device and reading the `omega2.bin` file that holds our firmware.

![bootloader-usb-rebooting](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/bootloader-usb-rebooting.PNG)
<!-- Screenshot of the reading the omega2.bin file -->

This process will take several minutes to read the file and then reflash and reboot your device! _Do not disconnect you Omega from power while the update is in the progress!_

Once it's done, the Omega will reboot automatically. You will see the Onion Omega Logo and the firmware version number

This will take several minutes to reflash and reboot your device. Once it is done, you will see `Onion Omega Logo` and the version number.

![bootloader-usb-flashed-rebooted](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/bootloader-usb-flashed-rebooted.PNG)
<!-- Screenshot of the finished flashing -->

Please, note that it matches the firmware we downloaded: `Ω - ware: 0.1.10 b160`. 

### Going Further

Having an Ethernet Expansion is handy since it not only can it allow you to de-brick your Omega, but also enable you to make a variety projects. Please refer to our Docs on [how to use the Ethernet Expansion](https://docs.onion.io/omega2-docs/using-ethernet-expansion.html#using-ethernet-expansion) and the [Wireless Projects from the Omega2 Project Book](https://docs.onion.io/omega2-project-book-vol1/wireless-projects.html)
Happy Hacking!

