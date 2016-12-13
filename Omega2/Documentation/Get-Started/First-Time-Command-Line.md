## Setup Using the Command Line {#first-time-setup-command-line}

// TODO: edit this a intro a little to make it smoother

Follow along with this guide to set up your Omega2 for the first time. We'll first go through how to properly connect your Omega to a Dock and power it up. Then we'll connect to its command line in order to set up a WiFi connection and update the Omega.

***If you've already gone through the Setup Wizard, you don't need to follow this guide as well, it does the same thing as the Setup Wizard but using the command line***


<!-- Prepare the Hardware -->
```{r child = './Unbox.md'}
```



<!-- Command Line Setup -->

### Setting Up Your Omega

**Some Computer Configuration**

Your computer may need some additional programs to access the Omega through a browser:

* If you are using Windows, install Apple's Bonjour Service
* If you are using OS X, you're all set to go
* If you are using Linux, the Zeroconf services should already be installed and you will be good to go

**The Omega's Name**

Let's find your Omega's name before going any further.

There's a sticker on the Omega's shielding:
![Omega2+](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/omega-name-0-just-omega.jpg)

The text printed here is the Omega's unique MAC address, we're interested in the last four digits that are in bold.

Your Omega's name is `Omega-ABCD` where `ABCD` are the last four digits from the sticker.

So the Omega from the picture above is named `Omega-296A`


**Connect to the Omega's WiFi Network**

The Omega hosts it's own WiFi network access point. Lets connect your computer to it. The WiFi network is named the same as your Omega and the default password is `12345678`

![Connect to AP](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-1-connect-to-wifi.png "Connect to AP")

**Connect to the Omega's Command Line**

We'll use SSH to connect to the Omega's command line

// TODO: insert SSH instructions for Windows, Mac, Linux

>To learn how to connect to the Omega's terminal you can read our [guide to connecting to the Omega](#connecting-to-the-omega-terminal)

**Provision the Omega's WiFi**

Now let's connect the Omega to your WiFi network so it can have internet access, we'll use the `wifisetup` command to help us with this task.

// TODO: add instructions on using wifisetup and the scan for wifi networks option

Enter `wifisetup` in a terminal, and you'll see the following output:

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


Enter your selection and you will be prompted for a password if required. Your network authentication type will be automatically detected in the scan:


```
Selection: 11
Network: OnionWiFi
Authentication type: WPA2PSK
Enter password:
```

Enter your password, and hit enter. Your Omega's network adapter will restart, causing the AP to go down for roughly 30 seconds. Once your network adapter is back up, it will attempt to connect to the network.


// TODO: make these cohesive
> For more on the Omega's wireless capabilities, see [our guide to the Omega and Wireless](#the-omega-and-wireless-connectivity), and to learn more about configuring the Omega's WiFi, see [our guide to using the command line to connect to the WiFi](#connecting-to-wifi-networks-command-line).

**Update to the Latest Version of the Operating System**

Since we've just connected your Omega to the internet, lets update the Omega's operating system to the latest version put out by Onion.

Enter the `oupgrade` command in the terminal, it will download and install the newest updates.

The update will take up to five minutes, sometimes more depending on your internet connection. The process will be complete when the Omega reboots, you'll see the Omega's LED start to flash and then turn solid when it's finished the boot sequence.

**Warning: Do not disconnect the Omega from wifi or power during this process!**


**All Done!**

Start using your fresh Omega, check out the [Using the Omega section](#doing stuff) for ideas on what the Omega can do!
<!-- Start using your fresh Omega, check out the [Tutorials section](./Tutorials/Contents) or the [Project guides](./Projects/Contents) for ideas on what to do next! -->
<!-- TODO: fix the links above when the content is available -->
