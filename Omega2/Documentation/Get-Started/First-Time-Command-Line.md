## Setup Using the Command Line {#first-time-setup-command-line}

<!--  TODO: edit this a intro a little to make it smoother -->

Follow along with this guide to set up your Omega2 for the first time. We'll be doing the following:

1. Connecting your Omega to a Dock and powering it on.
1. Connecting to its command line terminal.
1. Configuring it to join your WiFi network and then do some updates.

***If you've already gone through the Setup Wizard, you don't need to follow this guide. This is how to do the same setup process using the command line.***


<!-- Prepare the Hardware -->
```{r child = './Unbox.md'}
```


<!-- Command Line Setup -->

### Preparing to Connect

**Some Computer Configuration**

Your computer may need some additional programs to access the Omega through a browser depending on your operating system:

* Windows: install Apple's Bonjour Service
* Mac OS X: you're all set to go
* Linux: the Zeroconf services should already be installed and you will be good to go

**The Omega's Name**

Let's find your Omega's name before going any further.

There's a sticker on the Omega's shielding:
![Omega2+](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/omega-name-0-just-omega.jpg)

The text printed here is the Omega's unique MAC address. We're interested in the **bold last four digits**.

Your Omega's name is `Omega-ABCD`, where **`ABCD`** are the last four digits from the sticker.

In the example above, the Omega is named `Omega-5931`.


### Connecting to the Omega

#### Connecting to the Omega's WiFi Access Point

The Omega broadcasts its own WiFi network access point. Let's connect your computer to it.

* The WiFi network has the same name as your Omega by default.
    * In the example below, the Omega's name is `Omega-296A`.
* The default password is `12345678`.
* You can change the network name and password at any time by following [this guide](#adjusting-ap-network-through-command-line).

![Connect to AP](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-1-connect-to-wifi.png "Connect to AP")

### Connect to the Omega's Command Line

We'll use SSH to connect to the Omega's command line.

>To learn how to connect to the Omega's terminal you can read our [guide to connecting to the Omega](#connecting-to-the-omega-terminal). Find the section labelled "Connecting with SSH".

#### Provision the Omega's WiFi

Now let's connect the Omega to your WiFi network to give it Internet access. We'll use the `wifisetup` command to help us.

Enter `wifisetup` in a terminal and you'll see the following output:

```
root@Omega-2757:/# wifisetup
Onion Omega Wifi Setup

Select from the following:
1) Scan for Wifi networks
2) Type network info
q) Exit

Selection:

```

You can enter `1`, and your Omega will scan for available networks:

```
Selection: 1
Scanning for wifi networks...

Select Wifi network:
1) BYB-Guest
2) BYB-Corporate
3) studio six
4) maya
5) ITL
6) maya
7) EG Energy
8) maya
9) Omega_C02759
10) Authentica
11) OnionWiFi
12) Omega-2928
13) OnionFriends
14) Orpheus
15) Omega-18C2

Selection:
```


Enter your selection number and you will be prompted for a password if required. Your network authentication type will be automatically detected in the scan:


```
Selection: 11
Network: OnionWiFi
Authentication type: WPA2PSK
Enter password:
```

Enter your network's password. Your Omega's network adapter will now restart, causing the AP to go down for roughly 30 seconds. Once your network adapter is back up, it will attempt to connect to the network.

> For more on the Omega's wireless capabilities, see [our guide to the Omega and Wireless](#the-omega-and-wireless-connectivity).

>To learn more about configuring the Omega's WiFi connection, see [our guide to using the command line to connect to WiFi](#connecting-to-wifi-networks-command-line).

### Update the Omega's Firmware

Now that we've just connected your Omega to the internet, let's update the Omega's operating system to the latest version released by Onion.

Enter the `oupgrade` command in the terminal to download and install the newest updates. **Your Omega will now reboot on its own, no further action needed.**

The update will take up to five minutes, sometimes more depending on your Internet connection. You'll see the Omega's LED start to flash and then turn solid when it has finished the boot sequence.

**Warning: Do not disconnect the Omega from WiFi or power during this process or the firmware may become corrupted!**

Now you're all done!

Start using your fresh Omega and check out the [Using the Omega section](#doing stuff) for ideas on what the Omega can do!
<!-- Start using your fresh Omega, check out the [Tutorials section](./Tutorials/Contents) or the [Project guides](./Projects/Contents) for ideas on what to do next! -->
<!-- TODO: fix the links above when the content is available -->
