---
title: Ethernet Bridge
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

# Ethernet Bridge

In this tutorial, we are going to go through how we can enable other devices to use the Omega's Ethernet Expansion to connect to an existing WiFi network.

// add an illustration

# Overview

// bring this overview into all networking articles

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

// get rid of the 'click here ' links, make it a real sentence

[//]: # (Step 2)

## Step 2: Enable the Ethernet Connection in Omega

There is an existing tutorial for this as well, click [here](./Expansions/Using-the-Ethernet-Expansion) to learn more.

// get rid of the 'click here ' links, make it a real sentence

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
// rename this step

Now that the Omega is configured, we should be able to connect with other devices via Ethernet.

Make sure that your connection is set to `Obtain IP address and DNS address Automatically`. It should be set so by default.

// find outside links on how to setup ethernet to use DHCP on windows, mac, linux

![pic](../img/wifi-bridge-pic-1.png)
![pic](../img/wifi-bridge-pic-2.png)
![pic](../img/wifi-bridge-pic-3.png)
![pic](../img/wifi-bridge-pic-4.png)

[//]: # (Using the Project)

# Using This Setup

If you have a device that only can be connected via Ethernet and you only have WiFi available, you could apply this tutorial to make it work!

Or, you can extend Ethernet access to multiple cables using an Ethernet switch.

# Notes

* This will disable the Omega's WiFi AP.

// double check this and then get rid of the comment
