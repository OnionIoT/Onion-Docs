## First Time Setup using the Command Line {#first-time-setup-command-line}

<!--  TODO: edit this a intro a little to make it smoother -->

Follow along with this guide to set up your Omega2 for the first time using the command line.

***Follow this guide only if the Setup Wizard was not able to get your Omega2 up and running. If the Setup Wizard succeeded, you don't have to go through these steps!***

 We'll be doing the following:

1. Connecting your Omega to a Dock and powering it on.
1. Connecting to its command line terminal.
1. Configuring it to join your WiFi network and then do some updates.

> If you experience issues at any point in the process, try checking our [Troublshooting guide](#first-time-troubleshooting).

<!-- Prepare the Hardware -->
```{r child = './First-Time-Components/Hardware-Prep.md'}
```


<!-- Command Line Setup -->

### Preparing to Connect

<!-- Computer Config -->
```{r child = './First-Time-Components/First-Time-Component-01-computer-config.md'}
```

<!-- The Omega's Name -->
```{r child = './First-Time-Components/First-Time-Component-02-omega-name.md'}
```

<!-- Connect to Omega's Wifi AP -->
```{r child = './First-Time-Components/First-Time-Component-03-connect-to-omega-network.md'}
```

### Connect to the Omega's Command Line

We'll use SSH to connect to the Omega's command line.

>To learn how to connect to the Omega's terminal you can read our [guide to connecting to the Omega with SSH](#connecting-to-the-omega-terminal-ssh).

#### Provision the Omega's WiFi

Now let's connect the Omega to your WiFi network to give it Internet access. We'll use the `wifisetup` command to help us.

Enter `wifisetup` in a terminal and you'll see the following output:

<!-- wifisetup option 1 output -->
```{r child = './Using-the-Command-Line/Connecting-to-WiFi-Networks-Component-1-wifisetup-option-1.md'}
```

> For more on the Omega's wireless capabilities, see [our guide to the Omega and Wireless](#the-omega-and-wireless-connectivity).
>
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

### This Didn't Work!

Try checking our [Troublshooting guide](#first-time-troubleshooting) or posting on the [Onion Community](http://community.onion.io).
