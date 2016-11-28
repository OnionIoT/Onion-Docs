---
title: Ethernet Bridge
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

# Ethernet Bridge

In this tutorial, we are going to go through how we can enable other devices to use the Omega's Ethernet Expansion to connect to an existing WiFi network.

# Overview 

Tutorial Difficulty:

**Intermediate**

Time Required:

**5 mins**

Required Materials:
* Omega2 or Omega2+
* Expansion Dock
* Ethernet Dock
* (Optional) Lan Switch


[//]: # (The Actual Process)

# The Actual Process

What we are going to do is to first enable the Omega's ethernet connection, and then try to bridge the wireless internet connection with ethernet connection. There are several ways to do so, one of the ways is to modify the firewall configuration.


[//]: # (The Steps)

## Step 1: Connect Omega with WiFi

This step is fairly easy, and there are a lot of tutorials tell us how to do so in different ways. Click [here](../Get-Started) to view how to make it work.

[//]: # (Step 2)

## Step 2: Enable the Ethernet Connection in Omega

There is an existing tutorial for this as well, click [here](./Expansions/Using-the-Ethernet-Expansion) to learn more.

Basically what we need to do is to change the following code block located at `/etc/config/network`:

```
config interface 'wlan'
        option type 'bridge'
        option ifname 'eth0.1'
        option proto 'static'
        option ipaddr '192.168.3.1'
        option netmask '255.255.255.0'
        option ip6assign '60'

```

Change `option ifname 'eth0.1' to `option ifname 'eth0'`


Restart the network service by running the follow command, or simply rebooting the Omega:

```
/etc/init.d/network restart
```
Wait for the command prompt to show up and your Omega should be configured.

If you want to learn more, go to [Openwrt network configuration page](https://wiki.openwrt.org/doc/uci/network).

[//]: # (Step 3)
## Step 3: Connect to Lan Switch via Ethernet

Now that the Omega is configured, we should be able to connect with other devices via Ethernet.

Make sure that your conection is set to `Obtain IP address and DNS anddress Automatically`. It should be set so by default.

![pic](../img/wifi-bridge-pic-1.png)
![pic](../img/wifi-bridge-pic-2.png)
![pic](../img/wifi-bridge-pic-3.png)
![pic](../img/wifi-bridge-pic-4.png)

[//]: # (Using the Project)

# Using This Setup

If you have a device that only can be connected via Ethernet and you only have WiFi avaliable, you could apply this tutorial to make it work!

Or, you can extend Ethernet access to multiple cables using an Ethernet switch.

# Notes

* This will disable the Omega's WiFi AP.

## Related Tutorials

* [Get started](../Get-Started)
* [Using Ethernet Expansion](./Expansions/Using-the-Ethernet-Expansion)
* [Using Omega as a Router](./Using-Omega-As-A-Router)


[//]: # (Acknowledgements)

# Acknowledgements

Some more information can be found in our Onion Community thread [here](https://community.onion.io/topic/694/wireless-setup).

Or you can visit the following websites to learn more:
* [Openwrt network configuration page](https://wiki.openwrt.org/doc/uci/network)
* [Openwrt Firewall configuration page](https://wiki.openwrt.org/doc/uci/firewall)
