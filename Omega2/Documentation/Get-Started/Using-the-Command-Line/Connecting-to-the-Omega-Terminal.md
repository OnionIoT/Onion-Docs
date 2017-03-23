---
title: Connecting to the Omega's Command Line
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Connecting to the Omega's Command Line {#connecting-to-the-omega-terminal}


Now that your Omega is setup, connected to a WiFi network, and updated, you'll want to connect to it to start building and inventing.

There are two ways to connect to the Omega's command line:

* Using the local network to connect through SSH
* Using a USB connection to connect to the serial terminal

Both methods have their advantages and disadvantages. We recommend using SSH since it allows you to control wirelessly any Omega that's connected to your WiFi network.


>**The Command-Line Interface** <br>
>The command-line is a way of interacting with a computer by sending commands in the form of single lines of text. This is different from "point and click" graphical user interfaces (GUI) found on most PC operating systems. <br><br>
>Command-line interfaces provide a more concise and powerful means to control a program or operating system, especially with regards to scripting (Shell Scripting, Python, etc). <br><br>
>This interface may seem overwhelming at first, but if you take the time to learn the basic commands you'll find that it's an incredibly powerful and useful tool to have in your toolbox.


### Connecting with SSH {#connecting-to-the-omega-terminal-ssh}

```{r child = './Connecting-to-the-Omega-Terminal-Component-1-ssh-intro.md'}
```

#### The Connection method

The connection method will be different depending on what Operating System you're using on the computer used to connect. We've included guides for the following:

* [Mac OS X](#connecting-to-ssh-mac)
* [Linux](#connecting-to-ssh-linux)
* [Windows](#connecting-to-ssh-windows)


### SSH on a Mac device {#connecting-to-ssh-mac}

```{r child = './Connecting-to-the-Omega-Terminal-Component-2-ssh-mac.md'}
```

### SSH on a Linux device {#connecting-to-ssh-linux}

```{r child = './Connecting-to-the-Omega-Terminal-Component-3-ssh-linux.md'}
```

### SSH on a Windows Device {#connecting-to-ssh-windows}

```{r child = './Connecting-to-the-Omega-Terminal-Component-4-ssh-windows.md'}
```


### Using SSH Key Pairs

```{r child = './Connecting-to-the-Omega-Terminal-Component-5-ssh-key-pairs.md'}
```


### Connecting via Serial {#connecting-to-the-omega-terminal-serial}

The Omega's command prompt can also be accessed with a USB cable, as long as your **Omega is docked in either an Expansion Dock or a Mini Dock**. What's happening is that the Omega is using its UART pins to run a terminal, the USB-to-Serial chip found on the Dock is translating the Serial Terminal signals into USB signals that your computer can understand and vice versa.

<!-- // TODO: stylized picture of an Omega2 on an Expansion Dock connected to a laptop with a cable -->

Generally, we recommend using SSH to access the Omega's command line, but the serial terminal does have its advantages. For instance, the serial terminal will always be available as long as the Omega is powered on and does not depend on network connectivity. Additionally, when using the serial terminal, you will see messages such as this one:

![kernel message](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-kernel-messages.png)

This is an example of a message coming from the kernel. These messages can be listed out at any time using the `dmesg` command, so they can be seen when using SSH as well.

Note that the Expansion Dock and Mini Dock are the only docks that have USB-to-Serial chips, so the serial terminal will only work when using those docks. The serial terminal is meant for debugging during early development, for stable projects, SSH is the best method for accessing the command line.

We'll first identify the specific USB connection that we need to use to talk to the Omega, and then setting up the communication.

#### The Connection method

The connection method will be different depending on what Operating System you're using on the computer used to connect. We've included guides for the following:

* [Mac OS X](#connecting-via-serial-mac)
* [Linux](#connecting-via-serial-linux)
* [Windows](#connecting-via-serial-windows)

### Serial on a Mac Device {#connecting-via-serial-mac}

**Download Drivers**

Download and install the [Silicon Labs CP2102 driver for OS X](https://www.silabs.com/Support%20Documents/Software/Mac_OSX_VCP_Driver.zip).

**Check if Serial Device Exists**

Plug in your Omega & Dock and run `ls /dev/tty.*` to see if the USB-to-Serial device can be detected. If the driver is successfully installed, you should be able to see a device with a name similar to `/dev/tty.SLAB_USBtoUART`.

![Check if serial device exists](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-osx-check.jpg "Check if serial device exists")

**Log in**

Run `screen /dev/tty.SLAB_USBtoUART 115200` to connect to the Omega’s serial terminal using the `screen` utility.

![Log in through serial terminal](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-osx-login.jpg "Log in through serial terminal")

> We recommend taking a peek at [this tutorial](https://www.linode.com/docs/networking/ssh/using-gnu-screen-to-manage-persistent-terminal-sessions) to get an idea of how the `screen` utility works.

**All Done**

 Enjoy! You're now connected to your Omega!



### Serial on a Windows Device {#connecting-via-serial-windows}

**Download Drivers**

Download and install the [Silicon Labs CP2102 driver for Windows](https://www.silabs.com/Support%20Documents/Software/CP210x_VCP_Windows.zip).

**Find Serial Device**

Plug in your Omega & Dock and run Device Manager (Start > Enter "Device Manager" and press `ENTER`), look for Silicon Labs CP210x USB to UART Bridge under Ports (COM & LPT), and take note of the COM number in bracket.

![Computer Management](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-windows-device-manager.jpg "Computer Management")

**Download a Terminal Program**

We'll be using PuTTy, but you can use another terminal program that you like. You can download [Putty from this link](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

**Configure PuTTy**

Open up PuTTy, select Serial for Connection type, enter the COM number noted down in Step 2 as Serial line, and enter `115200` for the speed.

![Configure PuTTY](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-windows-putty-settings.jpg "Configure PuTTY")

**Connect**

Click on the Open button to connect to the Omega via the serial terminal.

![Log in through serial terminal](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-windows-login.jpg "Log in through serial terminal")

**All Done**:

Enjoy! You're now connected to your Omega!




### Serial on a Linux Device {#connecting-via-serial-linux}

**Step 1: Check if the serial drivers are already installed**

Some modern Linux Distros already have the required serial drivers installed. Run `modinfo cp210x` on the command line, if it outputs several lines of information, the driver is already installed and you can skip ahead to **Step 4**.

If the output is something along the lines of

```
modinfo: ERROR: Module cp210x not found.
```

the driver will need to be installed. Continue to **Step 2**.


**Step 2: Download and install the Silicon Labs CP2102 driver source files**

For Linux kernel [**3.x.x and higher**](https://www.silabs.com/Support%20Documents/Software/Linux_3.x.x_VCP_Driver_Source.zip).

For Linux kernel [**2.6.x**](https://www.silabs.com/Support%20Documents/Software/Linux_3.x.x_VCP_Driver_Source.zip).

**Step 3: Build and install the driver**

*For Ubuntu/Debian*:

Unzip the archive.

`cd` into the unzipped directory.

Compile the driver with `make`.

```bash
sudo cp cp210x.ko /lib/modules/<kernel-version>/kernel/drivers/usb/serial/
sudo insmod /lib/modules/<kernel-version>/kernel/drivers/usb/serial/usbserial.ko
sudo insmod cp210x.ko
sudo chmod 666 /dev/ttyUSB0
sudo usermod -a -G dialout $USER
```

*For RedHat/CentOS*:

```
sudo yum update kernel* //need to update the kernel first otherwise your header n't match
sudo yum install kernel-devel kernel-headers //get the devel and header packages
sudo reboot //your build link should be fixed after your system come back
```

Unzip the archive.

`cd` into the unzipped directory.

Compile the driver with `make`.

```
sudo cp cp210x.ko /lib/modules/<kernel-version>/kernel/drivers/usb/serial
sudo insmod /lib/modules/<kernel-version>/kernel/drivers/usb/serial/usbserial.ko
sudo insmod cp210x.ko
sudo chmod 666 /dev/ttyUSB0
sudo usermod -a -G dialout $USER
```


**Step 4: Install** `screen`

Let's install `screen`, a command line utility that will allow connecting to the Omega's serial terminal.

*For Ubuntu/Debian*:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install screen
```

*For RedHat/CentOS*:

```
sudo yum update
sudo yum install screen
```

> We recommend taking a peek at [this tutorial](https://www.linode.com/docs/networking/ssh/using-gnu-screen-to-manage-persistent-terminal-sessions) to get an idea of how the `screen` utility works

**Step 5: Look for the USB-to-Serial Device**

 Plug in your Omega & Dock and run `ls /dev/ttyUSB*` to see if the USB-to-Serial device can be detected. If the driver is successfully installed, you should be able to see a device with a name similar to `/dev/ttyUSB0`.

![Check if serial device exists](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-linux-check.png "Check if serial device exists")

**Step 6: Open Screen**

Run `sudo screen /dev/ttyUSB0 115200` to connect to the Omega’s serial terminal using screen.

![Log in through serial terminal](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/connecting-serial-linux-login.png "Log in through serial terminal")

If the screen remains blank, hit enter again to get to the command prompt.

**Step 7**:

Enjoy! You are now connected to your Omega!
