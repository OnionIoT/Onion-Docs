## Setup Using the Command Line {#first-time-setup-command-line}

// TODO: edit this a intro a little to make it smoother

Follow along with this guide to set up your Omega2 for the first time. We'll first learn how to properly connect your Omega to a Dock and power it up. Then we'll connect to its command line,  configure it to join your WiFi network and then do some updates.

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

**Provision the Omega's WiFi**

Now let's connect the Omega to your WiFi network so it can have internet access, we'll use the `wifisetup` command to help us with this task.

// TODO: add instructions on using wifisetup and the scan for wifi networks option

// TODO: make these cohesive
> For more on the Omega's wireless capabilities, see // TODO link to the omega connectivity overview and to learn more about configuring the Omega's WiFi, see // TODO link to commandline wifi article

**Update to the Latest Version of the Operating System**

Since we've just connected your Omega to the internet, lets update the Omega's operating system to the latest version put out by Onion.

Enter the `oupgrade` command in the terminal, it will download and install the newest updates.

The update will take up to five minutes, sometimes more depending on your internet connection. The process will be complete when the Omega reboots, you'll see the Omega's LED start to flash and then turn solid when it's finished the boot sequence.

**Warning: Do not disconnect the Omega from wifi or power during this process!**


**All Done!**

Start using your fresh Omega, check out the [Using the Omega section](#doing stuff) for ideas on what the Omega can do!
<!-- Start using your fresh Omega, check out the [Tutorials section](./Tutorials/Contents) or the [Project guides](./Projects/Contents) for ideas on what to do next! -->
<!-- TODO: fix the links above when the content is available -->
