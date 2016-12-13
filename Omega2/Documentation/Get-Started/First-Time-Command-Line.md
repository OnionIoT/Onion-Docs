## Setup Using the Command Line {#first-time-setup-command-line}

// TODO: edit this a intro a little to make it smoother

Follow along with this guide to set up your Omega2 for the first time. We'll first learn how to properly connect your Omega to a Dock and power it up. Then we'll connect to its command line,  configure it to join your WiFi network and then do some updates.

***If you've already gone through the Setup Wizard, you don't need to follow this guide as well, it does the same thing as the Setup Wizard but using the command line***


<!-- Prepare the Hardware -->
```{r child = './First-Time-Components/Hardware-Prep.md'}
```



<!-- Command Line Setup -->

### Setting Up Your Omega

<!-- Computer Config -->
```{r child = './First-Time-Components/First-Time-Component-01-computer-config.md'}
```

<!-- The Omega's Name -->
```{r child = './First-Time-Components/First-Time-Component-02-omega-name.md'}
```

<!-- Connect to Omega's Wifi AP -->
```{r child = './First-Time-Components/First-Time-Component-03-connect-to-omega-network.md'}
```

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
