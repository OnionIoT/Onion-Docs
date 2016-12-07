---
title: The Omega and Wireless Connectivity
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## The Omega & Wireless Connectivity {#the-omega-and-wireless-connectivity}

<!-- // this article will explain the different wireless configurations the Omega supports -->
<!-- // TODO: put an intro about:
//  - what we mean by Wireless Connectivity
//  - preview of the three modes -->


Your Omega has to wireless interfaces that accomplish to different tasks. The first interface broadcasts the Omega's Access Point, a wireless network that your other devices can connect to in order to communicate with the Omega. The second interface connects to an existing network that supplies the Omega with internet. These two interfaces work together to turn your Omega into a fully wireless device.

### Hosting a WiFi Access point

<!-- // highlight that this is the 'Out of the Box' state for the Omega -->

When you power on your Omega, other devices like your computer and smartphone will be able to connect to a new network called `Omega-ABCD`.

<!-- // include an illustration -->
![omega-access-point](../../Get-Started/img/setup-1-connect-to-wifi.png)


In the documentation, this network is what we refer to as the Omega's Access Point (AP), or the Omega's WiFi.

The Omega's AP is a network that your devices can connect to in order to send to, and receive data from the Omega. By connecting to this network, you can access the Omega's filesystem through a terminal, or even the Onion Console through the browser; all of this without having an active internet connection.

>Basically if you were in a place that didn't have internet, you could still wirelessly communicate with your Omega as long as you we powering it, and had a device that was connected to the Access Point.



### Connected to a WiFi network

<!-- // highlight that this is how we get internet on the omega; connecting to your own existing wifi network -->

<!-- // TODO: don't like the unlock - Connecting the Omega to the internet, greatly expands the capabilities of the Omega, etc -->

Connecting the Omega to the internet greatly expands the capabilities of the Omega. It gives you the ability to send and receive data over the internet, and the ability to download and install packages with `opkg`. For more on `opkg`, you can read this [article on using opkg](#using-opkg).

All of this is can be done by connecting your Omega to an existing WiFi network that is supplying internet, in the same way you would connect a laptop or a smartphone to internet.


<!-- // include an illustration -->

<!-- // explanation of what connecting to a Wifi network means and how there is a router somewhere out there, etc -->


### Connected to a WiFi network AND hosting a WiFi Access Point

<!-- // highlight that this is the state the omega is in after completing the setup Wizard -->

<!-- // TODO: mention that the Omega is different from other device (laptop, smartphone) in that it can SIMULTANEOUSLY host an AP and connect to a wifi network - this is cool because you can share internet access and other stuff between the two networks -->

Your Omega can **simultaneously** connect to an existing WiFi network, and host its own Access Point, yielding some interesting results. You can connect your other devices to the Omega's AP and access the internet, making your Omega into a router.
> For more on making your Omega into a router, check out our tutorial on [Turning your Omega into a Router](#omega-router)

You can even connect to the same network that your Omega is on, and communicate with it wirelessly that way. Or if you're really passionate, you can connect several Omega's on the same network, and communicate with them **ALL** wirelessly.

<!-- We need to have a project with an absurd amount of Omegas just for fun -->


### Managing Your Omega's Access Point

You can manage the access of the networks connected to your Omega's AP through the firewall configuration file. This file is located at `/etc/config/firewall` and holds the configurations for sharing internet, and forwarding connections.

*Note: Your Omega is already configured to handle the most practical applications. You need not edit this file unless you know what you're doing.*


To restart your firewall enter the following command:

```
/etc/init.d/firewall restart
```




<!-- // include an illustration -->

<!-- // explain that the Omega is super powerful and that it can connect to a Wifi network while simultaneously hosting it's own access point -->
<!-- // this is powerful because it can share/forward connectivity between the two networks, brief intro on the firewall (where the config can be found, how to restart it) -->
