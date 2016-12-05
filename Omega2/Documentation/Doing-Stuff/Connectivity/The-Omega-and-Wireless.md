---
title: The Omega and Wireless Connectivity
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## The Omega & Wireless Connectivity {the-omega-and-wireless-connectivity}

<!-- // this article will explain the different wireless configurations the Omega supports -->
// TODO: put an intro about:
//  - what we mean by Wireless Connectivity
//  - preview of the three modes

### Hosting a WiFi Access point

<!-- // highlight that this is the 'Out of the Box' state for the Omega -->

When you power on your Omega, a new network called `Omega-ABCD` will show up on your list of networks.

<!-- // include an illustration -->
![omega-access-point](../../Get-Started/img/setup-1-connect-to-wifi.png)

The Omega's AP gives you the ability to wirelessly connect to your Omega.
// TODO: mention and expand on what an AP is and does
// TODO: give an example of the usage
// TODO: 'you can even turn the omega into a fully-fledged router - link to article'
<!-- // explain what hosting a WiFi access point means ie that a bunch of other devices can connect to the Omega's network -->

In the documentation, this is what we mean when we refer to the Omega's Access Point (AP), or the Omega's WiFi.


### Connected to a WiFi network

<!-- // highlight that this is how we get internet on the omega; connecting to your own existing wifi network -->

// TODO: don't like the unlock - Connecting the Omega to the internet, greatly expands the capabilities of the Omega, etc
Your Omega can connect to the internet to unlock a lot of features, such as the ability to download packages with `opkg`. For more on `opkg`, you can read this [article on using opkg](#using-opkg).

This is done by connecting your Omega to an existing WiFi network that is supplying internet, giving your Omega access to the internet.
// TODO: draw parallel to connecting your laptop or smartphone to a wifi network


<!-- // include an illustration -->

<!-- // explanation of what connecting to a Wifi network means and how there is a router somewhere out there, etc -->


### Connected to a WiFi network AND hosting a WiFi Access Point

<!-- // highlight that this is the state the omega is in after completing the setup Wizard -->

// TODO: mention that the Omega is different from other device (laptop, smartphone) in that it can SIMULTANEOUSLY host an AP and connect to a wifi network - this is cool because you can share internet access and other stuff between the two networks
Once your Omega is connected to the internet, the Omega's AP will be able to supply an internet connection to the devices that are connected. This means that connecting to your device to your Omega's AP will give your device access to the internet.

You can manage the access of the networks connected to your Omega's AP through the firewall configuration file. This file is located at `/etc/config/firewall` and holds the configurations for sharing internet, and forwarding connections.


To restart your firewall enter the following command:

```
/etc/init.d/firewall restart
```




<!-- // include an illustration -->

<!-- // explain that the Omega is super powerful and that it can connect to a Wifi network while simultaneously hosting it's own access point -->
<!-- // this is powerful because it can share/forward connectivity between the two networks, brief intro on the firewall (where the config can be found, how to restart it) -->
